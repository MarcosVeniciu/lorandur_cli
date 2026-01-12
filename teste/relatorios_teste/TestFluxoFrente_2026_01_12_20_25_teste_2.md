# Relatório: Teste Completo: Trama & Frente Pipeline (Com Respostas)
**Data:** 2026_01_12_20_25 | **Status:** ✅ Sucesso

## 📊 Métricas de Execução

| Métrica | 1. Trama | 2. Front Arquiteto | 3. Front World | 4. Front Story | Total |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tempo Total** | 9.33s | 12.30s | 7.14s | 18.18s | **46.95s** |
| **Tokens Entrada** | 877 | 2784 | 3836 | 6822 | **14319** |
| **Tokens Saída** | 1698 | 2077 | 1347 | 3422 | **8544** |
| **Tokens Total** | 2575 | 4861 | 5183 | 10244 | **22863** |
| **Custo Estimado** | $0.000767 | $0.001109 | $0.000922 | $0.002051 | **$0.004849** |

---

## 1. 1. Trama (Módulo: `core_trama_generator`)
<details>
<summary><strong>⚙️ Ver Prompts & Request</strong></summary>

**System Prompt:**
```text
Você é um Mestre de RPG especialista e Designer Narrativo.

# Objetivo
Sua tarefa é criar uma estrutura de aventura completa e coesa a partir de sementes aleatórias, definindo o tom, o escopo e a gestão de mistérios.

# Instruções de Processamento

1. **Análise de Estilo (Geração de Subgêneros):**
   - O Gênero Principal é fixo pelo Cenário (Dieselpunk).
   - Analise a combinação da Trama sorteada ({'col1_event': 'Uma carga valiosa foi roubada', 'col2_goal': 'Recuperar a carga antes do amanhecer', 'col3_consequence': 'Guerra entre gangues rivais'}). Que tipo de história isso sugere? (Ex: Drama, Comédia, Terror, Noir, Ação Frenética).
   - Selecione 2 ou 3 **Subgêneros (Tags)** que darão personalidade única a essa aventura específica.

2. **Seleção de Escopo:**
   - Analise a lista de 'Níveis de Escopo Suportados' fornecida.
   - Escolha UM dos níveis que melhor sirva aos Subgêneros escolhidos e à Trama gerada.
   - **CRÍTICO:** No campo `escopo`, você deve copiar o texto **COMPLETO** da opção escolhida (incluindo a descrição após os dois pontos). Não abrevie e não coloque apenas o título. Exemplo de saída correta: "Nível 2 (Escopo Local): A trama ocorre em..."

3. **Construção Narrativa (Argumento e Premissas):**
   - **Crie o Argumento:** É o resumo da 'Verdade do Mestre'. Deve responder: Onde (local), Quando (tempo), Quem (envolvidos), Por que (motivação oculta) e Como (contexto).
   - **Defina as Premissas:**
     - *Premissa Evidente (O Briefing):* A 'falsa verdade' ou missão superficial entregue aos jogadores no início.
     - *Premissa Oculta (O Twist):* Os segredos do Argumento. A revelação que subverte a missão.

4. **Gestão da Informação (A Matriz):**
   - Crie uma 'Matriz de Controle de Informação' com 3 itens principais para gerenciar a Quebra de Expectativa.
   - Para cada item defina:
     - **Título:** Nome do mistério.
     - **A Verdade:** O fato real (Oculto).
     - **A Expectativa:** O clichê ou suposição que os jogadores terão inicialmente.
     - **A Camuflagem:** Como essa verdade está escondida na cena.
     - **O Gatilho:** O que precisa acontecer para a revelação (ex: investigar o corpo, hackear o terminal).
     - **A Revelação:** O que é entregue aos jogadores quando o gatilho é ativado.

# Formato de Saída
Gere a resposta EXCLUSIVAMENTE em formato JSON seguindo o schema estrito.
```
**User Prompt:**
```text
# DADOS DE ENTRADA

1. **Cenário (Gênero Principal):** Dieselpunk

2. **Rolagem de Trama (Dominus):**
   - *Algo Aconteceu:* Uma carga valiosa foi roubada
   - *Você Precisa:* Recuperar a carga antes do amanhecer
   - *Senão:* Guerra entre gangues rivais

3. **Níveis de Escopo Suportados:**
Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.
Nível 3 (Escopo Regional - A Estrada): A trama é uma jornada. O foco é a travessia de A para B, gestão de combustível, perseguições e encontros na estrada.

Crie a estrutura agora.
```
**Schema Enviado:**
```json
{
  "type": "object",
  "properties": {
    "configuracao_aventura": {
      "type": "object",
      "properties": {
        "genero_principal": {
          "type": "string"
        },
        "subgeneros_selecionados": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "escopo": {
          "type": "string",
          "description": "Deve conter o nome do nível E a descrição completa fornecida na entrada."
        },
        "justificativa_estilo": {
          "type": "string"
        },
        "justificativa_escopo": {
          "type": "string"
        }
      },
      "required": [
        "genero_principal",
        "subgeneros_selecionados",
        "escopo"
      ]
    },
    "argumento": {
      "type": "object",
      "properties": {
        "texto": {
          "type": "string",
          "description": "Resumo completo da verdade do mestre (Quem, Onde, Quando, Por que)."
        },
        "justificativa": {
          "type": "string"
        }
      },
      "required": [
        "texto"
      ]
    },
    "premissas": {
      "type": "object",
      "properties": {
        "evidente": {
          "type": "object",
          "properties": {
            "texto": {
              "type": "string"
            },
            "funcao": {
              "type": "string"
            }
          },
          "required": [
            "texto"
          ]
        },
        "oculta": {
          "type": "object",
          "properties": {
            "texto": {
              "type": "string"
            },
            "funcao": {
              "type": "string"
            }
          },
          "required": [
            "texto"
          ]
        },
        "justificativa": {
          "type": "string"
        }
      },
      "required": [
        "evidente",
        "oculta"
      ]
    },
    "matriz_controle_informacao": {
      "type": "object",
      "properties": {
        "itens": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer"
              },
              "titulo": {
                "type": "string"
              },
              "a_verdade": {
                "type": "string"
              },
              "a_expectativa": {
                "type": "string"
              },
              "a_camuflagem": {
                "type": "string"
              },
              "o_gatilho": {
                "type": "string"
              },
              "a_revelacao": {
                "type": "string"
              }
            },
            "required": [
              "titulo",
              "a_verdade",
              "a_expectativa",
              "a_camuflagem",
              "o_gatilho",
              "a_revelacao"
            ]
          }
        },
        "justificativa": {
          "type": "string"
        }
      },
      "required": [
        "itens"
      ]
    }
  },
  "required": [
    "configuracao_aventura",
    "argumento",
    "premissas",
    "matriz_controle_informacao"
  ]
}
```
</details>

### 🤖 Resposta do Modelo
```json
{
  "configuracao_aventura": {
    "genero_principal": "Dieselpunk",
    "subgeneros_selecionados": [
      "Noir",
      "Ação Frenética",
      "Mistério"
    ],
    "escopo": "Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.",
    "justificativa_escopo": "A trama de roubo de carga e a potencial guerra entre gangues se encaixam perfeitamente em um ambiente contido como um assentamento isolado. Isso permite focar nas intrigas, na gestão de recursos e nas consequências imediatas do roubo, em vez de uma jornada mais dispersa. O escopo local facilita a criação de um senso de urgência e claustrofobia.",
    "justificativa_estilo": "A combinação de roubo de carga, prazo apertado (antes do amanhecer) e a ameaça de guerra entre gangues sugere uma história com elementos de Noir (investigação, traição, moralidade cinzenta), Ação Frenética (a corrida contra o tempo, confrontos diretos) e Mistério (descobrir quem roubou, por quê e como evitar a guerra)."
  },
  "argumento": {
    "texto": "Na metrópole distópica de Aethelburg, uma carga de Orichalcum recém-extraído, vital para a sobrevivência do assentamento isolado de 'O Poço', foi roubada do depósito de segurança da gangue 'Os Engrenagens' na noite anterior. Os Engrenagens acreditam que a gangue rival, 'Os Soberanos', são osAuthors do roubo, o que desencadeará uma guerra aberta ao amanhecer se a carga não for recuperada. Na verdade, a carga foi interceptada pelo líder de Os Engrenagens (mestre Silas) e seu braço direito (Lia 'A Chave'), que planejam vender o Orichalcum para um mercado negro interestelar para fugir de suas dívidas com um sindicato criminoso maior. Eles incriminaram Os Soberanos para criar o caos que lhes permitiria desaparecer com a carga.",
    "justificativa": "O argumento define o local (Aethelburg, O Poço), o tempo (na noite anterior, com a guerra iminente ao amanhecer), os principais envolvidos (Os Engrenagens, Os Soberanos, o Mestre Silas e Lia), a motivação oculta (fuga de dívidas e ganância, não rivalidade) e o contexto (um assentamento dependente de Orichalcum em um mundo Dieselpunk)."
  },
  "premissas": {
    "evidente": {
      "texto": "Uma carga de Orichalcum, essencial para O Poço, foi roubada *pelos Soberanos* e deve ser recuperada antes do amanhecer, sob pena de uma guerra sangrenta que destruirá o assentamento.",
      "funcao": "Estabelece a missão imediata, o vilão aparente e o perigo iminente."
    },
    "oculta": {
      "texto": "O líder de Os Engrenagens, o Mestre Silas, e sua tenente Lia roubaram a carga para vendê-la e quitar suas dívidas com um sindicato criminoso. Eles plantaram pistas falsas para incriminar Os Soberanos, usando a ameaça de guerra como cortina de fumaça para sua fuga.",
      "funcao": "Revela a verdadeira conspiração, a traição e a verdadeira motivação por trás do roubo, mudando a percepção dos jogadores sobre os inimigos e aliados."
    },
    "justificativa": "A premissa evidente lança os jogadores em uma corrida contra o tempo com um inimigo claro. A premissa oculta, quando revelada, subverte essa noção, mostrando que a verdadeira ameaça é interna e que o conflito aparente é uma distração orquestrada."
  },
  "matriz_controle_informacao": {
    "itens": [
      {
        "titulo": "A Origem do Roubo",
        "a_verdade": "O Mestre Silas e Lia roubaram a carga para pagar dívidas.",
        "a_expectativa": "Os Soberanos, gangue rival, roubaram a carga por causa da rivalidade usual.",
        "a_camuflagem": "Pistas falsas deixadas deliberadamente (ex: uma jaqueta dos Soberanos perto do local do crime, testemunhas pagas para incriminá-los).",
        "o_gatilho": "Investigar a cena do crime com detalhes, questionar testemunhas-chave sob pressão, encontrar equipamentos de 'Os Engrenagens' usados no roubo.",
        "a_revelacao": "As pistas falsas são descobertas como armadilhas, e evidências concretas apontam para a participação de Os Engrenagens no roubo.",
        "id": 1
      },
      {
        "titulo": "O Destino da Carga",
        "a_verdade": "A carga de Orichalcum está sendo preparada para ser vendida no mercado negro interestelar por Silas e Lia.",
        "a_expectativa": "A carga ainda está escondida em algum local secreto de Os Soberanos, ou foi destruída.",
        "a_camuflagem": "Comunicações interceptadas entre Silas e um contato misterioso (do sindicato), movimentação suspeita de veículos de carga 'piratas' nos arredores do Poço.",
        "o_gatilho": "Rastrear a origem das comunicações encontradas, interceptar um dos veículos de carga suspeitos, interrogar um cúmplice menor de Silas.",
        "a_revelacao": "Revela que a carga está sendo movida para fora do Poço por Os Engrenagens, não levada por Os Soberanos, e para um destino fora do planeta.",
        "id": 2
      },
      {
        "titulo": "A Verdadeira Motivação de Silas",
        "a_verdade": "Silas está endividado com um sindicato criminoso perigoso e usa o roubo como plano de fuga.",
        "a_expectativa": "Silas é apenas um líder de gangue ambicioso que quer mais poder ou quer provocar Os Soberanos.",
        "a_camuflagem": "Registros financeiros incomuns de Silas, comportamento paranoico, segredos sujos que ele tenta esconder a todo custo, 'visitas' inesperadas de figuras sombrias ao seu território.",
        "o_gatilho": "Obter acesso aos registros pessoais de Silas, capturar um dos cobradores de dívida do sindicato, encontrar evidências de comunicação anterior entre Silas e o sindicato.",
        "a_revelacao": "Descobre que Silas não é um vilão independente, mas sim um peão encurralado, e que uma força externa maior está envolvida.",
        "id": 3
      }
    ],
    "justificativa": "Esta matriz gerencia a quebra de expectativa, focando nas mentiras de Os Engrenagens. Cada item começa com uma suposição comum na trama de gangues e a transforma em algo mais complexo e surpreendente, culminando na verdade sobre a dívida de Silas e o envolvimento de um sindicato maior, incentivando os jogadores a reavaliar seus alvos e objetivos."
  }
}
```

