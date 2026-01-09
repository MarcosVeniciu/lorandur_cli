# Relatório de Teste: Pipeline Trama + Frente
**Data:** 2026_01_09_00_59
**Cenário:** Dieselpunk

## 1. Módulo: Trama (core_trama_generator)
**Status:** Sucesso
### Contexto Enviado (Trama)
<details>
<summary>Ver System Prompt</summary>

```text
Você é um Mestre de RPG especialista e Designer Narrativo focado no sistema 'Dominus' e na metodologia de construção de aventuras do canal 'Narradores Narrados'.

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
</details>

<details>
<summary>Ver User Prompt</summary>

```text
# DADOS DE ENTRADA (Injeção de Contexto)

1. **Cenário (Gênero Principal):** Dieselpunk

2. **Rolagem de Trama (Dominus):**
   - *Algo Aconteceu:* Uma carga valiosa foi roubada
   - *Você Precisa:* Recuperar a carga antes do amanhecer
   - *Senão:* Guerra entre gangues rivais

3. **Níveis de Escopo Suportados:**
- Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.
- Nível 3 (Escopo Regional - A Estrada): A trama é uma jornada. O foco é a travessia de A para B, gestão de combustível, perseguições e encontros na estrada.

Crie a estrutura V3.0 agora.
```
</details>

### Output Schema (Enviado)
<details>
<summary>Ver JSON Schema (Trama)</summary>

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
        "escopo_selecionado": {
          "type": "string"
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
        "escopo_selecionado"
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

### Saída Gerada (Trama)
```json
{
  "configuracao_aventura": {
    "genero_principal": "Dieselpunk",
    "subgeneros_selecionados": [
      "Film Noir",
      "Ação Frenética"
    ],
    "escopo_selecionado": "Nível 2 (Escopo Local - O Refúgio)",
    "justificativa_estilo": "A trama de roubo, corrida contra o tempo para evitar uma guerra de gangues e o contexto Dieselpunk evocam um futuro distópico cheio de conspiração, desespero e confrontos explosivos, característicos do Film Noir e da Ação Frenética.",
    "justificativa_escopo": "A urgência ('antes do amanhecer') e a consequência (guerra de gangues em um distrito específico) indicam que a aventura se desenrolará dentro de um único local ou distrito industrial, permitindo investigações focadas e confrontos iminentes, sem a necessidade de uma vasta jornada regional."
  },
  "argumento": {
    "texto": "Onde: Um distrito industrial decadente e poluído de uma megacidade Dieselpunk conhecida como 'O Caldeirão'. Quando: Na calada da noite, com o amanhecer iminente. Quem: Os jogadores são contratados por um intermediário de um sindicato de carga obscuro para recuperar uma remessa roubada. Os ladrões são, superficialmente, membros da gangue 'Os Ferros-Velhos', que agora são perseguidos pela gangue rival 'Os Canhões de Névoa', que se acredita ter sido a vítima do roubo. Por que: A remessa, na verdade, contém componentes experimentais para uma superarma de energia projetada por uma facção secreta do governo ou corporativa ('A Congregação do Crepúsculo'). O roubo foi orquestrado por essa facção para semear caos, culpar as gangues rivais, enfraquecê-las e quebrar o monopólio de recursos de uma delas, permitindo que a Congregação recuperasse a carga e assumisse o controle do território.",
    "justificativa": "Este argumento define os elementos centrais da aventura: o cenário sombrio do 'Caldeirão', o prazo apertado, os jogadores como peças centrais em um jogo de poder entre gangues, e a verdadeira motivação oculta que liga o roubo, a ameaça de guerra e uma entidade manipuladora."
  },
  "premissas": {
    "evidente": {
      "texto": "Um contato de confiança (ou um membro desesperado de uma gangue) informa aos personagens que uma carga crucial foi roubada de forma audaciosa e que uma gangue rival está prestes a iniciar uma guerra declarada ao amanhecer caso a carga não seja devolvida. Sua missão é recuperar a remessa sem que as gangues rivais saibam que vocês estão envolvidos, impedindo o banho de sangue que se aproxima.",
      "funcao": "Estabelece a missão imediata, o senso de urgência e o conflito aparente entre as duas gangues, direcionando a ação inicial dos jogadores."
    },
    "oculta": {
      "texto": "A carga roubada não é apenas valiosa, mas sim um protótipo tecnológico de aplicação militar devastadora. O roubo foi uma operação de 'bandeira falsa' orquestrada por uma terceira força (A Congregação do Crepúsculo) para incriminar uma gangue, provocar uma guerra entre as outras e, no meio do caos, roubar ou confiscar a carga, eliminando rivais e ganhando controle sobre a tecnologia.",
      "funcao": "Subverte a compreensão inicial da missão, revelando que os jogadores são peões em um jogo maior, onde um conflito aparente é uma cortina de fumaça para um golpe de poder secreto."
    },
    "justificativa": "As premissas criam o arcabouço narrativo, apresentando aos jogadores uma 'verdade' superficial e, em seguida, revelando o plano secreto e as verdadeiras intenções dos antagonistas."
  },
  "matriz_controle_informacao": {
    "itens": [
      {
        "id": 1,
        "titulo": "A Natureza da 'Carga Valiosa'",
        "a_verdade": "Os componentes são para um protótipo de 'Guerra-Relâmpago' (Blitzkrieg unit), uma arma móvel de destruição em massa, com tecnologia secreta de energia e sistemas de mira.",
        "a_expectativa": "Materiais de construção raros, suprimentos médicos escassos, ou armas de gangue de alta qualidade.",
        "a_camuflagem": "Os contêineres estão selados, marcados com códigos industriais genéricos. Relatos de poucas testemunhas variam entre 'combustíveis perigosos' e 'equipamento de rádio avançado'.",
        "o_gatilho": "Investigar os contêineres recuperados e analisar seus componentes ou decifrar os registros de envio do local de origem.",
        "a_revelacao": "Os componentes indicam um nível tecnológico muito superior ao usual para as gangues, e a origem aponta para um centro de pesquisa secreto ou instalação militar."
      },
      {
        "id": 2,
        "titulo": "O Verdadeiro Culpado pelo Roubo",
        "a_verdade": "O roubo foi orquestrado pela 'Congregação do Crepúsculo', que usou mercenários ou cooptou membros de baixo escalão dos 'Ferros-Velhos', fornecendo-lhes a tecnologia e o conhecimento para o roubo, e plantando evidências falsas contra os 'Canhões de Névoa'.",
        "a_expectativa": "Os 'Ferros-Velhos' roubaram a carga, e os 'Canhões de Névoa' estão reagindo a este ato de agressão.",
        "a_camuflagem": "Evidências plantadas no local do roubo apontam diretamente para membros dos 'Ferros-Velhos'. Informantes podem confirmar que os 'Ferros-Velhos' 'venderiam a mãe por sucata'.",
        "o_gatilho": "Capturar e interrogar um dos supostos 'ladrões' ou encontrar um dispositivo de comunicação ou registro financeiro com vestígios da 'Congregação do Crepúsculo'.",
        "a_revelacao": "Os supostos ladrões revelam que foram contratados/forçados por uma entidade externa, descrevendo um contato distinto ou um símbolo da 'Congregação do Crepúsculo', confessando que não agiram por ordem dos 'Ferros-Velhos'."
      },
      {
        "id": 3,
        "titulo": "A 'Guerra' Iminente entre Gangues",
        "a_verdade": "A 'guerra' é uma oportunidade criada e manipulada pela 'Congregação do Crepúsculo' para enfraquecer ambas as gangues ('Ferros-Velhos' e 'Canhões de Névoa'), permitindo que a Congregação tome controle do território ou elimine concorrentes perigosos.",
        "a_expectativa": "As duas gangues estão prestes a entrar em guerra em decorrência do roubo, e retornar a carga irá apaziguar os 'Canhões de Névoa'.",
        "a_camuflagem": "Mensagens interceptadas entre as gangues, patrulhas de gangues em estado de alerta elevado, e confrontos de baixa intensidade simulados ou reais que parecem ser fruto da rivalidade.",
        "o_gatilho": "Observar uma comunicação clandestina entre líderes de ambas as gangues e um representante da 'Congregação do Crepúsculo' em um local neutro, ou descobrir que a 'vítima designada' (Canhões de Névoa) sabia do roubo com antecedência e se preparava para retaliar de forma coordenada.",
        "a_revelacao": "A confrontação entre as gangues está sendo orquestrada. Seus líderes não são os verdadeiros orquestradores da violência, mas sim peões controlados por uma força conjunta ou dividida pela 'Congregação do Crepúsculo', com o objetivo de um extermínio mútuo ou uma distração controlada."
      }
    ],
    "justificativa": "Esta matriz garante que os jogadores sejam apresentados com múltiplas camadas de engano, permitindo que suas investigações e descobertas gradualmente desvendem a complexa conspiração por trás do roubo e da ameaça de guerra."
  }
}
```

---

## 2. Módulo: Frente (core_front_generator)
**Status:** Sucesso
### Contexto Enviado (Frente)
<details>
<summary>Ver System Prompt</summary>

```text
Você é um Mestre de RPG especialista e Designer Narrativo.

