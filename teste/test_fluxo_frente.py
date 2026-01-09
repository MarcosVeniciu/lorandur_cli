import sys
import os
import time
import json

# Adiciona o diretório raiz ao path para importar os módulos
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path)

from game_controller import GameController
from engine.sync_manager import SyncManager

def calculate_cost(usage_dict):
    """
    Calcula custo estimado para Gemini 2.0 Flash (Preview/Free por enquanto).
    Baseado em preços de referência (Input: $0.10/1M, Output: $0.40/1M).
    """
    if not usage_dict:
        return 0.0
    
    prompt_tokens = usage_dict.get('prompt_tokens', 0)
    completion_tokens = usage_dict.get('completion_tokens', 0)
    
    price_input = 0.10 
    price_output = 0.40
    
    cost = (prompt_tokens / 1_000_000 * price_input) + (completion_tokens / 1_000_000 * price_output)
    return cost

def get_module_schema(module_filename):
    """
    Lê o schema de saída diretamente do arquivo fonte do módulo.
    Isso garante que vejamos exatamente o que está definido no projeto.
    """
    try:
        path = os.path.join(base_path, "modules_source", module_filename)
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("output_schema", {"error": "Schema not found in file"})
    except Exception as e:
        return {"error": f"Could not load schema file: {str(e)}"}

