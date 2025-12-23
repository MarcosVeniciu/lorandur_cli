import sys
import os

# Adiciona raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model_llm import llm_client
from utils.xml_parser import extract_all_tags

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

class MacroSceneDirector:
    def generate(self, game_state: dict) -> dict:
        state = game_state.get('state', {})
        front = state.get('campaign_front', {}) or {}
        
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