# Objetivo
Sua tarefa é criar uma "Frente de Aventura" (nível de sessão/episódio). Transforme a Trama em elementos jogáveis.

# Instruções

1. **Arquétipo de Enredo:** Escolha um (ex: Superar o Monstro, A Busca, Tragédia) e use sua Meta-Estrutura para guiar os presságios.

2. **Locais (Location Pool):**
   - Crie nomes evocativos para: 1 Local Inicial, 4 Locais de Investigação, 3 Locais de Clímax.

3. **Presságios Terríveis (CRÍTICO):**
   - Crie EXATAMENTE 5 eventos cronológicos.
   - **Locais:** Use o Local Inicial para o Presságio 1, Locais de Investigação para 2-4, e Clímax para 5.
   - **Mistérios:** Conecte cada presságio a um item da Matriz de Informação.

# Formato de Saída (JSON Plano)
Responda APENAS com um JSON. Não aninhe objetos desnecessariamente. Use as chaves exatas abaixo:
- `cabecalho_arquetipo`: O arquétipo escolhido.
- `cabecalho_foco`: Resumo da frente.
- `locais_iniciais`: Lista [1 string].
- `locais_investigacao`: Lista [4 strings].
- `locais_climax`: Lista [3 strings].
- `elenco_npcs`: Lista de nomes.
- `perigos`: Lista de objetos {nome, tipo, impulso}.
- `desastre_tipo`: O tipo do Game Over.
- `desastre_descricao`: O que acontece se falharem.
- `pressagios`: Lista de 5 objetos. CADA objeto deve ter os campos planos:
    - `ordem` (int)
    - `meta_estrutura` (string)
    - `local` (string)
    - `descricao_evento` (string)
    - `argumento_cena` (string)
    - `premissa_evidente` (string)
    - `premissa_oculta` (string)
    - `pista_tipo` (string)
    - `pista_conexao` (string)
