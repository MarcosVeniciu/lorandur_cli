import sys
import os
import json

# Adiciona raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model_llm import llm_client
from utils.xml_parser import extract_all_tags

# --- PROMPTS ---
MACRO_PROMPT = """
VOCÊ É: Diretor de Arte e Roteiro.
CONTEXTO: {context_summary}
SINOPSE DA TRAMA: {plot_summary}
AMEAÇA ATUAL: {threat_summary}
CENA ANTERIOR: {prev_location}

TAREFA: Crie a próxima MACRO CENA (O local geral e a atmosfera).
OUTPUT (XML):
<macro_scene>
    <location_context>Descrição rica do ambiente, clima e sons.</location_context>
    <main_objective>O objetivo geral aqui.</main_objective>
    <atmosphere>Tags de clima (Ex: Sombrio, Tenso).</atmosphere>
</macro_scene>
"""

MICRO_PROMPT = """
VOCÊ É: Level Designer.
MACRO LOCAL: {macro_location}
OBJETIVO GERAL: {macro_objective}

TAREFA: Crie uma MICRO CENA (Uma sala, corredor ou obstáculo específico dentro do Macro).
OUTPUT (XML):
<micro_scene>
    <sub_location>Nome específico da área (Ex: O Balcão do Bar).</sub_location>
    <local_element>Um objeto ou detalhe interativo.</local_element>
    <micro_objective>O desafio imediato desta sala.</micro_objective>
    <connection>Como isso liga ao objetivo maior.</connection>
</micro_scene>
"""

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

class MacroSceneDirector:
    def generate(self, game_state: dict) -> dict:
        state = game_state.get('state', {})
        front = state.get('campaign_front', {}) or {}
        plot = state.get('campaign_front', {}) # Fallback se estrutura variar
        
        # Previne erro se front for None
        danger = front.get('danger', 'Ameaça Desconhecida') if front else 'Desconhecido'
        doom = front.get('doom', 'Algo ruim') if front else 'Sobreviver'
        
        prev_scene = state.get('current_scene_context', {}).get('location_name', 'Início')
        
        prompt = MACRO_PROMPT.format(
            context_summary=game_state.get('world_data', {}).get('description', 'Mundo Genérico'),
            plot_summary=f"Impedir {doom}",
            threat_summary=danger,
            prev_location=prev_scene
        )

        response = llm_client.send_prompt(prompt, temperature=0.8)
        return extract_all_tags(response)

class MicroScenePlanner:
    def generate(self, macro_scene: dict) -> dict:
        if not macro_scene:
            macro_scene = {'location_context': 'Local Genérico', 'main_objective': 'Avançar'}

        prompt = MICRO_PROMPT.format(
            macro_location=macro_scene.get('location_context', 'Lugar Desconhecido')[:500],
            macro_objective=macro_scene.get('main_objective', 'Sobreviver')
        )
        
        response = llm_client.send_prompt(prompt, temperature=0.7)
        return extract_all_tags(response)

class TacticalBriefingGenerator:
    def generate(self, micro_scene: dict, macro_data: dict, clocks: dict) -> dict:
        # Blindagem contra None
        if not macro_data: macro_data = {'location_context': 'Local', 'main_objective': 'Sobreviver'}
        if not micro_scene: micro_scene = {'sub_location': 'Sala', 'local_element': 'Nada', 'micro_objective': 'Avançar'}
        
        # CORREÇÃO: Garante que clocks é dict. Se for string, tenta achar na raiz ou usa default.
        t_clock = {}
        r_clock = {}
        
        # Se clocks tiver 'threat_clock' como chave de dict, usa. 
        # Se não, checa se clocks É o threat_clock (caso tenha sido passado o objeto errado)
        if isinstance(clocks, dict):
            if isinstance(clocks.get('threat_clock'), dict):
                t_clock = clocks['threat_clock']
                r_clock = clocks.get('resolution_clock', {})
            elif 'current_segments' in clocks:
                # O próprio objeto passado já é um relógio (caso raro)
                t_clock = clocks
        
        # Valores Default de Segurança
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
        
        # Tenta achar os relógios.
        # Devido ao "achatamento" do XML Parser, 'threat_clock' pode estar na raiz de 'front'
        # e 'current_clocks' pode ser apenas uma string residual.
        
        clocks_source = {}
        
        # Prioridade 1: Relógios já estão na raiz do front (Parser achatou)
        if isinstance(front.get('threat_clock'), dict):
            clocks_source = front
            
        # Prioridade 2: Relógios estão dentro de 'current_clocks' e é um dict
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