## 2. 2. Front Arquiteto (Módulo: `step1_front_archetype`)
<details>
<summary><strong>⚙️ Ver Prompts & Request</strong></summary>

**System Prompt:**
```text
Você é um Mestre de RPG especialista e Designer Narrativo.

# **Objetivo**

Sua tarefa é iniciar a criação de uma "Frente de Aventura" (nível de sessão/episódio). Nesta **Fase 1**, você deve transformar os conceitos abstratos da Trama em uma estrutura sólida, definindo o **Tipo de Enredo**, o **Foco Narrativo** e a **Lista de Locais** onde a ação ocorrerá.

# **Instruções de Processamento**

1. **Análise de Contexto e Enredo:**
   * Analise o `genero_principal`, `subgeneros` e o `argumento` da trama.
   * Escolha UM dos 7 Tipos de Enredo abaixo para servir de espinha dorsal narrativa. Utilize a **Meta-Estrutura** do enredo escolhido para definir o tom dos Presságios:
   * **Superar o Monstro:** Foco em heroísmo e sobrevivência contra uma ameaça colossal.
     * **Meta-Estrutura:** 1. Antecipação/Chamado -> 2. Fase do Sonho (Preparação) -> 3. A Frustração -> 4. O Pesadelo -> 5. Fuga da Morte/Vitória.
   * **Da Miséria à Riqueza (Do Pano para a Manga):** Foco em crescimento pessoal e ascensão de status a partir do nada.
     * **Meta-Estrutura:** 1. Miséria Inicial -> 2. Sucesso Inicial -> 3. A Crise Central (Tudo dá errado) -> 4. Independência/Provação -> 5. Completude.
   * **A Busca:** Foco na viagem e trabalho em equipe para recuperar algo essencial.
     * **Meta-Estrutura:** 1. O Chamado -> 2. A Jornada -> 3. Chegada e Frustração (Barreira) -> 4. Provações Finais -> 5. O Objetivo.
   * **Viagem e Retorno:** Foco em exploração de um mundo estranho e a necessidade de escapar dele.
     * **Meta-Estrutura:** 1. Queda no Outro Mundo -> 2. Fascínio (Lua de Mel) -> 3. A Frustração (Regras Opressoras) -> 4. O Pesadelo (Sombra Hostil) -> 5. Fuga e Retorno.
   * **Renascimento:** Foco em redenção e libertação de uma maldição ou influência sombria.
     * **Meta-Estrutura:** 1. Queda sob a Sombra -> 2. Fase do Sonho (O Poder da Sombra) -> 3. A Frustração (Prisão) -> 4. O Pesadelo (Fundo do Poço) -> 5. O Renascimento.
   * **Tragédia:** Foco na consequência moral de buscar objetivos por meios proibidos.
     * **Meta-Estrutura:** 1. Tentação -> 2. Fase do Sonho (O Crime Compensa) -> 3. A Frustração (Consequências) -> 4. O Pesadelo (Perda de Controle) -> 5. Destruição.
   * **Comédia:** Foco em confusão, mal-entendidos e intriga social que caminham para a clareza.
     * **Meta-Estrutura:** 1. Sombra da Confusão -> 2. O Nó se Aperta -> 3. Clímax da Confusão (Caos Total) -> 4. A Revelação (Verdade) -> 5. Resolução/Festa.

2. **Instanciação de Locais (Location Pool):**
   * Trate a lista de 'tipos_locais_permitidos' como enredos narrativos abstratos e sementes temáticas, jamais como locais geográficos rígidos ou literais. Você deve adaptar dinamicamente esses descritores genéricos aplicando a técnica de **'Zoom Out Contextual'** para que se encaixem no Nível de Escopo (0 a 5) definido:
     * *Escalabilidade:* Se o descritor for 'Pequeno' mas o escopo for 'Macro', transforme-o em uma região/planeta com esse tema. Se for 'Vasto' mas o escopo for 'Micro', foque em um detalhe específico.
     * *Contexto de Gênero:* Interprete a semente de acordo com o tom (ex: 'Vila' no Sci-Fi pode ser uma colônia em asteroide).
     * **Regra de Diversidade:** Evite repetição. Se criar uma "Taverna", não crie um "Bar". Misture locais sociais, locais perigosos, locais de passagem e locais secretos.
     * **Contexto Geográfico:** Utilize a técnica de "Zoom Out". Se o `scope` for uma cidade, os locais são bairros ou prédios. Se for um reino, são cidades ou marcos geográficos.
     * **Descrição Sensorial:** No campo `descricao`, em um parágrafo diga o que é e local e como é estar lá. Use iluminação, cheiros, sons e texturas (ex: "O ar cheira a ozônio e o chão vibra com o maquinário subterrâneo").
   * **Regra de Coesão Geográfica (Campo `ancora_geografica`):**
Ao gerar o campo `ancora_geografica`, você deve tratar todos os locais como partes de um único ecossistema físico interconectado (um bairro, distrito ou complexo industrial). Não descreva o local isoladamente. Em vez disso:
  * 1. **Estabeleça a Posição Relativa:** Onde este local está em relação aos marcos principais (ex: 'nos esgotos abaixo do Mercado', 'no topo da colina com vista para o Porto')?
  * 2. **Defina a Transição Física:** Como o personagem entra ou sai daqui? Mencione a 'cola' física entre as zonas (pontes, túneis, elevadores de carga, becos estreitos).
  * 3. **Crie Sangramento Sensorial:** Elementos de um local vizinho devem ser percebidos aqui (o som da Forja é ouvido no Mercado; a fumaça do Porto cobre a Torre).
  **Objetivo:** O jogador deve sentir que pode desenhar um mapa mental de como ir do ponto A ao ponto B apenas lendo essa descrição.
   * Crie nomes específicos e evocativos para **8 locais**.
   * **Distribuição Obrigatória:**
     * 1 Local Inicial (Onde a aventura começa).
     * 4 Locais Intermediários (Investigação/Desenvolvimento).
     * 3 Locais de Clímax (Confronto Final/Desastre).

3. **Definição do Foco Narrativo:**
   * **Foco Narrativo:** Não escreva apenas um tema simples. Defina a "Lente Atmosférica" da aventura. Exemplo: Em vez de "Investigação", use "Investigação Noir sob chuva constante e corrupção moral".
```
**User Prompt:**
```text
### 1. Configuração da Aventura
* **Gênero:** Dieselpunk
* **Subgêneros:** Noir, Ação Frenética, Mistério
* **Escopo Geográfico:** Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.
* **Pool de Tipos de Locais (Inspiração):** Arena de Lutas, Ferro velho, Fila da ração, Armazém de comida, Mercado de pulgas, Bar movimentado, Mansão de um senhor de armas, Festival de Música, Torre de Vigia, Pista de Obstáculos, Escombros, Oficina de carros, Laboratório de química, Ferro Velho

### 2. A Alma da História
* **Argumento:** Na metrópole distópica de Aethelburg, uma carga de Orichalcum recém-extraído, vital para a sobrevivência do assentamento isolado de 'O Poço', foi roubada do depósito de segurança da gangue 'Os Engrenagens' na noite anterior. Os Engrenagens acreditam que a gangue rival, 'Os Soberanos', são osAuthors do roubo, o que desencadeará uma guerra aberta ao amanhecer se a carga não for recuperada. Na verdade, a carga foi interceptada pelo líder de Os Engrenagens (mestre Silas) e seu braço direito (Lia 'A Chave'), que planejam vender o Orichalcum para um mercado negro interestelar para fugir de suas dívidas com um sindicato criminoso maior. Eles incriminaram Os Soberanos para criar o caos que lhes permitiria desaparecer com a carga.
* **Premissa Evidente (Missão):** Uma carga de Orichalcum, essencial para O Poço, foi roubada *pelos Soberanos* e deve ser recuperada antes do amanhecer, sob pena de uma guerra sangrenta que destruirá o assentamento.
* **Premissa Oculta (Twist):** O líder de Os Engrenagens, o Mestre Silas, e sua tenente Lia roubaram a carga para vendê-la e quitar suas dívidas com um sindicato criminoso. Eles plantaram pistas falsas para incriminar Os Soberanos, usando a ameaça de guerra como cortina de fumaça para sua fuga.

### 3. Segredos da Campanha (Matriz)
Use estes segredos para garantir que os locais contenham pistas ou conexões temáticas com a verdade maior:
  - Titulo: A Origem do Roubo
  - A verdade: O Mestre Silas e Lia roubaram a carga para pagar dívidas.
  - A expectativa: Os Soberanos, gangue rival, roubaram a carga por causa da rivalidade usual.
  - A camuflagem: Pistas falsas deixadas deliberadamente (ex: uma jaqueta dos Soberanos perto do local do crime, testemunhas pagas para incriminá-los).
  - O gatilho: Investigar a cena do crime com detalhes, questionar testemunhas-chave sob pressão, encontrar equipamentos de 'Os Engrenagens' usados no roubo.
  - A revelacao: As pistas falsas são descobertas como armadilhas, e evidências concretas apontam para a participação de Os Engrenagens no roubo.
  - Id: 1

  - Titulo: O Destino da Carga
  - A verdade: A carga de Orichalcum está sendo preparada para ser vendida no mercado negro interestelar por Silas e Lia.
  - A expectativa: A carga ainda está escondida em algum local secreto de Os Soberanos, ou foi destruída.
  - A camuflagem: Comunicações interceptadas entre Silas e um contato misterioso (do sindicato), movimentação suspeita de veículos de carga 'piratas' nos arredores do Poço.
  - O gatilho: Rastrear a origem das comunicações encontradas, interceptar um dos veículos de carga suspeitos, interrogar um cúmplice menor de Silas.
  - A revelacao: Revela que a carga está sendo movida para fora do Poço por Os Engrenagens, não levada por Os Soberanos, e para um destino fora do planeta.
  - Id: 2

  - Titulo: A Verdadeira Motivação de Silas
  - A verdade: Silas está endividado com um sindicato criminoso perigoso e usa o roubo como plano de fuga.
  - A expectativa: Silas é apenas um líder de gangue ambicioso que quer mais poder ou quer provocar Os Soberanos.
  - A camuflagem: Registros financeiros incomuns de Silas, comportamento paranoico, segredos sujos que ele tenta esconder a todo custo, 'visitas' inesperadas de figuras sombrias ao seu território.
  - O gatilho: Obter acesso aos registros pessoais de Silas, capturar um dos cobradores de dívida do sindicato, encontrar evidências de comunicação anterior entre Silas e o sindicato.
  - A revelacao: Descobre que Silas não é um vilão independente, mas sim um peão encurralado, e que uma força externa maior está envolvida.
  - Id: 3

---

**Tarefa:** Defina a estrutura base (Enredo/Foco) e instancie a lista de **8 locais** detalhados onde essa trama irá desenrolar.
```
**Schema Enviado:**
```json
{
  "type": "object",
  "properties": {
    "cabecalho": {
      "type": "object",
      "properties": {
        "enredo_selecionado": {
          "type": "string",
          "description": "Nome do arquétipo de enredo escolhido."
        },
        "meta_estrutura_resumo": {
          "type": "string",
          "description": "Resumo dos 5 passos da meta-estrutura."
        },
        "foco_narrativo": {
          "type": "string",
          "description": "A atmosfera central da aventura."
        }
      },
      "required": [
        "enredo_selecionado",
        "meta_estrutura_resumo",
        "foco_narrativo"
      ]
    },
    "lista_locais": {
      "type": "array",
      "description": "Lista de 8 locais instanciados e conectados.",
      "items": {
        "type": "object",
        "properties": {
          "nome": {
            "type": "string"
          },
          "descricao": {
            "type": "string",
            "description": "Descrição sensorial completa (visual, som, cheiro)."
          },
          "tags": {
            "type": "string",
            "description": "Palavras-chave de atmosfera."
          },
          "funcao": {
            "type": "string",
            "enum": [
              "Inicial",
              "Intermediario",
              "Climax"
            ]
          },
          "ancora_geografica": {
            "type": "string",
            "description": "Conexão física e espacial com o restante do cenário (vias de acesso, posição relativa)."
          }
        },
        "required": [
          "nome",
          "descricao",
          "tags",
          "funcao",
          "ancora_geografica"
        ]
      },
      "minItems": 8,
      "maxItems": 8
    }
  },
  "required": [
    "cabecalho",
    "lista_locais"
  ]
}
```
</details>

