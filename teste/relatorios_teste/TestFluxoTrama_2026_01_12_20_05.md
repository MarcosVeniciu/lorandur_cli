# Relatório: Teste de Unidade: Trama Generator (V4.0 - Schema Strict)
**Data:** 2026_01_12_20_05 | **Status:** ✅ Sucesso

## 📊 Métricas de Execução

| Métrica | 1. Core Trama Generator | Total |
| :--- | :--- | :--- |
| **Tempo Total** | 33.31s | **33.31s** |
| **Tokens Entrada** | 875 | **875** |
| **Tokens Saída** | 5225 | **5225** |
| **Tokens Total** | 6100 | **6100** |
| **Custo Estimado** | $0.002177 | **$0.002177** |

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
      "Mistério",
      "Suspense",
      "Espionagem"
    ],
    "escopo": "Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.",
    "justificativa_estilo": "O gênero Dieselpunk, combinado com uma transmissão fantasma e a ameaça iminente de bombardeio, sugere uma atmosfera de suspense agudo, mistério tecnológico e espionagem em tempos de guerra, onde a inovação bélica encontra ruína e paranoia.",
    "justificativa_escopo": "A trama, centrada em decifrar um código para evitar o bombardeio de uma cidade, se encaixa perfeitamente em um escopo local, onde os personagens precisam defender um único assentamento ou base contra uma ameaça existencial."
  },
  "argumento": {
    "texto": "Em um mundo Dieselpunk devastado pela guerra que assola os céus e a terra, 'A Aberrações de Ferro', uma cidade fortificada construída em torno de uma instalação vital de radar e comunicações, capta uma estranha transmissão fantasma. Esta transmissão, repleta de dados criptografados, surge em meio à iminência de um ataque aéreo maciço do expansionista Regime Sulfúrico. A verdade é que a transmissão é uma armadilha elaborada e cruel: um sinal de socorro genuíno de uma unidade de reconhecimento amiga perdida, contendo inteligência essencial sobre a nova e devastadora tática de bombardeio inimiga. No entanto, o Regime Sulfúrico obteve controle sobre os receptores de comunicação da cidade, redirecionando o sinal para uma estação de decodificação interna comprometida. O inimigo planeja explorar o pânico e a distração gerados pela tentativa de decifração, usando-a para lançar seu ataque principal contra os pontos mais vulneráveis da cidade, explorando assim a confusão e as defesas desviadas. Quem está por trás do redirecionamento interno e como os jogadores podem desmantelar essa teia de sabotagem tecnológica e guerra psicológica é o cerne do conflito.",
    "justificativa": "Este argumento estabelece o 'Quem' (jogadores, Reconhecimento perdido, Regime Sulfúrico, agente interno), o 'Onde' (A Aberrações de Ferro), o 'Quando' (agora, sob iminência de ataque), e o 'Porquê' (o inimigo arma uma armadilha explorando a urgência e vulnerabilidade da cidade). O 'Como' é a manipulação da transmissão para fins de sabotagem e distração."
  },
  "premissas": {
    "evidente": {
      "texto": "\nUm sinal de rádio anômalo, uma 'transmissão fantasma' com dados criptografados, foi captado pelas defesas de Aberrações de Ferro. Com o inimigo prestes a lançar um ataque devastador, os jogadores são encarregados de decifrar o código contido nessa transmissão o mais rápido possível. As informações podem ser a chave para se defender ou a confirmação de uma ameaça desconhecida. A prioridade é garantir a segurança da cidade contra o ataque iminente.",
      "funcao": "Estabelecer a urgência e a missão inicial, focando na ameaça externa e na tarefa de decodificação como solução."
    },
    "oculta": {
      "texto": "A transmissão fantasma é uma simulação de armadilha orquestrada pelo inimigo. O sinal de socorro original de uma unidade amiga foi interceptado e modificado. O código resultante visa consumir os recursos da cidade em sua decifração, enquanto a verdadeira inteligência vital para a defesa está escondida em metadados 'corrompidos' ou em fragmentos descartados como ruído. A decifração completa servirá como um gatilho, sinalizando que a cidade está vulnerável e pronta para ser esmagada ou desarmada por uma força interna que facilita o ataque.",
      "funcao": "Desafiar a percepção dos jogadores sobre a natureza da ameaça, introduzindo elementos de sabotagem interna e guerra psicológica, revelando que a solução aparente é, na verdade, parte do problema."
    },
    "justificativa": "As premissas criam um contraste direto entre a percepção inicial dos jogadores e a dura realidade, promovendo o mistério e a necessidade de investigação aprofundada para superar a armadilha."
  },
  "matriz_controle_informacao": {
    "itens": [
      {
        "id": 1,
        "titulo": "A Natureza da Transmissão Fantasma",
        "a_verdade": "A transmissão é um sinal de socorro genuíno de uma unidade de reconhecimento amiga caída, desesperadamente tentando enviar dados sobre a nova arma de bombardeio do Regime Sulfúrico. No entanto, o sinal foi interceptado e tendo seus destinos de recepção comprometidos por agentes inimigos dentro da cidade.",
        "a_expectativa": "Os jogadores podem acreditar que é um sinal alienígena, uma anomalia paranormal, uma falha de equipamento militar, ou uma nova forma de comunicação secreta inimiga. A ideia de um pedido de socorro amigo perdido pode não ser a primeira a vir à mente.",
        "a_camuflagem": "O sinal é intermitente, contaminado por estática e ruído espectral. Fragmentos de voz distorcidos e dados corrompidos são difíceis de discernir, levando os técnicos a focar nos padrões de código mais claros, mas inúteis.",
        "o_gatilho": "Análise forense detalhada da transmissão, uso de filtros de áudio avançados, ou a descoberta de vestígios de manipulação de frequência detectados por um técnico leal.",
        "a_revelacao": "Os jogadores recuperam trechos claros da voz de um piloto relatando um ataque de 'Armas Sônicas Devastadoras' e as coordenadas do ataque primário, revelando que a transmissão foi adulterada para fins de engano."
      },
      {
        "id": 2,
        "titulo": "O Código: Isca ou Chave?",
        "a_verdade": "O código decifrado é deliberadamente projetado para ser enganoso e consumir tempo. Ele pode conter informações redundantes, falsas instruções de defesa, ou um sinal de ativação para desativar uma contramedida aliada vital, tornando a cidade mais vulnerável. A inteligência real está fragmentada em dados 'corrompidos' que foram descartados.",
        "a_expectativa": "Espera-se que decifrar o código revele a estratégia do inimigo, forneça coordenadas de ataque diretas, ou contenha um plano de contingência para a própria cidade. A decifração é vista como a solução primária.",
        "a_camuflagem": "O código principal, embora complexo, é apresentado de forma coerente e 'lógica' pelos sistemas de decodificação, enquanto os dados 'corrompidos' que contêm a verdade são rotulados como perda de pacote ou falha na transmissão, sendo fáceis de ignorar.",
        "o_gatilho": "Investigação dos dados marginais e metadados da transmissão, desconfiança sobre a facilidade/complexidade do código decifrado em comparação com a ameaça iminente, ou a análise comparativa com logs de comunicação da unidade perdida.",
        "a_revelacao": "Os fragmentos de 'ruído' revelam que o código é uma fachada. A verdadeira inteligência informa que o ataque real não é a invasão aérea esperada, mas uma infiltração subterrânea em um ponto específico, ou o uso de uma arma não convencional que anula as defesas aéreas."
      },
      {
        "id": 3,
        "titulo": "O Agente do Regime dentro de Casa",
        "a_verdade": "Um agente do Regime Sulfúrico está infiltrado em 'A Aberrações de Ferro' e foi o responsável por facilitar a interceptação da transmissão amiga e seu redirecionamento para a estação comprometida. Este agente pode ter a tarefa de sabotar sistemas críticos ou de ativar uma ameaça interna assim que o ataque principal começar.",
        "a_expectativa": "A ameaça é puramente externa, vinda do ar. A inteligência e sabotagem são operações de espionagem inimigas convencionais, sem qualquer componente interno significativo além de colaboradores ocasionais.",
        "a_camuflagem": "O agente age através de sutileza: pode ser um técnico de comunicação que 'assiste' de forma excessiva, um oficial de logística que pressiona por recursos em locais específicos (mas errados), ou um funcionário de infraestrutura cujas 'manutenções' criam falhas suspeitas que são atribuídas ao estresse da guerra ou sabotagem inimiga genérica.",
        "o_gatilho": "Investigação de falhas técnicas anômalas que não fazem sentido militar, rastreamento de comunicações internas suspeitas, ou exposição de um padrão de desinformação sendo consistentemente propagado por uma figura chave.",
        "a_revelacao": "O agente sabotador é identificado e confrontado. Sua confissão ou os documentos encontrados em sua posse revelam detalhes cruciais sobre como desativar uma bomba interna, neutralizar uma arma biológica/sônica que ele foi encarregado de implantar, ou fornecer o código de acesso para contramedidas contra o ataque inimigo."
      }
    ],
    "justificativa": "Esses itens de controle de informação cobrem os principais pontos de mistério da aventura: a verdadeira origem e propósito da transmissão, a natureza da armadilha do código, e a presença de um elemento traidor interno, cada um com camadas de expectativa e realidade para os jogadores desvendarem."
  }
}
```
