import unittest
import time
import sys
import os

# Garante que o diretório raiz do projeto esteja no path para importações
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from base_test import BaseFlowTest

class TestFluxoTrama(BaseFlowTest):
    """
    Suíte de testes para o módulo 'core_trama_generator'.
    
    Objetivo:
        Validar a geração da Trama Central (o esqueleto da aventura) e garantir
        que o sistema 'Data-Driven' (output_mapping) está salvando os dados
        corretamente no game_state sem intervenção manual.
    """

    def setUp(self):
        """
        Configuração do Ambiente de Teste (Fixture).
        
        Ações:
            1. Inicializa o GameController (via super().setUp()).
            2. Define 'Seeds' (Sementes) fixas para remover a aleatoriedade do input.
            3. Carrega o cenário 'dieselpunk' para fornecer o contexto (Gênero, Locais).
        """
        super().setUp()
        
        # Seeds mockadas: Garantem que o prompt gerado seja sempre sobre "transmissão fantasma"
        self.seeds_mock = {
            "col1_event": "Uma transmissão fantasma foi captada",
            "col2_goal": "Decifrar o código antes da invasão",
            "col3_consequence": "A cidade será bombardeada"
        }
        
        print(f"[SETUP] Iniciando jogo 'dieselpunk' para teste de Trama...")
        try:
            self.controller.start_new_game("dieselpunk", seed_data=self.seeds_mock)
        except FileNotFoundError:
            # Fallback de segurança para execução via CLI em diretórios diferentes
            self.controller.start_new_game("scenarios/dieselpunk", seed_data=self.seeds_mock)

    def test_geracao_trama_validacao_schema(self):
        """
        Teste de Integração: Geração e Persistência da Trama.
        
        Fluxo:
            1. Executa o módulo 'core_trama_generator' usando 'execute_and_apply'.
            2. Captura métricas de tempo e debug.
            3. Valida se o JSON retornado obedece ao Schema esperado.
            4. CRÍTICO: Valida se os dados foram salvos automaticamente em 'adventure.trama'.
        """
        print("\n=== TESTE: Geração de Trama (Data-Driven) ===")
        start = time.time()
        
        # 1. Execução Automática
        # O controlador não recebe o resultado para salvar manual. 
        # Ele delega para o ModuleExecutor ler o 'output_mapping' do JSON.
        trama_result = self.controller.module_executor.execute_and_apply(
            "core_trama_generator", 
            self.controller.game_state
        )
        
        duration = time.time() - start
        
        # 2. Rastreamento para Relatório
        # CORREÇÃO AQUI: Precisamos injetar o 'response_content' no debug_data
        # para que o base_test.py saiba renderizar o JSON no Markdown.
        debug_data = self.controller.module_executor.last_prompt_debug.copy()
        debug_data['response_content'] = trama_result 
        
        self.track_step("1. Core Trama Generator", duration, debug_data=debug_data)

        # 3. Asserções (Validações)
        self.assertIsNotNone(trama_result, "Falha: O módulo retornou None.")
        
        # Valida estrutura macro do JSON
        self.assertIn("configuracao_aventura", trama_result, "JSON inválido: Faltando 'configuracao_aventura'")
        self.assertIn("argumento", trama_result, "JSON inválido: Faltando 'argumento'")
        self.assertIn("matriz_controle_informacao", trama_result, "JSON inválido: Faltando 'matriz'")

        # === VALIDAÇÃO DE PERSISTÊNCIA (Data-Driven) ===
        # Verifica se o valor apareceu no game_state na chave correta ("adventure.trama")
        state_trama = self.controller.game_state["adventure"].get("trama")
        self.assertIsNotNone(state_trama, "ERRO CRÍTICO: O output_mapping falhou. Dados não persistidos no game_state.")
        
        # Compara o dado retornado com o dado salvo para garantir integridade
        self.assertEqual(
            state_trama["argumento"]["texto"], 
            trama_result["argumento"]["texto"], 
            "Inconsistência: O dado retornado difere do dado salvo no estado."
        )

        # === VALIDAÇÃO DE REGRA DE NEGÓCIO ===
        # Verifica se a mudança de "escopo_selecionado" para "escopo" foi aplicada corretamente
        config = trama_result["configuracao_aventura"]
        self.assertIn("escopo", config, "Schema antigo detectado: Campo 'escopo' ausente.")
        self.assertNotIn("escopo_selecionado", config, "Schema sujo: Campo antigo 'escopo_selecionado' ainda existe.")

        print("[OK] Trama gerada e persistida com sucesso.")

        # Geração do Relatório Markdown
        self.generate_report(title="Teste de Trama V4 (Data-Driven)")

if __name__ == "__main__":
    unittest.main()