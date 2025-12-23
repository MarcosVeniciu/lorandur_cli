# Lorandur CLI - Sistema de RPG GenAI

## 🏗️ Arquitetura

Este projeto é uma engine de RPG textual baseada em Inteligência Artificial Generativa (LLM). Ele utiliza uma arquitetura modular de "Agentes Especializados" para narrar, arbitrar regras e gerenciar o estado do jogo de forma determinística e criativa.

### 🎯 Estrutura do Projeto

```
lorandur_cli/
├── main.py                    # Entry Point e Loop Principal
├── game_controller.py         # O cérebro do sistema (Orquestrador)
├── model_llm.py               # Cliente da API LLM (OpenRouter/Gemini)
├── secrets.json               # Chaves de API e Configurações
├── test_llm.py                # Script de diagnóstico de conexão
├── ver_arvore.py              # Utilitário de visualização de arquivos
├── utils/                     # Ferramentas de suporte
│   ├── debug_logger.py        # Logger para depuração em Markdown
│   ├── file_manager.py        # Gerenciamento de I/O e Saves
│   └── xml_parser.py          # Extrator e limpador de tags XML
├── modules/                   # Agentes de Execução (Lógica do RPG)
│   ├── anpa_engine.py         # Motor de Ação e Física (ANPA)
│   ├── ens_narrator.py        # Sistema de Narração Elástica (ENS)
│   ├── pipeline_engine.py     # Executor de Pipelines (Setup/Crafting)
│   ├── rule_arbiter.py        # Árbitro de Regras e Julgamento
│   ├── scene_generator.py     # Orquestrador de Geração de Cenas
│   ├── macro_director.py      # Gerador de Ambiente Macro (Nível 1)
│   ├── micro_planner.py       # Planejador de Micro Local (Nível 2)
│   └── tactical_generator.py  # Gerador Tático e Mecânico (Nível 3)
├── data/                      # Dados do Sistema
│   └── core_rules.json        # Regras Core do Lorandur
├── scenarios/                 # Pacotes de Conteúdo (Settings)
│   ├── dieselpunk.json        # Cenário Dieselpunk
│   └── prehistoria.json       # Cenário Pré-História
├── saves/                     # Arquivos de Save Game (.json)
└── Logger/                    # Logs de execução
    └── game_logger/           # Histórico de partidas em Markdown
```



## 🏗️ Arquitetura do Sistema

O sistema segue o fluxo **Input -> Arbiter -> ANPA -> ENS -> Output**:

1. **Input:** O jogador digita uma ação.
2. **Arbiter:** Decide se uma regra mecânica (ex: teste de perícia) se aplica.
3. **ANPA (Action & Narrative Physics Agent):** Resolve o resultado lógico e atualiza o estado (inventário, vida, relógios).
4. **ENS (Elastic Narrative System):** Transforma os dados técnicos em uma narração imersiva.
5. **Scene Generator:** Cria novos locais e desafios proceduralmente quando necessário.

---

## 📂 Estrutura de Arquivos

### 🔴 Raiz (`/`)

Arquivos principais de execução e configuração.

* **`main.py`**: O ponto de entrada. Gerencia o menu inicial (Novo Jogo/Carregar), inicializa o `FileManager` e o loop principal de input do usuário.
* **`game_controller.py`**: O "cérebro" do sistema. Orquestra todos os módulos (Arbiter, ANPA, ENS), gerencia o ciclo de vida do turno, o autosave e as transições de cena.
* **`model_llm.py`**: Cliente de conexão com a API (OpenRouter/Google Gemini). Abstrai o envio de prompts e tratamento de erros de rede.
* **`secrets.json`**: Arquivo de configuração sensível contendo a `OPENROUTER_API_KEY` e URLs do site. **Não deve ser commitado**.
* **`test_llm.py`**: Script utilitário para testar se a conexão com a API da IA está funcionando antes de rodar o jogo.
* **`ver_arvore.py`**: Script auxiliar para visualizar a estrutura de pastas do projeto no terminal.

### 🧠 Módulos (`/modules`)

Agentes especializados que executam a lógica do RPG.

* **`pipeline_engine.py`**: Motor de execução de regras complexas em etapas (ex: criação inicial da campanha, crafting).
* **`rule_arbiter.py`**: Analisa o texto do jogador e decide qual regra do sistema (definida em `core_rules.json`) deve ser ativada (Veredito: Trigger + Condição).
* **`anpa_engine.py`**: O "Físico" do mundo. Recebe o veredito, calcula sucesso/falha, atualiza inventário, relógios de progresso e gera a árvore de previsão de ações futuras.
* **`ens_narrator.py`**: O "Narrador". Recebe os dados brutos do ANPA e escreve a resposta final para o jogador, garantindo o estilo literário e consistência.
* **`scene_generator.py`**: O orquestrador da geração de cenas. Ele chama os três sub-módulos abaixo para criar um local completo.
* **`macro_director.py`**: Define o ambiente geral e atmosfera (Nível 1).
* **`micro_planner.py`**: Define os detalhes da sala/local específico e objetos interativos (Nível 2).
* **`tactical_generator.py`**: Define mecânicas, NPCs, segredos e configura os Relógios de Ameaça/Resolução (Nível 3).



### 🛠️ Utilitários (`/utils`)

Ferramentas de suporte.

* **`file_manager.py`**: Gerencia leitura/escrita de arquivos JSON. Responsável por criar novos saves fundindo as regras do sistema (`core_rules`) com os dados do cenário escolhido (`dieselpunk.json`).
* **`xml_parser.py`**: Parser robusto (com regex e recursão) para extrair dados estruturados (XML) das respostas da IA, ignorando "alucinações" de markdown.
* **`debug_logger.py`**: Grava logs detalhados de cada turno na pasta `Logger/`, essencial para entender o raciocínio da IA.

### 📚 Dados (`/data` e `/scenarios`)

Conteúdo estático e estado do jogo.

* **`data/core_rules.json`**: Contém as regras universais do sistema (ex: como funciona combate, testes de perícia, pipelines de setup).
* **`scenarios/dieselpunk.json`**: Pacote de conteúdo específico. Define arquétipos, itens, veículos e tabelas aleatórias para o cenário Dieselpunk.
* **`saves/*.json`**: Arquivos de save game. Contêm o estado completo (persongem, mundo, histórico) em JSON.

---

## 🚀 Como Rodar

1. Certifique-se de ter o Python instalado.
2. Instale a dependência de requisições:
```bash
pip install requests

```


3. Configure sua chave no `secrets.json`.
4. Execute o jogo:
```bash
python main.py

```



---

## 📄 Referência de Documentação

A estrutura e nomenclatura deste projeto seguem as especificações encontradas nos arquivos de configuração do próprio sistema:

* **Versão da Engine:** v4.1 (Root Mode).
* **Sistema de Regras:** Lorandur Core Ruleset v4.1.
* **Conceitos:**
* *Pipeline Chain*: Método de construção sequencial de campanhas.
* *Type I/Type X Rules*: Categorização de regras (Construção vs Mecânica).
* *Dominus System*: Base para os desafios procedurais.