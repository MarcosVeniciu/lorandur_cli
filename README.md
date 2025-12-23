# Lorandur CLI - Sistema de RPG GenAI

## 🏗️ Arquitetura

Este projeto implementa um **sistema de RPG GenAI** usando uma arquitetura CLI (Command Line Interface) baseada no padrão **Orquestrador** e **Engine de Narrativa Silenciosa (ENS)**.

### 🎯 Estrutura do Projeto

```
lorandur_cli/
├── main.py                    # Entry Point e interface de usuário (terminal)
├── game_controller.py         # O cérebro do sistema (padrão Mediator)
├── model_llm.py              # Camada de abstração da API (Gateway)
├── secrets.json              # Configuração de APIs e chaves
├── utils/                     # Ferramentas e utilitários
│   ├── __init__.py
│   ├── debug_logger.py       # O Escrivão (observabilidade total)
│   └── file_manager.py       # O Arquivista (manipulação de I/O e merge)
├── data/                      # Dados estáticos e dinâmicos
│   ├── core_rules.json       # O System Pack (regras imutáveis)
│   └── game_history/         # Saves dos jogos
├── scenarios/                 # Pacotes de conteúdo
│   └── prehistoria.json      # Scenario Pack (Pré-História)
├── modules/                   # Agentes de execução
│   ├── __init__.py
│   └── module_ens_narrator/  # Engine de Narrativa Silenciosa (ENS)
│       ├── __init__.py
│       └── prompts/          # Repositório de templates
│           ├── __init__.py
│           └── ens_narrator.py
└── Logger/                    # Sistema de logs
    └── game_logger/          # Save dos logs
```

### 🔄 Fluxo de Operação

1. **Inicialização**: `main.py` lista cenários disponíveis
2. **Seleção**: Usuário escolhe um cenário
3. **Build**: `GameController` faz merge de `core_rules.json` + `cenario.json`
4. **Jogo**: Loop infinito de input -> processamento -> output
5. **Log**: Todo evento é registrado pelo `DebugLogger`

### 🎮 Como Executar

```bash
# Instalar dependências (quando implementadas)
pip install -r requirements.txt

# Executar o jogo
python main.py
```

### 📋 Próximos Passos

- [ ] Implementar lógica do `main.py`
- [ ] Implementar `GameController` com padrão Mediator
- [ ] Configurar comunicação com LLMs em `model_llm.py`
- [ ] Implementar `DebugLogger` para observabilidade
- [ ] Implementar `FileManager` com lógica de merge
- [ ] Desenvolver módulos ENS para geração de narrativa
- [ ] Criar mais cenários de jogo
- [ ] Implementar sistema de saves/carregamento

### 🔒 Segurança

- `secrets.json` contém chaves sensíveis e está no `.gitignore`
- Sempre use variáveis de ambiente para produção

---

**Nota**: Este projeto foi criado seguindo a arquitetura definida no documento *Arquitetura RPG GenAI v4.1* e *Núcleo Orquestrador*.
