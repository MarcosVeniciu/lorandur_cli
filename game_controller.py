import os
import json
import time
from typing import Dict, Any, Optional

from engine.module_executor import ModuleExecutor
from utils.file_manager import FileManager
from utils.debug_logger import DebugLogger

class GameController:
    """
    O Maestro do Lorandur V5.
    """

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.logger = DebugLogger("System")
        self.file_manager = FileManager()
        self.executor = ModuleExecutor()
        
        self.game_state: Dict[str, Any] = {}
        self.current_scenario_data: Dict[str, Any] = {}

    def start_new_game(self, scenario_name: str, seed_data: Dict[str, Any] = None):
        print(f"[Controller] Iniciando novo jogo: {scenario_name}")
        self.logger = DebugLogger(scenario_name)
        
        scenario_path = os.path.join(self.base_dir, "scenarios", f"{scenario_name}.json")
        try:
            with open(scenario_path, 'r', encoding='utf-8') as f:
                self.current_scenario_data = json.load(f)
        except FileNotFoundError:
            print(f"[Erro] Cenário {scenario_name} não encontrado.")
            return

        # Prepara a string de escopos suportados para injeção no prompt
        # Se não houver no JSON, usa um default genérico
        scopes_list = self.current_scenario_data.get("supported_scopes", [
            "Nível 2 (Local): Aventura em local confinado.",
            "Nível 3 (Regional): Aventura de viagem ou exploração."
        ])
        scopes_str = "\n".join([f"- {s}" for s in scopes_list])

        # Prepara lista de locais (compatibilidade com versões antigas de JSON)
        # Tenta pegar 'locations' direto ou dentro de 'tabelas.lugares.nomes'
        raw_locations = self.current_scenario_data.get("locations", [])
        if not raw_locations and "tabelas" in self.current_scenario_data:
             raw_locations = self.current_scenario_data["tabelas"].get("lugares", {}).get("nomes", [])
        
        locations_str = ", ".join(raw_locations)

        self.game_state = {
            "meta": {
                "created_at": time.time(),
                "scenario_name": scenario_name,
                "turn": 0
            },
            "system": {
                "last_roll": 0,
                "difficulty_mod": 0,
                "flags": {}
            },
            "context": {
                # Tenta pegar 'genre' direto ou dentro de 'cenario.tema'
                "genre": self.current_scenario_data.get("genre", 
                         self.current_scenario_data.get("cenario", {}).get("tema", "Generic")),
                
                "tone": self.current_scenario_data.get("tone", "Neutral"),
                
                "seeds": seed_data if seed_data else {
                    "col1_event": "Desconhecido", 
                    "col2_goal": "Sobreviver", 
                    "col3_consequence": "Morte"
                },
                
                # INJEÇÕES ESPECIAIS PARA TRAMA V3.0
                "available_locations_str": locations_str,
                "supported_scopes_str": scopes_str
            },
            "adventure": {
                "trama": None,
                "front": None,
                "scenes": []
            },
            "character": {}
        }
        self.logger.log_step("NEW_GAME", "Estado Inicializado", self.game_state)

    def step_generate_trama(self):
        if not self.game_state:
            print("[Erro] Nenhum jogo iniciado.")
            return None

        print("\n--- 🎬 Gerando Trama (V3.0) ---")
        try:
            result = self.executor.execute("core_trama_generator", self.game_state)
            self.game_state["adventure"]["trama"] = result
            
            # Log levemente diferente para V3 (pega o título dentro de argumento ou premissas se mudar schema)
            title = result.get('configuracao_aventura', {}).get('escopo_selecionado', 'Trama Gerada')
            print(f"✅ Trama Gerada: {title}")
            
            self.logger.log_step("TRAMA_GENERATED", "Sucesso", result)
            return result
        except Exception as e:
            print(f"❌ Erro ao gerar trama: {e}")
            self.logger.log_error("TRAMA_FAIL", str(e))
            return None

    def step_generate_front(self):
        """
        Gera a Frente de Aventura. Requer que a Trama já exista.
        """
        if not self.game_state:
            return None
            
        trama = self.game_state.get("adventure", {}).get("trama")
        if not trama:
            print("❌ Erro: Não é possível gerar Frente sem uma Trama.")
            return None

        print("\n--- 👹 Gerando Frente de Aventura ---")
        try:
            result = self.executor.execute("core_front_generator", self.game_state)
            self.game_state["adventure"]["front"] = result
            
            print(f"✅ Ameaça: {result.get('danger_name')}")
            self.logger.log_step("FRONT_GENERATED", "Sucesso", result)
            return result
        except Exception as e:
            print(f"❌ Erro ao gerar Frente: {e}")
            self.logger.log_error("FRONT_FAIL", str(e))
            return None

    def save_game(self):
        if not self.game_state:
            return
        timestamp = int(time.time())
        filename = f"save_{timestamp}.json"
        self.file_manager.save_json(filename, self.game_state, subdir="saves")
        print(f"[Controller] Jogo salvo em {filename}")

    def load_game(self, filename: str):
        data = self.file_manager.load_json(filename, subdir="saves")
        if data:
            self.game_state = data
            scenario_name = data["meta"].get("scenario_name")
            if scenario_name:
                self.logger = DebugLogger(scenario_name)
                scenario_path = os.path.join(self.base_dir, "scenarios", f"{scenario_name}.json")
                if os.path.exists(scenario_path):
                    with open(scenario_path, 'r', encoding='utf-8') as f:
                        self.current_scenario_data = json.load(f)
            print("[Controller] Jogo carregado com sucesso.")