### 🤖 Resposta do Modelo
```json
{
  "cabecalho": {
    "enredo_selecionado": "Tragédia",
    "meta_estrutura_resumo": "Os personagens são atraídos por uma oferta ou situação tentadora que revela ganhos fáceis, mas logo as consequências imprevistas do envolvimento escalam para um pesadelo, levando à destruição moral ou física.",
    "foco_narrativo": "Investigação Noir e Desespero em um assentamento dieselpunk à beira do colapso, onde a confiança é uma moeda rara e a sobrevivência depende de escolhas moralmente ambíguas sob constante pressão de tempo."
  },
  "lista_locais": [
    {
      "nome": "O Depósito das Engrenagens",
      "descricao": "Um armazém enferrujado e sinistro, com paredes de metal corroído que ressoam com o gotejar constante de umidade e o zumbido de geradores instáveis. O cheiro de óleo rançoso e metal frio impregna o ar, misturado a um leve odor de ozônio vindo de equipamentos improvisados. As sombras dançam nas pilhas de caixas e maquinário obsoleto, criando uma atmosfera de paranoia.",
      "tags": "Depósito, Roubo, Pistas Falsas, Engrenagens",
      "funcao": "Inicial",
      "ancora_geografica": "Localizado nos confins industriais do Poço, o Depósito das Engrenagens é uma estrutura maciça e isolada, acessível por um longo e esburacado caminho de terra que se afasta do centro do assentamento. Ele se aninha precariamente nas encostas de uma montanha de sucata, com o som distante de metal sendo triturado vindo da vizinhança do Ferro Velho."
    },
    {
      "nome": "O Mercado da Pulga Sussurrante",
      "descricao": "Um labirinto caótico de barracas improvisadas sob toldos esfarrapados onde o barulho de negociadores hostis, vendedores apregoando bugigangas e o chocalho de moedas ecoam. O ar é espesso com o aroma de comida de rua gordurosa, suor e produtos químicos baratos. Cada sombra parece esconder um espião.",
      "tags": "Mercado, Informação, Contato, Sussurros",
      "funcao": "Intermediario",
      "ancora_geografica": "No coração pulsante do Poço, o Mercado da Pulga Sussurrante é uma rede de becos estreitos e praças apertadas que se conectam como veias. Ele fica adjacente à Fila da Ração, onde o pânico latente pela escassez de suprimentos pode ser sentido, e a névoa de fumaça das oficinas de carros próximas sempre paira sobre as barracas."
    },
    {
      "nome": "A Taverna 'Fio do Motor'",
      "descricao": "Um bar escuro e fumegante, onde a música dissonante de um gramofone quebrado competes com o clamor de conversas. O cheiro de álcool barato, suor e graxa paira no ar. Luzes fracas e piscantes revelam rostos marcados pela fadiga e desesperança.",
      "tags": "Bar, Informante, Encontro, Contrabando",
      "funcao": "Intermediario",
      "ancora_geografica": "Aninhada em um nível inferior do Poço, perto das docas de carga abandonadas, a Taverna 'Fio do Motor' é um refúgio sombrio acessível por escadas de metal instáveis. O som de motores distantes de navios de carga raramente usados ocasionalmente penetra o barulho interno, assim como o cheiro marinho e de óleo industrial vindo da direção do Porto."
    },
    {
      "nome": "Oficina do Ferreiro 'Mão de Ferro'",
      "descricao": "Um espaço brutal de trabalho adornado com o brilho ameaçador de ferramentas quentes e o clangor incessante de martelos contra metal. O calor é opressivo, e o ar brilha com o cheiro pungente de metal em brasa e fumaça. Faíscas voam como insetos furiosos nas sombras.",
      "tags": "Oficina, Armas, Reparos, Engrenagens",
      "funcao": "Intermediario",
      "ancora_geografica": "Situada no distrito de manutenção do Poço, a Oficina do Ferreiro 'Mão de Ferro' está encravada entre torres de ventilação e tubulações de vapor, conectada por passarelas de metal rangentes. É uma área industrial ruidosa, onde o som contínuo da forja se mistura com o silvo de máquinas pneumáticas da vizinha Arena de Lutas."
    },
    {
      "nome": "O 'Ninho do Corvo' (Mansão de Silas)",
      "descricao": "Uma estrutura opulenta e decadente, contrastando com a sujeira geral do Poço. Lustres piscantes iluminam móveis caros e decrépitos, e o ar está impregnado com o aroma de charutos caros e um perfume forte e artificial. Um silêncio tenso, quebrado apenas pelo tic-tac de um relógio de pêndulo, paira sobre tudo.",
      "tags": "Mansão, Liderança, Segredos, Silas",
      "funcao": "Intermediario",
      "ancora_geografica": "Dominando uma colina elevada dentro do Poço, o 'Ninho do Corvo' oferece uma vista sombria do assentamento. A mansão é acessível por uma estrada de paralelepípedos mal conservada, que serpenteia para cima, passando por postos de guarda precários construídos com sucata. O som do vento uivando através das estruturas de metal e o cheiro de ozônio da estação de rádio próxima são constantes."
    },
    {
      "nome": "A Torre de Vigia Silenciosa",
      "descricao": "Uma torre alta e esquelética, feita de vigas de metal enferrujadas, dominando o horizonte do Poço. O vento assobia através de suas frestas, criando um som melancólico. A vista do topo é de um deserto de sucata e prédios em ruínas, pontuado pelas luzes fracas e distantes de outros postos de vigia.",
      "tags": "Vigia, Perigo, Emboscada, Confronto",
      "funcao": "Climax",
      "ancora_geografica": "Erguendo-se isolada em uma saliência rochosa nos arredores do Poço, a Torre de Vigia Silenciosa é uma estrutura solitária de observação. Ela está conectada ao assentamento por uma ponte de corda precária e desgastada, e abaixo dela se estendem os Escombros, onde o som de pedras caindo e ventos uivantes são os únicos sons."
    },
    {
      "nome": "O Ferro Velho de 'Os Soberanos'",
      "descricao": "Uma vasta extensão de sucata retorcida e máquinas despedaçadas, onde o fedor penetrante de metal enferrujado e óleo vazando é avassalador. O barulho de roedores correndo entre pilhas de sucata e o rangido cíclico de metal sob a carga do vento criam uma trilha sonora sinistra. As sombras são profundas e traiçoeiras.",
      "tags": "Ferro Velho, Rivalidade, Confronto, Soberanos",
      "funcao": "Climax",
      "ancora_geografica": "Situado em um desfiladeiro natural nos confins do Poço, o Ferro Velho de 'Os Soberanos' é uma paisagem de destruição acumulada. Ele se espalha por uma ravina, com o som de água suja correndo em canais improvisados vindo de áreas mais baixas, e o cheiro de combustíveis derramados de tanques quebrados pela proximidade com áreas de armazenamento."
    },
    {
      "nome": "O Pátio de Carga 'Porto Fantasma'",
      "descricao": "Um vasto pátio de concreto rachado, pontilhado por guindastes paralisados e contêineres enferrujados sob um céu perpetuamente cinzento. O ar é pesado com o cheiro de sal marinho, fuligem e produtos químicos evaporados. Ventos cortantes de onde antes era o oceano trazem um arrepio constante.",
      "tags": "Carga, Fuga, Contrabando, Clímax",
      "funcao": "Climax",
      "ancora_geografica": "A uma curta distância do assentamento principal do Poço, onde as ruínas de um antigo porto se encontram com a terra seca, o Pátio de Carga 'Porto Fantasma' é uma área desolada de desembarque. Ele é conectado ao resto do assentamento por uma ferrovia de carga abandonada e um túnel de serviço escuro, onde o som de eco e o cheiro de mofo e detritos orgânicos são predominantes."
    }
  ]
}
```

## 3. 3. Front World (Módulo: `step2_front_worldbuilder`)
<details>
<summary><strong>⚙️ Ver Prompts & Request</strong></summary>

