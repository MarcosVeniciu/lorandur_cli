import json
import os
from datetime import datetime

class FileManager:
    def __init__(self, data_dir="data", scenarios_dir="scenarios", saves_dir="saves"):
        # Ajusta os caminhos para serem relativos à raiz de execução
        self.data_dir = data_dir
        self.scenarios_dir = scenarios_dir
        self.saves_dir = saves_dir
        
        # Garante que as pastas existam
        os.makedirs(self.saves_dir, exist_ok=True)
        if not os.path.exists(self.data_dir):
            print(f"[AVISO] Pasta de dados do sistema não encontrada: {self.data_dir}")
        if not os.path.exists(self.scenarios_dir):
            print(f"[AVISO] Pasta de cenários não encontrada: {self.scenarios_dir}")

    def load_json(self, filepath):
        """Carrega um JSON de um caminho específico."""
        if not os.path.exists(filepath):
            print(f"[ERRO] Arquivo não encontrado: {filepath}")
            return {}
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[ERRO] Falha ao ler JSON {filepath}: {e}")
            return {}

    def create_new_campaign(self, scenario_filename):
        """
        Cria um novo save fundindo core_rules.json (de data/) + scenario.json (de scenarios/)
        """
        # 1. Carrega as Regras Básicas (Sempre em data/core_rules.json)
        core_path = os.path.join(self.data_dir, "core_rules.json")
        core_data = self.load_json(core_path)
        
        if not core_data:
            raise FileNotFoundError(f"CRÍTICO: core_rules.json não encontrado em {core_path}!")

        # 2. Carrega o Cenário Selecionado (Da pasta scenarios/)
        scenario_path = os.path.join(self.scenarios_dir, scenario_filename)
        scenario_data = self.load_json(scenario_path)
        
        scenario_id = scenario_data.get("pack_id", "custom_scenario")
        
        # 3. FUSÃO INTELIGENTE (Merge)
        game_state = {
            "meta": {
                "scenario_name": scenario_data.get("name", "Unknown Scenario"),
                "scenario_id": scenario_id,
                "turn_count": 1,
                "created_at": datetime.now().isoformat()
            },
            "world_data": core_data.get("world_data", {}),
            "state": {
                "character": {
                    "name": "Viajante",
                    "archetype": "Sobrevivente",
                    "inventory": [],
                    "stats": {}
                },
                "packages": {}, 
                "campaign_front": None,
                "temp": {}
            }
        }

        # 4. INICIALIZAÇÃO DE ESTADO DO CENÁRIO
        if "initial_state_template" in scenario_data:
            game_state["state"]["packages"][scenario_id] = scenario_data["initial_state_template"]
            print(f"[FILEMANAGER] Pacote '{scenario_id}' inicializado.")

        # 5. Aplica Overrides do Cenário
        sc_world = scenario_data.get("world_data", {})
        
        # A. Tabelas
        if "tables" in sc_world:
            for table_name, content in sc_world["tables"].items():
                game_state["world_data"]["tables"][table_name] = content

        # B. Regras
        if "rules" in sc_world:
            current_rules = game_state["world_data"].get("rules", [])
            new_rules = sc_world["rules"]
            existing_ids = {r['rule_id'] for r in current_rules}
            for rule in new_rules:
                if rule['rule_id'] in existing_ids:
                    current_rules = [r for r in current_rules if r['rule_id'] != rule['rule_id']]
                current_rules.append(rule)
            game_state["world_data"]["rules"] = current_rules

        # C. Descrição
        if "description" in sc_world:
            game_state["world_data"]["description"] = sc_world["description"]

        # 6. Salva
        save_filename = f"save_{int(datetime.now().timestamp())}.json"
        save_path = os.path.join(self.saves_dir, save_filename)
        
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(game_state, f, indent=2, ensure_ascii=False)
            
        return save_path

    def list_scenarios(self):
        """Lista apenas arquivos na pasta scenarios/"""
        if not os.path.exists(self.scenarios_dir):
            return []
        files = [f for f in os.listdir(self.scenarios_dir) if f.endswith('.json')]
        return files

    def list_saves(self):
        if not os.path.exists(self.saves_dir):
            return []
        return [f for f in os.listdir(self.saves_dir) if f.endswith('.json')]