import sys
import os
import json

# Adiciona raiz ao path para garantir imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model_llm import llm_client
from utils.xml_parser import extract_all_tags

ARBITER_PROMPT = """
VOCÊ É: O Árbitro de Regras (Rule Arbiter) de um RPG.
SUA FUNÇÃO: Analisar a ação do jogador e decidir se ela aciona alguma REGRA MECÂNICA específica da lista abaixo.

LISTA DE REGRAS ATIVAS:
{rules_list}

AÇÃO DO JOGADOR: "{action}"

INSTRUÇÕES:
1. Compare a ação com as descrições das regras.
2. Se a ação se encaixa claramente em uma regra (ex: Atacar -> RULE_COMBAT, Hackear -> RULE_SKILL), retorne o ID dela.
3. Se for uma ação narrativa simples ou não coberta (ex: "Olho ao redor"), retorne NULL.
4. Analise o contexto da frase para determinar se há Vantagem (facilidade) ou Desvantagem (dificuldade).

OUTPUT OBRIGATÓRIO (XML):
<rule_verdict>
    <trigger>ID_DA_REGRA ou NULL</trigger>
    <condition>NORMAL, ADVANTAGE ou DISADVANTAGE</condition>
</rule_verdict>
"""

class RuleArbiter:
    def judge_action(self, action_text: str, game_state: dict) -> dict:
        """
        Analisa a ação do usuário contra as regras carregadas no world_data.
        """
        # 1. Recupera as regras do mundo
        rules = game_state.get('world_data', {}).get('rules', [])
        
        # Formata a lista de regras para a IA ler
        rules_desc = ""
        for r in rules:
            # Filtra apenas regras de mecânica (TYPE_X) ou checagem (TYPE_A)
            # Ignora regras de construção (TYPE_I) que são automáticas
            if "TYPE_I" not in r.get('category', ''):
                rules_desc += f"- [{r['rule_id']}]: {r.get('description')}\n"

        if not rules_desc:
            rules_desc = "Nenhuma regra específica definida (Use senso comum)."

        # 2. Monta o Prompt
        prompt = ARBITER_PROMPT.format(
            rules_list=rules_desc,
            action=action_text
        )

        # 3. Consulta a LLM
        try:
            response = llm_client.send_prompt(prompt, temperature=0.1) # Baixa temperatura para ser preciso
            verdict = extract_all_tags(response)
            
            # Fallback se a IA falhar no XML
            if not verdict:
                return {"trigger": "NULL", "condition": "NORMAL"}
                
            return {
                "trigger": verdict.get('trigger', 'NULL').strip(),
                "condition": verdict.get('condition', 'NORMAL').strip().upper()
            }

        except Exception as e:
            print(f"[ARBITER] Erro ao julgar ação: {e}")
            return {"trigger": "NULL", "condition": "NORMAL"}