**System Prompt:**
```text
Você é um Mestre de RPG especialista e Designer Narrativo.

# **Objetivo**

Sua tarefa é dar vida à "Frente de Aventura". Utilizando o Arquétipo e os Locais definidos na fase anterior, você deve criar o **Elenco**, os **Perigos** ativos e definir o **Desastre Iminente**.

# **Instruções de Processamento**

1. **Definição do Contexto (Descrição):**
   * Escreva um breve parágrafo de **Descrição** da Frente. Resuma o foco central do conflito, conectando o Arquétipo de Enredo à ameaça imediata.

2. Criação do Elenco e Perigos:
 O objetivo é criar ameaças vivas, dinâmicas e memoráveis, evitando o 'vilão passivo' que apenas espera pelos heróis. Siga estritamente os passos abaixo, aplicando os princípios de **Agência**, **Vínculo** e **Presença**:
### **Passo A: Elenco (The Cast)**
Aqui definimos a *identidade* e a *alma* dos personagens principais (Antagonistas e Aliados chave).
 * Liste os NPCs e Organizações cruciais citados no Argumento.
* Para cada NPC principal (especialmente o vilão), defina:
    1. **Nome e Papel/Função**.
    2. **Detalhe Marcante:** Algo visual ou de comportamento que denote competência ou perigo (ex: 'Fala sussurrando, mas todos se calam para ouvir').
    3. **A Convicção (O Herói da Própria História):** Qual é a motivação interna dele? Ele deve acreditar que está fazendo o necessário (ex: 'Salvar a cidade através do controle total'). Evite o 'mal pelo mal'.
    4. **O Contraste (Humanização):** Uma característica que quebre a expectativa de monstruosidade (ex: 'Um general impiedoso que cuida com carinho de orquídeas raras').

### **Passo B: Perigos (Dangers)**
Aqui definimos a *ação* e a *mecânica* da ameaça em **Dungeon World**. O Perigo é o motor da narrativa.
* Crie 2 ou 3 ameaças ativas.
* Para cada Perigo, siga a estrutura:
    1. **Nome do Perigo:** (Ex: 'A Cruzada de Ferro de Lorde Kael').
    2. **Tipo e Impulso:** Selecione **estritamente** da lista oficial de Dungeon World (ex: *Horda - Impulso: Crescer em força e destruir*; *Inimigo Arcano - Impulso: Conquistar o poder proibido*).
    3. **A Ameaça à Verdade:** Como este perigo ataca não só o HP, mas as **crenças** ou o **moral** dos heróis? (ex: 'Eles provam que a democracia falhou').
    4. **Vínculo com Local/Rastro:** Onde ele está operando e qual cicatriz ele já deixou no mundo? (Mostre o impacto antes de mostrar o vilão).
    5. **Ação Iminente:** O que o perigo fará **agora** se os jogadores não intervierem? (O vilão deve ser ativo, não reativo).

### Exemplo de Estrutura Esperada (Output):
**ELENCO**
* **Silas Vance (O Arquiteto):** Líder da Corporação. *Detalhe:* Possui um braço mecânico de ouro polido que nunca suja de óleo. *Convicção:* Acredita que o livre-arbítrio gerou o caos da guerra; a ordem perfeita exige submissão. *Contraste:* Financia anonimamente orfanatos para vítimas de guerra.
**PERIGOS**
* **Perigo 1:** A Mente Colmeia de Silas (Organização Ambiciosa)
    * **Impulso:** Controlar através da influência e pactos.
    * **Ameaça à Verdade:** Desafia a ideia de liberdade dos heróis, oferecendo segurança absoluta em troca de obediência.
    * **Vínculo com Local:** Domina o Distrito Industrial, onde os operários agora trabalham em silêncio absoluto e sincronizado (o Rastro).
    * **Ação Iminente:** Está prestes a ativar as torres de sinal que suprimirão as emoções no setor residencial.

**Lista de Referência (Tipo: Impulso):**

* **Organizações Ambiciosas:**
  * *Culto:* Infestar a partir de dentro.
  * *Governo Corrupto:* Manter o status quo.
  * *Cabala:* Absorver aqueles que estão no poder, crescer.
  * *Organização Religiosa:* Estabelecer e seguir doutrinas.
* **Hordas:**
  * *Criaturas Humanoides (ex: Orcs, Goblins):* Crescer, multiplicar e consumir.
  * *Habitantes do Submundo:* Defender seus complexos de forasteiros.
  * *Praga de Mortos-Vivos:* Espalhar.
* **Inimigos Arcanos:**
  * *Lorde Morto-Vivo:* Buscar a verdadeira imortalidade.
  * *Mago Louco por Poder:* Buscar poder mágico a qualquer custo.
  * *Dragão:* Reunir ouro e joias, proteger sua ninhada.
* **Lugares Amaldiçoados:**
  * *Portal das Trevas:* Expelir demônios/monstros.
  * *Lugar de Poder:* Ser controlado ou domado.
* **Forças Planares:**
  * *Deus:* Reunir seguidores.
  * *Força do Caos:* Destruir qualquer semblante de ordem.
3. **Definição do Desastre Iminente:**
   * Defina o "Game Over" narrativo. O que acontece se os jogadores falharem completamente?
   * Escolha um Tipo de Desastre: Tirania, Pestilência, Destruição, Usurpação, Empobrecimento, Caos.
```
**User Prompt:**
```text
### 1. Estrutura da Frente
* **Gênero:** Dieselpunk
* **Subgêneros:** Noir, Ação Frenética, Mistério
* **Escopo Geográfico:** Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.
* **Arquétipo:** Tragédia
* **Foco Narrativo:** Investigação Noir e Desespero em um assentamento dieselpunk à beira do colapso, onde a confiança é uma moeda rara e a sobrevivência depende de escolhas moralmente ambíguas sob constante pressão de tempo.

### 2. Dados dos Locais (Step 1)
>>> DADOS DOS LOCAIS:
> **O Depósito das Engrenagens**
  - Descricao: Um armazém enferrujado e sinistro, com paredes de metal corroído que ressoam com o gotejar constante de umidade e o zumbido de geradores instáveis. O cheiro de óleo rançoso e metal frio impregna o ar, misturado a um leve odor de ozônio vindo de equipamentos improvisados. As sombras dançam nas pilhas de caixas e maquinário obsoleto, criando uma atmosfera de paranoia.
  - Tags: Depósito, Roubo, Pistas Falsas, Engrenagens
  - Funcao: Inicial
  - Ancora geografica: Localizado nos confins industriais do Poço, o Depósito das Engrenagens é uma estrutura maciça e isolada, acessível por um longo e esburacado caminho de terra que se afasta do centro do assentamento. Ele se aninha precariamente nas encostas de uma montanha de sucata, com o som distante de metal sendo triturado vindo da vizinhança do Ferro Velho.

> **O Mercado da Pulga Sussurrante**
  - Descricao: Um labirinto caótico de barracas improvisadas sob toldos esfarrapados onde o barulho de negociadores hostis, vendedores apregoando bugigangas e o chocalho de moedas ecoam. O ar é espesso com o aroma de comida de rua gordurosa, suor e produtos químicos baratos. Cada sombra parece esconder um espião.
  - Tags: Mercado, Informação, Contato, Sussurros
  - Funcao: Intermediario
  - Ancora geografica: No coração pulsante do Poço, o Mercado da Pulga Sussurrante é uma rede de becos estreitos e praças apertadas que se conectam como veias. Ele fica adjacente à Fila da Ração, onde o pânico latente pela escassez de suprimentos pode ser sentido, e a névoa de fumaça das oficinas de carros próximas sempre paira sobre as barracas.

> **A Taverna 'Fio do Motor'**
  - Descricao: Um bar escuro e fumegante, onde a música dissonante de um gramofone quebrado competes com o clamor de conversas. O cheiro de álcool barato, suor e graxa paira no ar. Luzes fracas e piscantes revelam rostos marcados pela fadiga e desesperança.
  - Tags: Bar, Informante, Encontro, Contrabando
  - Funcao: Intermediario
  - Ancora geografica: Aninhada em um nível inferior do Poço, perto das docas de carga abandonadas, a Taverna 'Fio do Motor' é um refúgio sombrio acessível por escadas de metal instáveis. O som de motores distantes de navios de carga raramente usados ocasionalmente penetra o barulho interno, assim como o cheiro marinho e de óleo industrial vindo da direção do Porto.

> **Oficina do Ferreiro 'Mão de Ferro'**
  - Descricao: Um espaço brutal de trabalho adornado com o brilho ameaçador de ferramentas quentes e o clangor incessante de martelos contra metal. O calor é opressivo, e o ar brilha com o cheiro pungente de metal em brasa e fumaça. Faíscas voam como insetos furiosos nas sombras.
  - Tags: Oficina, Armas, Reparos, Engrenagens
  - Funcao: Intermediario
  - Ancora geografica: Situada no distrito de manutenção do Poço, a Oficina do Ferreiro 'Mão de Ferro' está encravada entre torres de ventilação e tubulações de vapor, conectada por passarelas de metal rangentes. É uma área industrial ruidosa, onde o som contínuo da forja se mistura com o silvo de máquinas pneumáticas da vizinha Arena de Lutas.

> **O 'Ninho do Corvo' (Mansão de Silas)**
  - Descricao: Uma estrutura opulenta e decadente, contrastando com a sujeira geral do Poço. Lustres piscantes iluminam móveis caros e decrépitos, e o ar está impregnado com o aroma de charutos caros e um perfume forte e artificial. Um silêncio tenso, quebrado apenas pelo tic-tac de um relógio de pêndulo, paira sobre tudo.
  - Tags: Mansão, Liderança, Segredos, Silas
  - Funcao: Intermediario
  - Ancora geografica: Dominando uma colina elevada dentro do Poço, o 'Ninho do Corvo' oferece uma vista sombria do assentamento. A mansão é acessível por uma estrada de paralelepípedos mal conservada, que serpenteia para cima, passando por postos de guarda precários construídos com sucata. O som do vento uivando através das estruturas de metal e o cheiro de ozônio da estação de rádio próxima são constantes.

> **A Torre de Vigia Silenciosa**
  - Descricao: Uma torre alta e esquelética, feita de vigas de metal enferrujadas, dominando o horizonte do Poço. O vento assobia através de suas frestas, criando um som melancólico. A vista do topo é de um deserto de sucata e prédios em ruínas, pontuado pelas luzes fracas e distantes de outros postos de vigia.
  - Tags: Vigia, Perigo, Emboscada, Confronto
  - Funcao: Climax
  - Ancora geografica: Erguendo-se isolada em uma saliência rochosa nos arredores do Poço, a Torre de Vigia Silenciosa é uma estrutura solitária de observação. Ela está conectada ao assentamento por uma ponte de corda precária e desgastada, e abaixo dela se estendem os Escombros, onde o som de pedras caindo e ventos uivantes são os únicos sons.

> **O Ferro Velho de 'Os Soberanos'**
  - Descricao: Uma vasta extensão de sucata retorcida e máquinas despedaçadas, onde o fedor penetrante de metal enferrujado e óleo vazando é avassalador. O barulho de roedores correndo entre pilhas de sucata e o rangido cíclico de metal sob a carga do vento criam uma trilha sonora sinistra. As sombras são profundas e traiçoeiras.
  - Tags: Ferro Velho, Rivalidade, Confronto, Soberanos
  - Funcao: Climax
  - Ancora geografica: Situado em um desfiladeiro natural nos confins do Poço, o Ferro Velho de 'Os Soberanos' é uma paisagem de destruição acumulada. Ele se espalha por uma ravina, com o som de água suja correndo em canais improvisados vindo de áreas mais baixas, e o cheiro de combustíveis derramados de tanques quebrados pela proximidade com áreas de armazenamento.

> **O Pátio de Carga 'Porto Fantasma'**
  - Descricao: Um vasto pátio de concreto rachado, pontilhado por guindastes paralisados e contêineres enferrujados sob um céu perpetuamente cinzento. O ar é pesado com o cheiro de sal marinho, fuligem e produtos químicos evaporados. Ventos cortantes de onde antes era o oceano trazem um arrepio constante.
  - Tags: Carga, Fuga, Contrabando, Clímax
  - Funcao: Climax
  - Ancora geografica: A uma curta distância do assentamento principal do Poço, onde as ruínas de um antigo porto se encontram com a terra seca, o Pátio de Carga 'Porto Fantasma' é uma área desolada de desembarque. Ele é conectado ao resto do assentamento por uma ferrovia de carga abandonada e um túnel de serviço escuro, onde o som de eco e o cheiro de mofo e detritos orgânicos são predominantes.

### 3. Contexto da Trama
* **Argumento:** Na metrópole distópica de Aethelburg, uma carga de Orichalcum recém-extraído, vital para a sobrevivência do assentamento isolado de 'O Poço', foi roubada do depósito de segurança da gangue 'Os Engrenagens' na noite anterior. Os Engrenagens acreditam que a gangue rival, 'Os Soberanos', são osAuthors do roubo, o que desencadeará uma guerra aberta ao amanhecer se a carga não for recuperada. Na verdade, a carga foi interceptada pelo líder de Os Engrenagens (mestre Silas) e seu braço direito (Lia 'A Chave'), que planejam vender o Orichalcum para um mercado negro interestelar para fugir de suas dívidas com um sindicato criminoso maior. Eles incriminaram Os Soberanos para criar o caos que lhes permitiria desaparecer com a carga.
* **Premissa Evidente:** Uma carga de Orichalcum, essencial para O Poço, foi roubada *pelos Soberanos* e deve ser recuperada antes do amanhecer, sob pena de uma guerra sangrenta que destruirá o assentamento.
* **Premissa Oculta:** O líder de Os Engrenagens, o Mestre Silas, e sua tenente Lia roubaram a carga para vendê-la e quitar suas dívidas com um sindicato criminoso. Eles plantaram pistas falsas para incriminar Os Soberanos, usando a ameaça de guerra como cortina de fumaça para sua fuga.

### 4. Opções de Criação
* **Arquétipos Permitidos:** Músculo: Você é grande, pesado. Machucar e fazer façanhas físicas é com você., Cabeça: Pensamento ágil, consegue operar sistemas e máquinas antigas., Volante: Atrás de um volante, não há igual. Você é uma fera das estradas., Vigia: Olhos atentos e sempre no horizonte. Consegue atirar muito bem., Boca: Sempre sabe o que dizer. Carisma em pessoa. Mesmo que isso traga problemas., Novato: Nunca conheceu um mundo que não esse. Quer provar seu valor para os seus.

Agora, povoe este mundo.
```
**Schema Enviado:**
```json
{
  "type": "object",
  "properties": {
    "descricao_frente": {
      "type": "string",
      "description": "Resumo do conflito central e atmosfera."
    },
    "elenco": {
      "type": "array",
      "description": "Lista de NPCs e Facções, focando em suas motivações e contradições.",
      "items": {
        "type": "object",
        "properties": {
          "nome": {
            "type": "string"
          },
          "papel_funcao": {
            "type": "string"
          },
          "detalhe_marcante": {
            "type": "string",
            "description": "Algo visual ou de comportamento (competência/perigo)."
          },
          "conviccao": {
            "type": "string",
            "description": "A motivação interna ('O Herói da Própria História')."
          },
          "contraste": {
            "type": "string",
            "description": "Fator de humanização que quebra expectativas."
          }
        },
        "required": [
          "nome",
          "papel_funcao",
          "detalhe_marcante",
          "conviccao",
          "contraste"
        ]
      }
    },
    "perigos": {
      "type": "array",
      "description": "Ameaças ativas (2 ou 3) com mecânicas de Dungeon World.",
      "items": {
        "type": "object",
        "properties": {
          "nome": {
            "type": "string"
          },
          "tipo": {
            "type": "string",
            "description": "Ex: Horda, Inimigo Arcano, etc."
          },
          "impulso": {
            "type": "string",
            "description": "O impulso oficial correspondente."
          },
          "ameaca_verdade": {
            "type": "string",
            "description": "Como o perigo ataca as crenças ou moral dos heróis."
          },
          "local_vinculado": {
            "type": "string",
            "description": "Nome do local onde o perigo opera."
          },
          "rastro_destruicao": {
            "type": "string",
            "description": "A cicatriz ou impacto visível deixado no local."
          },
          "acao_iminente": {
            "type": "string",
            "description": "O que o perigo fará AGORA se não for impedido."
          }
        },
        "required": [
          "nome",
          "tipo",
          "impulso",
          "ameaca_verdade",
          "local_vinculado",
          "rastro_destruicao",
          "acao_iminente"
        ]
      }
    },
    "desastre_iminente": {
      "type": "object",
      "description": "O Game Over narrativo.",
      "properties": {
        "tipo_desastre": {
          "type": "string",
          "enum": [
            "Tirania",
            "Pestilência",
            "Destruição",
            "Usurpação",
            "Empobrecimento",
            "Caos"
          ]
        },
        "descricao": {
          "type": "string",
          "description": "O que acontece se nada for feito."
        }
      },
      "required": [
        "tipo_desastre",
        "descricao"
      ]
    }
  },
  "required": [
    "descricao_frente",
    "elenco",
    "perigos",
    "desastre_iminente"
  ]
}
```
</details>

