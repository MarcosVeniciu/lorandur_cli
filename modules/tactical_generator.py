import sys
import os

# Adiciona raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model_llm import llm_client
from utils.xml_parser import extract_all_tags

TACTICAL_PROMPT = """
VOCÊ É: Game Designer (Dungeon Master).
LOCAL: {sub_location} (dentro de {macro_loc})
ELEMENTO: {local_element}
OBJETIVO: {micro_objective}

ESTADO DOS RELÓGIOS:
- Ameaça: {threat_val}/{threat_max}
- Resolução: {res_val}/{res_max}

TAREFA: Gere o Briefing Tático JSON.
OUTPUT (XML):
<npc_name>Nome do NPC (ou 'Nenhum')</npc_name>
<npc_desc>Descrição visual breve</npc_desc>
<npc_mood>Humor atual</npc_mood>
<hidden_info>Um segredo ou item escondido aqui.</hidden_info>
<trigger_list>
- Ação 1: GATILHO_1
- Ação 2: GATILHO_2
</trigger_list>
<wildcard_tag>SCENE_COMPLETE_GENERIC</wildcard_tag>
"""

class TacticalBriefingGenerator:
    def generate(self, micro_scene: dict, macro_data: dict, clocks: dict) -> dict:
        # Blindagem contra None
        if not macro_data: macro_data = {'location_context': 'Local', 'main_objective': 'Sobreviver'}
        if not micro_scene: micro_scene = {'sub_location': 'Sala', 'local_element': 'Nada', 'micro_objective': 'Avançar'}
        
        # Lógica de Relógios
        t_clock = {}
        r_clock = {}
        
        if isinstance(clocks, dict):
            if isinstance(clocks.get('threat_clock'), dict):
                t_clock = clocks['threat_clock']
                r_clock = clocks.get('resolution_clock', {})
            elif 'current_segments' in clocks:
                t_clock = clocks
        
        t_val = t_clock.get('current_segments', 0)
        t_max = t_clock.get('max_segments', 6)
        r_val = r_clock.get('current_segments', 0)
        r_max = r_clock.get('max_segments', 4)

        macro_safe = macro_data.get('location_context', 'Local') or "Local"

        prompt = TACTICAL_PROMPT.format(
            sub_location=micro_scene.get('sub_location'),
            macro_loc=macro_safe[:50] + "...",
            local_element=micro_scene.get('local_element'),
            micro_objective=micro_scene.get('micro_objective'),
            threat_val=t_val,
            threat_max=t_max,
            res_val=r_val,
            res_max=r_max
        )

        response = llm_client.send_prompt(prompt, temperature=0.7)
        data = extract_all_tags(response)
        
        triggers = []
        if 'trigger_list' in data:
            triggers = [t.strip() for t in data['trigger_list'].split('\n') if '-' in t]
            
        return {
            "location_name": micro_scene.get('sub_location', 'Local Desconhecido'),
            "scene_objective": micro_scene.get('micro_objective', 'Avançar'),
            "npc_active": {
                "name": data.get('npc_name', 'Ninguém'),
                "description": data.get('npc_desc', 'Vazio'),
                "mood": data.get('npc_mood', 'Neutro'),
                "archetype": "NPC"
            },
            "hidden_info": data.get('hidden_info', 'Nada visível.'),
            "anpa_triggers": triggers,
            "wildcard_tag": data.get('wildcard_tag', 'SCENE_COMPLETE_GENERIC')
        }