import sys
import os
import json
import time
from datetime import datetime

# Adiciona raiz ao path para garantir imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.pipeline_engine import PipelineEngine
from modules.scene_generator import SceneGenerator
from modules.rule_arbiter import RuleArbiter
from modules.anpa_engine import ANPAEngine
from modules.ens_narrator import ENSNarrator
from utils.file_manager import FileManager

class GameController:
    def __init__(self, save_path):
        self.save_path = save_path
        self.fm = FileManager()
        
        # Carrega o estado do jogo
        try:
            with open(save_path, 'r', encoding='utf-8') as f:
                self.game_state = json.load(f)
        except Exception as e:
            print(f"[ERRO] Não foi possível carregar o save: {e}")
            raise e

        # Inicializa Módulos
        self.pipeline = PipelineEngine()
        self.scene_gen = SceneGenerator()
        self.arbiter = RuleArbiter()
        self.anpa = ANPAEngine()
        self.narrator = ENSNarrator()

        # Verifica se é um jogo novo (Turno 1 e sem Frente de Campanha)
        turn_count = self.game_state['meta'].get('turn_count', 1)
        front = self.game_state['state'].get('campaign_front')

        # 5. Setup Inicial Automático (Se não houver Frente de Campanha)
        # Verifica se é None ou Vazio
        if turn_count == 1 and not front:
            print("[CONTROLLER] Disparando Evento: ON_CAMPAIGN_START")
            self._initialize_campaign_structure()
        
        # Garante que a árvore de previsão exista para o primeiro turno
        self._ensure_prediction_ready()

    def _initialize_campaign_structure(self):
        """Executa o Pipeline de Setup para criar o Vilão e a Trama."""
        # 1. Executa a Regra de Setup
        campaign_data = self.pipeline.execute_rule(
            "RULE_SETUP_ADVENTURE", 
            self.game_state, 
            context_override={"SCENARIO_CONTEXT": self.game_state['world_data'].get('description', '')}
        )
        
        if campaign_data:
            # Salva o resultado no estado
            self.game_state['state']['campaign_front'] = campaign_data
            
            # Tenta pegar o nome da ameaça para logar
            danger = campaign_data.get('danger', 'Desconhecido')
            print(f"[CONTROLLER] Setup concluído: {danger}")
            
            # Gera a primeira cena imediatamente após o setup
            self._trigger_scene_transition("START_GAME")
            self.save_game()
        else:
            print("[ERRO CRÍTICO] Falha ao gerar Campanha. Pipeline retornou None.")

    def process_turn(self, user_input: str) -> str:
        """Ciclo Principal: Input -> Arbiter -> ANPA -> ENS -> Output"""
        print(f"[CONTROLLER] Processando: '{user_input}'")
        
        # 1. ARBITER (Verifica regras e testes)
        print("[1/5] Consultando Arbiter...")
        rule_verdict = self.arbiter.judge_action(user_input, self.game_state)
        rule_triggered = rule_verdict.get('trigger', 'NULL')
        print(f"      > Regra: {rule_triggered} | Condição: {rule_verdict.get('condition')}")

        # 2. ANPA (Resolve a ação e atualiza mecânicas)
        print("[3/5] ANPA: Resolvendo Ação...")
        anpa_outcome = self.anpa.resolve_turn(user_input, rule_verdict, self.game_state)
        
        # 3. APLICA ATUALIZAÇÕES (Inventário, Relógios, Transições)
        # O ANPA retorna 'system_dict' já limpo pelo anpa_engine.py
        system_updates = anpa_outcome.get('system_dict', {})
        self._apply_system_updates(system_updates)

        # 4. ENS (Gera a narração final)
        print("[4/5] Gerando Narração Final...")
        narration = self.narrator.narrate(
            anpa_outcome.get('narrator', ''), # Texto base da IA
            self.game_state
        )

        # 5. ATUALIZA HISTÓRICO E TURNO
        self.game_state['meta']['turn_count'] += 1
        
        # Salva no histórico (Temp)
        if 'history' not in self.game_state['state']: self.game_state['state']['history'] = []
        self.game_state['state']['history'].append({
            "role": "user", "content": user_input
        })
        self.game_state['state']['history'].append({
            "role": "assistant", "content": narration
        })

        # 6. GERA PREVISÃO PARA O PRÓXIMO TURNO
        self._ensure_prediction_ready()

        # 7. AUTO-SAVE
        self.save_game()

        return narration

    def _apply_system_updates(self, sistema_data: dict):
        """Aplica mudanças de estado vindas da IA (Inventário, Relógios, Transições)."""
        if not sistema_data: return
        
        print(f"\n[SISTEMA] Processando atualizações...")
        state = self.game_state['state']
        front = state.get('campaign_front', {})
        
        # --- CORREÇÃO DE INVENTÁRIO (BLINDAGEM CONTRA VAZIOS) ---
        if 'inventory_updates' in sistema_data:
            updates = sistema_data['inventory_updates']
            # Garante que é lista (caso o ANPA não tenha convertido)
            if isinstance(updates, dict): updates = [updates]
            if isinstance(updates, list):
                for update in updates:
                    item_name = update.get('item')
                    
                    # FILTRO: Ignora itens sem nome ou vazios
                    if not item_name or str(item_name).strip() == "":
                        continue

                    # Normaliza quantidade (qty vs quantity)
                    qty_change = int(update.get('qty', update.get('quantity', 0)))
                    if qty_change == 0: qty_change = 1 # Fallback

                    inventory = state['character'].get('inventory', [])
                    
                    # Verifica se item já existe
                    existing = next((i for i in inventory if i['item'] == item_name), None)
                    
                    if existing:
                        existing['qty'] = int(existing.get('qty', 1)) + qty_change
                        if existing['qty'] <= 0: inventory.remove(existing)
                    elif qty_change > 0:
                        inventory.append({"item": item_name, "qty": qty_change, "type": update.get('type', 'item')})
                    
                    state['character']['inventory'] = inventory
                    print(f"      > Item '{item_name}': {qty_change:+d}")

        # --- CORREÇÃO DOS RELÓGIOS (LOCALIZAÇÃO HÍBRIDA) ---
        def get_clock(clock_name):
            """Busca relógio na raiz ou aninhado em current_clocks"""
            if not front: return {}
            # 1. Tenta na raiz (Parser Achatado)
            if isinstance(front.get(clock_name), dict):
                return front[clock_name]
            # 2. Tenta dentro de current_clocks (Estrutura Aninhada)
            elif isinstance(front.get('current_clocks'), dict):
                return front['current_clocks'].get(clock_name, {})
            return {}

        trigger = sistema_data.get('event_trigger')
        
        # Lógica de Relógios
        if trigger == 'RESOLUTION_PROGRESS':
            clock = get_clock('resolution_clock')
            if clock:
                curr = int(clock.get('current_segments', 0))
                maxim = int(clock.get('max_segments', 4))
                clock['current_segments'] = min(curr + 1, maxim)
                print(f"      > [RELÓGIO] Resolução: {clock['current_segments']}/{maxim}")
                
                if clock['current_segments'] >= maxim:
                    self._trigger_scene_transition("ARC_CLIMAX_READY")

        elif trigger == 'THREAT_PROGRESS':
            clock = get_clock('threat_clock')
            if clock:
                curr = int(clock.get('current_segments', 0))
                maxim = int(clock.get('max_segments', 6))
                clock['current_segments'] = min(curr + 1, maxim)
                print(f"      > [RELÓGIO] Ameaça: {clock['current_segments']}/{maxim}")
                
                if clock['current_segments'] >= maxim:
                    self._trigger_scene_transition("ARC_FAILURE_IMMINENT")

        # Transições de Cena
        elif trigger in ['SCENE_COMPLETE', 'SCENE_COMPLETE_GENERIC']:
            self._trigger_scene_transition(trigger)
            
        elif trigger == 'ORACLE_CONSULT':
            print(f"      > [ORÁCULO]: {sistema_data.get('oracle_params')}")

    def _trigger_scene_transition(self, transition_type: str):
        """Gera uma nova cena e atualiza o contexto."""
        print(f"      > [EVENTO]: Transição de cena ({transition_type})...")
        
        # Chama o Gerador de Cenas
        new_scene = self.scene_gen.generate_new_scene(self.game_state)
        
        if new_scene:
            self.game_state['state']['current_scene_context'] = new_scene
            # Reseta árvore de previsão ao mudar de cena
            self.game_state['state']['prediction_tree'] = {} 
            
            # Log bonito no console
            print(f"\n=== NOVA CENA: {new_scene.get('location_name')} ===")
            print(f"Objetivo: {new_scene.get('scene_objective')}")
            print("=========================================\n")
            
            # (Opcional) Forçar uma narração de entrada de cena aqui se desejar
        else:
            print("[ERRO] Falha ao gerar nova cena.")

    def _ensure_prediction_ready(self):
        """Garante que existem sugestões de ação para o jogador."""
        try:
            tree = self.anpa.generate_prediction_tree(self.game_state)
            if tree:
                self.game_state['state']['prediction_tree'] = tree
        except Exception as e:
            print(f"[AVISO] Não foi possível gerar previsões: {e}")

    def save_game(self):
        """Salva o estado no disco."""
        with open(self.save_path, 'w', encoding='utf-8') as f:
            json.dump(self.game_state, f, indent=2, ensure_ascii=False)

    def get_recent_history_text(self):
        """Retorna o texto introdutório ao carregar o jogo."""
        scene = self.game_state['state'].get('current_scene_context', {})
        front = self.game_state['state'].get('campaign_front', {})
        danger = front.get('danger', 'Desconhecido') if front else 'Nenhum'
        
        return (
            f"[INTRO]: Retornando à aventura...\n"
            f"[SISTEMA]: Ameaça Atual: {danger}\n\n"
            f"        --- LOCAL ATUAL ---\n"
            f"        LOCAL: {scene.get('location_name', 'Desconhecido')}\n"
            f"        OBJETIVO: {scene.get('scene_objective', 'Sobreviver')}\n"
            f"        "
        )