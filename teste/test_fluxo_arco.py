import unittest
import time
import sys
import os

# Adiciona o diretório pai ao path para importação correta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from base_test import BaseFlowTest

class TestFluxoArco(BaseFlowTest):

    def setUp(self):
        """
        Configuração do teste:
        Carrega o cenário REAL 'dieselpunk' para garantir o preenchimento correto
        do contexto (Context) para todas as etapas.
        """
        super().setUp()
        
        # Seeds controladas para manter consistência nos testes
        seeds_mock = {
            "col1_event": "Uma carga valiosa foi roubada",
            "col2_goal": "Recuperar a carga antes do amanhecer",
            "col3_consequence": "Guerra entre gangues rivais"
        }
        
        print(f"[SETUP] Carregando cenário 'dieselpunk' com seeds de teste...")
        
        try:
            self.controller.start_new_game("dieselpunk", seed_data=seeds_mock)
        except FileNotFoundError:
            print("[WARN] Tentando caminho alternativo para scenarios...")
            self.controller.start_new_game("scenarios/dieselpunk", seed_data=seeds_mock)

    def _track_with_response(self, step_name, start_time, result):
        """
        Helper para capturar métricas e a resposta gerada para o relatório.
        """
        duration = time.time() - start_time
        
        # Copia debug da última chamada do executor
        debug_data = self.controller.module_executor.last_prompt_debug.copy() if self.controller.module_executor.last_prompt_debug else {}
        
        # Injeta o resultado final no debug para visualização no Markdown
        debug_data['response_content'] = result
        
        self.track_step(step_name, duration, debug_data=debug_data)

    def test_pipeline_completo_com_arco(self):
        """
        Executa o pipeline completo:
        Trama -> Frente (Steps 1, 2, 3) -> Arco de História (Step 4).
        Valida se os dados fluem corretamente até a geração das cenas.
        """
        print(">>> INICIANDO TESTE: PIPELINE COMPLETO ATÉ O ARCO <<<")

        # Garante estrutura base
        if "adventure" not in self.controller.game_state:
            self.controller.game_state["adventure"] = {}

        # =========================================================================
        # 1. TRAMA
        # =========================================================================
        start = time.time()
        print("[1/5] Gerando Trama...")
        trama_result = self.controller.step_generate_trama()
        
        # Atualiza Estado
        self.controller.game_state["adventure"]["trama"] = trama_result
        self._track_with_response("1. Trama", start, trama_result)
        
        self.assertIsNotNone(trama_result, "Trama falhou.")

        # =========================================================================
        # 2. FRENTE STEP 1 (Arquétipo)
        # =========================================================================
        start = time.time()
        print("[2/5] Step 1 (Arquétipo)...")
        
        self.controller.game_state["adventure"].setdefault("front", {})
        
        step1 = self.controller.module_executor.execute(
            "step1_front_archetype", 
            self.controller.game_state
        )
        
        self.controller.game_state["adventure"]["front"]["step1"] = step1
        self._track_with_response("2. Front Arquiteto", start, step1)
        
        self.assertIsNotNone(step1, "Step 1 falhou.")

        # =========================================================================
        # 3. FRENTE STEP 2 (Worldbuilder)
        # =========================================================================
        start = time.time()
        print("[3/5] Step 2 (Worldbuilder)...")
        
        step2 = self.controller.module_executor.execute(
            "step2_front_worldbuilder", 
            self.controller.game_state
        )
        
        self.controller.game_state["adventure"]["front"]["step2"] = step2
        self._track_with_response("3. Front World", start, step2)
        
        self.assertIsNotNone(step2, "Step 2 falhou.")

        # =========================================================================
        # 4. FRENTE STEP 3 (Storyteller)
        # =========================================================================
        start = time.time()
        print("[4/5] Step 3 (Storyteller)...")
        
        step3 = self.controller.module_executor.execute(
            "step3_front_storyteller", 
            self.controller.game_state
        )
        
        self.controller.game_state["adventure"]["front"]["step3"] = step3
        self._track_with_response("4. Front Story", start, step3)
        
        self.assertIsNotNone(step3, "Step 3 falhou.")

        # =========================================================================
        # 5. ARCO DE HISTÓRIA (NOVO TESTE)
        # =========================================================================
        start = time.time()
        print("[5/5] Executando Step 4 (Arco de História)...")
        
        # O módulo 'step4_arc_builder' consome dados da Trama e da Frente (Steps 1 e 2)
        # Verifique 'arco_historia.json' para ver o input_mapping completo.
        
        step4 = self.controller.module_executor.execute(
            "step4_arc_builder", 
            self.controller.game_state
        )
        
        # Salva o resultado no estado (pode ser usado por passos futuros)
        self.controller.game_state["adventure"]["arc"] = step4
        
        # Registra métricas
        self._track_with_response("5. Arco História", start, step4)

        # Validações Específicas do Arco
        self.assertIsNotNone(step4, "Step 4 (Arco) retornou None")
        self.assertIn("cabecalho_arco", step4, "Resposta do Arco sem cabeçalho.")
        self.assertIn("lista_cenas", step4, "Resposta do Arco sem lista de cenas.")
        
        # Verifica se gerou cenas
        cenas = step4.get("lista_cenas", [])
        self.assertTrue(len(cenas) > 0, "A lista de cenas está vazia.")
        
        print(f"    > Arco gerado com {len(cenas)} cenas.")

        # =========================================================================
        # RELATÓRIO FINAL
        # =========================================================================
        self.generate_report(title="Teste Pipeline Completo: Trama -> Frente -> Arco")

if __name__ == "__main__":
    unittest.main()