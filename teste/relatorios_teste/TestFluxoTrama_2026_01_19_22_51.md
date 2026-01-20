# Relatório: Teste de Trama V4 (Data-Driven)
**Data:** 2026_01_19_22_51 | **Status:** ✅ Sucesso

## 📊 Métricas de Execução

| Métrica | 1. Core Trama Generator | Total |
| :--- | :--- | :--- |
| **Tempo Total** | 10.08s | **10.08s** |
| **Tokens Entrada** | 873 | **873** |
| **Tokens Saída** | 1943 | **1943** |
| **Tokens Total** | 2816 | **2816** |
| **Custo Estimado** | $0.000865 | **$0.000865** |

---

## 1. 1. Core Trama Generator (Módulo: `core_trama_generator`)
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
   - Analise a combinação da Trama sorteada ({'col1_event': 'Uma transmissão fantasma foi captada', 'col2_goal': 'Decifrar o código antes da invasão', 'col3_consequence': 'A cidade será bombardeada'}). Que tipo de história isso sugere? (Ex: Drama, Comédia, Terror, Noir, Ação Frenética).
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
   - *Algo Aconteceu:* Uma transmissão fantasma foi captada
   - *Você Precisa:* Decifrar o código antes da invasão
   - *Senão:* A cidade será bombardeada

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
      "Tecno-Thriller",
      "Suspense Militar",
      "Mistério"
    ],
    "escopo": "Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.",
    "justificativa_escopo": "A trama de uma transmissão fantasma interceptada que leva a um bombardeio iminente se encaixa perfeitamente em um ambiente isolado ou base (Nível 2), onde o controle da informação e a defesa de perímetro são cruciais. Isso permite um foco maior na intriga e na urgência da descoberta sem a necessidade de uma jornada extensa.",
    "justificativa_estilo": "A combinação de 'transmissão fantasma', 'decifrar código antes da invasão' e 'cidade será bombardeada' em um cenário Dieselpunk sugere uma narrativa tensa e intelectual, com elementos de 'Tecno-Thriller' (a natureza da transmissão e do código), 'Suspense Militar' (a ameaça de bombardeio e invasão) e 'Mistério' (a origem e o significado da transmissão)."
  },
  "argumento": {
    "texto": "Na cidade fortificada de Ferrocrasto, protegida por antigas defesas Dieselpunk, os jogadores são convidados a decifrar uma antiga transmissão fantasma captada pelas torres de comunicação. O que eles não sabem é que a transmissão não é um aviso, mas sim as coordenadas de um ataque aéreo massivo, orquestrado por uma facção rival que está usando um antigo dispositivo de 'frequência fantasma' para mascarar seu movimento e comunicação. Se o código for decifrado sem antes desativar o dispositivo ou contrapor suas frequências, o sinal decifrado alertará os invasores sobre as defesas de Ferrocrasto, garantindo o sucesso do bombardeio e a queda da cidade.",
    "justificativa": "O argumento define o 'Onde' (cidade fortificada de Ferrocrasto), o 'Quando' (durante a captação da transmissão), o 'Quem' (jogadores, facção rival, supostos defensores da cidade), o 'Por que' (domínio da região através de um ataque aéreo surpresa e estratégico) e o 'Como' (uso de tecnologia de 'frequência fantasma' para mascarar as coordenadas e preparar o ataque)."
  },
  "premissas": {
    "evidente": {
      "texto": "Uma comunicação inimiga de origem desconhecida foi interceptada, contendo informações vitais. A prioridade é decifrar esse código o mais rápido possível, pois a inteligência militar acredita que ele contém os planos de um ataque iminente à cidade. Falhar em decifrar e agir a tempo resultará em um bombardeio devastador.",
      "funcao": "Fornece aos jogadores uma missão clara e urgente, focada na decodificação e na ameaça externa, estabelecendo a expectativa de um inimigo tecnológico convencional."
    },
    "oculta": {
      "texto": "A 'transmissão fantasma' é, na verdade, um sinal de rádio de alta frequência que, ao ser decifrado, atua como um farol para os bombardeiros inimigos, indicando as defesas mais vulneráveis de Ferrocrasto. A facção que enviou a transmissão não está apenas 'invadindo', ela está usando a própria decodificação dos jogadores como parte de seu plano de ataque, transformando-os inadvertidamente em peões para a destruição da cidade.",
      "funcao": "Subverte a expectativa de uma simples decodificação de inteligência, revelando que a própria ação dos jogadores é instrumental para o desastre, adicionando uma camada de traição e ironia trágica."
    },
    "justificativa": "As premissas criam um contraste entre a meta aparente (decifrar um aviso) e a verdade sombria (tornar-se o gatilho para o bombardeio), construindo a tensão e o suspense do mistério."
  },
  "matriz_controle_informacao": {
    "itens": [
      {
        "titulo": "A Natureza da Transmissão",
        "a_verdade": "A transmissão fantasma é um sinal de 'frequência fantasma' que, curiosamente, ressoa com o equipamento de comunicação de Ferrocrasto, o que o torna detectável. Seu propósito inicial era mascarar as comunicações da facção invasora.",
        "a_expectativa": "A transmissão é uma mensagem encriptada normal de um inimigo, talvez um código de lançamento ou comunicado de guerra.",
        "a_camuflagem": "A transmissão é recebida em frequências não usuais, com ruído intermitente, fazendo parecer mais uma falha técnica ou um sinal alienígena do que um código.",
        "o_gatilho": "Investigar a fonte da peculiaridade do sinal, talvez buscando a origem do ruído ou estudando as anomalias espectrais da transmissão através de equipamentos de análise avançados.",
        "a_revelacao": "A transmissão não é uma mensagem para ser decifrada no sentido tradicional, mas sim um sinal de 'farol' que o próprio decodificador amplificará e direcionará para o alvo.",
        "id": 1
      },
      {
        "titulo": "A Identidade dos Transmissores Invasores",
        "a_verdade": "A facção que envia a transmissão não são os 'invasores' que planejam o bombardeio por conta própria. Eles são, na verdade, batedores de uma força muito maior que usou a tecnologia de frequência fantasma para testar as defesas e as respostas de Ferrocrasto, pretendendo usar as informações coletadas pelo próprio ato de decodificação dos jogadores como inteligência para um ataque futuro e massivo.",
        "a_expectativa": "A transmissão é uma comunicação de guerra direta de uma força militar inimiga estabelecida.",
        "a_camuflagem": "A transmissão não contém identificadores claros da facção, apenas um padrão de sinalização repetitivo e ameaçador. As comunicações recebidas de outras zonas costumam ser assim, levando à suposição.",
        "o_gatilho": "Analisar os restos de dados não decifráveis na transmissão, procurar por padrões recorrentes em outras frequências próximas em momentos de 'silêncio' de Ferrocrasto, ou rastrear a direção do sinal original até um ponto de origem vago e suspeito.",
        "a_revelacao": "Os transmissores são um grupo de reconhecimento de alta tecnologia que estão investigando Ferrocrasto e usando os receptores de defesa como sondas involuntárias para suas próprias operações.",
        "id": 2
      },
      {
        "titulo": "O Propósito do Bombardeio",
        "a_verdade": "O bombardeio não é simplesmente Destruição pela Destruição. A facção invasora quer a cidade de Ferrocrasto não em ruínas, mas intacta para seus próprios fins, possivelmente como um ponto estratégico ou um depósito de recursos. O 'bombardeio' será uma demonstração de força para forçar a rendição, seguido por uma ocupação.",
        "a_expectativa": "A cidade será bombardeada e destruída para aniquilar a resistência.",
        "a_camuflagem": "A mensagem 'a cidade será bombardeada' é uma ameaça, mas o contexto e a tecnologia de 'frequência fantasma' sugerem um ataque que pode ter objetivos mais sutis do que a mera aniquilação.",
        "o_gatilho": "Interceptar comunicações adicionais ou relatórios de reconhecimento que mencionem 'ocupação' ou 'recursos' em vez de 'terra arrasada', ou analisar a trajetória planejada dos 'bombardeios' que parecem contornar certas áreas de importância estratégica.",
        "a_revelacao": "A intenção não é destruir a cidade, mas sim subjugá-la e tomá-la, transformando seu valor tático em um prêmio para a facção invasora.",
        "id": 3
      }
    ],
    "justificativa": "A matriz oferece pontos de clareza graduais, começando com a natureza técnica estranha da transmissão, progredindo para a revelação da verdadeira natureza dos 'invasores' e, finalmente, o motivo por trás da ameaça de 'bombardeio', tudo cuidadosamente camuflado em elementos do cenário Dieselpunk."
  }
}
```
