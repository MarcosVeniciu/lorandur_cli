import unittest
import time
import sys
import os

# Adiciona o diretório pai ao path para importação correta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from base_test import BaseFlowTest

class TestFluxoFrente(BaseFlowTest):

    def setUp(self):
        """
        Configuração do teste:
        Carrega o cenário REAL 'dieselpunk' para garantir que listas de
        locais, arquétipos e escopos estejam populadas corretamente no Contexto.
        """
        super().setUp()
        
        # Seeds controladas para o teste (Mock apenas da aleatoriedade)
        seeds_mock = {
            "col1_event": "Uma carga valiosa foi roubada",
            "col2_goal": "Recuperar a carga antes do amanhecer",
            "col3_consequence": "Guerra entre gangues rivais"
        }
        
        print(f"[SETUP] Carregando cenário 'dieselpunk' com seeds de teste...")
        
        try:
            self.controller.start_new_game("dieselpunk", seed_data=seeds_mock)
        except FileNotFoundError:
            # Fallback caso o script seja rodado de um diretório diferente
            print("[WARN] Tentando caminho alternativo para scenarios...")
            self.controller.start_new_game("scenarios/dieselpunk", seed_data=seeds_mock)

    def _track_with_response(self, step_name, start_time, result):
        """
        Helper privado para capturar o debug completo + a resposta do modelo
        e enviar para o sistema de relatório.
        """
        duration = time.time() - start_time
        
        # Copia os dados de debug do último prompt executado (Usage, Prompts, Schema)
        debug_data = self.controller.module_executor.last_prompt_debug.copy() if self.controller.module_executor.last_prompt_debug else {}
        
        # Injeta a resposta estruturada para aparecer no relatório
        debug_data['response_content'] = result
        
        self.track_step(step_name, duration, debug_data=debug_data)

    def test_full_sequence_granular(self):
        """
        Executa Trama -> Frente Step 1 -> Step 2 -> Step 3.
        Mede o tempo e custo de cada etapa individualmente e registra as respostas.
        """
        print(">>> INICIANDO TESTE: FLUXO COMPLETO (GRANULAR) <<<")

        # Garante que a estrutura base 'adventure' existe (caso start_new_game não crie)
        if "adventure" not in self.controller.game_state:
            self.controller.game_state["adventure"] = {}

        # =========================================================================
        # 1. TRAMA (Gera Argumento, Premissas e Matriz)
        # =========================================================================
        start = time.time()
        print("[1/4] Gerando Trama...")
        trama_result = self.controller.step_generate_trama()
        
        # CORREÇÃO CRÍTICA 1: Forçar atualização do estado com o resultado da Trama.
        # Sem isso, os passos seguintes veem [N/A] nos campos de argumento/premissas.
        self.controller.game_state["adventure"]["trama"] = trama_result
        
        # Registra métricas + resposta
        self._track_with_response("1. Trama", start, trama_result)

        # Validação básica
        self.assertIsNotNone(trama_result, "Trama retornou None")
        self.assertIn("matriz_controle_informacao", trama_result)

        # =========================================================================
        # 2. FRENTE STEP 1 (Arquétipo & Locais)
        # =========================================================================
        start = time.time()
        print("[2/4] Executando Step 1 (Arquétipo)...")
        
        # CORREÇÃO CRÍTICA 2: Garantir que a chave 'front' existe antes de atribuir
        self.controller.game_state["adventure"].setdefault("front", {})

        step1 = self.controller.module_executor.execute(
            "step1_front_archetype", 
            self.controller.game_state
        )
        
        # Atualiza o estado
        self.controller.game_state["adventure"]["front"]["step1"] = step1
        
        # Registra métricas + resposta
        self._track_with_response("2. Front Arquiteto", start, step1)

        self.assertIsNotNone(step1, "Step 1 retornou None")

        # =========================================================================
        # 3. FRENTE STEP 2 (Worldbuilder: Elenco & Perigos)
        # =========================================================================
        start = time.time()
        print("[3/4] Executando Step 2 (Worldbuilder)...")
        
        # O Step 2 usa dados de "adventure.front.step1" (garantido acima)
        # e "adventure.trama" (garantido na correção 1)
        
        step2 = self.controller.module_executor.execute(
            "step2_front_worldbuilder", 
            self.controller.game_state
        )
        
        self.controller.game_state["adventure"]["front"]["step2"] = step2
        
        # Registra métricas + resposta
        self._track_with_response("3. Front World", start, step2)
        
        self.assertIsNotNone(step2, "Step 2 retornou None")

        # =========================================================================
        # 4. FRENTE STEP 3 (Storyteller: Presságios)
        # =========================================================================
        start = time.time()
        print("[4/4] Executando Step 3 (Storyteller)...")
        
        # O Step 3 usa dados de "adventure.front.step2" (garantido acima)
        
        step3 = self.controller.module_executor.execute(
            "step3_front_storyteller", 
            self.controller.game_state
        )
        
        self.controller.game_state["adventure"]["front"]["step3"] = step3
        
        # Registra métricas + resposta
        self._track_with_response("4. Front Story", start, step3)
        
        self.assertIsNotNone(step3, "Step 3 retornou None")

        # =========================================================================
        # RELATÓRIO FINAL
        # =========================================================================
        self.generate_report(title="Teste Completo: Trama & Frente Pipeline (Com Respostas)")

if __name__ == "__main__":
    unittest.main()