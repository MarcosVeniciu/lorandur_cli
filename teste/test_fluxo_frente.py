import unittest
import time
import sys
import os

# Adiciona o diretório pai ao path para importação correta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from base_test import BaseFlowTest

class TestFluxoFrente(BaseFlowTest):
    """
    Suíte de testes para o Pipeline da Frente de Aventura.
    
    FLUXO COMPLETO (End-to-End):
    Este teste executa desde a geração da Trama até a conclusão da Frente.
    Todos os passos são registrados no relatório para validação integral dos dados.
    """

    def setUp(self):
        """
        Configuração do teste:
        Carrega apenas o cenário e as seeds. 
        A execução dos módulos de IA foi movida para o teste principal para fins de relatório.
        """
        super().setUp()
        
        # Seeds controladas
        self.seeds_mock = {
            "col1_event": "Uma carga valiosa foi roubada",
            "col2_goal": "Recuperar a carga antes do amanhecer",
            "col3_consequence": "Guerra entre gangues rivais"
        }
        
        print(f"[SETUP] Carregando cenário 'dieselpunk'...")
        try:
            self.controller.start_new_game("dieselpunk", seed_data=self.seeds_mock)
        except FileNotFoundError:
            self.controller.start_new_game("scenarios/dieselpunk", seed_data=self.seeds_mock)

    def _track_with_response(self, step_name, start_time, result):
        """Helper para registrar métricas e injetar a resposta no relatório."""
        duration = time.time() - start_time
        debug = self.controller.module_executor.last_prompt_debug.copy()
        debug['response_content'] = result 
        self.track_step(step_name, duration, debug_data=debug)

    def test_pipeline_frente_completo(self):
        """
        Executa a cadeia completa: Trama -> Frente Step 1 -> Step 2 -> Step 3.
        Gera um relatório unificado contendo todo o contexto criativo.
        """
        print("\n=== INICIANDO PIPELINE DE FRENTE (Fluxo Completo) ===")

        # =========================================================================
        # 0. PRÉ-REQUISITO: TRAMA
        # =========================================================================
        print("[1/4] Gerando Trama Base (Dependência)...")
        start = time.time()
        
        trama_result = self.controller.module_executor.execute_and_apply(
            "core_trama_generator", 
            self.controller.game_state
        )
        
        self._track_with_response("1. Trama (Contexto)", start, trama_result)
        self.assertIsNotNone(trama_result, "Falha ao gerar Trama.")

        # =========================================================================
        # 1. FRENTE STEP 1 (Arquétipo e Locais)
        # =========================================================================
        print("[2/4] Executando Step 1 (Arquétipo)...")
        start = time.time()
        
        step1 = self.controller.module_executor.execute_and_apply(
            "step1_front_archetype", 
            self.controller.game_state
        )
        
        self._track_with_response("2. Front Archetype", start, step1)
        self.assertIsNotNone(step1)

        # =========================================================================
        # 2. FRENTE STEP 2 (Worldbuilder: Ameaças)
        # =========================================================================
        print("[3/4] Executando Step 2 (Worldbuilder)...")
        start = time.time()
        
        step2 = self.controller.module_executor.execute_and_apply(
            "step2_front_worldbuilder", 
            self.controller.game_state
        )
        
        self._track_with_response("3. Front World", start, step2)
        self.assertIsNotNone(step2)

        # =========================================================================
        # 3. FRENTE STEP 3 (Storyteller: Presságios)
        # =========================================================================
        print("[4/4] Executando Step 3 (Storyteller)...")
        start = time.time()
        
        step3 = self.controller.module_executor.execute_and_apply(
            "step3_front_storyteller", 
            self.controller.game_state
        )
        
        self._track_with_response("4. Front Story", start, step3)
        self.assertIsNotNone(step3)

        print("[OK] Pipeline de Frente concluído e dados integrados.")

        # Relatório Final
        self.generate_report(title="Teste Completo: Frente Pipeline (Com Trama)")

if __name__ == "__main__":
    unittest.main()