import re
import json
from typing import Dict, Any, List, Optional
from database.db_manager import DBManager
from model_llm import ModelLLM
from engine.dice_utils import DiceUtils

class ModuleExecutor:
    """
    O Cérebro Genérico da Engine Lorandur.
    """

    def __init__(self):
        self.db = DBManager()
        self.llm = ModelLLM()
        self._var_pattern = re.compile(r'\{\{([a-zA-Z0-9_.]+)\}\}')
        
        # Guarda os dados completos da última execução para auditoria
        self.last_prompt_debug: Dict[str, Any] = {}

    def execute(self, module_id: str, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executa um módulo completo.
        """
        print(f"[Executor] Iniciando módulo: {module_id}")
        self.last_prompt_debug = {}

        # 1. Carregar Módulo
        module_data = self.db.get_module(module_id)
        if not module_data:
            raise ValueError(f"Módulo '{module_id}' não encontrado no banco de dados.")

        # 2. Preparar Inputs
        mapped_inputs = self._resolve_input_mapping(module_data.get('input_mapping', {}), game_state)
        context = {**game_state.get('system', {}), **mapped_inputs}

        # 3. Renderizar Prompts
        raw_prompts = module_data.get('prompts', {})
        system_prompt = self._render_text(raw_prompts.get('system', ''), context)
        user_prompt = self._render_text(raw_prompts.get('user', ''), context)

        # 4. Injeções Narrativas
        injections = self._process_injections(module_data.get('narrative_injections', []), game_state)
        if injections:
            system_prompt += "\n\n### SISTEMA (CONDIÇÕES ATIVAS) ###\n" + "\n".join(injections)

        # 5. Configuração
        config = module_data.get('configuration', {})
        schema = module_data.get('output_schema')
        preset = config.get('model_preset')

        # 6. Execução LLM
        try:
            print(f"[Executor] Enviando para LLM (Preset: {preset})...")
            
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

            # Processamento da Resposta Bruta
            content_str = raw_response.get("content", "{}")
            usage = raw_response.get("usage", {})
            finish_reason = raw_response.get("finish_reason")
            
            # Guarda Debug COMPLETO (Agora incluindo o Schema)
            self.last_prompt_debug = {
                "module_id": module_id,
                "system": system_prompt,
                "user": user_prompt,
                "usage": usage,
                "finish_reason": finish_reason,
                "raw_content": content_str,
                "schema": schema  # <--- ADICIONADO AQUI
            }

            try:
                parsed_json = json.loads(content_str)
                return parsed_json
            except json.JSONDecodeError:
                print(f"[Executor] Falha no Parse JSON. Conteúdo: {content_str[:100]}...")
                return {"error": "JSON_PARSE_FAILED"}

        except Exception as e:
            print(f"[Executor] Erro crítico: {e}")
            raise e

    def _resolve_input_mapping(self, mapping: Dict[str, str], game_state: Dict[str, Any]) -> Dict[str, Any]:
        resolved = {}
        for key, path in mapping.items():
            value = self._get_nested_value(game_state, path)
            resolved[key] = value
        return resolved

    def _get_nested_value(self, data: Any, path: str) -> Any:
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

    def _render_text(self, text: str, context: Dict[str, Any]) -> str:
        def replace_match(match):
            variable_path = match.group(1)
            if variable_path in context:
                val = context[variable_path]
            else:
                val = self._get_nested_value(context, variable_path)
            if isinstance(val, list):
                return ", ".join(str(x) for x in val)
            return str(val) if val is not None else "[N/A]"
        return self._var_pattern.sub(replace_match, text)

    def _process_injections(self, rules: List[Dict], game_state: Dict) -> List[str]:
        active = []
        for rule in rules:
            conds = rule.get('conditions')
            text = rule.get('text')
            if not conds:
                active.append(text)
                continue
            
            target = conds.get('target')
            if target and "{{" in target:
                target = self._render_text(target, game_state)
            
            curr = self._get_nested_value(game_state, target) if target else None
            req = conds.get('value')
            check = conds.get('check_type', 'EQUALS')
            
            match = False
            if check == 'EQUALS': match = str(curr) == str(req)
            elif check == 'VALUE_MATCH': match = str(curr) == str(req) # Alias
            elif check == 'EXISTS': match = curr is not None
            
            if match:
                active.append(self._render_text(text, game_state))
        return active