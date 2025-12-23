import os
import sys

# Importações diretas (já que modules, utils e game_controller estão na raiz)
from game_controller import GameController
from utils.file_manager import FileManager

def main():
    # CONFIGURAÇÃO DE PASTAS (Baseado na sua imagem)
    # data/ -> Contém core_rules.json
    # scenarios/ -> Contém dieselpunk.json
    # saves/ -> Será criada para salvar os jogos
    fm = FileManager(data_dir="data", scenarios_dir="scenarios", saves_dir="saves")
    
    print("\n=== LORANDUR RPG ENGINE v4.1 (ROOT MODE) ===")
    print("1. Novo Jogo")
    print("2. Carregar Jogo")
    print("0. Sair")
    
    choice = input("\nEscolha: ").strip()
    save_path = None
    
    if choice == "1":
        # --- NOVO JOGO ---
        scenarios = fm.list_scenarios()
        
        if not scenarios:
            print(f"\n[ERRO] Nenhum cenário encontrado na pasta '{fm.scenarios_dir}'.")
            print("Verifique se 'dieselpunk.json' está dentro da pasta 'scenarios'.")
            return

        print("\n=== CENÁRIOS DISPONÍVEIS ===")
        for i, sc in enumerate(scenarios):
            print(f"{i+1}. {sc}")
        print("0. Cancelar")
        
        try:
            sel = int(input("\nEscolha o número do cenário: "))
            if sel == 0: return
            if 1 <= sel <= len(scenarios):
                chosen_file = scenarios[sel-1]
                print(f"\nGerando novo mundo baseado em {chosen_file}...")
                # Aqui o FileManager sabe buscar em 'scenarios/' e fundir com 'data/core_rules.json'
                save_path = fm.create_new_campaign(chosen_file)
            else:
                print("Opção inválida.")
                return
        except ValueError:
            print("Entrada inválida.")
            return

    elif choice == "2":
        # --- CARREGAR JOGO ---
        saves = fm.list_saves()
        if not saves:
            print(f"\nNenhum save encontrado em '{fm.saves_dir}'.")
            return
            
        print("\n=== JOGOS SALVOS ===")
        saves.sort(reverse=True)
        for i, sv in enumerate(saves):
            print(f"{i+1}. {sv}")
        
        try:
            sel = int(input("\nEscolha o save: "))
            if 1 <= sel <= len(saves):
                save_path = os.path.join(fm.saves_dir, saves[sel-1])
            else:
                return
        except:
            return

    elif choice == "0":
        print("Saindo...")
        return

    # --- LOOP DE JOGO ---
    if save_path:
        try:
            controller = GameController(save_path)
            
            print("\n" + "="*40)
            print(controller.get_recent_history_text())
            print("="*40 + "\n")
            
            while True:
                user_input = input("\nVocê > ").strip()
                
                if user_input.lower() in ["/sair", "/exit", "/quit"]:
                    print("Salvando e saindo...")
                    break
                
                if user_input.lower() == "/debug":
                    # Mostra estado interno para debug
                    print(json.dumps(controller.game_state['state'], indent=2, ensure_ascii=False))
                    continue
                
                if user_input:
                    response = controller.process_turn(user_input)
                    print(response)
                    
        except Exception as e:
            print(f"\n[ERRO CRÍTICO]: {e}")
            import traceback
            traceback.print_exc()
            input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()