### 🤖 Resposta do Modelo
```json
{
  "descricao_frente": "Em 'O Poço', um assentamento dieselpunk à beira do colapso, a confiança é um artigo de luxo. Com a vital carga de Orichalcum roubada e a ameaça de uma guerra fratricida com 'Os Soberanos' iminente, os heróis precisam navegar por uma teia de mentiras sussurradas em mercados sombrios e becos sujos. O tempo urge, e cada escolha moralmente ambígua pode acelerar a queda do Poço ou expor a verdade por trás da tragédia orquestrada.",
  "elenco": [
    {
      "nome": "Silas 'O Mestre' (Líder dos Engrenagens)",
      "papel_funcao": "Líder da gangue Os Engrenagens",
      "detalhe_marcante": "Tem um olhar penetrante e uma cicatriz em forma de engrenagem em sua têmpora, que ele adora acariciar quando pensa.",
      "conviccao": "A ordem, mesmo que imposta pela força e pela traição, é a única salvação para este Poço decadente. Ele precisa de um novo começo, longe das dívidas e do caos.",
      "contraste": "Coleciona engrenagens de relógios antigos, emoldurando-as como obras de arte em seu escritório."
    },
    {
      "nome": "Lia 'A Chave' (Braço Direito)",
      "papel_funcao": "Tenente de Silas e especialista em logística",
      "detalhe_marcante": "Sempre carrega um conjunto de gazuas e ferramentas multifuncionais em seu cinto, que ela usa com precisão quase cirúrgica.",
      "conviccao": "A sobrevivência em 'O Poço' exige pragmatismo e, por vezes, crueldade. Ela acredita que Silas está fazendo o que é necessário para garantir um futuro para ambos, longe das garras de sindicatos maiores.",
      "contraste": "Tem um carinho peculiar por pássaros mecânicos que ela constrói e solta nas áreas mais altas do Poço."
    },
    {
      "nome": "Roric 'O Martelo' (Líder dos Soberanos)",
      "papel_funcao": "Líder da gangue rival Os Soberanos",
      "detalhe_marcante": "Um homem robusto com braços musculosos manchados de graxa, cujas falas são curtas e diretas, raramente expressando emoção além da raiva ou desprezo.",
      "conviccao": "O Poço pertence aos fortes e aos trabalhadores, não aos parasitas e traidores que se escondem nas sombras. Ele quer justiça e recompensa pelo trabalho árduo de seu povo.",
      "contraste": "É absurdamente leal à sua tripulação e insiste que não roubariam suprimentos vitais para o bem-estar de todos, especialmente Orichalcum."
    }
  ],
  "perigos": [
    {
      "nome": "A Rede de Dívidas do Sindicato",
      "tipo": "Organização",
      "impulso": "Escravizar e extorquir.",
      "ameaca_verdade": "Sua influência corruptora prova que não importa o quão bem-sucedidos ou bem-intencionados sejam os heróis, sempre haverá uma força maior espreitando nas sombras, pronta para cobrá-los.",
      "local_vinculado": "O Mercado da Pulga Sussurrante / A Taverna 'Fio do Motor'",
      "rastro_destruicao": "Mercadores e pequenos criminosos com dívidas crescentes, forçados a entregar seus bens ou serviços para Agentes do Sindicato que operam discretamente.",
      "acao_iminente": "Enviar cobradores para 'renegociar' as dívidas de Silas e Lia, usando informações roubadas para pressioná-los a acelerar a venda do Orichalcum e ameaçando expor o plano dos Engrenagens se o pagamento não for rápido."
    },
    {
      "nome": "A Guerra Civil Iminente",
      "tipo": "Horda",
      "impulso": "Multiplicar e consumir.",
      "ameaca_verdade": "A violência e o caos são as respostas naturais para qualquer problema, minando a esperança de que a comunicação e a diplomacia possam prevalecer em 'O Poço'.",
      "local_vinculado": "O Ferro Velho de 'Os Soberanos' / O Pátio de Carga 'Porto Fantasma'",
      "rastro_destruicao": "Patrulhas de ambas as gangues ('Os Engrenagens' e 'Os Soberanos') em choque constante nas fronteiras de seus territórios, deixando corpos e sucata destruída para trás.",
      "acao_iminente": "Silas, para desesperar os heróis e criar uma distração, orquestrará um 'ataque' dos Soberanos contra o Depósito das Engrenagens, usando pistas plantadas para incriminar Roric e garantir que os combatentes de ambos os lados se enfrentem abertamente ao amanhecer."
    }
  ],
  "desastre_iminente": {
    "tipo_desastre": "Destruição",
    "descricao": "Se o Orichalcum não for recuperado e a verdade não for revelada, a guerra aberta entre Os Engrenagens e Os Soberanos irromperá. Ambos os lados, enfurecidos e desconfiados, se aniquilarão em combates brutais dentro e fora do Poço. O Sindicato, aproveitando o caos, acabará subjugando os sobreviventes e tomando o controle, transformando 'O Poço' em um deserto de sucata sem alma. Os heróis podem até escapar com Silas e Lia, mas o assentamento que juraram proteger estará perdido para sempre."
  }
}
```

## 4. 4. Front Story (Módulo: `step3_front_storyteller`)
<details>
<summary><strong>⚙️ Ver Prompts & Request</strong></summary>

