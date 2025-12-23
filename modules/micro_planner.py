import sys
import os

# Adiciona raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model_llm import llm_client
from utils.xml_parser import extract_all_tags

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