- `perguntas_dramatica`: Lista de 3 perguntas.
```
</details>

<details>
<summary>Ver User Prompt</summary>

```text
# DADOS DE ENTRADA

1. **Configuração:**
   - Gênero: Dieselpunk
   - Escopo: Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.

2. **Trama:**
Onde: Um distrito industrial decadente e poluído de uma megacidade Dieselpunk conhecida como 'O Caldeirão'. Quando: Na calada da noite, com o amanhecer iminente. Quem: Os jogadores são contratados por um intermediário de um sindicato de carga obscuro para recuperar uma remessa roubada. Os ladrões são, superficialmente, membros da gangue 'Os Ferros-Velhos', que agora são perseguidos pela gangue rival 'Os Canhões de Névoa', que se acredita ter sido a vítima do roubo. Por que: A remessa, na verdade, contém componentes experimentais para uma superarma de energia projetada por uma facção secreta do governo ou corporativa ('A Congregação do Crepúsculo'). O roubo foi orquestrado por essa facção para semear caos, culpar as gangues rivais, enfraquecê-las e quebrar o monopólio de recursos de uma delas, permitindo que a Congregação recuperasse a carga e assumisse o controle do território.

3. **Matriz de Mistérios:**
- **MISTÉRIO: A Natureza da 'Carga Valiosa'**
  > *Expectativa:* Materiais de construção raros, suprimentos médicos escassos, ou armas de gangue de alta qualidade.
  > *A Verdade:* Os componentes são para um protótipo de 'Guerra-Relâmpago' (Blitzkrieg unit), uma arma móvel de destruição em massa, com tecnologia secreta de energia e sistemas de mira.
  > *Gatilho:* Investigar os contêineres recuperados e analisar seus componentes ou decifrar os registros de envio do local de origem.
  > *Revelação:* Os componentes indicam um nível tecnológico muito superior ao usual para as gangues, e a origem aponta para um centro de pesquisa secreto ou instalação militar.

