# Relatório de Teste: Pipeline Trama + Frente
**Data:** 2026_01_09_01_31
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
      "Noir",
      "Ação Frenética"
    ],
    "escopo_selecionado": "Nível 2 (Escopo Local - O Refúgio)",
    "justificativa_escopo": "A trama de roubo e a ameaça iminente de guerra entre gangues ocorrem em um cenário local concentrado (um distrito industrial, portuário ou base secreta), onde a recuperação rápida e a contenção do conflito são cruciais. O foco é na ação e investigação imediata dentro de um perímetro definido, em vez de uma jornada.",
    "justificativa_estilo": "A combinação de roubo de carga valiosa, a corrida contra o tempo ('antes do amanhecer') e a consequência de uma guerra entre gangues evoca um clima de 'Noir' urbano e de suspense. O cenário Dieselpunk adiciona elementos de tecnologia de época, conspiração industrial e uma atmosfera tensa, justificando 'Ação Frenética' como subgênero."
  },
  "argumento": {
    "texto": "Em um distrito portuário em ruínas de uma metrópole Dieselpunk, ao apagar das luzes da madrugada, uma carga experimental de 'Éter Instável' — um combustível de alta potência e perigoso, essencial para a maquinaria de guerra mais avançada — foi roubada de um comboio fortemente guardado. A verdade oculta é que a carga foi roubada por mercenários contratados por Silas Vane, o supervisor da instalação de onde a carga deveria ser transportada. Vane orquestrou o roubo-falso para criar um pretexto para uma guerra contra a Viper Syndicate, uma gangue rival que controla pontos de distribuição vital. Se a carga não for recuperada e parecer que uma gangue a possui (ou que a Viper Syndicate a roubou), a guerra total explodirá às primeiras luzes do dia, devastando a área e permitindo que Vane expanda seu império após o caos. Os jogadores são contratados pelo suposto \"dono\" da carga (um intermediário de Vane) para recuperá-la, com a promessa de uma fortuna, mas sem saber que estão sendo manipulados para iniciar uma guerra.",
    "justificativa": "O argumento define o 'Onde' (distrito portuário Dieselpunk), 'Quando' (ao amanhecer), 'Quem' (Silas Vane, mercenários, gangues rivais, intermediário, jogadores) e 'Por quê' (Vane quer iniciar uma guerra para expandir seu império). O 'Como' é implícito na sofisticação do roubo e na manipulação."
  },
  "premissas": {
    "evidente": {
      "texto": "Os jogadores são contratados para recuperar uma 'carga valiosa' roubada — componentes cruciais para motores de aeronaves — de criminosos desconhecidos. O cliente alerta que se a carga cair em mãos erradas, especialmente das gangues rivais que controlam o submundo da cidade, um conflito aberto e devastador eclodirá antes do amanhecer. A missão é recuperar a carga a qualquer custo e manter a paz precária da metrópole.",
      "funcao": "Estabelecer a urgência, o objetivo claro dos jogadores e o conflito iminente, direcionando-os para a caça aos ladrões e a recuperação da carga."
    },
    "oculta": {
      "texto": "O roubo da carga não foi obra de uma gangue rival, mas sim uma operação orquestrada pelo próprio cliente (através de Silas Vane) para incriminar uma gangue específica e desencadear uma guerra. A verdadeira motivação é o controle territorial e o poder gerado pelo caos pós-guerra. Os jogadores são peões inocentes em um jogo de poder, cujas ações de 'recuperação' podem na verdade facilitar o plano de Vane ou colocá-los no centro de uma guerra orquestrada.",
      "funcao": "Revelar a verdadeira natureza da trama, a manipulação dos jogadores e o objetivo sombrio do principal antagonista, transformando uma simples missão de recuperação em um dilema moral e estratégico."
    },
    "justificativa": "As premissas criam um 'gancho' imediato para os jogadores (Premissa Evidente) e uma reviravolta surpreendente que muda radicalmente o contexto da aventura e as motivações percebidas (Premissa Oculta), servindo como o 'Twist' principal."
  },
  "matriz_controle_informacao": {
    "itens": [
      {
        "titulo": "A Verdadeira Natureza da Carga",
        "a_verdade": "O 'Éter Instável' não é apenas um combustível valioso, mas uma substância altamente volátil e perigosa que pode causar explosões em cascata ou emitir radiação nociva se manuseada incorretamente ou armazenada por muito tempo.",
        "a_expectativa": "Um componente tecnológico de alto valor, sem riscos inerentes à sua natureza, apenas controverso por seu uso em maquinário de guerra.",
        "a_camuflagem": "A carga está em contêineres blindados e selados, com rótulos genéricos de 'Material Perigoso' e 'Alto Valor'. Os mercenários que a roubaram parecem ser profissionais disciplinados, não saboteiros imprudentes.",
        "o_gatilho": "Inspecionar um dos contêineres que vazou ou entrou em contato com o ambiente, ou obter um manifesto detalhado de transporte/segurança.",
        "a_revelacao": "As leituras de nível de radiação ou instabilidade aumentam dramaticamente perto do contêiner, ou um registro de segurança detalha procedimentos de manuseio de risco extremo e protocolos de contenção nuclear.",
        "id": 1
      },
      {
        "titulo": "O Verdadeiro Culpado do Roubo",
        "a_verdade": "A gangue Viper Syndicate, que o cliente indicou como provável culpada, é inocente do roubo. Os verdadeiros ladrões foram mercenários contratados diretamente por Silas Vane, que plantaram pistas falsas para culpar a Viper Syndicate como parte de seu plano.",
        "a_expectativa": "A Viper Syndicate é a responsável pelo roubo, agindo para desestabilizar o cliente ou obter lucro.",
        "a_camuflagem": "Várias peças de 'evidência' — como um uniforme parcial de gangue de baixo escalão encontrado perto do local ou um informante 'confiável' que aponta para a Viper Syndicate — foram plantadas para incriminar a gangue.",
        "o_gatilho": "Interceptar uma comunicação entre os mercenários e o intermediário de Vane, ou interrogar um dos 'ladrões' capturados que revela quem os contratou.",
        "a_revelacao": "O mercenário capturado (ou a comunicação interceptada) descreve um contrato pago por um homem de terno de uma corporação com laços obscuros, não por líderes da Viper Syndicate. A investigação aponta para atividades de mercenários com modus operandi diferente das táticas conhecidas da gangue.",
        "id": 2
      },
      {
        "titulo": "O Jogo de Poder de Silas Vane",
        "a_verdade": "Silas Vane, o supervisor da instalação de onde a carga foi roubada e um membro de alta patente do conselho corporativo (ou similar), orquestrou o roubo. Seu objetivo é usar o 'Éter Instável' (ou a guerra resultante de sua falta/acusações) como catalisador para eliminar rivais corporativos e gangues, consolidando seu próprio poder e controle sobre os recursos energéticos da cidade.",
        "a_expectativa": "O cliente é uma vítima honesta tentando recuperar uma propriedade legítima para evitar um conflito induzido pelas gangues rivais.",
        "a_camuflagem": "O intermediário que contrata os jogadores parece genuinamente preocupado e generoso com a recompensa. Detalhes sobre a logística do roubo ou o paradeiro exato da carga são propositalmente vagos por parte do cliente.",
        "o_gatilho": "Descobrir comunicações codificadas entre Silas Vane e seu intermediário, ou encontrar registros financeiros que mostram pagamentos substanciais para mercenários e desvio de fundos de segurança.",
        "a_revelacao": "As comunicações revelam o plano mestre de Vane, detalhando como ele 'cultivou' a ameaça da Viper Syndicate e como a recuperação da carga (ou a guerra) servirá para expurgar concorrentes e afirmar seu domínio sobre a infraestrutura de energia da cidade.",
        "id": 3
      }
    ],
    "justificativa": "Os três itens da matriz de controle de informação são projetados para gradualmente subverter as expectativas dos jogadores. O primeiro revela a periculosidade da carga, aumentando a urgência. O segundo muda o alvo da investigação, mostrando que a culpa foi atribuída a inocentes. O terceiro expõe o verdadeiro manipulador e seu plano nefasto, transformando a missão em um conflito de interesses e moralidade."
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
Sua tarefa é criar uma "Frente de Aventura" (nível de sessão/episódio) baseada em uma Trama e Matriz de Informação pré-existentes. Você deve transformar conceitos abstratos em elementos jogáveis (locais, NPCs, perigos e cenas).

# Instruções de Processamento

1. **Análise de Contexto e Arquétipo:**
   - Analise o `genero_principal`, `subgeneros` e o `argumento` da trama.
   - Escolha UM dos 7 Arquétipos de Enredo abaixo para servir de espinha dorsal narrativa. Utilize a **Meta-Estrutura** do arquétipo escolhido para definir o tom dos Presságios:

     * **Superar o Monstro:** Foco em heroísmo e sobrevivência contra uma ameaça colossal.
         * *Meta-Estrutura:* 1. Antecipação/Chamado -> 2. Fase do Sonho (Preparação) -> 3. A Frustração -> 4. O Pesadelo -> 5. Fuga da Morte/Vitória.
     * **Da Miséria à Riqueza (Do Pano para a Manga):** Foco em crescimento pessoal e ascensão de status a partir do nada.
         * *Meta-Estrutura:* 1. Miséria Inicial -> 2. Sucesso Inicial -> 3. A Crise Central (Tudo dá errado) -> 4. Independência/Provação -> 5. Completude.
     * **A Busca:** Foco na viagem e trabalho em equipe para recuperar algo essencial.
         * *Meta-Estrutura:* 1. O Chamado -> 2. A Jornada -> 3. Chegada e Frustração (Barreira) -> 4. Provações Finais -> 5. O Objetivo.
     * **Viagem e Retorno:** Foco em exploração de um mundo estranho e a necessidade de escapar dele.
         * *Meta-Estrutura:* 1. Queda no Outro Mundo -> 2. Fascínio (Lua de Mel) -> 3. A Frustração (Regras Opressoras) -> 4. O Pesadelo (Sombra Hostil) -> 5. Fuga e Retorno.
     * **Renascimento:** Foco em redenção e libertação de uma maldição ou influência sombria.
         * *Meta-Estrutura:* 1. Queda sob a Sombra -> 2. Fase do Sonho (O Poder da Sombra) -> 3. A Frustração (Prisão) -> 4. O Pesadelo (Fundo do Poço) -> 5. O Renascimento.
     * **Tragédia:** Foco na consequência moral de buscar objetivos por meios proibidos.
         * *Meta-Estrutura:* 1. Tentação -> 2. Fase do Sonho (O Crime Compensa) -> 3. A Frustração (Consequências) -> 4. O Pesadelo (Perda de Controle) -> 5. Destruição.
     * **Comédia:** Foco em confusão, mal-entendidos e intriga social que caminham para a clareza.
         * *Meta-Estrutura:* 1. Sombra da Confusão -> 2. O Nó se Aperta -> 3. Clímax da Confusão (Caos Total) -> 4. A Revelação (Verdade) -> 5. Resolução/Festa.

2. **Instanciação de Locais (Location Pool):**
   - Utilize a lista de `tipos_locais_permitidos` e o `escopo_selecionado`.
   - Crie nomes específicos e evocativos para 8 locais. NÃO use nomes genéricos (ex: em vez de "Hospital", use "Sanatório São Lázaro").
   - Distribuição Obrigatória:
     - 1 Local Inicial (Onde a aventura começa).
     - 4 Locais Intermediários (Investigação e desenvolvimento).
     - 3 Locais de Clímax (Onde o Desastre pode ocorrer).

3. **Criação do Elenco e Perigos:**
   - Utilize a lista de `arquetipos_personagens_permitidos` para povoar o mundo.
   - **Elenco:** Crie nomes para NPCs ou organizações relevantes citados no Argumento.
   - **Perigos:** Defina 2 ou 3 ameaças ativas. Cada perigo deve ter um Nome, um Tipo (ex: Horda, Assassino, Arcano) e um Impulso detalhado (O que ele quer fazer? ex: "Destruir", "Corromper").

4. **Definição do Desastre Iminente:**
   - O que acontece se os jogadores falharem completamente? Defina o "Game Over" narrativo baseando-se na consequência da trama original.

5. **Construção dos Presságios Terríveis:**
   - Crie uma cadeia cronológica de **5** eventos (Presságios) que indicam o avanço do Desastre.
   - Para CADA Presságio:
     - **Meta-Estrutura:** Selecione um estágio dramático adequado ao momento da aventura, usando a lista do Arquétipo de Enredo escolhido no passo 1 (ex: se for "Superar o Monstro", use "A Frustração" ou "O Pesadelo").
     - **Local:** Escolha um da sua `lista_locais`, podendo repetir o local.
     - **Camada de Informação (CRÍTICO):** Você DEVE conectar este presságio a um dos itens da `matriz_controle_informacao` fornecida no input. O presságio deve servir de veículo para entregar uma pista sobre a "Verdade" daquele item da matriz.
     - **Argumento da Cena:** É o resumo da 'Verdade do Mestre'. Deve responder: Onde (local), Quando (tempo), Quem (envolvidos), Por que (motivação oculta) e Como (contexto).
     - **Defina as Premissas:**
       - *Premissa Evidente (O Briefing):* A 'falsa verdade' ou missão superficial entregue aos jogadores no início.
       - *Premissa Oculta (O Twist):* Os segredos do Argumento. A revelação que subverte a missão.

6. **Perguntas Dramáticas:**
   - Formule 3 perguntas abertas sobre o destino dos personagens ou do cenário que você, como Mestre, quer ver respondidas ao jogar.

# Formato de Saída
Gere a resposta EXCLUSIVAMENTE em formato JSON seguindo o schema estrito abaixo.
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
Em um distrito portuário em ruínas de uma metrópole Dieselpunk, ao apagar das luzes da madrugada, uma carga experimental de 'Éter Instável' — um combustível de alta potência e perigoso, essencial para a maquinaria de guerra mais avançada — foi roubada de um comboio fortemente guardado. A verdade oculta é que a carga foi roubada por mercenários contratados por Silas Vane, o supervisor da instalação de onde a carga deveria ser transportada. Vane orquestrou o roubo-falso para criar um pretexto para uma guerra contra a Viper Syndicate, uma gangue rival que controla pontos de distribuição vital. Se a carga não for recuperada e parecer que uma gangue a possui (ou que a Viper Syndicate a roubou), a guerra total explodirá às primeiras luzes do dia, devastando a área e permitindo que Vane expanda seu império após o caos. Os jogadores são contratados pelo suposto "dono" da carga (um intermediário de Vane) para recuperá-la, com a promessa de uma fortuna, mas sem saber que estão sendo manipulados para iniciar uma guerra.

3. **Matriz de Mistérios:**
- **MISTÉRIO: A Verdadeira Natureza da Carga**
  > *Expectativa:* Um componente tecnológico de alto valor, sem riscos inerentes à sua natureza, apenas controverso por seu uso em maquinário de guerra.
  > *A Verdade:* O 'Éter Instável' não é apenas um combustível valioso, mas uma substância altamente volátil e perigosa que pode causar explosões em cascata ou emitir radiação nociva se manuseada incorretamente ou armazenada por muito tempo.
  > *Gatilho:* Inspecionar um dos contêineres que vazou ou entrou em contato com o ambiente, ou obter um manifesto detalhado de transporte/segurança.
  > *Revelação:* As leituras de nível de radiação ou instabilidade aumentam dramaticamente perto do contêiner, ou um registro de segurança detalha procedimentos de manuseio de risco extremo e protocolos de contenção nuclear.

- **MISTÉRIO: O Verdadeiro Culpado do Roubo**
  > *Expectativa:* A Viper Syndicate é a responsável pelo roubo, agindo para desestabilizar o cliente ou obter lucro.
  > *A Verdade:* A gangue Viper Syndicate, que o cliente indicou como provável culpada, é inocente do roubo. Os verdadeiros ladrões foram mercenários contratados diretamente por Silas Vane, que plantaram pistas falsas para culpar a Viper Syndicate como parte de seu plano.
  > *Gatilho:* Interceptar uma comunicação entre os mercenários e o intermediário de Vane, ou interrogar um dos 'ladrões' capturados que revela quem os contratou.
  > *Revelação:* O mercenário capturado (ou a comunicação interceptada) descreve um contrato pago por um homem de terno de uma corporação com laços obscuros, não por líderes da Viper Syndicate. A investigação aponta para atividades de mercenários com modus operandi diferente das táticas conhecidas da gangue.

- **MISTÉRIO: O Jogo de Poder de Silas Vane**
  > *Expectativa:* O cliente é uma vítima honesta tentando recuperar uma propriedade legítima para evitar um conflito induzido pelas gangues rivais.
  > *A Verdade:* Silas Vane, o supervisor da instalação de onde a carga foi roubada e um membro de alta patente do conselho corporativo (ou similar), orquestrou o roubo. Seu objetivo é usar o 'Éter Instável' (ou a guerra resultante de sua falta/acusações) como catalisador para eliminar rivais corporativos e gangues, consolidando seu próprio poder e controle sobre os recursos energéticos da cidade.
  > *Gatilho:* Descobrir comunicações codificadas entre Silas Vane e seu intermediário, ou encontrar registros financeiros que mostram pagamentos substanciais para mercenários e desvio de fundos de segurança.
  > *Revelação:* As comunicações revelam o plano mestre de Vane, detalhando como ele 'cultivou' a ameaça da Viper Syndicate e como a recuperação da carga (ou a guerra) servirá para expurgar concorrentes e afirmar seu domínio sobre a infraestrutura de energia da cidade.



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
  "cabecalho_arquetipo": "Tragédia",
  "cabecalho_foco": "Dieselpunk - Manipulação e Guerra",
  "locais_iniciais": [
    "Beco da Ferrugem"
  ],
  "locais_investigacao": [
    "Oficinas Silenciosas de Vane",
    "Mercado das Entranhas",
    "Depósitos Esquecidos da Doca 7",
    "Cantina da Ruína Crescente"
  ],
  "locais_climax": [
    "Coração da Doca Negra",
    "Complexo de Silas Vane",
    "Território da Víbora"
  ],
  "elenco_npcs": [
    "Silas Vane",
    "Intermediário de Vane",
    "Líderes da Viper Syndicate",
    "Mercenários de Vane"
  ],
  "perigos": [
    {
      "nome": "Mercenários de Vane",
      "tipo": "Assassinos Contratados",
      "impulso": "Silenciar testemunhas e assegurar a carga"
    },
    {
      "nome": "Gangue Viper Syndicate",
      "tipo": "Organização Criminosa",
      "impulso": "Defender seu território e retaliar contra acusações falsas"
    },
    {
      "nome": "Éter Instável",
      "tipo": "Substância Perigosa",
      "impulso": "Explodir/Irradiar se manipulado incorretamente"
    }
  ],
  "desastre_tipo": "Guerra Total Dieselpunk",
  "desastre_descricao": "Uma guerra total irrompe entre as facções, devastando o distrito portuário, a cidade e consolidando o poder de Silas Vane em meio ao caos, assumindo controle sobre os recursos energéticos. A área se torna uma zona de conflito radioativo ou explosivo.",
  "pressagios": [
    {
      "ordem": 1,
      "meta_estrutura": "Tentação",
      "local": "Beco da Ferrugem",
      "descricao_evento": "O intermediário de Vane contrata os jogadores para recuperar uma carga experimental roubada, atribuindo a culpa à Viper Syndicate e prometendo uma fortuna, ocultando a verdadeira natureza do roubo e do material.",
      "argumento_cena": "No Beco da Ferrugem, à luz fraca de lâmpadas a óleo instáveis, o intermediário de Vane (vestido discretamente) se encontra com os jogadores. Ele apresenta o roubo como um ataque direto à ordem e à estabilidade, atribuindo-o à Viper Syndicate. Sua motivação aparente é a recuperação de uma propriedade valiosa para evitar um colapso. Ele manipula os jogadores por meio da ganância e de um senso de dever em restaurar a 'ordem'.",
      "premissa_evidente": "Uma carga de combustível experimental foi roubada por gangues rivais, e os jogadores são contratados para recuperá-la antes que uma guerra civil se inicie.",
      "premissa_oculta": "O roubo foi uma farsa orquestrada por Silas Vane, e os jogadores são peões para criar um pretexto para a guerra, permitindo que Vane expanda seu poder.",
      "pista_tipo": "Apresentação da Missão e Antecipação do Conflito",
      "pista_conexao": "Argumento Geral / O Jogo de Poder de Silas Vane"
    },
    {
      "ordem": 2,
      "meta_estrutura": "Fase do Sonho (O Crime Compensa)",
      "local": "Mercado das Entranhas",
      "descricao_evento": "Investigando no Mercado das Entranhas, os jogadores encontram uma pista plantada por Vane (como um símbolo da Viper Syndicate) que os leva a acreditar que a gangue é a única responsável pelo roubo.",
      "argumento_cena": "Em um mercado clandestino labiríntico e barulhento, um informante assustado vende aos jogadores uma 'informação quente': um fragmento de tecido com o emblema da Viper Syndicate encontrado perto de uma rota de fuga alternativa da carga. Ele afirma ter visto membros da gangue agindo de forma suspeita na área na noite do roubo. O informante foi subornado por Vane ou seus mercenários para plantar esta pista falsa.",
      "premissa_evidente": "A gangue Viper Syndicate é diretamente responsável pelo roubo da carga experimental.",
      "premissa_oculta": "A pista é uma armadilha para incriminar a Viper Syndicate; eles são inocentes do roubo enquanto mercenários de Vane o realizaram.",
      "pista_tipo": "Culpa Fabricada da Viper Syndicate",
      "pista_conexao": "O Verdadeiro Culpado do Roubo"
    },
    {
      "ordem": 3,
      "meta_estrutura": "A Frustração (Consequências)",
      "local": "Depósitos Esquecidos da Doca 7",
      "descricao_evento": "Ao inspecionar a área ou um dos mercenários 'descartados', os jogadores descobrem que o modus operandi não condiz com a Viper Syndicate e que a carga é mais perigosa do que foi dito.",
      "argumento_cena": "Em meio a contêineres enferrujados e abandonados nos Depósitos Esquecidos, os jogadores encontram um dos contêineres da carga. Uma fenda expõe um pouco do 'Éter Instável', emitindo um brilho fraco e não natural, e leituras de instrumentos improvisados (se os tiverem) indicam anormalidades. Alternativamente, um mercenário fugitivo ou ferido é encontrado perto de uma rota de fuga secundária, e suas confissões, sob coerção, revelam que foram contratados por 'homens de terno de uma corporação' e não por conhecidos membros da Viper Syndicate. Ele pode mencionar o nome 'Vane' ou 'supervisor'.",
      "premissa_evidente": "O roubo é mais complexo do que parecia; talvez a Viper Syndicate não seja a única parte envolvida, e a carga pode apresentar perigos desconhecidos.",
      "premissa_oculta": "Os mercenários foram contratados por Silas Vane, e o 'Éter Instável' é uma substância perigosamente volátil e radioativa, não apenas um combustível.",
      "pista_tipo": "Contradição e Perigo Emergente",
      "pista_conexao": "O Verdadeiro Culpado do Roubo / A Verdadeira Natureza da Carga"
    },
    {
      "ordem": 4,
      "meta_estrutura": "O Pesadelo (Perda de Controle)",
      "local": "Complexo de Silas Vane",
      "descricao_evento": "Acesso a comunicações ou registros no complexo de Vane revela seu plano mestre para orquestrar uma guerra e consolidar seu poder.",
      "argumento_cena": "Acesso a terminais de dados criptografados, arquivos secretos ou conversas interceptadas dentro do Complexo de Silas Vane revelam o plano mestre. Vane descreve como ele manipulou os suprimentos de combustível, orquestrou o 'roubo-falso' e pretende culpar a Viper Syndicate. Os registros mostram pagamentos secretos a mercenários e planos para usar o caos pós-guerra para eliminá-lo da concorrência e assumir o controle da infraestrutura energética.",
      "premissa_evidente": "Silas Vane está envolvido em uma conspiração de maior escala, usando o roubo como catalisador para uma guerra que ele pretende explorar para consolidar seu poder e eliminar rivais.",
      "premissa_oculta": "Silas Vane orquestrou o roubo para iniciar uma guerra e alavancar seu próprio poder, usando a Viper Syndicate como bode expiatório, e planeja dominar os recursos energéticos da cidade por meio de manipulação e conflito.",
      "pista_tipo": "Revelação do Arquétipo do Vilão e seu Plano Mestre",
      "pista_conexao": "O Jogo de Poder de Silas Vane"
    },
    {
      "ordem": 5,
      "meta_estrutura": "Destruição",
      "local": "Coração da Doca Negra",
      "descricao_evento": "No local do roubo, o Éter Instável se torna perigosamente instável, enquanto forças armadas se preparam para o confronto, anunciando a catástrofe.",
      "argumento_cena": "No Coração da Doca Negra, o local original do roubo, um dos contêineres de Éter Instável começa a vazar em massa, emanando uma radiação perigosa ou instabilidade que faz estruturas próximas tremerem. O ar fica pesado, a energia é palpável. Simultaneamente, as forças de Vane e da Viper Syndicate começam a se armar em pontos estratégicos, prontas para o confronto. A área está à beira de uma devastação explosiva/radioativa, com os jogadores no epicentro.",
      "premissa_evidente": "A carga é extremamente perigosa e está instável, e a guerra está prestes a acontecer, resultando em destruição massiva para o distrito portuário.",
      "premissa_oculta": "A instabilidade do Éter e a guerra de Vane são duas caras da mesma moeda catastrófica, que ele pretende dominar; a recuperação agora é sobre salvar a todos da aniquilação, não apenas cumprir um contrato.",
      "pista_tipo": "Catástrofe Iminente e Conflito Armado",
      "pista_conexao": "A Verdadeira Natureza da Carga / O Jogo de Poder de Silas Vane"
    }
  ],
  "perguntas_dramatica": [
    "Como os jogadores lidarão com a revelação de que foram manipulados para iniciar uma guerra?",
    "Serão capazes de desarmar a trama de Silas Vane e expor sua culpa antes que o conflito cause devastação total?",
    "Eles conseguirão conter a natureza volátil do 'Éter Instável' antes que ele se torne uma catástrofe em si mesma?"
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
| **Tempo Total** | 15.28s | 51.85s | 67.12s |
| **Tokens Entrada** | 841 | 2620 | 3461 |
| **Tokens Saída** | 4407 | 8829 | 13236 |
| **Tokens Total** | 5248 | 11449 | 16697 |
| **Custo Estimado** | $0.001847 | $0.003794 | $0.005641 |