**System Prompt:**
```text
Você é um **Mestre de RPG Especialista e Arquiteto de Narrativas**.

# **Objetivo**

Esta é a etapa de síntese. Você deve fundir a Estrutura (Fase 1) e as Ameaças (Fase 2) para criar a **Progressão Dramática** da aventura. Sua missão é gerar os **Presságios Terríveis** e as **Perguntas Dramáticas**.

# **Conceito Fundamental: O Presságio como Mini-Arco**

**IMPORTANTE:** Não trate o Presságio Terrível apenas como um evento passivo ou uma cena única. Cada Presságio deve ser estruturado como um **Mini-Arco de História** jogável. Ele representa um degrau na escalada do vilão que os jogadores podem investigar, combater ou interagir. Ele deve ter complexidade suficiente para sustentar uma parte da sessão de jogo.

# **Guia de Referência dos Enredos**

Você deve consultar esta lista para definir o tom de cada presságio com base no Enredo selecionado para a aventura.

* **Superar o Monstro (Foco: Terror e Heroísmo)**
1. **Antecipação:** O perigo é distante ou um rumor. O Presságio deve ser um aviso, um rastro de destruição ou um lacaio menor.
2. **Fase do Sonho:** Os heróis parecem estar ganhando ou avançando facilmente. O Presságio deve ser uma "vitória falsa" ou uma preparação do vilão que passa despercebida.
3. **A Frustração:** O inimigo revela seu verdadeiro poder. O Presságio deve ser um revés significativo, uma armadilha ou a perda de um refúgio.
4. **O Pesadelo:** A situação parece impossível. O Presságio deve ser um evento de grande escala, devastação ou isolamento total dos heróis.
5. **Fuga da Morte/Vitória:** O confronto final é iminente. O Presságio é o gatilho final do Desastre (o ritual começa, o portão se abre).

* **Da Miséria à Riqueza (Foco: Evolução e Teste de Caráter)**
1. **Miséria Inicial:** O cenário está oprimido ou pobre. O Presságio mostra a tirania do status quo ou a falta de recursos.
2. **Sucesso Inicial:** Uma oportunidade surge. O Presságio é um evento que oferece poder rápido, mas com riscos ocultos.
3. **A Crise Central:** Algo dá errado com o "novo poder". O Presságio mostra a perda de aliados, traição ou um erro de cálculo grave.
4. **Independência:** Os heróis são despidos de ajudas externas. O Presságio deve forçá-los a enfrentar o perigo sozinhos, sem mentores ou itens mágicos.
5. **Completude:** A prova final de valor. O Presságio é o desafio que define se eles merecem o status de heróis.

* **A Busca (Foco: Viagem e Objetivos)**
1. **O Chamado:** A necessidade da jornada. O Presságio é o evento que torna ficar em casa impossível (uma praga, um roubo, um ultimato).
2. **A Jornada:** O mundo se expande. O Presságio introduz perigos ambientais ou monstros estranhos no caminho.
3. **Frustração (Barreira):** O caminho é bloqueado. O Presságio é um guardião poderoso, uma prisão ou um desvio forçado para um local hostil.
4. **Provações Finais:** O destino está à vista, mas é mortal. O Presságio é a defesa de elite do vilão ou uma zona de morte.
5. **O Objetivo:** O prêmio está ao alcance. O Presságio é a última salvaguarda ou o despertar do guardião final.

* **Viagem e Retorno (Foco: Estranhamento e Adaptação)**
1. **Queda:** A entrada no "Outro Mundo". O Presságio é a transição (portal, naufrágio) ou o primeiro contato com leis físicas/sociais bizarras.
2. **Fascínio:** A beleza do perigo. O Presságio é sedutor, onírico ou enganosamente pacífico.
3. **A Frustração:** O sonho vira pesadelo. O Presságio revela que o mundo estranho é hostil e aprisionador.
4. **O Pesadelo:** A ameaça de nunca mais voltar. O Presságio é a caçada total aos "estrangeiros" (os heróis).
5. **Retorno:** A corrida para a saída. O Presságio é o fechamento da rota de fuga ou a perseguição final.

* **Renascimento (Foco: Corrupção e Redenção)**
1. **A Sombra:** O mal já está no controle. O Presságio mostra a aceitação passiva da população ou a "normalidade" do mal.
2. **O Poder da Sombra:** A ameaça se fortalece. O Presságio mostra o vilão convertendo aliados ou corrompendo locais sagrados.
3. **A Frustração (Prisão):** A esperança diminui. O Presságio é o encarceramento (físico ou mental) de figuras importantes ou dos heróis.
4. **O Pesadelo (Fundo do Poço):** O triunfo aparente do mal. O Presságio é a execução de inocentes ou a perda total de fé.
5. **Renascimento:** A luz na escuridão. O Presságio é o momento de virada onde o sacrifício ou a verdade quebra o poder do vilão.

* **Tragédia (Foco: Tentação e Consequência)**
1. **Tentação:** O fruto proibido. O Presságio oferece algo que os heróis ou NPCs querem, mas o custo é moralmente duvidoso.
2. **O Crime Compensa:** O ganho fácil. O Presságio mostra os antagonistas (ou heróis) ganhando poder através de meios ilícitos sem punição imediata.
3. **A Frustração (Consequências):** As rachaduras aparecem. O Presságio mostra os efeitos colaterais, paranoia ou vingança das vítimas.
4. **O Pesadelo (Perda de Controle):** A espiral descendente. O Presságio é o caos gerado pelas ações anteriores; o vilão perde o controle de sua própria trama.
5. **Destruição:** O colapso inevitável. O Presságio é a aniquilação mútua ou a destruição do cenário.

* **Comédia (Foco: Confusão e Verdade)**
1. **Confusão:** A realidade é distorcida. O Presságio é baseado em mentiras, disfarces ou informações erradas circulando.
2. **O Nó se Aperta:** As tentativas de conserto pioram tudo. O Presságio complica a situação (falsos culpados são presos, aliados brigam).
3. **Caos Total:** Ninguém se entende. O Presságio é um evento de anarquia social, motim ou absurdo lógico.
4. **A Revelação:** A verdade emerge dolorosamente. O Presságio é a exposição dos segredos (o vilão é desmascarado, mas ainda perigoso).
5. **Resolução:** A ordem restaurada. O Presságio é a união dos personagens contra a ameaça final agora clara.

# **Instruções de Processamento**

### **1. Construção dos Presságios Terríveis**
Crie uma cadeia cronológica de **5 Presságios** que indicam o avanço do Desastre.

**PROCESSO DE SELEÇÃO DO ENREDO:**
1. Verifique qual é o `Enredo Selecionado` nos dados de entrada.
2. Consulte o **Guia de Referência dos Enredos** acima.
3. Aplique a lógica dos passos 1 a 5 daquele enredo específico para ditar o **Tom** e a **Atmosfera** de cada presságio.

Para **CADA** Presságio, siga rigorosamente a estrutura abaixo:

#### **A. Configuração Técnica**
* **Meta-Estrutura:** Cite o nome do estágio (ex: "A Frustração") conforme o Guia de Referência e explique brevemente como o evento se encaixa nele.
* **Local:** Escolha obrigatoriamente um local da `lista_locais` onde este mini-arco ocorre.
* **Conexão com a Matriz (CRÍTICO):** Conecte este arco a um item específico da `matriz_controle_informacao`. Que pista sobre a "Verdade Maior" os jogadores podem encontrar aqui se tiverem sucesso (ou falharem)?

#### **B. O Tríptico Narrativo (Argumento, Evidente, Oculto)**
Para cada presságio, você deve desenvolver três blocos de texto distintos. Cada bloco deve ter **pelo menos 1 parágrafo robusto**.

1. **O Argumento da Cena (A Lógica do Mestre)**
* *Definição:* É a realidade factual e logística do mini-arco. É o resumo do que vai acontecer "atrás das cortinas".
* *O que deve conter:* Responda objetivamente: **Quem** está agindo (o vilão/monstro)? **Onde** exatamente no local? **Quando** isso ocorre (dia, noite, durante um festival)? **Por que** isso avança o plano do vilão? **Como** o conflito se estabelece? Este é o roteiro "duro" para o Mestre.

2. **A Premissa Evidente (A Camada Sensorial)**
* *Definição:* É a "isca". É como o problema se apresenta inicialmente aos jogadores. É a primeira impressão, aquilo que seus sentidos captam e o que os NPCs acreditam que está acontecendo.
* *O que deve conter:* Descreva a atmosfera, o problema superficial e a missão aparente. O que parece ser o perigo? (Ex: "Parece um simples ataque de bandidos à caravana"). Venda a "mentira" ou a "meia-verdade" inicial.

3. **A Premissa Oculta (A Virada/Twist Local)**
* *Definição:* É o "anzol". É a revelação que subverte a expectativa criada na Premissa Evidente. **Não confunda com a Conexão com a Matriz.** A Premissa Oculta é o *twist imediato* desta cena.
* *O que deve conter:* O que está escondido sob a superfície? Como a situação muda drasticamente quando os jogadores investigam a fundo? (Ex: "Os bandidos não querem ouro, estão sequestrando pessoas específicas para um ritual e são, na verdade, cultistas disfarçados").

### **2. Perguntas Dramáticas**

Formule **3 Perguntas Dramáticas** (abertas).

* *Definição:* Não são perguntas sobre regras ou fatos ("Onde está a chave?"), mas sim sobre **temas e consequências**. Elas surgem da incerteza do choque entre os Heróis e os Presságios.
* *Critério:* A resposta para essas perguntas não existe ainda; ela só surgirá durante o jogo ("play to find out").
* *Exemplo:* "Será que o Paladino conseguirá manter seu juramento de pureza quando descobrir que a corrupção vem de sua própria Igreja?"
```
**User Prompt:**
```text
### 1. Configuração da Aventura
* **Gênero:** Dieselpunk
* **Subgêneros:** Noir, Ação Frenética, Mistério
* **Escopo Geográfico:** Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.

### 2. Contexto da Trama
* **Argumento:** Na metrópole distópica de Aethelburg, uma carga de Orichalcum recém-extraído, vital para a sobrevivência do assentamento isolado de 'O Poço', foi roubada do depósito de segurança da gangue 'Os Engrenagens' na noite anterior. Os Engrenagens acreditam que a gangue rival, 'Os Soberanos', são osAuthors do roubo, o que desencadeará uma guerra aberta ao amanhecer se a carga não for recuperada. Na verdade, a carga foi interceptada pelo líder de Os Engrenagens (mestre Silas) e seu braço direito (Lia 'A Chave'), que planejam vender o Orichalcum para um mercado negro interestelar para fugir de suas dívidas com um sindicato criminoso maior. Eles incriminaram Os Soberanos para criar o caos que lhes permitiria desaparecer com a carga.
* **Premissa Evidente:** Uma carga de Orichalcum, essencial para O Poço, foi roubada *pelos Soberanos* e deve ser recuperada antes do amanhecer, sob pena de uma guerra sangrenta que destruirá o assentamento.
* **Premissa Oculta:** O líder de Os Engrenagens, o Mestre Silas, e sua tenente Lia roubaram a carga para vendê-la e quitar suas dívidas com um sindicato criminoso. Eles plantaram pistas falsas para incriminar Os Soberanos, usando a ameaça de guerra como cortina de fumaça para sua fuga.
* **Arquétipos Permitidos:** Músculo: Você é grande, pesado. Machucar e fazer façanhas físicas é com você., Cabeça: Pensamento ágil, consegue operar sistemas e máquinas antigas., Volante: Atrás de um volante, não há igual. Você é uma fera das estradas., Vigia: Olhos atentos e sempre no horizonte. Consegue atirar muito bem., Boca: Sempre sabe o que dizer. Carisma em pessoa. Mesmo que isso traga problemas., Novato: Nunca conheceu um mundo que não esse. Quer provar seu valor para os seus.

### 3. Dados da Fase 1 (Estrutura)
* **Arquétipo Selecionado:** Tragédia
* **Foco Narrativo:** Investigação Noir e Desespero em um assentamento dieselpunk à beira do colapso, onde a confiança é uma moeda rara e a sobrevivência depende de escolhas moralmente ambíguas sob constante pressão de tempo.

>>> LISTA DE LOCAIS (Referência para Localização dos Presságios):
> **O Depósito das Engrenagens**
  - Descricao: Um armazém enferrujado e sinistro, com paredes de metal corroído que ressoam com o gotejar constante de umidade e o zumbido de geradores instáveis. O cheiro de óleo rançoso e metal frio impregna o ar, misturado a um leve odor de ozônio vindo de equipamentos improvisados. As sombras dançam nas pilhas de caixas e maquinário obsoleto, criando uma atmosfera de paranoia.
  - Tags: Depósito, Roubo, Pistas Falsas, Engrenagens
  - Funcao: Inicial
  - Ancora geografica: Localizado nos confins industriais do Poço, o Depósito das Engrenagens é uma estrutura maciça e isolada, acessível por um longo e esburacado caminho de terra que se afasta do centro do assentamento. Ele se aninha precariamente nas encostas de uma montanha de sucata, com o som distante de metal sendo triturado vindo da vizinhança do Ferro Velho.

> **O Mercado da Pulga Sussurrante**
  - Descricao: Um labirinto caótico de barracas improvisadas sob toldos esfarrapados onde o barulho de negociadores hostis, vendedores apregoando bugigangas e o chocalho de moedas ecoam. O ar é espesso com o aroma de comida de rua gordurosa, suor e produtos químicos baratos. Cada sombra parece esconder um espião.
  - Tags: Mercado, Informação, Contato, Sussurros
  - Funcao: Intermediario
  - Ancora geografica: No coração pulsante do Poço, o Mercado da Pulga Sussurrante é uma rede de becos estreitos e praças apertadas que se conectam como veias. Ele fica adjacente à Fila da Ração, onde o pânico latente pela escassez de suprimentos pode ser sentido, e a névoa de fumaça das oficinas de carros próximas sempre paira sobre as barracas.

> **A Taverna 'Fio do Motor'**
  - Descricao: Um bar escuro e fumegante, onde a música dissonante de um gramofone quebrado competes com o clamor de conversas. O cheiro de álcool barato, suor e graxa paira no ar. Luzes fracas e piscantes revelam rostos marcados pela fadiga e desesperança.
  - Tags: Bar, Informante, Encontro, Contrabando
  - Funcao: Intermediario
  - Ancora geografica: Aninhada em um nível inferior do Poço, perto das docas de carga abandonadas, a Taverna 'Fio do Motor' é um refúgio sombrio acessível por escadas de metal instáveis. O som de motores distantes de navios de carga raramente usados ocasionalmente penetra o barulho interno, assim como o cheiro marinho e de óleo industrial vindo da direção do Porto.

> **Oficina do Ferreiro 'Mão de Ferro'**
  - Descricao: Um espaço brutal de trabalho adornado com o brilho ameaçador de ferramentas quentes e o clangor incessante de martelos contra metal. O calor é opressivo, e o ar brilha com o cheiro pungente de metal em brasa e fumaça. Faíscas voam como insetos furiosos nas sombras.
  - Tags: Oficina, Armas, Reparos, Engrenagens
  - Funcao: Intermediario
  - Ancora geografica: Situada no distrito de manutenção do Poço, a Oficina do Ferreiro 'Mão de Ferro' está encravada entre torres de ventilação e tubulações de vapor, conectada por passarelas de metal rangentes. É uma área industrial ruidosa, onde o som contínuo da forja se mistura com o silvo de máquinas pneumáticas da vizinha Arena de Lutas.

> **O 'Ninho do Corvo' (Mansão de Silas)**
  - Descricao: Uma estrutura opulenta e decadente, contrastando com a sujeira geral do Poço. Lustres piscantes iluminam móveis caros e decrépitos, e o ar está impregnado com o aroma de charutos caros e um perfume forte e artificial. Um silêncio tenso, quebrado apenas pelo tic-tac de um relógio de pêndulo, paira sobre tudo.
  - Tags: Mansão, Liderança, Segredos, Silas
  - Funcao: Intermediario
  - Ancora geografica: Dominando uma colina elevada dentro do Poço, o 'Ninho do Corvo' oferece uma vista sombria do assentamento. A mansão é acessível por uma estrada de paralelepípedos mal conservada, que serpenteia para cima, passando por postos de guarda precários construídos com sucata. O som do vento uivando através das estruturas de metal e o cheiro de ozônio da estação de rádio próxima são constantes.

> **A Torre de Vigia Silenciosa**
  - Descricao: Uma torre alta e esquelética, feita de vigas de metal enferrujadas, dominando o horizonte do Poço. O vento assobia através de suas frestas, criando um som melancólico. A vista do topo é de um deserto de sucata e prédios em ruínas, pontuado pelas luzes fracas e distantes de outros postos de vigia.
  - Tags: Vigia, Perigo, Emboscada, Confronto
  - Funcao: Climax
  - Ancora geografica: Erguendo-se isolada em uma saliência rochosa nos arredores do Poço, a Torre de Vigia Silenciosa é uma estrutura solitária de observação. Ela está conectada ao assentamento por uma ponte de corda precária e desgastada, e abaixo dela se estendem os Escombros, onde o som de pedras caindo e ventos uivantes são os únicos sons.

> **O Ferro Velho de 'Os Soberanos'**
  - Descricao: Uma vasta extensão de sucata retorcida e máquinas despedaçadas, onde o fedor penetrante de metal enferrujado e óleo vazando é avassalador. O barulho de roedores correndo entre pilhas de sucata e o rangido cíclico de metal sob a carga do vento criam uma trilha sonora sinistra. As sombras são profundas e traiçoeiras.
  - Tags: Ferro Velho, Rivalidade, Confronto, Soberanos
  - Funcao: Climax
  - Ancora geografica: Situado em um desfiladeiro natural nos confins do Poço, o Ferro Velho de 'Os Soberanos' é uma paisagem de destruição acumulada. Ele se espalha por uma ravina, com o som de água suja correndo em canais improvisados vindo de áreas mais baixas, e o cheiro de combustíveis derramados de tanques quebrados pela proximidade com áreas de armazenamento.

> **O Pátio de Carga 'Porto Fantasma'**
  - Descricao: Um vasto pátio de concreto rachado, pontilhado por guindastes paralisados e contêineres enferrujados sob um céu perpetuamente cinzento. O ar é pesado com o cheiro de sal marinho, fuligem e produtos químicos evaporados. Ventos cortantes de onde antes era o oceano trazem um arrepio constante.
  - Tags: Carga, Fuga, Contrabando, Clímax
  - Funcao: Climax
  - Ancora geografica: A uma curta distância do assentamento principal do Poço, onde as ruínas de um antigo porto se encontram com a terra seca, o Pátio de Carga 'Porto Fantasma' é uma área desolada de desembarque. Ele é conectado ao resto do assentamento por uma ferrovia de carga abandonada e um túnel de serviço escuro, onde o som de eco e o cheiro de mofo e detritos orgânicos são predominantes.

### 4. Dados da Fase 2 (Ameaças e Elenco)
Use estes dados para definir QUEM causa os presságios.

>>> ELENCO PRINCIPAL:
> **Silas 'O Mestre' (Líder dos Engrenagens)**
  - Papel funcao: Líder da gangue Os Engrenagens
  - Detalhe marcante: Tem um olhar penetrante e uma cicatriz em forma de engrenagem em sua têmpora, que ele adora acariciar quando pensa.
  - Conviccao: A ordem, mesmo que imposta pela força e pela traição, é a única salvação para este Poço decadente. Ele precisa de um novo começo, longe das dívidas e do caos.
  - Contraste: Coleciona engrenagens de relógios antigos, emoldurando-as como obras de arte em seu escritório.

> **Lia 'A Chave' (Braço Direito)**
  - Papel funcao: Tenente de Silas e especialista em logística
  - Detalhe marcante: Sempre carrega um conjunto de gazuas e ferramentas multifuncionais em seu cinto, que ela usa com precisão quase cirúrgica.
  - Conviccao: A sobrevivência em 'O Poço' exige pragmatismo e, por vezes, crueldade. Ela acredita que Silas está fazendo o que é necessário para garantir um futuro para ambos, longe das garras de sindicatos maiores.
  - Contraste: Tem um carinho peculiar por pássaros mecânicos que ela constrói e solta nas áreas mais altas do Poço.

> **Roric 'O Martelo' (Líder dos Soberanos)**
  - Papel funcao: Líder da gangue rival Os Soberanos
  - Detalhe marcante: Um homem robusto com braços musculosos manchados de graxa, cujas falas são curtas e diretas, raramente expressando emoção além da raiva ou desprezo.
  - Conviccao: O Poço pertence aos fortes e aos trabalhadores, não aos parasitas e traidores que se escondem nas sombras. Ele quer justiça e recompensa pelo trabalho árduo de seu povo.
  - Contraste: É absurdamente leal à sua tripulação e insiste que não roubariam suprimentos vitais para o bem-estar de todos, especialmente Orichalcum.

>>> PERIGOS ATIVOS:
> **A Rede de Dívidas do Sindicato**
  - Tipo: Organização
  - Impulso: Escravizar e extorquir.
  - Ameaca verdade: Sua influência corruptora prova que não importa o quão bem-sucedidos ou bem-intencionados sejam os heróis, sempre haverá uma força maior espreitando nas sombras, pronta para cobrá-los.
  - Local vinculado: O Mercado da Pulga Sussurrante / A Taverna 'Fio do Motor'
  - Rastro destruicao: Mercadores e pequenos criminosos com dívidas crescentes, forçados a entregar seus bens ou serviços para Agentes do Sindicato que operam discretamente.
  - Acao iminente: Enviar cobradores para 'renegociar' as dívidas de Silas e Lia, usando informações roubadas para pressioná-los a acelerar a venda do Orichalcum e ameaçando expor o plano dos Engrenagens se o pagamento não for rápido.

> **A Guerra Civil Iminente**
  - Tipo: Horda
  - Impulso: Multiplicar e consumir.
  - Ameaca verdade: A violência e o caos são as respostas naturais para qualquer problema, minando a esperança de que a comunicação e a diplomacia possam prevalecer em 'O Poço'.
  - Local vinculado: O Ferro Velho de 'Os Soberanos' / O Pátio de Carga 'Porto Fantasma'
  - Rastro destruicao: Patrulhas de ambas as gangues ('Os Engrenagens' e 'Os Soberanos') em choque constante nas fronteiras de seus territórios, deixando corpos e sucata destruída para trás.
  - Acao iminente: Silas, para desesperar os heróis e criar uma distração, orquestrará um 'ataque' dos Soberanos contra o Depósito das Engrenagens, usando pistas plantadas para incriminar Roric e garantir que os combatentes de ambos os lados se enfrentem abertamente ao amanhecer.

* **Desastre Iminente (Game Over):** Destruição - Se o Orichalcum não for recuperado e a verdade não for revelada, a guerra aberta entre Os Engrenagens e Os Soberanos irromperá. Ambos os lados, enfurecidos e desconfiados, se aniquilarão em combates brutais dentro e fora do Poço. O Sindicato, aproveitando o caos, acabará subjugando os sobreviventes e tomando o controle, transformando 'O Poço' em um deserto de sucata sem alma. Os heróis podem até escapar com Silas e Lia, mas o assentamento que juraram proteger estará perdido para sempre.

### 5. Matriz de Controle de Informação
Conecte os presságios aos segredos abaixo (Camada de Informação).

>>> SEGREDOS DA CAMPANHA:
  - Titulo: A Origem do Roubo
  - A verdade: O Mestre Silas e Lia roubaram a carga para pagar dívidas.
  - A expectativa: Os Soberanos, gangue rival, roubaram a carga por causa da rivalidade usual.
  - A camuflagem: Pistas falsas deixadas deliberadamente (ex: uma jaqueta dos Soberanos perto do local do crime, testemunhas pagas para incriminá-los).
  - O gatilho: Investigar a cena do crime com detalhes, questionar testemunhas-chave sob pressão, encontrar equipamentos de 'Os Engrenagens' usados no roubo.
  - A revelacao: As pistas falsas são descobertas como armadilhas, e evidências concretas apontam para a participação de Os Engrenagens no roubo.
  - Id: 1

  - Titulo: O Destino da Carga
  - A verdade: A carga de Orichalcum está sendo preparada para ser vendida no mercado negro interestelar por Silas e Lia.
  - A expectativa: A carga ainda está escondida em algum local secreto de Os Soberanos, ou foi destruída.
  - A camuflagem: Comunicações interceptadas entre Silas e um contato misterioso (do sindicato), movimentação suspeita de veículos de carga 'piratas' nos arredores do Poço.
  - O gatilho: Rastrear a origem das comunicações encontradas, interceptar um dos veículos de carga suspeitos, interrogar um cúmplice menor de Silas.
  - A revelacao: Revela que a carga está sendo movida para fora do Poço por Os Engrenagens, não levada por Os Soberanos, e para um destino fora do planeta.
  - Id: 2

  - Titulo: A Verdadeira Motivação de Silas
  - A verdade: Silas está endividado com um sindicato criminoso perigoso e usa o roubo como plano de fuga.
  - A expectativa: Silas é apenas um líder de gangue ambicioso que quer mais poder ou quer provocar Os Soberanos.
  - A camuflagem: Registros financeiros incomuns de Silas, comportamento paranoico, segredos sujos que ele tenta esconder a todo custo, 'visitas' inesperadas de figuras sombrias ao seu território.
  - O gatilho: Obter acesso aos registros pessoais de Silas, capturar um dos cobradores de dívida do sindicato, encontrar evidências de comunicação anterior entre Silas e o sindicato.
  - A revelacao: Descobre que Silas não é um vilão independente, mas sim um peão encurralado, e que uma força externa maior está envolvida.
  - Id: 3

Agora, gere a progressão dramática.
```
**Schema Enviado:**
```json
{
  "type": "object",
  "properties": {
    "pressagios_terriveis": {
      "type": "array",
      "description": "Lista cronológica de 5 eventos/cenas.",
      "items": {
        "type": "object",
        "properties": {
          "ordem": {
            "type": "integer"
          },
          "meta_estrutura": {
            "type": "string",
            "description": "Nome do estágio do arquétipo (ex: 'A Frustração')."
          },
          "local_sugerido": {
            "type": "string"
          },
          "o_pressagio": {
            "type": "string",
            "description": "Descrição narrativa do evento."
          },
          "argumento_arco_historia": {
            "type": "string",
            "description": "Argumento do Mini-Arco: Quem, Onde, Quando, Por que."
          },
          "premissas_arco_historia": {
            "type": "object",
            "description": "A dualidade do mini-arco.",
            "properties": {
              "evidente": {
                "type": "string",
                "description": "O conflito visível/público deste arco."
              },
              "oculta": {
                "type": "string",
                "description": "O segredo ou twist local deste arco."
              }
            },
            "required": [
              "evidente",
              "oculta"
            ]
          },
          "camada_informacao": {
            "type": "object",
            "properties": {
              "id_matriz": {
                "type": "integer"
              },
              "conexao_explicada": {
                "type": "string",
                "description": "Como este mini-arco revela a verdade da Matriz."
              }
            },
            "required": [
              "id_matriz",
              "conexao_explicada"
            ]
          }
        },
        "required": [
          "ordem",
          "meta_estrutura",
          "local_sugerido",
          "o_pressagio",
          "argumento_arco_historia",
          "premissas_arco_historia",
          "camada_informacao"
        ]
      },
      "minItems": 5,
      "maxItems": 5
    },
    "perguntas_dramatica": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 3,
      "maxItems": 3
    }
  },
  "required": [
    "pressagios_terriveis",
    "perguntas_dramatica"
  ]
}
```
</details>