- **MISTÉRIO: O Verdadeiro Culpado pelo Roubo**
  > *Expectativa:* Os 'Ferros-Velhos' roubaram a carga, e os 'Canhões de Névoa' estão reagindo a este ato de agressão.
  > *A Verdade:* O roubo foi orquestrado pela 'Congregação do Crepúsculo', que usou mercenários ou cooptou membros de baixo escalão dos 'Ferros-Velhos', fornecendo-lhes a tecnologia e o conhecimento para o roubo, e plantando evidências falsas contra os 'Canhões de Névoa'.
  > *Gatilho:* Capturar e interrogar um dos supostos 'ladrões' ou encontrar um dispositivo de comunicação ou registro financeiro com vestígios da 'Congregação do Crepúsculo'.
  > *Revelação:* Os supostos ladrões revelam que foram contratados/forçados por uma entidade externa, descrevendo um contato distinto ou um símbolo da 'Congregação do Crepúsculo', confessando que não agiram por ordem dos 'Ferros-Velhos'.

- **MISTÉRIO: A 'Guerra' Iminente entre Gangues**
  > *Expectativa:* As duas gangues estão prestes a entrar em guerra em decorrência do roubo, e retornar a carga irá apaziguar os 'Canhões de Névoa'.
  > *A Verdade:* A 'guerra' é uma oportunidade criada e manipulada pela 'Congregação do Crepúsculo' para enfraquecer ambas as gangues ('Ferros-Velhos' e 'Canhões de Névoa'), permitindo que a Congregação tome controle do território ou elimine concorrentes perigosos.
  > *Gatilho:* Observar uma comunicação clandestina entre líderes de ambas as gangues e um representante da 'Congregação do Crepúsculo' em um local neutro, ou descobrir que a 'vítima designada' (Canhões de Névoa) sabia do roubo com antecedência e se preparava para retaliar de forma coordenada.
  > *Revelação:* A confrontação entre as gangues está sendo orquestrada. Seus líderes não são os verdadeiros orquestradores da violência, mas sim peões controlados por uma força conjunta ou dividida pela 'Congregação do Crepúsculo', com o objetivo de um extermínio mútuo ou uma distração controlada.



4. **Listas Base:**
   - Personagens: Motorista, Mecânico, Guerreiro da Estrada, Imperator
   - Locais: A Cidadela de Ferro, O Deserto de Sal, A Rodovia Infinita, O Oásis Tóxico, As Ruínas da Velha Capital

