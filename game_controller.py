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
    Controlador principal do fluxo do jogo.
    Gerencia o estado (game_state), orquestra os módulos e corrige inconsistências de dados.
    """
    
    def __init__(self):
        self.db_manager = DBManager()
        self.module_executor = ModuleExecutor()
        self.file_manager = FileManager()
        self.logger = logging.getLogger("GameController")
        self.debug_logger = DebugLogger()
        
        # Estado Inicial
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
            "adventure": {} # Será populado/resetado no start_new_game
        }
        # Garante estrutura limpa na inicialização
        self._reset_adventure_state()

    def _reset_adventure_state(self):
        """
        Reseta a estrutura de aventura para evitar contaminação de dados
        entre sessões de jogo diferentes na mesma instância.
        """
        self.game_state["adventure"] = {
            "trama": {},
            "front": {
                "step1": {},  # Archetype
                "step2": {},  # Worldbuilder
                "step3": {},  # Storyteller
                "status": "pending"
            }
        }

    async def initialize(self):
        self.logger.info("Inicializando GameController...")
        pass

    def start_new_game(self, scenario_name: str, seed_data: Dict[str, Any] = None):
        """
        Carrega o cenário e prepara o contexto inicial.
        """
        self.logger.info(f"Iniciando novo jogo: {scenario_name}")
        
        # 1. Limpeza de Estado Anterior (CRÍTICO)
        self._reset_adventure_state()
        
        # 2. Carregar Cenário
        # Assume que o FileManager sabe buscar na pasta scenarios
        scenario_data = self.file_manager.load_json(f"{scenario_name}.json", subdir="scenarios")
        
        if not scenario_data:
            # Fallback para tentar achar o arquivo direto se o nome for complexo
            if os.path.exists(f"scenarios/{scenario_name}.json"):
                with open(f"scenarios/{scenario_name}.json", 'r', encoding='utf-8') as f:
                    scenario_data = json.load(f)
            else:
                raise FileNotFoundError(f"Cenário '{scenario_name}' não encontrado.")

        # 3. Popula Contexto Básico
        self.game_state["context"]["genre"] = scenario_data.get("genre", "Generic")
        self.game_state["context"]["supported_scopes_str"] = "\n".join(scenario_data.get("supported_scopes", []))
        
        # Locais e Arquétipos do Cenário (Stringfy para o prompt)
        locs = scenario_data.get("locations", [])
        archs = scenario_data.get("archetypes", [])
        self.game_state["context"]["available_locations_str"] = ", ".join(locs) if isinstance(locs, list) else str(locs)
        self.game_state["context"]["available_archetypes_str"] = ", ".join(archs) if isinstance(archs, list) else str(archs)

        # 4. Seeds (Sementes da Trama)
        if seed_data:
            self.game_state["context"]["seeds"] = seed_data
        
        self.logger.info("Contexto inicial configurado com sucesso.")

    def step_generate_trama(self) -> Dict[str, Any]:
        """
        Executa o módulo de Trama e corrige dados para os próximos passos.
        """
        self.logger.info(">>> Gerando Trama...")
        
        trama_result = self.module_executor.execute(
            "core_trama_generator", 
            self.game_state
        )
        
        if not trama_result:
            raise Exception("Falha na geração da Trama.")
        
        self.set_trama_state(trama_result)
        self.debug_logger.log_step("Trama Gerada", trama_result)
        
        return trama_result

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

    def save_game(self, filename: str = None):
        """Salva o estado atual."""
        if not filename:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"save_{timestamp}.json"
        
        # Garante que o diretório existe (Segurança)
        os.makedirs("saves", exist_ok=True)
        
        self.file_manager.save_json(filename, self.game_state, subdir="saves")
        print(f"[GameController] Jogo salvo em: saves/{filename}")

    def load_game(self, filename: str):
        data = self.file_manager.load_json(filename, subdir="saves")
        if data:
            self.game_state = data
            print(f"[GameController] Jogo carregado: {filename}")
        else:
            print("[GameController] Erro ao carregar save.")

    async def generate_adventure_front_pipeline(self) -> Dict[str, Any]:
        """
        Executa o Pipeline de 3 Estágios para gerar a Frente de Aventura.
        """
        self.logger.info("=== Iniciando Pipeline da Frente de Aventura ===")
        
        try:
            # Inicialização defensiva para garantir que 'front' existe
            self.game_state["adventure"].setdefault("front", {
                "step1": {}, "step2": {}, "step3": {}, "status": "pending"
            })

            # -------------------------------------------------------
            # STEP 1: ARQUÉTIPO & LOCAIS
            # -------------------------------------------------------
            self.logger.info(">>> Executando Step 1: Definição de Arquétipo...")
            
            step1_result = self.module_executor.execute(
                "step1_front_archetype", 
                self.game_state
            )
            
            if not step1_result:
                raise Exception("Falha na execução do Step 1 (Arquétipo).")
            
            self.game_state["adventure"]["front"]["step1"] = step1_result
            self.debug_logger.log_step("Front Step 1", step1_result)

            # -------------------------------------------------------
            # STEP 2: WORLDBUILDER (AMEAÇAS)
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
            # STEP 3: STORYTELLER (PRESSÁGIOS)
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
            # Garante que 'front' existe antes de setar o status
            if "front" in self.game_state["adventure"]:
                self.game_state["adventure"]["front"]["status"] = "error"
            raise e

    def get_full_state(self) -> Dict[str, Any]:
        return self.game_state