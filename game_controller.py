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
    
    Responsabilidades:
    1. Gerenciar o Ciclo de Vida do Jogo (Iniciar, Salvar, Carregar).
    2. Manter o Estado Global (Game State) em memória.
    3. Preparar o Contexto (Variáveis) para os Módulos de IA.
    4. Orquestrar chamadas ao ModuleExecutor.
    """

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.logger = DebugLogger("System")
        self.file_manager = FileManager()
        self.executor = ModuleExecutor()
        
        self.game_state: Dict[str, Any] = {}
        self.current_scenario_data: Dict[str, Any] = {}

    def start_new_game(self, scenario_name: str, seed_data: Dict[str, Any] = None):
        """
        Inicializa um novo jogo a partir de um arquivo de cenário (JSON).
        Prepara todas as variáveis de contexto necessárias para os prompts.
        """
        print(f"[Controller] Iniciando novo jogo: {scenario_name}")
        self.logger = DebugLogger(scenario_name)
        
        scenario_path = os.path.join(self.base_dir, "scenarios", f"{scenario_name}.json")
        try:
            with open(scenario_path, 'r', encoding='utf-8') as f:
                self.current_scenario_data = json.load(f)
        except FileNotFoundError:
            print(f"[Erro] Cenário {scenario_name} não encontrado.")
            return

        # Prepara strings de contexto (Flattening)
        scopes_list = self.current_scenario_data.get("supported_scopes", [
            "Nível 2 (Local): Aventura em local confinado.",
            "Nível 3 (Regional): Aventura de viagem ou exploração."
        ])
        scopes_str = "\n".join([f"- {s}" for s in scopes_list])

        raw_locations = self.current_scenario_data.get("locations", [])
        if not raw_locations and "tabelas" in self.current_scenario_data:
             raw_locations = self.current_scenario_data["tabelas"].get("lugares", {}).get("nomes", [])
        locations_str = ", ".join(raw_locations)

        raw_archetypes = self.current_scenario_data.get("archetypes", [])
        if not raw_archetypes and "tabelas" in self.current_scenario_data:
             raw_archetypes = self.current_scenario_data["tabelas"].get("personagens", {}).get("tipos", [])
        archetypes_str = ", ".join(raw_archetypes)

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
                "genre": self.current_scenario_data.get("genre", 
                         self.current_scenario_data.get("cenario", {}).get("tema", "Generic")),
                "tone": self.current_scenario_data.get("tone", "Neutral"),
                "seeds": seed_data if seed_data else {
                    "col1_event": "Desconhecido", 
                    "col2_goal": "Sobreviver", 
                    "col3_consequence": "Morte"
                },
                "available_locations_str": locations_str,
                "available_archetypes_str": archetypes_str,
                "supported_scopes_str": scopes_str,
                "runtime": {} 
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
            
            config = result.get('configuracao_aventura', {})
            title = config.get('escopo_selecionado', 'Trama Gerada')
            print(f"✅ Trama Gerada com Sucesso: {title}")
            print(f"   Subgêneros: {config.get('subgeneros_selecionados', [])}")
            
            self.logger.log_step("TRAMA_GENERATED", "Sucesso", result)
            return result
        except Exception as e:
            print(f"❌ Erro ao gerar trama: {e}")
            self.logger.log_error("TRAMA_FAIL", str(e))
            return None

    def step_generate_front(self):
        """
        Executa o módulo 'core_front_generator' (Versão Flattened/Achatada).
        """
        if not self.game_state:
            return None
            
        trama = self.game_state.get("adventure", {}).get("trama")
        if not trama:
            print("❌ Erro: Não é possível gerar Frente sem uma Trama.")
            return None

        print("\n--- 👹 Gerando Frente de Aventura (V3.3 Flat) ---")
        
        # --- PRÉ-PROCESSAMENTO ---
        scope_title = trama.get("configuracao_aventura", {}).get("escopo_selecionado", "")
        full_scope_desc = scope_title 

        supported_scopes = self.current_scenario_data.get("supported_scopes", [])
        for scope_line in supported_scopes:
            if scope_title.split('(')[0].strip() in scope_line: 
                full_scope_desc = scope_line
                break
        
        matrix_items = trama.get("matriz_controle_informacao", {}).get("itens", [])
        formatted_matrix = ""
        for item in matrix_items:
            formatted_matrix += f"- **MISTÉRIO: {item.get('titulo', 'Desconhecido')}**\n"
            formatted_matrix += f"  > *Expectativa:* {item.get('a_expectativa', '')}\n"
            formatted_matrix += f"  > *A Verdade:* {item.get('a_verdade', '')}\n"
            formatted_matrix += f"  > *Gatilho:* {item.get('o_gatilho', '')}\n"
            formatted_matrix += f"  > *Revelação:* {item.get('a_revelacao', '')}\n\n"

        self.game_state["context"]["runtime"]["full_scope_description"] = full_scope_desc
        self.game_state["context"]["runtime"]["formatted_matrix"] = formatted_matrix
        # -------------------------

        try:
            result = self.executor.execute("core_front_generator", self.game_state)
            self.game_state["adventure"]["front"] = result
            
            # --- Parsing Adaptado ao Schema Achatado ---
            # Os dados agora estão na raiz do result, não mais em result['frente_aventura']
            # Se o LLM ainda gerar o wrapper por alucinação, tentamos acessá-lo.
            data = result.get('frente_aventura', result)
            
            arquetipo = data.get('cabecalho_arquetipo', 'Desconhecido')
            foco = data.get('cabecalho_foco', 'N/A')
            pressagios = data.get('pressagios', [])
            
            print(f"✅ Frente Gerada: {arquetipo}")
            print(f"   Foco: {foco}")
            print(f"   Presságios: {len(pressagios)} eventos definidos.")
            
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