Gere a Frente de Aventura (JSON Plano).
```
</details>

### Output Schema (Enviado)
<details>
<summary>Ver JSON Schema (Frente)</summary>

```json
{
  "type": "object",
  "properties": {
    "cabecalho_arquetipo": {
      "type": "string"
    },
    "cabecalho_foco": {
      "type": "string"
    },
    "locais_iniciais": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "locais_investigacao": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "locais_climax": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "elenco_npcs": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "perigos": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "nome": {
            "type": "string"
          },
          "tipo": {
            "type": "string"
          },
          "impulso": {
            "type": "string"
          }
        },
        "required": [
          "nome",
          "tipo",
          "impulso"
        ],
        "additionalProperties": false
      }
    },
    "desastre_tipo": {
      "type": "string"
    },
    "desastre_descricao": {
      "type": "string"
    },
    "pressagios": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ordem": {
            "type": "integer"
          },
          "meta_estrutura": {
            "type": "string"
          },
          "local": {
            "type": "string"
          },
          "descricao_evento": {
            "type": "string"
          },
          "argumento_cena": {
            "type": "string"
          },
          "premissa_evidente": {
            "type": "string"
          },
          "premissa_oculta": {
            "type": "string"
          },
          "pista_tipo": {
            "type": "string"
          },
          "pista_conexao": {
            "type": "string"
          }
        },
        "required": [
          "ordem",
          "meta_estrutura",
          "local",
          "descricao_evento",
          "argumento_cena",
          "premissa_evidente",
          "premissa_oculta",
          "pista_tipo",
          "pista_conexao"
        ],
        "additionalProperties": false
      }
    },
    "perguntas_dramatica": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "cabecalho_arquetipo",
    "cabecalho_foco",
    "locais_iniciais",
    "locais_investigacao",
    "locais_climax",
    "elenco_npcs",
    "perigos",
    "desastre_tipo",
    "desastre_descricao",
    "pressagios",
    "perguntas_dramatica"
  ],
  "additionalProperties": false
}
```
</details>

### Saída Gerada (Frente)
```json
{
  "cabecalho_arquetipo": "A Conspiração",
  "cabecalho_foco": "Um intermediário contrata os jogadores para recuperar uma carga roubada 'Ferros-Velhos', apenas para descobrir que o roubo foi orquestrado pela 'Congregação do Crepúsculo' para culpar gangues rivais e encobrir o roubo de componentes para uma super-arma.",
  "locais_iniciais": [
    "O Refúgio Empoeirado"
  ],
  "locais_investigacao": [
    "Canteiro dos Ferros-Velhos",
    "Beco das Névoas Químicas",
    "Depósito Esquecido 7B",
    "Altoforno Desativado Cronos"
  ],
  "locais_climax": [
    "A Sala de Controle da Congregação",
    "Plataforma de Lançamento da Super-Arma",
    "O Ninho dos Corvos Metálicos"
  ],
  "elenco_npcs": [
    "O Contratante (Intermediário do Sindicato)",
    "Jax 'Ferro-Velho' (Líder dos Ferros-Velhos)",
    "Carmesim Nevoeiro (Líder dos Canhões de Névoa)",
    "Agente Silencioso (Operativo da Congregação)"
  ],
  "perigos": [
    {
      "nome": "Os Ferros-Velhos",
      "tipo": "Gangue Urbana",
      "impulso": "Territorialismo e Vingança"
    },
    {
      "nome": "Os Canhões de Névoa",
      "tipo": "Gangue Urbana",
      "impulso": "Controle de Território e Represália"
    },
    {
      "nome": "Agentes da Congregação",
      "tipo": "Infiltrados/Operativos",
      "impulso": "Sigilo e Execução da Agenda"
    },
    {
      "nome": "Ambiente Poluído do Caldeirão",
      "tipo": "Perigo Ambiental",
      "impulso": "Desgaste e Instabilidade Estrutural"
    },
    {
      "nome": "Carga Experimental da Congregação",
      "tipo": "Tecnológico Instável",
      "impulso": "Detonação ou Malfuncionamento Catastrófico"
    }
  ],
  "desastre_tipo": "A Congregação Consolida Controle",
  "desastre_descricao": "A Congregação do Crepúsculo usa o conflito entre as gangues como cortina de fumaça para lançar sua super-arma, obliterar qualquer resistência, e assumir o controle total do Caldeirão, com os jogadores falhando em impedir a catástrofe.",
  "pressagios": [
    {
      "ordem": 1,
      "meta_estrutura": "A Conspiração",
      "local": "O Refúgio Empoeirado",
      "descricao_evento": "Um mensageiro pálido e apressado chega com a notícia do roubo da carga, antes mesmo de ser entregue aos PCs. O contratante exige eficiência imediata.",
      "argumento_cena": "Os jogadores recebem o objetivo e a urgência dada pelo contratante, com uma recompensa promissora.",
      "premissa_evidente": "A carga escolhida foi roubada por 'Os Ferros-Velhos' e deve ser recuperada urgentemente.",
      "premissa_oculta": "Esta 'carga' valiosíssima é mais do que apenas materiais comuns; seu valor é desproporcional e seu propósito é secreto.",
      "pista_tipo": "Mensagem Urgente",
      "pista_conexao": "A Natureza da 'Carga Valiosa'"
    },
    {
      "ordem": 2,
      "meta_estrutura": "A Conspiração",
      "local": "Canteiro dos Ferros-Velhos",
      "descricao_evento": "Ao investigar o território dos 'Ferros-Velhos', os jogadores ouvem sussurros entre membros de baixo escalão sobre 'contratos externos' e o uso de 'equipamentos estranhos' durante o roubo.",
      "argumento_cena": "Os jogadores confrontam a gangue principal suspeita e obtêm informações que apontam para uma origem não gangue, semeando a primeira dúvida sobre a culpa direta.",
      "premissa_evidente": "Os 'Ferros-Velhos' parecem ter realizado o roubo, mas possivelmente com auxílio externo incomum.",
      "premissa_oculta": "A ajuda externa sugere uma terceira parte desconhecida com recursos significativos e um interesse oculto no roubo.",
      "pista_tipo": "Interrogatório/Informação de Gangue",
      "pista_conexao": "O Verdadeiro Culpado pelo Roubo"
    },
    {
      "ordem": 3,
      "meta_estrutura": "A Conspiração",
      "local": "Beco das Névoas Químicas",
      "descricao_evento": "Os jogadores encontram patrulhas dos 'Canhões de Névoa', mas notam que estão mais bem equipados e posicionados do que o esperado para uma mera retaliação, com rotas de fuga e suprimentos avançados de guerra.",
      "argumento_cena": "Os jogadores percebem que a resposta da gangue rival não é uma reação orgânica ao roubo, mas um preparo coordenado para algo maior.",
      "premissa_evidente": "Os 'Canhões de Névoa' estão se preparando para uma guerra total contra os 'Ferros-Velhos' de forma inesperada.",
      "premissa_oculta": "O preparo excessivo indica que os 'Canhões de Névoa' podem ter sabido do roubo com antecedência ou estão sendo manipulados a agir em um confronto orquestrado.",
      "pista_tipo": "Observação de Patrulha/Preparativos",
      "pista_conexao": "A 'Guerra' Iminente entre Gangues"
    },
    {
      "ordem": 4,
      "meta_estrutura": "A Conspiração",
      "local": "Depósito Esquecido 7B",
      "descricao_evento": "Uma busca em um depósito usado como ponto de troca revela contêineres parcialmente descarregados contendo componentes tecnológicos de altíssima qualidade, e um dispositivo de comunicação que capta sinais codificados ligando a 'Congregação do Crepúsculo'.",
      "argumento_cena": "Os jogadores descobrem a verdadeira natureza tecnológica da carga roubada e identificam o principal agente manipulador por trás de tudo.",
      "premissa_evidente": "O roubo envolveu tecnologia ou materiais de alto valor e origem não gangue.",
      "premissa_oculta": "Os componentes são para uma arma experimental secreta, e a 'Congregação do Crepúsculo' orquestrou tudo para seus próprios fins.",
      "pista_tipo": "Evidência Tecnológica/Comunicação Interceptada",
      "pista_conexao": "A Natureza da 'Carga Valiosa' / O Verdadeiro Culpado pelo Roubo"
    },
    {
      "ordem": 5,
      "meta_estrutura": "A Conspiração",
      "local": "Plataforma de Lançamento da Super-Arma",
      "descricao_evento": "Ao chegarem ao local secreto onde a Congregação está montando sua arma, os jogadores interceptam uma comunicação final detalhando como o caos das gangues serve de distração para o lançamento iminente.",
      "argumento_cena": "A verdadeira ameaça e o plano mestre da Congregação são revelados: o roubo e a guerra de gangues são meras cortinas de fumaça para o lançamento da arma e a tomada de controle do território.",
      "premissa_evidente": "A Congregação do Crepúsculo possui uma super-arma e pretende usá-la em breve.",
      "premissa_oculta": "O roubo de carga e a iminente guerra de gangues foram orquestrados como uma distração controlada para o lançamento da arma e a consolidação do poder da Congregação.",
      "pista_tipo": "Comunicação Final da Congregação",
      "pista_conexao": "A 'Guerra' Iminente entre Gangues"
    }
  ],
  "perguntas_dramatica": [
    "Quão longe vocês irão para cumprir um contrato que cheira a traição e manipulação?",
    "Quais gangues, se alguma, valem a pena salvar em um território que prospera no caos?",
    "O que acontece quando o poder real surge das sombras para dominar tudo, e vocês são apenas peões nessa partida?"
  ]
}
```

### Análise Rápida (Elementos Chave)
- **Arquétipo de Enredo:** None
- **Foco:** None
- **Qtd. Presságios:** 0

---

## 📊 Métricas de Execução Total
| Métrica | Trama | Frente de aventura | Total |
| :--- | :--- | :--- | :--- |
| **Tempo Total** | 35.86s | 33.64s | 69.50s |
| **Tokens Entrada** | 843 | 1663 | 2506 |
| **Tokens Saída** | 4449 | 5291 | 9740 |
| **Tokens Total** | 5292 | 6954 | 12246 |
| **Custo Estimado** | $0.001864 | $0.002283 | $0.004147 |