### 🤖 Resposta do Modelo
```json
{
  "pressagios_terriveis": [
    {
      "ordem": 1,
      "meta_estrutura": "Tentação",
      "local_sugerido": "O Depósito das Engrenagens",
      "o_pressagio": "Ao chegarem ao Depósito das Engrenagens, os heróis descobrem um cenário de desordem meticulosamente orquestrada. A rampa de acesso principal está em chamas, bloqueando a entrada principal com uma simulação de ataque ousado. Barricadas improvisadas, feitas de sucata e máquinas quebradas, cercam a área, sugerindo um conflito prolongado. O cheiro de pólvora barata e óleo queimado paira no ar, e os sons de disparos esporádicos ecoam das paredes de metal. Entre a fumaça e a confusão, a silhueta de um homem encapuzado, que se assemelha a um membro dos Soberanos, é vislumbrada a fugir, deixando cair uma ferramenta peculiar que não pertence a nenhum dos Soberanos conhecidos.",
      "argumento_arco_historia": "Noite. O Depósito das Engrenagens. Silas, o Mestre, orquestrou o 'ataque' para criar uma cena de crime convincente e plantar pistas falsas. Ele usou mercenários contratados para simular o confronto e incriminar Os Soberanos, garantindo que o foco fosse desviado de sua fuga. Ele quer que os jogadores acreditem que um ataque brutal ocorreu, incriminando a gangue rival, e que o Orichalcum foi levado durante o caos.",
      "premissas_arco_historia": {
        "evidente": "Os Soberanos realizaram um ataque audacioso e destrutivo ao Depósito das Engrenagens, roubando o Orichalcum em meio a um tiroteio e um incêndio. A aparência de um Soberano fugindo com uma ferramenta incomum reforça essa crença.",
        "oculta": "A cena inteira é uma encenação montada por Silas para incriminar Os Soberanos e desviar a atenção do roubo real. A ferramenta deixada para trás é de fato um item de logística usado por Lia, das Engrenagens, e o 'ataque' foi realizado por mercenários contratados por Silas."
      },
      "camada_informacao": {
        "id_matriz": 1,
        "conexao_explicada": "A investigação da cena do crime revela que as 'pistas falsas' (o mercenário disfarçado, a ferramenta inadequada para os Soberanos) são propositalmente mal executadas para desacreditar Os Soberanos, mas de uma forma que pode ser detectada por observadores atentos. Isso começa a expor a verdade por trás da origem do roubo."
      }
    },
    {
      "ordem": 2,
      "meta_estrutura": "O Crime Compensa",
      "local_sugerido": "O Mercado da Pulga Sussurrante",
      "o_pressagio": "Seguindo uma pista de um informante assustado no Mercado da Pulga Sussurrante, os heróis descobrem um pequeno esconderijo temporário usado pelos ladrões. Dentro, encontram um mapa rudimentar do Poço, rabiscado com rotas de fuga para fora do assentamento. Mais intrigante é um pedaço de tecnologia de comunicação - um transmissor de longo alcance com um chip de criptografia peculiar. Ao tentar ativá-lo, eles captam uma breve transmissão codificada que fala de 'reunião em órbita' e da entrega de 'carga valiosa', juntamente com uma ameaça velada de 'cobrança pelo atraso'. O informante, sob interrogatório, murmura sobre mercenários 'sem rosto' e 'olhos frios' que estiveram ali mais cedo, buscando 'informações sobre rotas de carga'.",
      "argumento_arco_historia": "Um dia. O Mercado da Pulga Sussurrante. Silas e Lia, após o roubo, usam o mercado para obter suprimentos e informações para sua fuga. Eles deixaram para trás um local temporário para a carga futura, onde um transmissor foi acidentalmente deixado para trás durante a pressa. Sibas, em paralelo, está recebendo pressão do Sindicato para acelerar o pagamento, o que se reflete na ameaça da transmissão interceptada.",
      "premissas_arco_historia": {
        "evidente": "Os Soberanos roubaram o Orichalcum e estão se preparando para vendê-lo no mercado negro para um comprador interestelar desconhecido. A transmissão codificada e a menção de 'cobrança pelo atraso' sugerem que eles estão sob pressão de um sindicato criminoso maior.",
        "oculta": "A carga não pertence aos Soberanos, mas sim a Silas e Lia das Engrenagens, que a roubaram para pagar suas próprias dívidas com o notório Sindicato. O transmissor e a transmissão são evidências diretas da tentativa de fuga de Silas e da pressão que ele está sofrendo, não uma prova da posse dos Soberanos."
      },
      "camada_informacao": {
        "id_matriz": 2,
        "conexao_explicada": "A interceptação da comunicação revela que a carga está sendo movida para 'fora do planeta', um destino incompatível com a simples manutenção da rivalidade local. Isso aponta diretamente para o plano de fuga de Silas e Lia e desmente a expectativa de posse dos Soberanos, ligando-se à 'Verdadeira Motivação de Silas'."
      }
    },
    {
      "ordem": 3,
      "meta_estrutura": "A Frustração",
      "local_sugerido": "A Taverna 'Fio do Motor'",
      "o_pressagio": "No ambiente sombrio da Taverna 'Fio do Motor', os heróis rastreiam um contato que pode ter informações sobre os mercenários que viram no depósito. No entanto, o contato está visivelmente aterrorizado e reluta em falar. Subitamente, dois indivíduos corpulentos e mal-encarados entram na taverna, seus olhares frios e penetrantes varrendo a multidão. Um deles, com uma cicatriz notável no rosto, se aproxima da mesa dos heróis. 'Silas mandou avisar', ele rosna, 'para pararem com essa investigação. Se não, o Sindicato cobrara de vocês também.' O outro homem, mais silencioso, limpa um pequeno dispositivo de comunicação em sua mão, que emite um leve zumbido de energia. Os mercenários, percebendo sua recusa em cooperar, deixam a taverna com ameaças sussurradas, deixando para trás uma sensação palpável de perigo iminente.",
      "argumento_arco_historia": "Tarde da noite. A Taverna 'Fio do Motor'. Silas, sentindo que sua encenação no depósito pode não ser suficiente, utiliza seus contatos com o Sindicato para enviar cobradores e intimidar qualquer um que possa atrapalhar seus planos, incluindo os heróis. Os cobradores, operando sob as ordens do Sindicato, ameaçam os heróis em nome de Silas e do Sindicato.",
      "premissas_arco_historia": {
        "evidente": "Silas, o líder dos Engrenagens, está tentando encobrir o roubo, usando força bruta e intimidando os heróis para que parem de investigar. Ele está conectado ao Sindicato, que apoia suas ações e ameaça os heróis com represálias maiores.",
        "oculta": "Os cobradores não estão agindo apenas em nome de Silas, mas do próprio Sindicato, que está pressionando Silas a concluir a venda do Orichalcum o mais rápido possível para quitar suas dívidas. A ameaça direcionada aos heróis revela a extensão do poder do Sindicato e o quão desesperado Silas está para satisfazê-los."
      },
      "camada_informacao": {
        "id_matriz": 3,
        "conexao_explicada": "O encontro na taverna expõe diretamente a conexão de Silas com o Sindicato e sua dívida iminente. A revelação de que os cobradores representam uma força maior do que Silas sugere ajuda a desmascarar a 'Verdadeira Motivação de Silas', mostrando que ele é um peão sob pressão, não um vilão independente."
      }
    },
    {
      "ordem": 4,
      "meta_estrutura": "O Pesadelo",
      "local_sugerido": "O Ferro Velho de 'Os Soberanos'",
      "o_pressagio": "Os heróis chegam ao Ferro Velho de 'Os Soberanos', esperando encontrar Roric e confrontá-lo sobre o roubo. Em vez disso, eles encontram o lugar em estado de alerta máximo. Vigilantes Soberanos relatam que homens armados, usando o mesmo tipo de equipamento que os mercenários do depósito, estão cercando a área, provocando confrontos abertos e plantando explosivos. Um dos Soberanos feridos, antes de sucumbir, grita: 'Eles querem que lutemos! Silas quer que lutemos!'. Ao mesmo tempo, um ataque repentino e brutal de 'Os Engrenagens' começa em pontos estratégicos do ferro-velho, com Silas liderando a carga, gritando que 'Os Soberanos roubaram o metal!'. O caos irrompe, com ambos os lados se vendo em meio a uma verdadeira batalha campal orquestrada por Silas.",
      "argumento_arco_historia": "Amanhecer. O Ferro Velho de 'Os Soberanos'. Para garantir que a guerra civil irrompa, Silas e Lia orquestram um ataque simulado 'dos Soberanos' contra o seu próprio pessoal em um ponto estratégico, plantando mais evidências para incriminar Roric. Esta ação força uma resposta dos Soberanos e, com o ataque de Silas, a guerra total se torna iminente.",
      "premissas_arco_historia": {
        "evidente": "Os Soberanos, em um ato de provocação, atacaram o Ferro Velho, dando início a uma guerra aberta. Silas e seus Engrenagens estão reagindo defensivamente para proteger o Poço, enquanto combatem os agressores Soberanos.",
        "oculta": "A batalha é totalmente orquestrada por Silas. Os 'ataques dos Soberanos' iniciais foram encenados por mercenários, e o ataque dos Engrenagens é um ataque direto e deliberado para incriminar Roric e forçar a guerra. O objetivo é usar o caos para encobrir a fuga de Silas e Lia com o Orichalcum."
      },
      "camada_informacao": {
        "id_matriz": 1,
        "conexao_explicada": "A descoberta de que a guerra civil iminente é uma farsa orquestrada por Silas desmascara completamente a expectativa inicial de um conflito entre gangues rivais. Isso revela que a maior ameaça não é a rivalidade em si ou Os Soberanos, mas a manipulação de Silas, expondo a 'Origem do Roubo' como uma trama."
      }
    },
    {
      "ordem": 5,
      "meta_estrutura": "Destruição",
      "local_sugerido": "O Pátio de Carga 'Porto Fantasma'",
      "o_pressagio": "Enquanto o Poço se afunda no caos da guerra civil, os heróis rastreiam Silas e Lia até o Pátio de Carga 'Porto Fantasma', onde um cargueiro espacial pirata está prestes a decolar. Silas e Lia estão carregando os contêineres de Orichalcum, prontos para fugir para sempre. Quando confrontados, Silas, em um ato de desespero, ativa um dispositivo que inicia uma contagem regressiva em todos os geradores de energia instáveis do Pátio, ameaçando transformar a área em um inferno de explosões e radiação. Ele aponta para os heróis e grita: 'Se não posso ter, ninguém terá! E se eu cair, vou levar este esquife maldito comigo!'. Ele e Lia se preparam para embarcar, deixando os heróis com o dilema de salvar o Poço ou impedir a partida da carga e dos culpados.",
      "argumento_arco_historia": "Manhã. O Pátio de Carga 'Porto Fantasma'. Silas e Lia estão prestes a escapar com o Orichalcum. Com a guerra civil em pleno andamento (orquestrada por ele), ele sabe que seu tempo é limitado. Para garantir que ele não seja pego, ele decide destruir o Pátio de Carga e o Orichalcum, usando a situação caótica a seu favor para sua fuga final e para o Sindicato, já que isso elimina a evidência. Ele ativa os geradores instáveis para causar uma reação em cadeia e destruir tudo.",
      "premissas_arco_historia": {
        "evidente": "Silas e Lia estão tentando fugir com o Orichalcum roubado para evitar a punição e a guerra civil. Desesperados, eles ativaram um dispositivo que destruirá o Pátio de Carga e tudo ao redor, incluindo os heróis, se eles tentarem impedi-los de escapar.",
        "oculta": "O objetivo de Silas não é apenas fugir, mas também destruir a evidência (o Orichalcum e o Pátio de Carga) para o Sindicato, potencialmente para evitar sua própria execução ou para evitar que o Sindicato receba uma carga que ele não pode mais controlar. Sua ação é uma destruição desesperada para cobrir seus rastros e lidar com a pressão do Sindicato."
      },
      "camada_informacao": {
        "id_matriz": 2,
        "conexao_explicada": "A tentativa de Silas de destruir o Pátio de Carga e o Orichalcum em vez de simplesmente fugir com ele revela uma motivação mais complexa do que a simples ganância. Sua ação em 'O Destino da Carga' é um último ato desesperado para apagar todas as pistas, ligando-se à sua dívida com o Sindicato e confirmando a verdade sobre o destino da carga."
      }
    }
  ],
  "perguntas_dramatica": [
    "Até onde os heróis estão dispostos a ir para expor a verdade e salvar 'O Poço', mesmo que isso signifique sacrificar a paz temporária ou suas próprias vidas?",
    "Será que o pragmatismo de Lia e sua lealdade a Silas podem ser quebrados pela iminente destruição que ele planeja, ou ela o seguirá até o fim no 'outro mundo'?",
    "Que papel o Sindicato realmente desempenha nas aspirações de Silas, e como sua influência se estende para além do Poço, mesmo que a carga seja destruída e Silas e Lia escapem ou pereçam?"
  ]
}
```
