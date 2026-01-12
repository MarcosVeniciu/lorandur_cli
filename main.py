import sys
import os
import asyncio
from typing import Dict, Any

# Garante que o Python encontre os módulos locais
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from game_controller import GameController
from engine.sync_manager import SyncManager
from database.db_manager import DBManager

def system_bootstrap():
    """
    Inicialização do Sistema.
    Verifica integridade, sincroniza módulos e prepara o ambiente.
    """
    print("\n[SYSTEM] 🚀 Inicializando Lorandur Engine V5...")
    
    # 0. Limpeza de Banco (Solicitado para remover prompts antigos)
    print("[SYSTEM] Limpando cache de módulos antigos...")
    db = DBManager()
    db.clear_all_modules()

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
        print("3. Testar Geração Completa (Trama + Frente)")
        print("0. Sair")
        
        choice = input("\nEscolha: ")
        
        if choice == "1":
            seeds = {
                "col1_event": input("O que aconteceu? (Enter para Padrão): ") or "Um comboio desapareceu",
                "col2_goal": input("Objetivo? (Enter para Padrão): ") or "Resgatar sobreviventes",
                "col3_consequence": input("Consequência? (Enter para Padrão): ") or "A cidade fica sem água"
            }
            controller.start_new_game("dieselpunk", seed_data=seeds)
            
            print("\nGerando Trama Inicial...")
            controller.step_generate_trama()
            
            print("\nGerando Frente de Aventura (Pipeline)...")
            # Pipeline é async, precisamos rodar no loop
            loop = asyncio.get_event_loop()
            loop.run_until_complete(controller.generate_adventure_front_pipeline())
            
            controller.save_game()
            
        elif choice == "2":
            # Listar saves (simplificado)
            base_dir = os.path.dirname(os.path.abspath(__file__))
            save_dir = os.path.join(base_dir, "saves")
            if not os.path.exists(save_dir): os.makedirs(save_dir)
            
            saves = [f for f in os.listdir(save_dir) if f.endswith(".json")]
            if not saves:
                print("Nenhum save encontrado.")
                continue
            
            print("\nSaves Disponíveis:")
            for i, s in enumerate(saves):
                print(f"{i+1}. {s}")
            
            try:
                idx = int(input("Qual save carregar? ")) - 1
                if 0 <= idx < len(saves):
                    controller.load_game(saves[idx])
            except ValueError:
                print("Entrada inválida.")
                
        elif choice == "3":
            print("Iniciando teste rápido...")
            controller.start_new_game("dieselpunk")
            controller.step_generate_trama()
            loop = asyncio.get_event_loop()
            loop.run_until_complete(controller.generate_adventure_front_pipeline())
            
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