def testar_fluxo_completo():
    print(">>> INICIANDO TESTE DE INTEGRAÇÃO: TRAMA + FRENTE (V5) <<<")
    
    # 1. Sincronização e Setup
    SyncManager().sync_all()
    controller = GameController()
    
    seeds_teste = {
        "col1_event": "Uma carga valiosa foi roubada",
        "col2_goal": "Recuperar a carga antes do amanhecer",
        "col3_consequence": "Guerra entre gangues rivais"
    }

    # Inicia Jogo (Carrega Cenário e Contexto)
    controller.start_new_game("dieselpunk", seed_data=seeds_teste)

    # --- ETAPA 1: GERAR TRAMA ---
    print("\n[TESTE] 1. Gerando Trama...")
    t1_start = time.time()
    trama_result = controller.step_generate_trama()
    t1_duration = time.time() - t1_start
    
    # Captura métricas da Trama
    debug_trama = controller.executor.last_prompt_debug.copy()
    usage_trama = debug_trama.get('usage', {})
    cost_trama = calculate_cost(usage_trama)
    
    if not trama_result:
        print("❌ Falha crítica na Trama. Abortando.")
        return

    # --- ETAPA 2: GERAR FRENTE ---
    print("\n[TESTE] 2. Gerando Frente de Aventura...")
    t2_start = time.time()
    front_result = controller.step_generate_front()
    t2_duration = time.time() - t2_start
    
    # Captura métricas da Frente
    debug_front = controller.executor.last_prompt_debug.copy()
    usage_front = debug_front.get('usage', {})
    cost_front = calculate_cost(usage_front)

    # --- GERAÇÃO DO RELATÓRIO ---
    timestamp = time.strftime("%Y_%m_%d_%H_%M")
    report_file = os.path.join(base_path, "teste", "relatorios_teste", f"test_fluxo_frente_{timestamp}.md")
    os.makedirs(os.path.dirname(report_file), exist_ok=True)

    # Carrega schemas para o relatório
    schema_trama = get_module_schema("trama.json")
    schema_frente = get_module_schema("frente_aventura.json")

    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(f"# Relatório de Teste: Pipeline Trama + Frente\n")
        f.write(f"**Data:** {timestamp}\n")
        f.write(f"**Cenário:** Dieselpunk\n\n")
        
        # 1. Detalhamento da Trama
        f.write("## 1. Módulo: Trama (core_trama_generator)\n")
        f.write(f"**Status:** {'Sucesso' if trama_result else 'Falha'}\n")
        
        # Prompt Trama
        f.write("### Contexto Enviado (Trama)\n")
        f.write("<details>\n<summary>Ver System Prompt</summary>\n\n")
        f.write(f"```text\n{debug_trama.get('system', 'N/A')}\n```\n</details>\n\n")
        f.write("<details>\n<summary>Ver User Prompt</summary>\n\n")
        f.write(f"```text\n{debug_trama.get('user', 'N/A')}\n```\n</details>\n\n")
        
        # Schema Trama
        f.write("### Output Schema (Enviado)\n")
        f.write("<details>\n<summary>Ver JSON Schema (Trama)</summary>\n\n")
        f.write(f"```json\n{json.dumps(schema_trama, indent=2, ensure_ascii=False)}\n```\n</details>\n\n")

        # Saída Trama
        f.write("### Saída Gerada (Trama)\n")
        f.write(f"```json\n{json.dumps(trama_result, indent=2, ensure_ascii=False)}\n```\n\n")
        
        f.write("---\n\n")

        # 2. Detalhamento da Frente
        f.write("## 2. Módulo: Frente (core_front_generator)\n")
        f.write(f"**Status:** {'Sucesso' if front_result else 'Falha'}\n")

        if front_result:
            # Prompt Frente
            f.write("### Contexto Enviado (Frente)\n")
            f.write("<details>\n<summary>Ver System Prompt</summary>\n\n")
            f.write(f"```text\n{debug_front.get('system', 'N/A')}\n```\n</details>\n\n")
            f.write("<details>\n<summary>Ver User Prompt</summary>\n\n")
            f.write(f"```text\n{debug_front.get('user', 'N/A')}\n```\n</details>\n\n")

            # Schema Frente
            f.write("### Output Schema (Enviado)\n")
            f.write("<details>\n<summary>Ver JSON Schema (Frente)</summary>\n\n")
            f.write(f"```json\n{json.dumps(schema_frente, indent=2, ensure_ascii=False)}\n```\n</details>\n\n")
            
            # Saída Frente
            f.write("### Saída Gerada (Frente)\n")
            f.write(f"```json\n{json.dumps(front_result, indent=2, ensure_ascii=False)}\n```\n\n")
            
            # Análise Rápida Frente
            frente_data = front_result.get('frente_aventura', {})
            cabecalho = frente_data.get('cabecalho', {})
            pressagios = frente_data.get('pressagios_terriveis', [])
            
            f.write("### Análise Rápida (Elementos Chave)\n")
            f.write(f"- **Arquétipo de Enredo:** {cabecalho.get('arquetipo_enredo')}\n")
            f.write(f"- **Foco:** {cabecalho.get('descricao_frente')}\n")
            f.write(f"- **Qtd. Presságios:** {len(pressagios)}\n")
            if pressagios:
                p1 = pressagios[0]
                f.write(f"- **Primeiro Presságio:** {p1.get('o_pressagio')} ({p1.get('local_sugerido')})\n")
        else:
            f.write("❌ Erro na geração da Frente. Verifique logs do sistema.\n")
            f.write(f"Erro cru: {debug_front.get('error', 'Desconhecido')}\n")

        f.write("\n---\n\n")

        # 3. Tabela Consolidada
        total_time = t1_duration + t2_duration
        total_tokens_in = usage_trama.get('prompt_tokens', 0) + usage_front.get('prompt_tokens', 0)
        total_tokens_out = usage_trama.get('completion_tokens', 0) + usage_front.get('completion_tokens', 0)
        total_tokens_all = usage_trama.get('total_tokens', 0) + usage_front.get('total_tokens', 0)
        total_cost = cost_trama + cost_front

        f.write("## 📊 Métricas de Execução Total\n")
        f.write("| Métrica | Trama | Frente de aventura | Total |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        f.write(f"| **Tempo Total** | {t1_duration:.2f}s | {t2_duration:.2f}s | {total_time:.2f}s |\n")
        f.write(f"| **Tokens Entrada** | {usage_trama.get('prompt_tokens', 0)} | {usage_front.get('prompt_tokens', 0)} | {total_tokens_in} |\n")
        f.write(f"| **Tokens Saída** | {usage_trama.get('completion_tokens', 0)} | {usage_front.get('completion_tokens', 0)} | {total_tokens_out} |\n")
        f.write(f"| **Tokens Total** | {usage_trama.get('total_tokens', 0)} | {usage_front.get('total_tokens', 0)} | {total_tokens_all} |\n")
        f.write(f"| **Custo Estimado** | ${cost_trama:.6f} | ${cost_front:.6f} | ${total_cost:.6f} |\n")

    print(f"\n✅ Relatório Completo Gerado: {report_file}")

if __name__ == "__main__":
    testar_fluxo_completo()