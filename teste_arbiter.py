import json
from modules.rule_arbiter import RuleArbiter

# 1. Carrega o Mock (Dieselpunk) que criamos
with open("data/game_history/save_mock_dieselpunk.json", "r") as f:
    state = json.load(f)

# 2. Instancia o Arbiter
arbiter = RuleArbiter()

# 3. Define cenários de teste
testes = [
    "Eu olho ao redor procurando inimigos.", # Esperado: NULL (Sem risco)
    "Atiro com minha escopeta no bandido!", # Esperado: RULE_DOMINUS_CHALLENGE + VANTAGEM (Item adequado)
    "Tento hackear a porta eletrônica.",     # Esperado: RULE_DOMINUS_CHALLENGE + DESVANTAGEM (Arquétipo errado)
]

print("=== INICIANDO TESTE DO ARBITER ===")

for acao in testes:
    print(f"\nJOGADOR: '{acao}'")
    resultado = arbiter.analyze(acao, state)
    print(f"VEREDITO: {resultado}")