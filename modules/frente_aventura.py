import sys
import os
import json

# Adiciona raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model_llm import llm_client

# --- SCHEMA JSON DA FRENTE (Baseado em "Frete de Aventura.md") ---
FRENTE_SCHEMA = {
    "type": "object",
    "properties": {
        "danger": {
            "type": "object",
            "description": "A força antagonista principal (Vilão, Facção ou Desastre Natural).",
            "properties": {
                "name": {"type": "string", "description": "Nome do Perigo."},
                "type": {"type": "string", "description": "Tipo (ex: Senhor da Guerra, Culto, Besta, Ambiente)."},
                "impulse": {"type": "string", "description": "O impulso ou motivação principal (ex: 'Destruir tudo', 'Acumular poder')."},
                "description": {"type": "string", "description": "Descrição breve da ameaça."}
            },
            "required": ["name", "type", "impulse", "description"]
        },
        "doom": {
            "type": "string",
            "description": "A DESGRAÇA. O que acontece se o Relógio de Ameaça encher (Game Over ou Mudança drástica de mundo)."
        },
        "grim_portents": {
            "type": "array",
            "description": "Lista sequencial de eventos ruins que acontecerão se o herói não agir.",
            "items": {
                "type": "object",
                "properties": {
                    "index": {"type": "integer"},
                    "description": {"type": "string", "description": "O evento que ocorre."},
                    "visible_sign": {"type": "string", "description": "O que o jogador VÊ ou percebe quando isso avança (Pista)."}
                },
                "required": ["index", "description", "visible_sign"]
            },
            "minItems": 3,
            "maxItems": 5
        },
        "clocks": {
            "type": "object",
            "description": "Configuração inicial dos Relógios de Cabo de Guerra.",
            "properties": {
                "threat_clock_name": {"type": "string", "description": "Nome temático do relógio ruim (ex: 'O Ritual', 'A Infecção')."},
                "threat_clock_max": {"type": "integer", "default": 6},
                "resolution_clock_name": {"type": "string", "description": "Nome temático do relógio bom (ex: 'A Cura', 'A Invasão')."},
                "resolution_clock_max": {"type": "integer", "default": 4}
            },
            "required": ["threat_clock_name", "threat_clock_max", "resolution_clock_name", "resolution_clock_max"]
        }
    },
    "required": ["danger", "doom", "grim_portents", "clocks"],
    "additionalProperties": False
}

SYSTEM_PROMPT = """
VOCÊ É: Um Game Designer de RPG especialista em "Frentes de Aventura" (Dungeon World/Apocalypse World).
SUA TAREFA: Criar a mecânica de antagonismo baseada na Trama fornecida.

ESTRUTURA:
1. PERIGO (Danger): Use a 'Premissa Oculta' da trama para definir o verdadeiro vilão/ameaça.
2. DESGRAÇA (Doom): O "Bad Ending" se o vilão vencer.
3. PRESSÁGIOS SOMBRIOS (Grim Portents): 3 a 5 passos lógicos que levam ao Doom. 
   - O primeiro presságio deve estar ligado à 'Premissa Evidente' (o que já está acontecendo).
4. RELÓGIOS (Cabo de Guerra):
   - Ameaça (6 segmentos): O avanço do vilão.
   - Resolução (4 segmentos): O objetivo do herói para vencer.
"""

class ModuloFrente:
    def __init__(self):
        pass

    def gerar_frente(self, trama_data: dict, scenario_genre: str) -> dict:
        """
        Gera a Frente de Aventura (Vilão, Doom, Relógios) baseada na Trama.
        """
        
        # Extrai dados relevantes da trama para o prompt
        trama_summary = f"""
        [TÍTULO]: {trama_data.get('title')}
        [TAGS]: {", ".join(trama_data.get('tags', []))}
        [ESCOPO]: {", ".join(trama_data.get('scope', []))}
        [PREMISSA EVIDENTE (O SINTOMA)]: {trama_data.get('evident_premise')}
        [PREMISSA OCULTA (A DOENÇA/VILÃO)]: {trama_data.get('hidden_premise')}
        """

        user_content = f"""
        ### DADOS DO CENÁRIO ###
        [GÊNERO]: {scenario_genre}

        ### TRAMA APROVADA ###
        {trama_summary}

        Construa a Frente de Aventura agora.
        """

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content}
        ]

        # Chamada ao LLM com Schema
        response = llm_client.send_prompt(
            messages=messages,
            json_schema=FRENTE_SCHEMA,
            temperature=0.7
        )
        
        response['debug_messages'] = messages
        
        return response