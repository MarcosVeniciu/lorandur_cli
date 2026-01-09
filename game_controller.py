import asyncio
import logging
from typing import Dict, Any, Optional

from engine.module_executor import ModuleExecutor
from database.db_manager import DatabaseManager
from utils.debug_logger import DebugLogger

class GameController:
    """
    Controlador principal do fluxo do jogo.
    Gerencia o Estado do Jogo (GameState) e orquestra a execução dos módulos.
    """
    
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.module_executor = ModuleExecutor()
        self.logger = logging.getLogger("GameController")
        self.debug_logger = DebugLogger()
        
        # Estado do Jogo em memória (Volátil durante a execução, persistido se necessário)
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
                    "step3": {},  # Storyteller (Final Result)
                    "status": "pending"
                }
            }
        }

    async def initialize(self):
        """Inicializa conexões e carrega dados básicos."""
        self.logger.info("Inicializando GameController...")
        # Aqui poderia carregar configurações do DB
        pass

    def update_context(self, context_data: Dict[str, Any]):
        """Atualiza o contexto global do jogo (inputs do usuário/sistema)."""
        # Merge recursivo simples ou substituição direta
        for key, value in context_data.items():
            if key in self.game_state["context"]:
                if isinstance(self.game_state["context"][key], dict) and isinstance(value, dict):
                    self.game_state["context"][key].update(value)
                else:
                    self.game_state["context"][key] = value
        
        self.logger.info(f"Contexto atualizado. Genre: {self.game_state['context'].get('genre')}")

    def set_trama_state(self, trama_data: Dict[str, Any]):
        """Define o estado da Trama após a execução do módulo de Trama."""
        self.game_state["adventure"]["trama"] = trama_data
        self.logger.info("Estado da Trama definido.")

    async def generate_adventure_front_pipeline(self) -> Dict[str, Any]:
        """
        Executa o Pipeline de 3 Estágios para gerar a Frente de Aventura.
        Substitui a antiga chamada monolítica.
        """
        self.logger.info("=== Iniciando Pipeline da Frente de Aventura ===")
        
        try:
            # -------------------------------------------------------
            # STEP 1: ARQUÉTIPO (The Architect)
            # -------------------------------------------------------
            self.logger.info(">>> Executando Step 1: Definição de Arquétipo...")
            step1_result = await self.module_executor.execute_module(
                "step1_front_archetype", 
                self.game_state
            )
            
            if not step1_result:
                raise Exception("Falha na execução do Step 1 (Arquétipo).")
                
            # Salva no State para que o Step 2 possa ler
            self.game_state["adventure"]["front"]["step1"] = step1_result
            self.debug_logger.log_step("Front Step 1", step1_result)

            # -------------------------------------------------------
            # STEP 2: WORLDBUILDER (The Builder)
            # -------------------------------------------------------
            self.logger.info(">>> Executando Step 2: Construção de Mundo...")
            step2_result = await self.module_executor.execute_module(
                "step2_front_worldbuilder", 
                self.game_state
            )

            if not step2_result:
                raise Exception("Falha na execução do Step 2 (Worldbuilder).")

            # Salva no State para que o Step 3 possa ler
            self.game_state["adventure"]["front"]["step2"] = step2_result
            self.debug_logger.log_step("Front Step 2", step2_result)

            # -------------------------------------------------------
            # STEP 3: STORYTELLER (The Narrator)
            # -------------------------------------------------------
            self.logger.info(">>> Executando Step 3: Criação de Presságios...")
            step3_result = await self.module_executor.execute_module(
                "step3_front_storyteller", 
                self.game_state
            )

            if not step3_result:
                raise Exception("Falha na execução do Step 3 (Storyteller).")

            self.game_state["adventure"]["front"]["step3"] = step3_result
            self.game_state["adventure"]["front"]["status"] = "completed"
            self.debug_logger.log_step("Front Step 3", step3_result)

            self.logger.info("=== Pipeline da Frente concluído com sucesso ===")
            
            # Retorna uma estrutura consolidada para quem chamou (UI/Main)
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