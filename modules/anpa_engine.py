import sys
import os
import json

# Adiciona raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model_llm import llm_client
from utils.xml_parser import extract_all_tags

# --- PROMPT PARA RESOLUÇÃO DE AÇÃO ---
ANPA_PROMPT = """
VOCÊ É: Narrador e Árbitro de RPG (Dungeon Master).
CONTEXTO DO MUNDO: {world_context}
CENA ATUAL: {scene_context}
AÇÃO DO JOGADOR: "{action}"
VEREDITO DE REGRA (Arbiter): {rule_verdict}

ESTADO ATUAL:
- Ameaça: {threat_val}/{threat_max}
- Resolução: {res_val}/{res_max}

TAREFA:
1. Determine o resultado da ação (Sucesso, Falha, Sucesso Parcial).
2. Atualize o estado do jogo (Inventário, Relógios).
3. Narre o resultado de forma imersiva.

OUTPUT OBRIGATÓRIO (XML):
<turn_outcome>
    <summary>Resumo técnico do que aconteceu.</summary>
    <impact_level>MINOR ou MAJOR</impact_level>
    <system_tags>
        <event_trigger>RESOLUTION_PROGRESS (se ajudou objetivo), THREAT_PROGRESS (se falhou/perigoso), NONE</event_trigger>
        <inventory_updates>
             <item quantity="1">Nome do Item</item>
        </inventory_updates>
    </system_tags>
</turn_outcome>

<narrator>
Sua narração aqui...
</narrator>
"""

# --- PROMPT PARA PREVISÃO DE OPÇÕES ---
PREDICTION_PROMPT = """
VOCÊ É: Game Designer Auxiliar.
CENA ATUAL: {scene_context}
OBJETIVO: {objective}

TAREFA: Sugira 3 abordagens possíveis para o jogador avançar na cena.
1. CRITICAL: O caminho óbvio/direto (Risco Normal).
2. CREATIVE: Uma abordagem lateral ou inteligente (Risco Baixo ou Recompensa Alta).
3. FAILURE_RISK: O que acontece se ele ignorar o perigo (Consequência).

OUTPUT OBRIGATÓRIO (XML):
<prediction_tree>
    <node type="CRITICAL">
        <trigger>Ação sugerida...</trigger>
        <consequence>O que acontece...</consequence>
    </node>
    <node type="CREATIVE">
        <trigger>Ação sugerida...</trigger>
        <consequence>O que acontece...</consequence>
    </node>
    <node type="FAILURE_RISK">
        <trigger>Ignorar/Esperar...</trigger>
        <consequence>O que acontece...</consequence>
    </node>
</prediction_tree>
"""

class ANPAEngine:
    def resolve_turn(self, user_action: str, arbiter_verdict: dict, game_state: dict) -> dict:
        state = game_state.get('state', {})
        front = state.get('campaign_front', {}) or {}
        
        # Busca relógios de forma segura
        def get_clock(name):
            if isinstance(front.get(name), dict): return front[name]
            if isinstance(front.get('current_clocks'), dict): return front['current_clocks'].get(name, {})
            return {}

        t_clock = get_clock('threat_clock')
        r_clock = get_clock('resolution_clock')
        scene_ctx = state.get('current_scene_context', {})
        
        prompt = ANPA_PROMPT.format(
            world_context=game_state.get('world_data', {}).get('description', ''),
            scene_context=f"Local: {scene_ctx.get('location_name')}. Obj: {scene_ctx.get('scene_objective')}",
            action=user_action,
            rule_verdict=json.dumps(arbiter_verdict, ensure_ascii=False),
            threat_val=t_clock.get('current_segments', 0),
            threat_max=t_clock.get('max_segments', 6),
            res_val=r_clock.get('current_segments', 0),
            res_max=r_clock.get('max_segments', 4)
        )

        response = llm_client.send_prompt(prompt, temperature=0.7)
        outcome_data = extract_all_tags(response)

        # 1. Extração Híbrida (JSON/XML) das tags de sistema
        outcome_data['system_dict'] = {}
        if 'system_tags' in outcome_data:
            raw_tags = outcome_data['system_tags']
            if isinstance(raw_tags, dict):
                outcome_data['system_dict'] = raw_tags
            else:
                try:
                    outcome_data['system_dict'] = json.loads(raw_tags)
                except:
                    # Se não for JSON, tenta parsear como XML
                    outcome_data['system_dict'] = extract_all_tags(raw_tags)

        # 2. SANITIZAÇÃO DE INVENTÁRIO (A CORREÇÃO CRÍTICA)
        sys_d = outcome_data['system_dict']
        
        if 'inventory_updates' in sys_d:
            raw_inv = sys_d['inventory_updates']
            clean_inv = []

            # Se for uma string (XML solto ou Texto), converte para dict
            if isinstance(raw_inv, str):
                parsed = extract_all_tags(raw_inv)
                if 'item' in parsed:
                    clean_inv.append({'item': parsed['item'], 'qty': 1})
                else:
                    # Se não achou tag <item>, assume que a string toda é o nome
                    clean_inv.append({'item': raw_inv, 'qty': 1})
            
            # Se for um único dict, bota na lista
            elif isinstance(raw_inv, dict):
                clean_inv.append(raw_inv)
                
            # Se for lista, varre e corrige itens que sejam strings
            elif isinstance(raw_inv, list):
                for i in raw_inv:
                    if isinstance(i, dict):
                        clean_inv.append(i)
                    elif isinstance(i, str):
                         # Tenta extrair XML da string da lista
                         parsed = extract_all_tags(i)
                         if 'item' in parsed:
                             clean_inv.append({'item': parsed['item'], 'qty': 1})
                         else:
                             clean_inv.append({'item': i, 'qty': 1})
            
            # Substitui a versão suja pela limpa
            sys_d['inventory_updates'] = clean_inv

        return outcome_data

    def generate_prediction_tree(self, game_state: dict) -> dict:
        """
        Gera 3 opções de ação para o jogador (Crítico, Criativo, Risco).
        """
        state = game_state.get('state', {})
        scene_ctx = state.get('current_scene_context', {})
        
        prompt = PREDICTION_PROMPT.format(
            scene_context=scene_ctx.get('location_name', 'Local Desconhecido'),
            objective=scene_ctx.get('scene_objective', 'Sobreviver')
        )

        response = llm_client.send_prompt(prompt, temperature=0.7)
        data = extract_all_tags(response)
        return data