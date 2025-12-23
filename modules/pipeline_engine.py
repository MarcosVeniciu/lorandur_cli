import sys
import os
import json
import random

# Adiciona raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model_llm import llm_client
from utils.xml_parser import extract_all_tags

PROMPTS = {
    "PlotRefiner": """
VOCÊ É: Um Roteirista Sênior de RPG.
INPUT: [EVENTO]: "{event}" | [OBJETIVO]: "{goal}" | [CENÁRIO]: {scenario_context}
TAREFA: Crie um gancho de aventura.
OUTPUT OBRIGATÓRIO (XML):
<refined_plot>
    <title>Título</title>
    <synopsis>Sinopse curta.</synopsis>
</refined_plot>
""",
    "FrontBuilder": """
VOCÊ É: Um Game Designer.
INPUT SINOPSE: {plot_data}
TAREFA: Defina a Ameaça e Relógios.
OUTPUT OBRIGATÓRIO (XML):
<danger>Nome do Vilão</danger>
<doom>O Desastre Final</doom>
<threat_clock_max>6</threat_clock_max>
<resolution_clock_max>4</resolution_clock_max>
""",
    "ItemCrafter": """
INPUT: {intent} | INV: {inventory}
OUTPUT (XML):
<crafted_item>null</crafted_item> OU JSON do item
<message>Texto.</message>
"""
}

class PipelineEngine:
    def execute_rule(self, rule_id: str, game_state: dict, context_override: dict = None) -> dict:
        rules = game_state.get('world_data', {}).get('rules', [])
        rule = next((r for r in rules if r['rule_id'] == rule_id), None)

        if not rule:
            return None

        # print(f"[PIPELINE] Executando: {rule.get('description')}")
        memory = {}
        if context_override: memory.update(context_override)

        steps = rule.get('construction_policy', {}).get('steps', [])
        
        for step in steps:
            action = step.get('action')
            output_var = step.get('output_var')
            
            if action == 'RNG_TABLE_LOOKUP':
                table_name = step.get('target_table')
                tables = game_state.get('world_data', {}).get('tables', {}).get(table_name, {})
                seed = {}
                for col in step.get('required_columns', []):
                    opts = tables.get(col, [])
                    seed[col] = random.choice(opts) if opts else "Indefinido"
                memory[output_var] = seed

            elif action == 'LLM_AGENT_CALL':
                role = step.get('agent_role')
                template = PROMPTS.get(role)
                
                if template:
                    inputs = {}
                    for ctx_key in step.get('input_context', []):
                        clean_key = ctx_key.replace('{{', '').replace('}}', '')
                        val = memory.get(clean_key, "Dados Ausentes")
                        if isinstance(val, (dict, list)):
                            val = json.dumps(val, ensure_ascii=False)
                        inputs[clean_key] = val
                    
                    p_args = {}
                    if role == "PlotRefiner":
                        raw = json.loads(inputs.get('raw_plot_seed', '{}'))
                        p_args = {"event": raw.get('col1_event'), "goal": raw.get('col2_goal'), "scenario_context": inputs.get('SCENARIO_CONTEXT', '')}
                    elif role == "FrontBuilder":
                        plot_raw = inputs.get('refined_plot', '')
                        if isinstance(plot_raw, dict): 
                            plot_raw = plot_raw.get('synopsis', str(plot_raw))
                        p_args = {"plot_data": plot_raw}
                    elif role == "ItemCrafter":
                        p_args = {"intent": inputs.get('intent'), "inventory": inputs.get('inventory')}

                    try:
                        final_prompt = template.format(**p_args)
                        response = llm_client.send_prompt(final_prompt, temperature=0.7)
                        
                        result = extract_all_tags(response)
                        
                        # INJEÇÃO MANUAL DE RELÓGIOS (Fallback)
                        if role == "FrontBuilder" and 'current_clocks' not in result:
                            result['current_clocks'] = {
                                "threat_clock": {"current_segments": 0, "max_segments": int(result.get('threat_clock_max', 6))},
                                "resolution_clock": {"current_segments": 0, "max_segments": int(result.get('resolution_clock_max', 4))}
                            }

                        memory[output_var] = result

                    except Exception as e:
                        print(f"    [ERRO PIPELINE]: {e}")
                        memory[output_var] = {}

        if steps:
            last_var = steps[-1].get('output_var')
            return memory.get(last_var)
        return None