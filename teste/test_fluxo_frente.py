import unittest
import asyncio
import os
import json
import logging
import sys
from datetime import datetime

# === CORREÇÃO DE IMPORTAÇÃO ===
# Adiciona o diretório pai (raiz do projeto) ao sys.path para encontrar game_controller
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_controller import GameController

# Configuração de Logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TestFluxoCompleto")

class TestFluxoCompleto(unittest.TestCase):
    """
    Teste de Integração TOTAL (End-to-End).
    Executa sequencialmente:
    1. Trama (Geração da semente)
    2. Frente Step 1 (Arquiteto)
    3. Frente Step 2 (Worldbuilder)
    4. Frente Step 3 (Storyteller)
    
    Gera um relatório contendo Prompts e Respostas para auditoria.
    """

    def setUp(self):
        self.controller = GameController()
        
        # === 1. DEFINIÇÃO DO CONTEXTO INICIAL ===
        # Não mockamos a Trama. Apenas definimos o Gênero e o Mundo.
        self.context_input = {
            "genre": "Dieselpunk",
            "available_locations_str": "Fábrica de Autômatos, Estação de Trem Blindada, Bar Clandestino (Speakeasy), Hangar de Zeppelins, Torre de Rádio da Propaganda, Esgotos de Óleo, Mansão do Barão, Doca de Carregamento",
            "available_archetypes_str": "Veterano da Grande Guerra, Mecânico de Autômatos, Espião Corporativo, Cientista Louco, Aristocrata Decadente, Líder Operário",
            "runtime": {
                "full_scope_description": "A Cidade-Fornalha de Ferrus. Uma distopia industrial onde a fumaça cobre o sol. A elite vive em torres de vidro acima da fuligem, enquanto os trabalhadores operam as grandes máquinas no nível da rua. Há rumores de que o combustível 'Éter Negro' é feito de pessoas.",
                "formatted_matrix": (
                    "1. O Barão de Ferro está morto há anos; uma IA analógica controla sua voz.\n"
                    "2. O carregamento de 'Carvão Azul' é, na verdade, almas cristalizadas.\n"
                    "3. A Resistência foi infiltrada pela polícia secreta (Gestapo de Ferro) desde o início.\n"
                    "4. A Doca 7 esconde o protótipo de uma bomba de antimatéria."
                )
            }
        }
        self.controller.update_context(self.context_input)

    def test_full_sequence_execution(self):
        """Executa a cadeia completa de geração e valida o fluxo de dados."""
        logger.info(">>> Iniciando Sequência Completa de Geração...")

        # Loop de Eventos para chamadas assíncronas
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            # === FASE 1: GERAR TRAMA ===
            logger.info(">>> [1/4] Executando Módulo Trama...")
            # Assumindo que o ID do módulo de trama é 'trama'
            trama_result = loop.run_until_complete(
                self.controller.module_executor.execute_module("trama", self.controller.game_state)
            )
            self.assertIsNotNone(trama_result, "A Trama não deve ser nula.")
            
            # Atualiza o estado com a Trama gerada (Input real para a Frente)
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
            logger.info("✓ Pipeline da Frente concluído com sucesso.")

            # === RELATÓRIO ===
            self._generate_detailed_report(trama_result, front_result)

        finally:
            loop.close()

    def _get_module_data(self, module_filename):
        """Lê o arquivo JSON do módulo para extrair Prompts e Schema."""
        try:
            # Caminho corrigido para buscar modules_source a partir da raiz
            root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
            path = os.path.join(root_path, "modules_source", module_filename)
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Não foi possível ler o arquivo do módulo {module_filename}: {e}")
            return {"prompts": {"system": "Erro ao ler arquivo", "user": "Erro ao ler arquivo"}, "output_schema": {}}

    def _generate_detailed_report(self, trama, frente):
        """Gera Markdown combinando Prompts usados e Respostas geradas."""
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M")
        # Garante que a pasta existe no caminho correto
        root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        report_dir = os.path.join(root_path, "teste", "relatorios_teste")
        os.makedirs(report_dir, exist_ok=True)
        
        filename = os.path.join(report_dir, f"full_flow_{timestamp}.md")

        # Carrega dados brutos dos módulos para exibição
        mod_trama = self._get_module_data("trama.json")
        mod_step1 = self._get_module_data("frente_step1_archetype.json")
        mod_step2 = self._get_module_data("frente_step2_worldbuilder.json")
        mod_step3 = self._get_module_data("frente_step3_storyteller.json")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Relatório Completo: Fluxo Trama -> Frente (V5)\n")
            f.write(f"**Data:** {timestamp} | **Gênero:** {self.context_input['genre']}\n")
            f.write(f"**Escopo:** {self.context_input['runtime']['full_scope_description']}\n\n")
            
            # helper para escrever seções
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
            write_section("Fase 1: A Trama", mod_trama, trama, "📜")
            
            # Visualização Humana da Trama
            f.write(f"**Resumo Trama:** {trama.get('argumento', {}).get('texto', 'N/A')}\n")
            f.write(f"**Premissa Oculta:** {trama.get('premissas', {}).get('oculta', {}).get('texto', 'N/A')}\n")
            f.write("\n---\n")

            # 2. STEP 1
            write_section("Fase 2.1: Arquiteto (Estrutura)", mod_step1, frente['structure'], "🏛️")
            s1 = frente['structure']
            f.write(f"**Arquétipo:** {s1.get('analise_arquetipica', {}).get('arquetipo_selecionado')}\n")
            f.write(f"**Justificativa:** {s1.get('racional_criativo', {}).get('motivo_escolha')}\n")
            f.write("\n---\n")

            # 3. STEP 2
            write_section("Fase 2.2: Worldbuilder (Ativos)", mod_step2, frente['world'], "🌍")
            
            # 4. STEP 3
            write_section("Fase 2.3: Storyteller (Presságios)", mod_step3, frente['story'], "🎬")
            
            # Visualização Humana dos Presságios (Mini-Arcos)
            s3 = frente['story']
            f.write("### ⚔️ Visualização Final dos Presságios\n")
            for p in s3.get('pressagios_sequencia', []):
                f.write(f"**{p.get('ordem')}. {p.get('titulo_pressagio')}** ({p.get('fase_meta_estrutura')})\n")
                f.write(f"> *{p.get('descricao_mini_arco')}*\n\n")
                f.write(f"- **Evidente:** {p.get('camadas_realidade', {}).get('premissa_evidente')}\n")
                f.write(f"- **Oculto:** {p.get('camadas_realidade', {}).get('premissa_oculta')}\n")
                f.write(f"- **Justificativa:** {p.get('camadas_realidade', {}).get('justificativa_dualidade')}\n\n")

        logger.info(f"Relatório Completo gerado em: {filename}")

if __name__ == "__main__":
    unittest.main()