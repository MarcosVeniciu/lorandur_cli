import sys
import os
import time
from typing import Dict, Any

# Garante que o Python encontre os módulos locais
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from game_controller import GameController
from engine.sync_manager import SyncManager
from utils.debug_logger import DebugLogger

def system_bootstrap():
    """
    Inicialização do Sistema.
    Verifica integridade, sincroniza módulos e prepara o ambiente.
    """
    print("\n[SYSTEM] 🚀 Inicializando Lorandur Engine V5...")
    
    # 1. Sincronização de Dados (Data-Driven Engine)
    # Lê os JSONs em modules_source/ e atualiza o SQLite criptografado
    print("[SYSTEM] Sincronizando Módulos de Regras...")
    sync = SyncManager()
    report = sync.sync_all()
    
    # Feedback visual rápido
    if report['updated']:
        print(f"[SYSTEM] ✅ Módulos Atualizados: {len(report['updated'])}")
    if report['errors']:
        print(f"[SYSTEM] ⚠️  Erros na Sincronização: {report['errors']}")
    
    print("[SYSTEM] Bootstrap Concluído.\n")

def main_menu():
    controller = GameController()
    
    while True:
        print("\n=== LORANDUR RPG CLI (V5) ===")
        print("1. Novo Jogo (Dieselpunk)")
        print("2. Carregar Jogo")
        print("3. Testar Geração de Trama (Rápido)")
        print("0. Sair")
        
        choice = input("\nEscolha: ")
        
        if choice == "1":
            # Dados Mockados para teste rápido (Input do usuário viria aqui)
            seeds = {
                "col1_event": input("O que aconteceu? (Enter para Padrão): ") or "Um comboio desapareceu",
                "col2_goal": input("Objetivo? (Enter para Padrão): ") or "Resgatar sobreviventes",
                "col3_consequence": input("Consequência? (Enter para Padrão): ") or "A cidade fica sem água"
            }
            controller.start_new_game("dieselpunk", seed_data=seeds)
            
            # Exemplo de fluxo: Gera Trama -> Salva
            controller.step_generate_trama()
            controller.save_game()
            
        elif choice == "2":
            saves = [f for f in os.listdir("lorandur_cli/saves") if f.endswith(".json")]
            if not saves:
                print("Nenhum save encontrado.")
                continue
            
            print("\nSaves Disponíveis:")
            for i, s in enumerate(saves):
                print(f"{i+1}. {s}")
            
            idx = int(input("Qual save carregar? ")) - 1
            if 0 <= idx < len(saves):
                controller.load_game(saves[idx])
                
        elif choice == "3":
            # Atalho para debug
            print("Iniciando teste rápido de trama...")
            controller.start_new_game("dieselpunk")
            controller.step_generate_trama()
            
        elif choice == "0":
            print("Saindo... Que os dados rolem a seu favor.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    try:
        system_bootstrap()
        main_menu()
    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário.")
    except Exception as e:
        print(f"\n[CRITICAL ERROR] O sistema falhou: {e}")
        # Em produção, logar stacktrace em arquivo