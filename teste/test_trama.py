import sys
import os
import json
import random

# Adiciona raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.trama import ModuloTrama
from teste.test_utils import TestOrchestrator

def run_test():
    tester = TestOrchestrator("Trama")
    
    tester.log_section("Setup", "Carregando cenário 'dieselpunk.json'.")
    
    scenario_path = os.path.join("scenarios", "dieselpunk.json")
    if not os.path.exists(scenario_path):
        print("ERRO: dieselpunk.json não encontrado.")
        return

    with open(scenario_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        tables = data.get('world_data', {}).get('tables', {})
        genre = data.get('name', 'Dieselpunk')
        places_raw = tables.get('scenes', {}).get('places', [])
        available_locations = places_raw 

    plot_table = tables.get('plot', {})
    seeds = {
        "col1_event": random.choice(plot_table.get('col1_event', ['Evento'])),
        "col2_goal": random.choice(plot_table.get('col2_goal', ['Objetivo'])),
        "col3_consequence": random.choice(plot_table.get('col3_consequence', ['Consequência']))
    }
    
    print(f"Sementes: {seeds['col1_event']}...")
    tester.log_section("Inputs", {"seeds": seeds, "genre": genre})

    trama_module = ModuloTrama()
    print("Invocando LLM...")
    
    response = trama_module.gerar_trama(seeds, genre, available_locations)

    if 'error' in response:
        print(f"❌ ERRO: {response['error']}")
        tester.log_section("Erro", response['error'])
    else:
        content = response['content']
        debug_messages = response.get('debug_messages', [])
        
        tester.log_llm_interaction("Geração Trama (Análise + Evidente/Oculta)", debug_messages, response)
        tester.log_result(content)
        
        print("\n✅ Trama Gerada:")
        print(f"Título: {content.get('title')}")
        print(f"\n[Análise IA]: {content.get('analysis')[:150]}...")
        print(f"\n[Evidente]: {content.get('evident_premise')[:100]}...")
        print(f"[Oculta]: {content.get('hidden_premise')[:100]}...")

if __name__ == "__main__":
    run_test()