import unittest
import asyncio
import os
import json
import logging
import sys
import time
from datetime import datetime

# Adiciona o diretório pai (raiz do projeto) ao sys.path para encontrar os módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_controller import GameController
from engine.sync_manager import SyncManager

# Configuração de Logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TestFluxoCompleto")

def calculate_cost(usage_dict):
    """
    Calcula custo estimado para Gemini 2.0 Flash (Preview/Free por enquanto).
    """
    if not usage_dict:
        return 0.0
    
    prompt_tokens = usage_dict.get('prompt_tokens', 0)
    completion_tokens = usage_dict.get('completion_tokens', 0)
    
    # Preços por 1 Milhão de tokens (Referência genérica)
    price_input = 0.10 
    price_output = 0.40
    
    cost = (prompt_tokens / 1_000_000 * price_input) + (completion_tokens / 1_000_000 * price_output)
    return cost

class TestFluxoCompleto(unittest.TestCase):
    """
    Teste de Integração TOTAL (End-to-End).
    Executa sequencialmente:
    1. Trama (Geração da semente e Matriz)
    2. Frente Step 1 (Arquiteto & Locais Sensoriais)
    3. Frente Step 2 (Worldbuilder & Ameaças)
    4. Frente Step 3 (Storyteller & Presságios Conectados)
    
    Gera um relatório markdown contendo Prompts e Respostas para auditoria.
    """

    def setUp(self):
        # === 0. SINCRONIZAÇÃO OBRIGATÓRIA ===
        # Garante que os arquivos JSON mais recentes sejam lidos
        # print("\n[SETUP] Sincronizando banco de dados de módulos...")
        # SyncManager().sync_all()

        self.controller = GameController()
        
        # === 1. DEFINIÇÃO DO CONTEXTO INICIAL ===
        # ATUALIZAÇÃO: Não precisamos mais definir 'runtime' ou 'formatted_matrix' manualmente.
        # O GameController agora gerencia o fluxo de dados diretamente via JSON mapping.
        self.context_input = {
            "genre": "Dieselpunk",
            "available_locations_str": "Fábrica de Autômatos, Estação de Trem Blindada, Bar Clandestino (Speakeasy), Hangar de Zeppelins, Torre de Rádio da Propaganda, Esgotos de Óleo, Mansão do Barão, Doca de Carregamento",
            "available_archetypes_str": "Veterano da Grande Guerra, Mecânico de Autômatos, Espião Corporativo, Cientista Louco, Aristocrata Decadente, Líder Operário"
        }
        self.controller.update_context(self.context_input)

    def test_full_sequence_execution(self):
        """Executa a cadeia completa de geração e valida o fluxo de dados."""
        logger.info(">>> Iniciando Sequência Completa de Geração...")

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        start_time = time.time()  # Início da medição de tempo

        try:
            # === FASE 1: GERAR TRAMA ===
            logger.info(">>> [1/4] Executando Módulo Trama...")
            trama_result = self.controller.module_executor.execute("core_trama_generator", self.controller.game_state)
            
            self.assertIsNotNone(trama_result, "A Trama não deve ser nula.")
            # Valida campos essenciais da Trama V3.0
            self.assertIn("matriz_controle_informacao", trama_result)
            
            # Atualiza o controller com a Trama.
            # O GameController armazena isso em adventure.trama, que será lido automaticamente pelos próximos passos.
            self.controller.set_trama_state(trama_result)
            logger.info("✓ Trama Gerada e salva no Estado.")

            # === FASE 2: GERAR FRENTE (PIPELINE) ===
            logger.info(">>> [2/4] Executando Pipeline da Frente (Steps 1, 2, 3)...")
            
            front_result = loop.run_until_complete(
                self.controller.generate_adventure_front_pipeline()
            )
            
            self.assertIsNotNone(front_result, "O resultado da Frente não deve ser nulo.")
            self.assertIn("structure", front_result)
            self.assertIn("world", front_result)
            self.assertIn("story", front_result)
            
            # Validações Básicas dos Schemas
            self.assertIn("cabecalho", front_result["structure"], "Step 1 deve ter 'cabecalho'")
            self.assertIn("perigos", front_result["world"], "Step 2 deve ter 'perigos'")
            self.assertIn("pressagios_terriveis", front_result["story"], "Step 3 deve ter 'pressagios_terriveis'")

            logger.info("✓ Pipeline da Frente concluído com sucesso.")

            # Cálculo de duração
            duration = time.time() - start_time

            # === RELATÓRIO ===
            self._generate_detailed_report(trama_result, front_result, duration)

        except Exception as e:
            logger.error(f"Erro durante o teste: {e}")
            self.fail(f"Teste interrompido por erro: {e}")
            
        finally:
            loop.close()

    def _get_module_data(self, module_filename):
        """Lê o arquivo JSON do módulo para extrair Prompts e Schema."""
        try:
            root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
            path = os.path.join(root_path, "modules_source", module_filename)
            # Tenta ler do diretório source local se existir, senão ignora (ou mocka)
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {"prompts": {"system": "N/A", "user": "N/A"}, "output_schema": {}}
        except Exception as e:
            logger.warning(f"Não foi possível ler o arquivo do módulo {module_filename}: {e}")
            return {"prompts": {"system": "Erro", "user": "Erro"}, "output_schema": {}}

    def _generate_detailed_report(self, trama, frente, duration):
        """Gera Markdown combinando Prompts usados e Respostas geradas (Atualizado para Schemas V2.x)."""
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M")
        root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        report_dir = os.path.join(root_path, "teste", "relatorios_teste")
        os.makedirs(report_dir, exist_ok=True)
        
        filename = os.path.join(report_dir, f"full_flow_v2_{timestamp}.md")

        # Dados de métricas do último passo executado
        debug_data = self.controller.module_executor.last_prompt_debug or {}
        usage = debug_data.get('usage', {})
        cost = calculate_cost(usage)

        # Carrega dados dos módulos para referência no relatório
        mod_trama = self._get_module_data("trama.json")
        mod_step1 = self._get_module_data("frente_step1_archetype.json")
        mod_step2 = self._get_module_data("frente_step2_worldbuilder.json")
        mod_step3 = self._get_module_data("frente_step3_storyteller.json")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Relatório Completo: Fluxo Trama -> Frente (Schemas Atualizados)\n")
            f.write(f"**Data:** {timestamp} | **Gênero:** {self.context_input['genre']}\n")
            f.write(f"**Status:** ✅ Sucesso\n\n")
            
            # --- BLOCO DE MÉTRICAS ---
            f.write("## 📊 Métricas de Execução\n")
            f.write("| Métrica | Valor |\n")
            f.write("| :--- | :--- |\n")
            f.write(f"| **Tempo Total (Fluxo)** | {duration:.2f}s |\n")
            f.write(f"| **Tokens Total (Last Step)** | {usage.get('total_tokens', 0)} |\n")
            f.write(f"| **Custo Estimado (Last Step)** | ${cost:.6f} |\n")
            f.write("\n---\n")

            # Helper para escrever seções
            def write_section(title, module_data, result_data, icon):
                f.write(f"\n## {icon} {title}\n")
                f.write("<details>\n<summary><strong>⚙️ Ver Prompts & Schema (Técnico)</strong></summary>\n\n")
                f.write(f"**System Prompt:**\n```text\n{module_data.get('prompts', {}).get('system', '')}\n```\n")
                f.write(f"**User Prompt Template:**\n```text\n{module_data.get('prompts', {}).get('user', '')}\n```\n")
                f.write(f"**Output Schema:**\n```json\n{json.dumps(module_data.get('output_schema', {}), indent=2)}\n```\n")
                f.write("</details>\n\n")
                
                f.write("### 🤖 Resposta Gerada:\n")
                f.write(f"```json\n{json.dumps(result_data, indent=2, ensure_ascii=False)}\n```\n")
                f.write("\n---\n")

            # 1. TRAMA
            write_section("Fase 1: A Trama (V3)", mod_trama, trama, "📜")
            f.write(f"**Argumento:** {trama.get('argumento', {}).get('texto', 'N/A')}\n")
            f.write(f"**Premissa Oculta:** {trama.get('premissas', {}).get('oculta', {}).get('texto', 'N/A')}\n")
            f.write("**Matriz de Informação (Resumo):**\n")
            for item in trama.get('matriz_controle_informacao', {}).get('itens', []):
                f.write(f"- [ID {item.get('id')}] {item.get('titulo')}: {item.get('a_verdade')}\n")
            f.write("\n---\n")

            # 2. STEP 1
            write_section("Fase 2.1: Arquiteto (Palco)", mod_step1, frente['structure'], "🏛️")
            s1 = frente['structure']
            cabecalho = s1.get('cabecalho', {})
            f.write(f"**Arquétipo:** {cabecalho.get('arquetipo_selecionado')}\n")
            f.write(f"**Foco Narrativo:** {cabecalho.get('foco_narrativo')}\n")
            f.write("**Amostra de Locais (Sensorial):**\n")
            for loc in s1.get('lista_locais', [])[:3]: # Mostra 3 primeiros
                f.write(f"- **{loc.get('nome')}**: {loc.get('descricao')}\n")
            f.write("\n---\n")

            # 3. STEP 2
            write_section("Fase 2.2: Worldbuilder (Ameaças)", mod_step2, frente['world'], "🌍")
            s2 = frente['world']
            f.write(f"**Desastre Iminente:** {s2.get('desastre_iminente', {}).get('descricao')}\n")
            f.write("**Perigos:**\n")
            for p in s2.get('perigos', []):
                f.write(f"- {p.get('nome')} ({p.get('tipo')}): {p.get('descricao')}\n")
            f.write("\n---\n")

            # 4. STEP 3
            write_section("Fase 2.3: Storyteller (Linha do Tempo)", mod_step3, frente['story'], "🎬")
            s3 = frente['story']
            
            # Visualização Humana dos Presságios (Adaptado para Schema V2.5)
            f.write("### ⚔️ Visualização dos Presságios Terríveis\n")
            pressagios = s3.get('pressagios_terriveis', [])
            
            for p in pressagios:
                f.write(f"**{p.get('ordem')}. {p.get('meta_estrutura')}** (Local: {p.get('local_sugerido')})\n")
                f.write(f"> *{p.get('o_pressagio')}*\n\n")
                f.write(f"- **Evidente:** {p.get('premissas_cena', {}).get('evidente')}\n")
                f.write(f"- **Oculta:** {p.get('premissas_cena', {}).get('oculta')}\n")
                f.write(f"- **🧩 Conexão Matriz [ID {p.get('camada_informacao', {}).get('id_matriz')}]:** {p.get('camada_informacao', {}).get('conexao_explicada')}\n\n")

            f.write("\n### ❓ Perguntas Dramáticas\n")
            for q in s3.get('perguntas_dramatica', []):
                f.write(f"- {q}\n")

        logger.info(f"Relatório Completo gerado em: {filename}")

if __name__ == "__main__":
    unittest.main()