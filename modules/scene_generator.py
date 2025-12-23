import sys
import os

# Adiciona raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importa as classes separadas
from modules.macro_director import MacroSceneDirector
from modules.micro_planner import MicroScenePlanner
from modules.tactical_generator import TacticalBriefingGenerator

class SceneGenerator:
    def __init__(self):
        self.macro_gen = MacroSceneDirector()
        self.micro_gen = MicroScenePlanner()
        self.tactical_gen = TacticalBriefingGenerator()

    def generate_new_scene(self, game_state: dict) -> dict:
        print("[SCENE GEN] Criando nova MACRO CENA (Nível 1)...")
        current_macro = self.macro_gen.generate(game_state)
        
        print("[SCENE GEN] Planejando MICRO CENA (Nível 2)...")
        micro_scene = self.micro_gen.generate(current_macro)
        
        print("[SCENE GEN] Gerando BRIEFING TÁTICO (Nível 3)...")
        
        # --- LÓGICA DE CORREÇÃO DOS RELÓGIOS ---
        front = game_state.get('state', {}).get('campaign_front', {})
        if not front: front = {}
        
        clocks_source = {}
        
        # Prioridade 1: Relógios já estão na raiz do front (Parser achatou)
        if isinstance(front.get('threat_clock'), dict):
            clocks_source = front
            
        # Prioridade 2: Relógios estão dentro de 'current_clocks'
        elif isinstance(front.get('current_clocks'), dict):
            clocks_source = front['current_clocks']
            
        # Prioridade 3: Fallback (Cria relógios zerados)
        else:
            clocks_source = {
                'threat_clock': {'current_segments': 0, 'max_segments': 6},
                'resolution_clock': {'current_segments': 0, 'max_segments': 4}
            }
            
        briefing = self.tactical_gen.generate(micro_scene, current_macro, clocks_source)
        
        # Mescla informações para contexto total
        full_context = {**micro_scene, **briefing}
        full_context['macro_context'] = current_macro.get('location_context')
        
        return full_context