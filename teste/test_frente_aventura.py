import sys
import os
import json
import random

# Adiciona raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.trama import ModuloTrama
from modules.frente_aventura import ModuloFrente
from teste.test_utils import TestOrchestrator

def run_test():
    tester = TestOrchestrator("Frente_Aventura")
    
    # --- PASSO 1: SETUP E GERAÇÃO DA TRAMA (Dependência) ---
    tester.log_section("Passo 1", "Gerando Trama Real (Dependência)...")
    
    # Carrega cenário
    scenario_path = os.path.join("scenarios", "dieselpunk.json")
    if not os.path.exists(scenario_path):
        print("ERRO: dieselpunk.json não encontrado.")
        return
        
    with open(scenario_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        tables = data.get('world_data', {}).get('tables', {})
        genre = data.get('name', 'Dieselpunk')
        places = tables.get('scenes', {}).get('places', ["Local Genérico"])

    # Seeds aleatórias
    plot_table = tables.get('plot', {})
    seeds = {
        "col1_event": random.choice(plot_table.get('col1_event', ['E1'])),
        "col2_goal": random.choice(plot_table.get('col2_goal', ['E2'])),
        "col3_consequence": random.choice(plot_table.get('col3_consequence', ['E3']))
    }
    
    # Executa Módulo Trama
    print("1. Gerando Trama...")
    trama_module = ModuloTrama()
    resp_trama = trama_module.gerar_trama(seeds, genre, places)
    
    if 'error' in resp_trama:
        print("Erro na Trama. Abortando.")
        tester.log_section("Erro Trama", resp_trama['error'])
        return
        
    trama_content = resp_trama['content']
    print(f"   > Trama: {trama_content['title']}")
    tester.log_section("Output Trama (Input para Frente)", trama_content)

    # --- PASSO 2: TESTE DO MÓDULO FRENTE ---
    print("2. Gerando Frente de Aventura...")
    frente_module = ModuloFrente()
    
    # Injeta a trama gerada no passo anterior
    resp_frente = frente_module.gerar_frente(trama_content, genre)

    if 'error' in resp_frente:
        print(f"❌ ERRO FRENTE: {resp_frente['error']}")
        tester.log_section("Erro Frente", resp_frente['error'])
    else:
        content = resp_frente['content']
        debug_msgs = resp_frente.get('debug_messages', [])
        
        tester.log_llm_interaction("Geração Frente", debug_msgs, resp_frente)
        tester.log_result(content)
        
        # Validação Visual
        print("\n✅ Frente Gerada:")
        danger = content.get('danger', {})
        print(f"PERIGO: {danger.get('name')} ({danger.get('type')})")
        print(f"IMPULSO: {danger.get('impulse')}")
        print(f"DOOM: {content.get('doom')}")
        print("\nRELÓGIOS:")
        clocks = content.get('clocks', {})
        print(f"- Ameaça: {clocks.get('threat_clock_name')} (0/{clocks.get('threat_clock_max')})")
        print(f"- Resolução: {clocks.get('resolution_clock_name')} (0/{clocks.get('resolution_clock_max')})")
        
        print("\nPRESSÁGIOS:")
        for gp in content.get('grim_portents', []):
            print(f"{gp['index']}. {gp['description']}")

if __name__ == "__main__":
    run_test()