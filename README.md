# Lorandur CLI - Sistema de RPG GenAI

## 🏗️ Arquitetura

Este projeto é uma engine de RPG textual baseada em Inteligência Artificial Generativa (LLM). Ele utiliza uma **Arquitetura Orientada a Dados**, onde a lógica do jogo vive em arquivos JSON (`modules_source/`) e é executada por um motor genérico (`engine/module_executor.py`).

### 🎯 Nova Estrutura do Projeto

```
lorandur_cli/
├── main.py                    # Entry Point e Loop Principal
├── game_controller.py         # Orquestrador do sistema
├── model_llm.py               # Cliente da API LLM (OpenRouter/Gemini)
├── secrets.json               # Chaves de API e Configurações
│
├── database/                  # Camada de Dados
│   └── db_manager.py          # Gerenciador do SQLite
│
├── engine/                    # O Motor Genérico
│   ├── crypto_utils.py        # Criptografia
│   ├── dice_utils.py          # Rolador de Dados (Dice Notation)
│   ├── module_executor.py     # Executor Universal de módulos JSON
│   └── sync_manager.py        # Sincronizador JSON -> DB
│
├── modules_source/            # Módulos de Jogo (Lógica em JSON)
│   └── trama.json             # Módulo de Criação de Trama
│
├── data/                      # Dados do Sistema
│   └── core_rules.json        # Regras Core do Lorandur
│
├── scenarios/                 # Pacotes de Conteúdo (Settings)
│   ├── dieselpunk.json        # Cenário Dieselpunk
│   └── prehistoria.json       # Cenário Pré-História
│
├── saves/                     # Saves dos jogadores
│
├── teste/                     # Testes automatizados
│   └── fixtures/              # JSONs de teste
│
├── utils/                     # Ferramentas de suporte
│   ├── debug_logger.py        # Logger para depuração em Markdown
│   ├── file_manager.py        # Gerenciamento de I/O e Saves
│   └── xml_parser.py          # Extrator e limpador de tags XML
│
└── Logger/                    # Logs de execução
    └── game_logger/           # Histórico de partidas em Markdown
```

---

## 📐 Arquitetura Orientada a Dados

### Conceito Principal

Na **Arquitetura Imperativa Anterior** (v4.x), cada módulo era um arquivo Python:
- `modules/trama.py`, `modules/frente_aventura.py`, etc.

Na **Nova Arquitetura Orientada a Dados** (v5.0), a lógica vive em JSON:
- `modules_source/trama.json`, `modules_source/frente_aventura.json`, etc.

### Como Funciona

1. **Definição:** A lógica do jogo é definida em arquivos JSON dentro de `modules_source/`
2. **Execução:** O `engine/module_executor.py` lê o JSON e executa a lógica
3. **Dados:** `data/core_rules.json` contém as regras universais
4. **Conteúdo:** `scenarios/` contém os pacotes de cenário específicos

### Vantagens

- **Extensibilidade:** Novos módulos podem ser adicionados sem código
- **Manutenibilidade:** Alterações na lógica são feitas em JSON, não Python
- **Testabilidade:** JSONs podem ser validados independentemente
- **Versionamento:** Mudanças de lógica podem ser versionadas facilmente

---

## 🚀 Como Rodar

1. Certifique-se de ter o Python instalado
2. Instale a dependência de requisições:
```bash
pip install requests
```

3. Configure sua chave no `secrets.json`

4. Execute o jogo:
```bash
python main.py
```

---

## 📚 Referência de Documentação

- **Versão da Engine:** v5.0 (Data-Oriented Architecture)
- **Sistema de Regras:** Lorandur Core Ruleset v5.0
- **Conceitos:**
  - *Module Executor*: Motor genérico que executa módulos JSON
  - *Sync Manager*: Sincroniza estado entre JSON e SQLite
  - *Data-Driven Design*: Lógica definida em dados, não código
