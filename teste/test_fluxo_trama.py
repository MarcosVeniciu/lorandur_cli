import sys
import os
import time
import json

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path)

from game_controller import GameController
from engine.sync_manager import SyncManager

def calculate_cost(usage_dict):
    """
    Calcula custo estimado para Gemini 2.0 Flash (Preview/Free por enquanto).
    Usando tabela hipotética barata para referência:
    Input: $0.10 / 1M tokens
    Output: $0.40 / 1M tokens
    """
    if not usage_dict:
        return 0.0
    
    prompt_tokens = usage_dict.get('prompt_tokens', 0)
    completion_tokens = usage_dict.get('completion_tokens', 0)
    
    # Preços por 1 Milhão de tokens (Referência)
    price_input = 0.10 
    price_output = 0.40
    
    cost = (prompt_tokens / 1_000_000 * price_input) + (completion_tokens / 1_000_000 * price_output)
    return cost

def testar_geracao_trama():
    print(">>> INICIANDO TESTE DE INTEGRAÇÃO: TRAMA (V5 - Schema V3.0) <<<")
    
    SyncManager().sync_all()
    controller = GameController()
    
    seeds_teste = {
        "col1_event": "Uma carga valiosa foi roubada",
        "col2_goal": "Recuperar a carga antes do amanhecer",
        "col3_consequence": "Guerra entre gangues rivais"
    }

    # Verifica cenário
    scenario_path = os.path.join(base_path, "scenarios", "dieselpunk_2.0.json")
    if not os.path.exists(scenario_path):
        scenario_path = os.path.join(base_path, "scenarios", "dieselpunk.json")

    controller.start_new_game("dieselpunk", seed_data=seeds_teste)

    print("[TESTE] Solicitando geração à IA...")
    start_time = time.time()
    trama_result = controller.step_generate_trama()
    duration = time.time() - start_time

    # Debug e Métricas
    debug_data = controller.executor.last_prompt_debug
    usage = debug_data.get('usage', {})
    cost = calculate_cost(usage)
    finish_reason = debug_data.get('finish_reason', 'Unknown')

    timestamp = time.strftime("%Y_%m_%d_%H_%M")
    report_file = os.path.join(base_path, "teste", "relatorios_teste", f"test_fluxo_trama_{timestamp}.md")
    os.makedirs(os.path.dirname(report_file), exist_ok=True)

    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(f"# Relatório de Teste: Fluxo de Trama V5\n")
        f.write(f"**Data:** {timestamp}\n")
        
        # --- BLOCO DE MÉTRICAS ---
        f.write("\n## 📊 Métricas de Execução\n")
        f.write("| Métrica | Valor |\n")
        f.write("| :--- | :--- |\n")
        f.write(f"| **Tempo Total** | {duration:.2f}s |\n")
        f.write(f"| **Tokens Entrada** | {usage.get('prompt_tokens', 0)} |\n")
        f.write(f"| **Tokens Saída** | {usage.get('completion_tokens', 0)} |\n")
        f.write(f"| **Tokens Total** | {usage.get('total_tokens', 0)} |\n")
        f.write(f"| **Custo Estimado** | ${cost:.6f} |\n")
        f.write(f"| **Stop Reason** | {finish_reason} |\n\n")

        f.write(f"**Módulo:** {debug_data.get('module_id', 'Unknown')}\n\n")
        
        f.write("## 1. Contexto Enviado\n")
        f.write("### System Prompt\n")
        f.write(f"```text\n{debug_data.get('system', 'N/A')}\n```\n\n")
        
        f.write("### User Prompt\n")
        f.write(f"```text\n{debug_data.get('user', 'N/A')}\n```\n\n")

        if trama_result:
            f.write("## 2. Resposta Recebida (Output JSON)\n")
            f.write(f"```json\n{json.dumps(trama_result, indent=2, ensure_ascii=False)}\n```\n\n")
            
            # Adaptação Schema V3.0
            config = trama_result.get('configuracao_aventura', {})
            premissas = trama_result.get('premissas', {})
            matriz = trama_result.get('matriz_controle_informacao', {}).get('itens', [])
            
            escopo = config.get('escopo_selecionado', 'N/A')
            subgeneros = ", ".join(config.get('subgeneros_selecionados', []))
            
            evidente_txt = premissas.get('evidente', {}).get('texto', 'N/A')
            oculta_txt = premissas.get('oculta', {}).get('texto', 'N/A')
            
            f.write("### 3. Análise Rápida (Schema V3.0)\n")
            f.write(f"- **Escopo:** {escopo}\n")
            f.write(f"- **Subgêneros:** {subgeneros}\n")
            f.write(f"- **Premissa Evidente:** {evidente_txt}\n")
            f.write(f"- **Premissa Oculta:** {oculta_txt}\n")
            
            if matriz:
                f.write("\n#### Matriz de Informação (Item 1):\n")
                item1 = matriz[0]
                f.write(f"- **{item1.get('titulo')}:** {item1.get('a_expectativa')} -> *{item1.get('a_verdade')}*\n")

        else:
            f.write("## ❌ Status: FALHA\n")
            f.write("O controller retornou None. Verifique os logs.\n")

    print(f"\n>>> Teste finalizado. Relatório salvo em: {report_file}")

if __name__ == "__main__":
    testar_geracao_trama()