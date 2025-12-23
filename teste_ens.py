import json
from modules.ens_narrator import ENSNarrator

# 1. Carrega o Mock
with open("data/game_history/save_mock_dieselpunk.json", "r") as f:
    state = json.load(f)

# 2. Instancia a ENS
narrator = ENSNarrator()

# 3. Cenários de Teste
testes = [
    {
        "input": "Quem é você e o que quer?", 
        "success": True, 
        "desc": "Conversa Simples (NPC deve responder)"
    },
    {
        "input": "Ataco ele com minha escopeta!", 
        "success": True, 
        "desc": "Gatilho de Combate (Deve ativar COMBAT_START)"
    },
    {
        "input": "Olho se tem sniper no telhado.", 
        "success": True, 
        "desc": "Dúvida de Oráculo (Deve ativar ORACLE_CONSULT)"
    }
]

print("=== INICIANDO TESTE DA ENS ===")

for t in testes:
    print(f"\n--- TESTE: {t['desc']} ---")
    print(f"INPUT: '{t['input']}' (Sucesso no Dado: {t['success']})")
    
    resultado = narrator.generate(t['input'], state, action_success=t['success'])
    
    print("\n[RESPOSTA IA]:")
    if 'pensamento' in resultado:
        print(f"PENSAMENTO: {resultado['pensamento']}")
    if 'narrator' in resultado:
        print(f"NARRADOR: {resultado['narrator']}")
    if 'npc' in resultado:
        print(f"NPC: {resultado['npc']}")
    if 'sistema' in resultado:
        print(f"SISTEMA: {resultado['sistema']}")