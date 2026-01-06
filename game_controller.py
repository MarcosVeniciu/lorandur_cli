import os
import json
import random
import time
from datetime import datetime

# Importa o gerenciador de arquivos e os módulos
from utils.file_manager import FileManager
from modules.trama import ModuloTrama
from modules.frente_aventura import ModuloFrente

class GameController:
    def __init__(self):
        self.file_manager = FileManager()
        self.game_state = {}
        
        # Instancia Módulos
        self.trama_module = ModuloTrama()
        self.frente_module = ModuloFrente()
        # Futuros: self.scene_module, etc.
        
    def start_new_campaign(self, scenario_name: str, player_name: str):
        """Inicia uma nova campanha do zero."""
        print(f"\n[SISTEMA] Inicializando cenário: {scenario_name}...")
        
        # 1. Carregar dados
        world_data = self.file_manager.load_scenario(scenario_name)
        if not world_data:
            print("Erro crítico: Cenário não encontrado.")
            return

        # 2. Estado Inicial
        self.game_state = {
            "metadata": {
                "created_at": datetime.now().isoformat(),
                "player_name": player_name,
                "scenario": scenario_name,
                "turn_count": 0
            },
            "world_data": world_data,
            "character": {},
            "current_plot": {},
            "adventure_front": {}, # Será preenchido pelo ModuloFrente
            "scenes_history": [],
            "current_scene": {},
            "inventory": [],
            "flags": {}
        }

        # 3. Pipeline
        success = self._execute_setup_pipeline()
        
        if success:
            self.save_game()
            print("\n[SISTEMA] Campanha criada com sucesso!")
            self._display_adventure_status()
        else:
            print("\n[SISTEMA] Falha na criação da campanha.")

    def _execute_setup_pipeline(self) -> bool:
        print("\n--- FASE 1: O ARQUITETO DE TRAMAS ---")
        
        # A. Preparar Dados
        tables = self.game_state['world_data'].get('tables', {})
        genre = self.game_state['world_data'].get('name', 'Cenário Genérico')
        
        places_raw = tables.get('scenes', {}).get('places', [])
        if not places_raw: places_raw = tables.get('places', ["Local Genérico"])
        
        plot_table = tables.get('plot', {})
        seeds = {
            "col1_event": random.choice(plot_table.get('col1_event', ['E1'])),
            "col2_goal": random.choice(plot_table.get('col2_goal', ['E2'])),
            "col3_consequence": random.choice(plot_table.get('col3_consequence', ['E3']))
        }
        print(f"[RNG] Sementes: {seeds['col1_event']}...")

        # B. TRAMA (IA)
        print("[IA] Gerando Trama...")
        resp_trama = self.trama_module.gerar_trama(seeds, genre, places_raw)
        
        if 'error' in resp_trama:
            print(f"[ERRO] Trama: {resp_trama['error']}")
            return False
            
        self.game_state['current_plot'] = {
            "seeds": seeds,
            **resp_trama['content'] # title, evident_premise, hidden_premise, etc.
        }
        
        print("\n--- FASE 2: A FRENTE DE AVENTURA ---")
        # C. FRENTE (IA)
        print("[IA] Definindo Vilão e Presságios...")
        resp_frente = self.frente_module.gerar_frente(self.game_state['current_plot'], genre)
        
        if 'error' in resp_frente:
            print(f"[ERRO] Frente: {resp_frente['error']}")
            return False

        frente_data = resp_frente['content']
        
        # Inicializa o estado dinâmico dos relógios
        clocks_config = frente_data['clocks']
        
        self.game_state['adventure_front'] = {
            "danger": frente_data['danger'],
            "doom": frente_data['doom'],
            "grim_portents": frente_data['grim_portents'],
            "active_clocks": {
                "threat": {
                    "name": clocks_config['threat_clock_name'],
                    "current": 0,
                    "max": clocks_config['threat_clock_max']
                },
                "resolution": {
                    "name": clocks_config['resolution_clock_name'],
                    "current": 0,
                    "max": clocks_config['resolution_clock_max']
                }
            }
        }
        
        return True

    def _display_adventure_status(self):
        """Mostra resumo da aventura criada."""
        plot = self.game_state['current_plot']
        front = self.game_state['adventure_front']
        
        print("\n" + "="*50)
        print(f"AVENTURA: {plot['title']}")
        print(f"MISSÃO: {plot['evident_premise']}")
        print("-" * 50)
        print(f"AMEAÇA OCULTA: {front['danger']['name']}")
        print(f"RELÓGIO RUIM: {front['active_clocks']['threat']['name']} [0/{front['active_clocks']['threat']['max']}]")
        print(f"RELÓGIO BOM:  {front['active_clocks']['resolution']['name']} [0/{front['active_clocks']['resolution']['max']}]")
        print("="*50 + "\n")

    def save_game(self):
        filename = f"save_{int(time.time())}.json"
        self.file_manager.save_game(self.game_state, filename)

    def load_game(self, filename: str):
        self.game_state = self.file_manager.load_game(filename)
        if self.game_state:
            print(f"[SISTEMA] Jogo '{filename}' carregado.")
            self._display_adventure_status()