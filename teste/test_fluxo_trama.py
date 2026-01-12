import unittest
import time
import sys
import os

# Adiciona o diretório pai ao path para importação correta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa a base que você acabou de fornecer
from base_test import BaseFlowTest

class TestFluxoTrama(BaseFlowTest):

    def setUp(self):
        """
        Configuração do teste:
        Inicializa o controlador e carrega um cenário com Seeds fixas para reprodutibilidade.
        """
        super().setUp()
        
        # Seeds mockadas para garantir consistência no teste
        self.seeds_mock = {
            "col1_event": "Uma transmissão fantasma foi captada",
            "col2_goal": "Decifrar o código antes da invasão",
            "col3_consequence": "A cidade será bombardeada"
        }
        
        print(f"[SETUP] Iniciando jogo 'dieselpunk' para teste de Trama...")
        try:
            self.controller.start_new_game("dieselpunk", seed_data=self.seeds_mock)
        except FileNotFoundError:
            # Fallback caso o script seja rodado de um diretório diferente
            self.controller.start_new_game("scenarios/dieselpunk", seed_data=self.seeds_mock)

    def test_geracao_trama_validacao_schema(self):
        """
        Teste focado na geração da Trama e validação rigorosa dos campos novos
        (especialmente a mudança de 'escopo_selecionado' para 'escopo').
        """
        print(">>> INICIANDO TESTE: GERAÇÃO DE TRAMA (Schema V4) <<<")

        start = time.time()
        
        # 1. Execução
        trama_result = self.controller.step_generate_trama()
        duration = time.time() - start

        # 2. Coleta de Debug para Relatório
        # Pega os dados técnicos do executor
        debug_data = self.controller.module_executor.last_prompt_debug.copy() if self.controller.module_executor.last_prompt_debug else {}
        
        # [CORREÇÃO] Injeta a resposta dentro do debug_data para ser lida pelo base_test.py
        debug_data['response_content'] = trama_result
        
        # 3. Rastreamento (Métricas + Resposta)
        self.track_step("1. Core Trama Generator", duration, debug_data=debug_data)

        # 4. Validações (Assertions)
        self.assertIsNotNone(trama_result, "A Trama retornou None (falha na geração).")
        
        # Validação da Estrutura Principal
        self.assertIn("configuracao_aventura", trama_result)
        self.assertIn("argumento", trama_result)
        self.assertIn("matriz_controle_informacao", trama_result)

        # === VALIDAÇÃO CRÍTICA DO ESCOPO ===
        config = trama_result["configuracao_aventura"]
        
        # Verifica se o campo NOVO existe (se você atualizou o trama.json)
        self.assertIn("escopo", config, 
            "ERRO: O campo 'escopo' não foi encontrado. Verifique se o trama.json foi atualizado para 'escopo'.")
        
        # Verifica se o campo ANTIGO foi removido
        self.assertNotIn("escopo_selecionado", config, 
            "ERRO: O campo 'escopo_selecionado' ainda existe. O Schema não está rejeitando propriedades adicionais.")

        # Validação de Conteúdo (Sanity Check)
        self.assertTrue(len(config["subgeneros_selecionados"]) >= 1)
        self.assertTrue(len(trama_result["matriz_controle_informacao"]["itens"]) >= 3)

        print("[OK] Validação de Schema (Escopo) aprovada.")

        # 5. Geração do Relatório
        self.generate_report(title="Teste de Unidade: Trama Generator (V4.0 - Schema Strict)")

if __name__ == "__main__":
    unittest.main()