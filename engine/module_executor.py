import re
import json
from typing import Dict, Any, List, Optional
from database.db_manager import DBManager
from model_llm import ModelLLM
from engine.dice_utils import DiceUtils

class ModuleExecutor:
    """
    O Cérebro Genérico da Engine Lorandur.
    
    Esta classe é responsável por orquestrar a execução de módulos de IA definidos em JSON.
    Ela atua como uma ponte entre o Estado do Jogo (Game State), as Regras (JSONs) e o Modelo de Linguagem (LLM).

    Arquitetura:
        - Data-Driven Input: Lê dados do estado baseado em 'input_mapping'.
        - Data-Driven Output: Grava dados no estado baseado em 'output_mapping'.
        - Prompt Rendering: Substitui variáveis {{...}} no texto.
        - Structured Output: Garante que o LLM retorne JSON válido conforme schema.
    """

    def __init__(self):
        """
        Inicializa os componentes fundamentais do executor.
        """
        self.db = DBManager()     # Gerenciador de acesso aos módulos (JSONs)
        self.llm = ModelLLM()     # Interface com a API de IA (Gemini/OpenAI)
        
        # Regex pré-compilada para encontrar variáveis no formato {{caminho.da.variavel}}
        self._var_pattern = re.compile(r'\{\{([a-zA-Z0-9_.]+)\}\}')
        
        # Armazena metadados da última execução para fins de debug e auditoria
        self.last_prompt_debug: Dict[str, Any] = {}

    def execute(self, module_id: str, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executa um módulo em modo SOMENTE LEITURA (Read-Only).
        
        Processa o prompt, envia para a IA e retorna a resposta estruturada,
        MAS NÃO altera o 'game_state' persistente. Útil para testes ou simulações.

        Args:
            module_id (str): O ID único do módulo no banco de dados (ex: 'core_trama_generator').
            game_state (Dict): O dicionário contendo todo o estado atual do jogo.

        Returns:
            Dict[str, Any]: O JSON parseado retornado pela IA.

        Raises:
            ValueError: Se o módulo não for encontrado.
            Exception: Erros de conexão com LLM ou falha crítica de parsing.
        """
        print(f"[Executor] Iniciando módulo (modo readonly): {module_id}")
        self.last_prompt_debug = {}

        # 1. Carregar Definição do Módulo
        module_data = self.db.get_module(module_id)
        if not module_data:
            raise ValueError(f"Módulo '{module_id}' não encontrado no banco de dados.")

        # 2. Resolução de Inputs (Input Mapping)
        # Transforma definições abstratas ("genre": "context.genre") em dados reais ("genre": "Cyberpunk")
        mapped_inputs = self._resolve_input_mapping(module_data.get('input_mapping', {}), game_state)
        
        # Mescla inputs resolvidos com dados globais do sistema
        context = {**game_state.get('system', {}), **mapped_inputs}

        # 3. Renderização de Prompts (Jinja-like replacement)
        raw_prompts = module_data.get('prompts', {})
        system_prompt = self._render_text(raw_prompts.get('system', ''), context)
        user_prompt = self._render_text(raw_prompts.get('user', ''), context)

        # 4. Injeções Narrativas Dinâmicas
        # Adiciona regras extras ao prompt do sistema se certas condições do jogo forem atendidas
        injections = self._process_injections(module_data.get('narrative_injections', []), game_state)
        if injections:
            system_prompt += "\n\n### SISTEMA (CONDIÇÕES ATIVAS) ###\n" + "\n".join(injections)

        # 5. Configuração Técnica
        config = module_data.get('configuration', {})
        schema = module_data.get('output_schema') # O contrato JSON que a IA deve obedecer
        preset = config.get('model_preset')

        # 6. Execução no LLM
        try:
            print(f"[Executor] Enviando para LLM (Preset: {preset})...")
            
            # Configura o modo 'JSON Mode' estrito do modelo
            response_format = {
                "type": "json_schema",
                "json_schema": {
                    "name": "structured_output",
                    "strict": True,
                    "schema": schema
                }
            }

            raw_response = self.llm.generate(
                system_instruction=system_prompt,
                prompt=user_prompt,
                response_format=response_format,
                model_preset=preset
            )

            # Extração de Metadados
            content_str = raw_response.get("content", "{}")
            usage = raw_response.get("usage", {})
            finish_reason = raw_response.get("finish_reason")
            
            # Snapshot de Debug (Essencial para entender o que a IA "pensou")
            self.last_prompt_debug = {
                "module_id": module_id,
                "system": system_prompt,
                "user": user_prompt,
                "usage": usage,
                "finish_reason": finish_reason,
                "raw_content": content_str,
                "schema": schema
            }

            # Parse e Retorno
            try:
                parsed_json = json.loads(content_str)
                return parsed_json
            except json.JSONDecodeError:
                print(f"[Executor] Falha no Parse JSON. Conteúdo: {content_str[:100]}...")
                return {"error": "JSON_PARSE_FAILED"}

        except Exception as e:
            print(f"[Executor] Erro crítico: {e}")
            raise e

    def execute_and_apply(self, module_id: str, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executa o módulo e APLICA o resultado no 'game_state' (Modo Escrita).
        
        Esta função é o coração da arquitetura Data-Driven. Ela consulta o campo
        'output_mapping' do JSON do módulo para saber onde salvar cada pedaço da resposta.

        Args:
            module_id (str): ID do módulo.
            game_state (Dict): O estado do jogo (será modificado in-place).

        Returns:
            Dict[str, Any]: O resultado gerado (já aplicado ao estado).
        """
        # 1. Executa a lógica padrão (geração de conteúdo)
        result_json = self.execute(module_id, game_state)
        
        # 2. Carrega configurações para ler as regras de saída
        module_data = self.db.get_module(module_id)
        output_mapping = module_data.get('output_mapping', {})

        if not output_mapping:
            print(f"[Executor] AVISO: Módulo '{module_id}' executado sem 'output_mapping'. Estado não alterado.")
            return result_json

        print(f"[Executor] Aplicando Output Mapping para '{module_id}'...")

        # 3. Aplica as mudanças no Estado (Escrita no Game State)
        for source_key, dest_path in output_mapping.items():
            try:
                if source_key == "@ROOT":
                    # Estratégia: Mapear TODO o objeto de resposta para um caminho
                    # Ex: Todo o JSON gerado vai para "adventure.trama"
                    self._set_nested_value(game_state, dest_path, result_json)
                    print(f"  -> @ROOT mapeado para '{dest_path}'")
                
                elif source_key in result_json:
                    # Estratégia: Mapear chaves específicas (Granular)
                    # Ex: Apenas o campo "npc_list" vai para "adventure.front.npcs"
                    self._set_nested_value(game_state, dest_path, result_json[source_key])
                    print(f"  -> Chave '{source_key}' mapeada para '{dest_path}'")
                
                else:
                    print(f"  [!] Chave '{source_key}' não encontrada na resposta do módulo.")
            
            except Exception as e:
                print(f"  [ERRO] Falha ao mapear '{source_key}' para '{dest_path}': {e}")
                # Não paramos a execução total, mas logamos o erro de mapeamento
                raise e

        return result_json

    def _resolve_input_mapping(self, mapping: Dict[str, str], game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Converte o dicionário de mapeamento em um dicionário de valores reais.
        Ex: {"genre": "context.genre"} -> {"genre": "Horror"}
        """
        resolved = {}
        for key, path in mapping.items():
            value = self._get_nested_value(game_state, path)
            resolved[key] = value
        return resolved

    def _get_nested_value(self, data: Any, path: str) -> Any:
        """
        Navega em um dicionário aninhado usando notação de ponto (dot notation).
        Ex: "adventure.trama.titulo"
        Suporta índices de lista numéricos. Ex: "adventure.scenes.0.title"
        """
        keys = path.split('.')
        current = data
        try:
            for k in keys:
                if isinstance(current, dict):
                    current = current.get(k)
                elif isinstance(current, list) and k.isdigit():
                    current = current[int(k)]
                else:
                    return f"[Caminho inválido: {path}]"
                if current is None:
                    return None
            return current
        except Exception:
            return f"[Erro leitura: {path}]"

    def _set_nested_value(self, data: Dict[str, Any], path: str, value: Any):
        """
        Define um valor em um dicionário aninhado, criando a estrutura se necessário.
        
        Algoritmo:
        1. Separa o caminho por pontos.
        2. Navega até o penúltimo item.
        3. Se um nível intermediário não existir, cria um novo dicionário {}.
        4. Define o valor na chave final.

        Args:
            data: O dicionário raiz (game_state).
            path: O caminho string (ex: "adventure.trama.argumento").
            value: O valor a ser salvo.
        """
        keys = path.split('.')
        current = data
        
        # Navega até o penúltimo item
        for i, key in enumerate(keys[:-1]):
            # Auto-criação de dicionários faltantes (Auto-vivification)
            if key not in current:
                current[key] = {}
            
            # Validação de Estrutura: Não podemos adicionar chaves a Strings ou Listas
            if not isinstance(current[key], dict):
                raise ValueError(f"Conflito de estrutura em '{path}'. '{key}' (índice {i}) não é um dicionário.")
            
            current = current[key]

        # Define o valor na última chave (a "folha" da árvore)
        last_key = keys[-1]
        current[last_key] = value

    def _render_text(self, text: str, context: Dict[str, Any]) -> str:
        """
        Processa o texto do prompt substituindo variáveis {{var}} pelos valores do contexto.
        Inclui lógica de formatação inteligente para listas e dicionários.
        """
        def replace_match(match):
            variable_path = match.group(1)
            
            # Busca o valor no contexto (Input Mapping + System Vars)
            if variable_path in context:
                val = context[variable_path]
            else:
                # Fallback: tenta buscar direto no state global se o caminho for absoluto
                val = self._get_nested_value(context, variable_path)
            
            # --- LÓGICA DE FORMATAÇÃO ---
            if isinstance(val, list):
                if not val:
                    return ""
                
                # Caso 1: Lista de Objetos/Dicionários (ex: Lista de Locais)
                # Formata como blocos de texto legíveis (Markdown-like)
                if isinstance(val[0], dict):
                    formatted_items = []
                    for item in val:
                        lines = []
                        # Destaque para o nome
                        if 'nome' in item:
                            lines.append(f"> **{item['nome']}**")
                        
                        # Lista os outros atributos
                        for k, v in item.items():
                            if k == 'nome': continue 
                            clean_key = k.replace('_', ' ').capitalize()
                            lines.append(f"  - {clean_key}: {v}")
                        
                        formatted_items.append("\n".join(lines))
                    return "\n\n".join(formatted_items)

                # Caso 2: Lista Simples (Strings, Ints)
                return ", ".join(str(x) for x in val)
            
            return str(val) if val is not None else "[N/A]"

        return self._var_pattern.sub(replace_match, text)

    def _process_injections(self, rules: List[Dict], game_state: Dict) -> List[str]:
        """
        Avalia regras condicionais para injetar texto extra no System Prompt.
        Permite que o prompt mude dinamicamente (ex: se SANIDADE < 10, injeta regra de loucura).
        """
        active = []
        for rule in rules:
            conds = rule.get('conditions')
            text = rule.get('text')
            
            # Sem condições = injeção global
            if not conds:
                active.append(text)
                continue
            
            # Avaliação da Condição
            target = conds.get('target')
            if target and "{{" in target:
                target = self._render_text(target, game_state)
            
            curr = self._get_nested_value(game_state, target) if target else None
            req = conds.get('value')
            check = conds.get('check_type', 'EQUALS')
            
            match = False
            if check == 'EQUALS': match = str(curr) == str(req)
            elif check == 'VALUE_MATCH': match = str(curr) == str(req) 
            elif check == 'EXISTS': match = curr is not None
            
            if match:
                active.append(self._render_text(text, game_state))
        return active