import asyncio
import logging
from typing import Dict, Any, Optional

from engine.module_executor import ModuleExecutor
from database.db_manager import DBManager
from utils.debug_logger import DebugLogger

class GameController:
    """
    Controlador principal do fluxo do jogo.
    Adaptado para chamar o Executor de forma síncrona.
    """
    
    def __init__(self):
        self.db_manager = DBManager()
        self.module_executor = ModuleExecutor()
        self.logger = logging.getLogger("GameController")
        self.debug_logger = DebugLogger()
        
        self.game_state = {
            "context": {
                "genre": "",
                "available_locations_str": "",
                "available_archetypes_str": "",
                "runtime": {
                    "full_scope_description": "",
                    "formatted_matrix": ""
                }
            },
            "adventure": {
                "trama": {},
                "front": {
                    "step1": {},  # Archetype
                    "step2": {},  # Worldbuilder
                    "step3": {},  # Storyteller
                    "status": "pending"
                }
            }
        }

    async def initialize(self):
        self.logger.info("Inicializando GameController...")
        pass

    def update_context(self, context_data: Dict[str, Any]):
        for key, value in context_data.items():
            if key in self.game_state["context"]:
                if isinstance(self.game_state["context"][key], dict) and isinstance(value, dict):
                    self.game_state["context"][key].update(value)
                else:
                    self.game_state["context"][key] = value
        
        self.logger.info(f"Contexto atualizado. Genre: {self.game_state['context'].get('genre')}")

    def set_trama_state(self, trama_data: Dict[str, Any]):
        self.game_state["adventure"]["trama"] = trama_data
        self.logger.info("Estado da Trama definido.")

    async def generate_adventure_front_pipeline(self) -> Dict[str, Any]:
        """
        Executa o Pipeline de 3 Estágios para gerar a Frente de Aventura.
        NOTA: O método é async para compatibilidade, mas as chamadas ao executor são síncronas.
        """
        self.logger.info("=== Iniciando Pipeline da Frente de Aventura ===")
        
        try:
            # -------------------------------------------------------
            # STEP 1: ARQUÉTIPO
            # -------------------------------------------------------
            self.logger.info(">>> Executando Step 1: Definição de Arquétipo...")
            
            # MUDANÇA: Chamada direta sem await, método renomeado para 'execute'
            step1_result = self.module_executor.execute(
                "step1_front_archetype", 
                self.game_state
            )
            
            if not step1_result:
                raise Exception("Falha na execução do Step 1 (Arquétipo).")
                
            self.game_state["adventure"]["front"]["step1"] = step1_result
            self.debug_logger.log_step("Front Step 1", step1_result)

            # -------------------------------------------------------
            # STEP 2: WORLDBUILDER
            # -------------------------------------------------------
            self.logger.info(">>> Executando Step 2: Construção de Mundo...")
            step2_result = self.module_executor.execute(
                "step2_front_worldbuilder", 
                self.game_state
            )

            if not step2_result:
                raise Exception("Falha na execução do Step 2 (Worldbuilder).")

            self.game_state["adventure"]["front"]["step2"] = step2_result
            self.debug_logger.log_step("Front Step 2", step2_result)

            # -------------------------------------------------------
            # STEP 3: STORYTELLER
            # -------------------------------------------------------
            self.logger.info(">>> Executando Step 3: Criação de Presságios...")
            step3_result = self.module_executor.execute(
                "step3_front_storyteller", 
                self.game_state
            )

            if not step3_result:
                raise Exception("Falha na execução do Step 3 (Storyteller).")

            self.game_state["adventure"]["front"]["step3"] = step3_result
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
        return self.game_state