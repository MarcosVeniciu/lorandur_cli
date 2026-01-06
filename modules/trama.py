import sys
import os
import json

# Adiciona raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model_llm import llm_client

# --- SCHEMA JSON ATUALIZADO (Com Análise e Camadas) ---
TRAMA_SCHEMA = {
    "type": "object",
    "properties": {
        "analysis": {
            "type": "string",
            "description": "Breve análise inicial das sementes, potencial dramático e como os locais disponíveis podem ser usados."
        },
        "title": {
            "type": "string",
            "description": "Um título evocativo para a aventura."
        },
        "tags": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Tags de Gênero/Tom (ex: Horror, Mistério, Guerra)."
        },
        "scope": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Lista dos locais onde a aventura ocorrerá (Selecionados da lista fornecida)."
        },
        "evident_premise": {
            "type": "string",
            "description": "O que os personagens SABEM ou VEEM no início. O gancho imediato ou a missão aparente."
        },
        "hidden_premise": {
            "type": "string",
            "description": "A verdade secreta, a reviravolta ou o verdadeiro antagonista que só será revelado durante a investigação."
        },
        "connection": {
            "type": "string",
            "description": "Como a premissa evidente leva à descoberta da premissa oculta (a pista chave)."
        }
    },
    "required": ["analysis", "title", "tags", "scope", "evident_premise", "hidden_premise"],
    "additionalProperties": False
}

SYSTEM_PROMPT = """
VOCÊ É: Um Mestre de RPG e Roteirista Sênior focado em mistérios e camadas narrativas.
SUA TAREFA: Criar uma estrutura de aventura com DUAS CAMADAS baseada nas sementes fornecidas.

1. ANÁLISE INICIAL
Analise as sementes e os locais. Pense em como conectar o objetivo aparente com uma reviravolta oculta.

2. CAMADA 1: PREMISSA EVIDENTE
O que parece estar acontecendo. O problema superficial que atrai os jogadores.
Deve usar as sementes [O QUE ACONTECEU] e [OBJETIVO].

3. CAMADA 2: PREMISSA OCULTA
A realidade subjacente. O segredo sombrio, a traição ou a força sobrenatural que causou o evento.
Deve se relacionar com a [CONSEQUÊNCIA] se os jogadores falharem ou descobrirem tarde demais.

DIRETRIZES DE ESCOPO:
Selecione locais da lista [LOCAIS PERMITIDOS] que sirvam de palco para a transição da mentira (evidente) para a verdade (oculta).
"""

class ModuloTrama:
    def __init__(self):
        pass

    def gerar_trama(self, seeds: dict, scenario_genre: str, available_locations: list) -> dict:
        """
        Gera uma trama estruturada (Análise + Evidente vs Oculta) baseada nas sementes e locais disponíveis.
        """
        event = seeds.get('col1_event', 'Algo aconteceu')
        goal = seeds.get('col2_goal', 'Sobreviver')
        consequence = seeds.get('col3_consequence', 'Tudo acaba')
        
        # Formata a lista de locais para o prompt
        locais_str = ", ".join([f'"{loc}"' for loc in available_locations])

        user_content = f"""
        ### DADOS DO CENÁRIO ###
        [GÊNERO]: {scenario_genre}
        [LOCAIS PERMITIDOS]: {locais_str}

        ### PREMISSA DE ENTRADA (SEMENTES) ###
        1. [O QUE ACONTECEU]: {event}
        2. [OBJETIVO]: {goal}
        3. [CONSEQUÊNCIA]: {consequence}

        Crie a Trama com análise e as duas camadas agora.
        """

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content}
        ]

        # Chamada ao LLM com Schema
        response = llm_client.send_prompt(
            messages=messages,
            json_schema=TRAMA_SCHEMA,
            temperature=0.75
        )
        
        response['debug_messages'] = messages
        
        return response