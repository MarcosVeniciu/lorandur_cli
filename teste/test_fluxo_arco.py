import unittest
import time
import sys
import os

# Adiciona o diretório pai ao path para importação correta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from base_test import BaseFlowTest

class TestFluxoArco(BaseFlowTest):
    """
    Suíte de testes para o módulo 'step4_arc_builder'.
    
    FLUXO COMPLETO (End-to-End):
    Este teste simula uma sessão real de criação do zero.
    Executa: Trama -> Frente (1, 2, 3) -> Arco.
    """

    def setUp(self):
        super().setUp()
        
        seeds_mock = {
            "col1_event": "Uma carga valiosa foi roubada",
            "col2_goal": "Recuperar a carga antes do amanhecer",
            "col3_consequence": "Guerra entre gangues rivais"
        }
        
        print(f"[SETUP] Carregando cenário 'dieselpunk'...")
        try:
            self.controller.start_new_game("dieselpunk", seed_data=seeds_mock)
        except FileNotFoundError:
            self.controller.start_new_game("scenarios/dieselpunk", seed_data=seeds_mock)

    def _track_with_response(self, step_name, start_time, result):
        duration = time.time() - start_time
        debug = self.controller.module_executor.last_prompt_debug.copy()
        debug['response_content'] = result 
        self.track_step(step_name, duration, debug_data=debug)

    def test_geracao_arco_historia_full_trace(self):
        """
        Gera toda a árvore genealógica da aventura (Trama -> Frente -> Arco).
        """
        print("\n=== TESTE: Geração de Arco de História (Trace Completo) ===")
        
        # 1. TRAMA
        print("[1/5] Gerando Trama...")
        start = time.time()
        self.controller.module_executor.execute_and_apply("core_trama_generator", self.controller.game_state)
        self._track_with_response("1. Trama", start, self.controller.game_state["adventure"]["trama"])
        
        # 2. FRENTE 1
        print("[2/5] Gerando Frente (Arquétipo)...")
        start = time.time()
        self.controller.module_executor.execute_and_apply("step1_front_archetype", self.controller.game_state)
        self._track_with_response("2. Frente Step 1", start, self.controller.game_state["adventure"]["front"]["step1"])

        # 3. FRENTE 2
        print("[3/5] Gerando Frente (World)...")
        start = time.time()
        self.controller.module_executor.execute_and_apply("step2_front_worldbuilder", self.controller.game_state)
        self._track_with_response("3. Frente Step 2", start, self.controller.game_state["adventure"]["front"]["step2"])

        # 4. FRENTE 3
        print("[4/5] Gerando Frente (Story)...")
        start = time.time()
        self.controller.module_executor.execute_and_apply("step3_front_storyteller", self.controller.game_state)
        self._track_with_response("4. Frente Step 3", start, self.controller.game_state["adventure"]["front"]["step3"])

        # 5. ARCO (O TESTE PRINCIPAL)
        print("[5/5] Gerando Arco de História...")
        start = time.time()
        
        step4 = self.controller.module_executor.execute_and_apply(
            "step4_arc_builder", 
            self.controller.game_state
        )
        
        self._track_with_response("5. Arco História", start, step4)

        # Validações
        self.assertIsNotNone(step4, "Step 4 (Arco) retornou None")
        state_arc = self.controller.game_state["adventure"].get("arc")
        self.assertIsNotNone(state_arc, "Dados do Arco não foram persistidos.")
        
        cenas = step4.get("lista_cenas", [])
        self.assertTrue(len(cenas) > 0)
        
        print(f"    > Arco gerado com {len(cenas)} cenas.")

        # Validação de Detalhamento
        if len(cenas) >= 1:
            self.assertEqual(cenas[0]["tipo_detalhamento"], "Detalhado")
        if len(cenas) >= 3:
            self.assertEqual(cenas[2]["tipo_detalhamento"], "Esboco")

        print("[OK] Ciclo de vida completo validado.")

        self.generate_report(title="Teste Completo: Trama -> Frente -> Arco")

if __name__ == "__main__":
    unittest.main()