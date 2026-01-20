import asyncio
import logging
import os
import json
import time
from typing import Dict, Any, Optional

from engine.module_executor import ModuleExecutor
from database.db_manager import DBManager
from utils.debug_logger import DebugLogger
from utils.file_manager import FileManager

class GameController:
    """
    Controlador Principal (Maestro) do fluxo do jogo.
    
    Responsabilidade:
        - Gerenciar o ciclo de vida da sessão (Start, Save, Load).
        - Manter a "Fonte Única da Verdade" (game_state).
        - Orquestrar chamadas de alto nível para o ModuleExecutor.
    
    Refatoração Data-Driven:
        Esta classe NÃO define mais a estrutura interna dos dados de aventura.
        Ela delega o armazenamento para o 'ModuleExecutor', que segue as regras
        de 'output_mapping' dos JSONs.
    """
    
    def __init__(self):
        self.db_manager = DBManager()
        self.module_executor = ModuleExecutor()
        self.file_manager = FileManager()
        self.logger = logging.getLogger("GameController")
        self.debug_logger = DebugLogger()
        
        # Estado Inicial Base
        # Define apenas a raiz. A estrutura interna cresce organicamente.
        self.game_state = {
            "context": {
                "genre": "",
                "seeds": {},
                "supported_scopes_str": "",
                "available_locations_str": "",
                "available_archetypes_str": "",
                "runtime": {
                    "full_scope_description": "",
                    "formatted_matrix": ""
                }
            },
            "adventure": {} 
        }
        self._reset_adventure_state()

    def _reset_adventure_state(self):
        """
        Reseta a estrutura de aventura.
        Apenas limpa a raiz 'adventure' e define status inicial.
        """
        self.game_state["adventure"] = {
            "trama": {},
            "front": {
                "status": "pending"
            }
        }

    async def initialize(self):
        """Setup assíncrono (se necessário no futuro)."""
        self.logger.info("Inicializando GameController...")
        pass

    def start_new_game(self, scenario_name: str, seed_data: Dict[str, Any] = None):
        """
        Inicia uma nova sessão de jogo.
        
        1. Limpa estado anterior.
        2. Carrega configuração do cenário (JSON).
        3. Prepara strings de contexto para os prompts.
        """
        self.logger.info(f"Iniciando novo jogo: {scenario_name}")
        
        # 1. Limpeza de Estado Anterior
        self._reset_adventure_state()
        
        # 2. Carregar Cenário
        scenario_data = self.file_manager.load_json(f"{scenario_name}.json", subdir="scenarios")
        
        if not scenario_data:
            # Fallback de busca
            if os.path.exists(f"scenarios/{scenario_name}.json"):
                with open(f"scenarios/{scenario_name}.json", 'r', encoding='utf-8') as f:
                    scenario_data = json.load(f)
            else:
                raise FileNotFoundError(f"Cenário '{scenario_name}' não encontrado.")

        # 3. Popula Contexto Básico (Genre, Scopes, Locais)
        self.game_state["context"]["genre"] = scenario_data.get("genre", "Generic")
        self.game_state["context"]["supported_scopes_str"] = "\n".join(scenario_data.get("supported_scopes", []))
        
        # Formata listas como strings para injeção direta em prompts
        locs = scenario_data.get("locations", [])
        archs = scenario_data.get("archetypes", [])
        self.game_state["context"]["available_locations_str"] = ", ".join(locs) if isinstance(locs, list) else str(locs)
        self.game_state["context"]["available_archetypes_str"] = ", ".join(archs) if isinstance(archs, list) else str(archs)

        # 4. Seeds (Dados aleatórios de entrada, ex: Dominus)
        if seed_data:
            self.game_state["context"]["seeds"] = seed_data
        
        self.logger.info("Contexto inicial configurado com sucesso.")

    def step_generate_trama(self) -> Dict[str, Any]:
        """
        Passo 1: Geração da Trama Central.
        
        Executa o módulo 'core_trama_generator'.
        NOTA: Não salva manualmente o resultado. O 'execute_and_apply' 
        lê o output_mapping do JSON e salva em 'adventure.trama' automaticamente.
        """
        self.logger.info(">>> Gerando Trama...")
        
        trama_result = self.module_executor.execute_and_apply(
            "core_trama_generator", 
            self.game_state
        )
        
        if not trama_result:
            raise Exception("Falha na geração da Trama.")
        
        self.debug_logger.log_step("Trama Gerada", trama_result)
        
        return trama_result

    def update_context(self, context_data: Dict[str, Any]):
        """Atualiza variáveis de contexto manualmente (se necessário)."""
        for key, value in context_data.items():
            if key in self.game_state["context"]:
                if isinstance(self.game_state["context"][key], dict) and isinstance(value, dict):
                    self.game_state["context"][key].update(value)
                else:
                    self.game_state["context"][key] = value
        
        self.logger.info(f"Contexto atualizado. Genre: {self.game_state['context'].get('genre')}")

    def save_game(self, filename: str = None):
        """Serializa e salva o game_state atual em disco."""
        if not filename:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"save_{timestamp}.json"
        
        os.makedirs("saves", exist_ok=True)
        self.file_manager.save_json(filename, self.game_state, subdir="saves")
        print(f"[GameController] Jogo salvo em: saves/{filename}")

    def load_game(self, filename: str):
        """Carrega um game_state do disco e restaura a sessão."""
        data = self.file_manager.load_json(filename, subdir="saves")
        if data:
            self.game_state = data
            print(f"[GameController] Jogo carregado: {filename}")
        else:
            print("[GameController] Erro ao carregar save.")

    async def generate_adventure_front_pipeline(self) -> Dict[str, Any]:
        """
        Executa o Pipeline da Frente de Aventura (Steps 1, 2 e 3).
        
        Fluxo:
            1. Arquétipo & Locais
            2. Worldbuilding & Ameaças
            3. Storytelling & Presságios
            
        O Controller apenas comanda a sequência. A passagem de dados entre
        os passos ocorre via game_state (Input Mapping -> Output Mapping).
        """
        self.logger.info("=== Iniciando Pipeline da Frente de Aventura ===")
        
        try:
            # Inicialização de estrutura básica para flags de controle
            if "front" not in self.game_state["adventure"]:
                self.game_state["adventure"]["front"] = {}
            self.game_state["adventure"]["front"]["status"] = "pending"

            # -------------------------------------------------------
            # STEP 1: ARQUÉTIPO & LOCAIS
            # -------------------------------------------------------
            self.logger.info(">>> Executando Step 1: Definição de Arquétipo...")
            
            step1_result = self.module_executor.execute_and_apply(
                "step1_front_archetype", 
                self.game_state
            )
            
            if not step1_result:
                raise Exception("Falha na execução do Step 1 (Arquétipo).")
            
            self.debug_logger.log_step("Front Step 1", step1_result)

            # -------------------------------------------------------
            # STEP 2: WORLDBUILDER (AMEAÇAS)
            # -------------------------------------------------------
            self.logger.info(">>> Executando Step 2: Construção de Mundo...")
            step2_result = self.module_executor.execute_and_apply(
                "step2_front_worldbuilder", 
                self.game_state
            )

            if not step2_result:
                raise Exception("Falha na execução do Step 2 (Worldbuilder).")

            self.debug_logger.log_step("Front Step 2", step2_result)

            # -------------------------------------------------------
            # STEP 3: STORYTELLER (PRESSÁGIOS)
            # -------------------------------------------------------
            self.logger.info(">>> Executando Step 3: Criação de Presságios...")
            step3_result = self.module_executor.execute_and_apply(
                "step3_front_storyteller", 
                self.game_state
            )

            if not step3_result:
                raise Exception("Falha na execução do Step 3 (Storyteller).")

            # Finalização: Atualiza status de controle (flag de sistema)
            self.game_state["adventure"]["front"]["status"] = "completed"
            self.debug_logger.log_step("Front Step 3", step3_result)

            self.logger.info("=== Pipeline da Frente concluído com sucesso ===")
            
            return {
                "structure": step1_result,
                "world": step2_result,
                "story": step3_result
            }

        except Exception as e:
            self.logger.error(f"Erro crítico no Pipeline da Frente: {e}")
            self.game_state["adventure"]["front"]["status"] = "error"
            raise e

    def get_full_state(self) -> Dict[str, Any]:
        """Retorna o estado completo para debug ou serialização."""
        return self.game_state