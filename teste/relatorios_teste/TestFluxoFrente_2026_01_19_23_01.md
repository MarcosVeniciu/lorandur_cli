# Relatório: Teste Completo: Frente Pipeline (Com Trama)
**Data:** 2026_01_19_23_01 | **Status:** ✅ Sucesso

## 📊 Métricas de Execução

| Métrica | 1. Trama (Contexto) | 2. Front Archetype | 3. Front World | 4. Front Story | Total |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tempo Total** | 9.28s | 10.59s | 7.33s | 14.07s | **41.27s** |
| **Tokens Entrada** | 877 | 3053 | 4094 | 7574 | **15598** |
| **Tokens Saída** | 2018 | 2307 | 1672 | 3328 | **9325** |
| **Tokens Total** | 2895 | 5360 | 5766 | 10902 | **24923** |
| **Custo Estimado** | $0.000895 | $0.001228 | $0.001078 | $0.002089 | **$0.005290** |

---

## 1. 1. Trama (Contexto) (Módulo: `core_trama_generator`)
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
      "Drama de Baixo Nível"
    ],
    "escopo": "Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.",
    "justificativa_escopo": "Este escopo é ideal, pois a trama gira em torno de uma carga roubada dentro de um local contido, com a ameaça imediata de conflito aberto entre gangues. Um assentamento isolado ou base se encaixa perfeitamente, permitindo um foco em intriga local e nas consequências diretas do roubo, sem a necessidade de uma viagem extensa.",
    "justificativa_estilo": "A combinação de roubo, prazo apertado (antes do amanhecer) e a consequência de guerra entre gangues sugere uma atmosfera Noir, repleta de investigação, traições e um senso de urgência. A ação frenética se encaixa na necessidade de recuperação rápida, e o drama de baixo nível surge das motivações e rivalidades dentro do assentamento. O cenário Dieselpunk adiciona um toque de tecnologia retrofuturista à mistura."
  },
  "argumento": {
    "texto": "Em uma cidade portuária sombria e industrial, sob o véu pesado da noite Dieselpunk, uma carga de 'cristais de éter' (combustível de alta octanagem para máquinas de guerra) foi roubada do armazém da gangue 'Os Ferros-Velhos'. A gangue rival, 'A Sombra Metálica', é a principal suspeita. Se a carga não for recuperada antes do amanhecer, a frágil trégua entre as facções será quebrada, mergulhando a cidade em uma guerra aberta e sangrenta. Na verdade, a carga não foi roubada pela Sombra Metálica, mas sim por um membro dissidente dos Ferros-Velhos que busca expor a corrupção interna e o uso indevido dos cristais para projetos militares secretos, armando uma armadilha para incriminar a gangue rival e deflagrar o conflito que ele secretamente deseja.",
    "justificativa": "Define o 'Onde' (cidade portuária sombria e industrial), o 'Quando' (noite, com prazo para o amanhecer), o 'O Quê' (carga de cristais de éter roubada) e o 'Por Quê' (motivação para a guerra, mas com uma verdade oculta de traição interna e conspiração). Os 'Quem' são as gangues Ferros-Velhos e Sombra Metálica, além do traidor."
  },
  "premissas": {
    "evidente": {
      "texto": "Vocês são contratados (ou coagidos) pelos Ferros-Velhos para recuperar uma carga valiosa de cristais de éter roubada de seus armazéns. Eles suspeitam que a gangue rival, A Sombra Metálica, é a responsável. Vocês têm até o amanhecer para achar a carga, ou a cidade afundará em uma guerra sangrenta entre as gangues.",
      "funcao": "Estabelece a missão imediata, define o prazo, o inimigo aparente e a consequência direta, criando um senso de urgência e um alvo claro para os jogadores."
    },
    "oculta": {
      "texto": "A carga não foi roubada pela Sombra Metálica. Foi roubada por um membro dos próprios Ferros-Velhos, o engenheiro Silas, que planejou o roubo para incriminar a Sombra Metálica e forçar uma guerra. Ele quer usar o caos para expor os planos secretos do líder dos Ferros-Velhos de vender a carga para uma potência estrangeira, ou usá-la em experimentos perigosos.",
      "funcao": "Subverte a narrativa apresentada na premissa evidente, revelando a verdadeira causa do conflito e introduzindo um novo antagonista com motivações complexas, que adiciona camadas à investigação e ao drama."
    },
    "justificativa": "A premissa evidente joga com a suspeita óbvia, direcionando os jogadores contra a gangue rival. A premissa oculta introduz a reviravolta, explicando o roubo de uma perspectiva interna e adicionando complexidade moral e de conspiração ao cenário."
  },
  "matriz_controle_informacao": {
    "itens": [
      {
        "titulo": "A Natureza da Carga",
        "a_verdade": "Os 'cristais de éter' são compostos instáveis, perigosos de manusear e com potencial destrutivo muito maior do que o combustível de guerra declarado. Eles são a base para uma arma experimental secreta.",
        "a_expectativa": "Uma carga valiosa de combustível de alta octanagem, de grande importância estratégica para as gangues.",
        "a_camuflagem": "A carga está em caixas seladas e identificada apenas como 'combustível especial'. A urgência em recuperá-la impede uma análise detalhada. Informes iniciais dos Ferros-Velhos falam apenas do seu valor como 'combustível'.",
        "o_gatilho": "Um acidente envolvendo a carga (vazamento, explosão parcial, aquecimento extremo) ou uma investigação química detalhada após a recuperação.",
        "a_revelacao": "Os jogadores descobrem a verdadeira natureza perigosa e o potencial destrutivo dos cristais, que vão além de simples combustível.",
        "id": 1
      },
      {
        "titulo": "O Verdadeiro Ladrão",
        "a_verdade": "Silas, um engenheiro descontente dos Ferros-Velhos, é o responsável pelo roubo. Ele orquestrou tudo para incriminar a Sombra Metálica e iniciar uma guerra que ele acredita ser necessária para expor os planos mais sombrios de seu próprio líder.",
        "a_expectativa": "A gangue Sombra Metálica é a culpada pelo roubo, agindo por rivalidade e ganância.",
        "a_camuflagem": "Silas é um figura periférica conhecida por sua inteligência e dissidência sutil. Ele não aparece como um antagonista direto, mas suas ações indiretas (alertas falsos, pistas plantadas) confundem a investigação. Os Ferros-Velhos apontam diretamente para a Sombra Metálica.",
        "o_gatilho": "Investigação dos locais de origem e do modus operandi do roubo; interrogatório de membros menores dos Ferros-Velhos que possam ter visto Silas; rastreamento de tecnologia especializada usada no roubo.",
        "a_revelacao": "Os jogadores descobrem que o verdadeiro ladrão é um 'insider' com motivos próprios, e que a Sombra Metálica pode ter sido vítima de uma armação.",
        "id": 2
      },
      {
        "titulo": "A Falsa Guerra",
        "a_verdade": "O líder dos Ferros-Velhos, \"Mandíbula\" Mortem, deseja a guerra não apenas para eliminá-la como rival, mas para encobrir seu próprio tráfico dos cristais de éter para uma potência estrangeira ou para financiar experimentos perigosos em segredo.",
        "a_expectativa": "A guerra entre gangues é uma consequência inevitável do roubo, motivada pela honra, território e pela quebra da trégua.",
        "a_camuflagem": "As declarações inflamadas de \"Mandíbula\" Mortem sobre vingança e a honra da gangue mascaram suas verdadeiras intenções. Os planos de guerra parecem um resultado direto do roubo, sem menção a agendas ocultas para aquisição ilícita.",
        "o_gatilho": "Descobrir comunicações secretas ou transações financeiras dos Ferros-Velhos; interceptar negociações com compradores externos; encontrar evidências de planos de contingência para a \"guerra\" que beneficiam exclusivamente o líder.",
        "a_revelacao": "Os jogadores percebem que a guerra pode ser uma manobra orquestrada por um dos líderes para seu próprio benefício, em vez de uma reação genuína ao roubo.",
        "id": 3
      }
    ],
    "justificativa": "Esta matriz foi projetada para desmantelar as suposições iniciais dos jogadores: a natureza da carga, a identidade do ladrão e a verdadeira motivação para a iminente guerra. Cada item apresenta um enigma onde a 'expectativa' é a pista inicial, e a 'verdade' é descoberta através da investigação, revelando uma camada mais profunda de conspiração e traição no coração do cenário Dieselpunk."
  }
}
```

## 2. 2. Front Archetype (Módulo: `step1_front_archetype`)
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
* **Subgêneros:** Noir, Ação Frenética, Drama de Baixo Nível
* **Escopo Geográfico:** Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.
* **Pool de Tipos de Locais (Inspiração):** Arena de Lutas, Ferro velho, Fila da ração, Armazém de comida, Mercado de pulgas, Bar movimentado, Mansão de um senhor de armas, Festival de Música, Torre de Vigia, Pista de Obstáculos, Escombros, Oficina de carros, Laboratório de química, Ferro Velho

### 2. A Alma da História
* **Argumento:** Em uma cidade portuária sombria e industrial, sob o véu pesado da noite Dieselpunk, uma carga de 'cristais de éter' (combustível de alta octanagem para máquinas de guerra) foi roubada do armazém da gangue 'Os Ferros-Velhos'. A gangue rival, 'A Sombra Metálica', é a principal suspeita. Se a carga não for recuperada antes do amanhecer, a frágil trégua entre as facções será quebrada, mergulhando a cidade em uma guerra aberta e sangrenta. Na verdade, a carga não foi roubada pela Sombra Metálica, mas sim por um membro dissidente dos Ferros-Velhos que busca expor a corrupção interna e o uso indevido dos cristais para projetos militares secretos, armando uma armadilha para incriminar a gangue rival e deflagrar o conflito que ele secretamente deseja.
* **Premissa Evidente (Missão):** Vocês são contratados (ou coagidos) pelos Ferros-Velhos para recuperar uma carga valiosa de cristais de éter roubada de seus armazéns. Eles suspeitam que a gangue rival, A Sombra Metálica, é a responsável. Vocês têm até o amanhecer para achar a carga, ou a cidade afundará em uma guerra sangrenta entre as gangues.
* **Premissa Oculta (Twist):** A carga não foi roubada pela Sombra Metálica. Foi roubada por um membro dos próprios Ferros-Velhos, o engenheiro Silas, que planejou o roubo para incriminar a Sombra Metálica e forçar uma guerra. Ele quer usar o caos para expor os planos secretos do líder dos Ferros-Velhos de vender a carga para uma potência estrangeira, ou usá-la em experimentos perigosos.

### 3. Segredos da Campanha (Matriz)
Use estes segredos para garantir que os locais contenham pistas ou conexões temáticas com a verdade maior:
  - Titulo: A Natureza da Carga
  - A verdade: Os 'cristais de éter' são compostos instáveis, perigosos de manusear e com potencial destrutivo muito maior do que o combustível de guerra declarado. Eles são a base para uma arma experimental secreta.
  - A expectativa: Uma carga valiosa de combustível de alta octanagem, de grande importância estratégica para as gangues.
  - A camuflagem: A carga está em caixas seladas e identificada apenas como 'combustível especial'. A urgência em recuperá-la impede uma análise detalhada. Informes iniciais dos Ferros-Velhos falam apenas do seu valor como 'combustível'.
  - O gatilho: Um acidente envolvendo a carga (vazamento, explosão parcial, aquecimento extremo) ou uma investigação química detalhada após a recuperação.
  - A revelacao: Os jogadores descobrem a verdadeira natureza perigosa e o potencial destrutivo dos cristais, que vão além de simples combustível.
  - Id: 1

  - Titulo: O Verdadeiro Ladrão
  - A verdade: Silas, um engenheiro descontente dos Ferros-Velhos, é o responsável pelo roubo. Ele orquestrou tudo para incriminar a Sombra Metálica e iniciar uma guerra que ele acredita ser necessária para expor os planos mais sombrios de seu próprio líder.
  - A expectativa: A gangue Sombra Metálica é a culpada pelo roubo, agindo por rivalidade e ganância.
  - A camuflagem: Silas é um figura periférica conhecida por sua inteligência e dissidência sutil. Ele não aparece como um antagonista direto, mas suas ações indiretas (alertas falsos, pistas plantadas) confundem a investigação. Os Ferros-Velhos apontam diretamente para a Sombra Metálica.
  - O gatilho: Investigação dos locais de origem e do modus operandi do roubo; interrogatório de membros menores dos Ferros-Velhos que possam ter visto Silas; rastreamento de tecnologia especializada usada no roubo.
  - A revelacao: Os jogadores descobrem que o verdadeiro ladrão é um 'insider' com motivos próprios, e que a Sombra Metálica pode ter sido vítima de uma armação.
  - Id: 2

  - Titulo: A Falsa Guerra
  - A verdade: O líder dos Ferros-Velhos, "Mandíbula" Mortem, deseja a guerra não apenas para eliminá-la como rival, mas para encobrir seu próprio tráfico dos cristais de éter para uma potência estrangeira ou para financiar experimentos perigosos em segredo.
  - A expectativa: A guerra entre gangues é uma consequência inevitável do roubo, motivada pela honra, território e pela quebra da trégua.
  - A camuflagem: As declarações inflamadas de "Mandíbula" Mortem sobre vingança e a honra da gangue mascaram suas verdadeiras intenções. Os planos de guerra parecem um resultado direto do roubo, sem menção a agendas ocultas para aquisição ilícita.
  - O gatilho: Descobrir comunicações secretas ou transações financeiras dos Ferros-Velhos; interceptar negociações com compradores externos; encontrar evidências de planos de contingência para a "guerra" que beneficiam exclusivamente o líder.
  - A revelacao: Os jogadores percebem que a guerra pode ser uma manobra orquestrada por um dos líderes para seu próprio benefício, em vez de uma reação genuína ao roubo.
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
    "enredo_selecionado": "A Busca",
    "meta_estrutura_resumo": "1. O Chamado -> 2. A Jornada -> 3. Chegada e Frustração (Barreira) -> 4. Provações Finais -> 5. O Objetivo.",
    "foco_narrativo": "A Urgência Noir sob a eterna poluição industrial: Uma corrida contra a madrugada onde cada sombra oculta traição e cada pista leva a um beco sem saída em meio ao fedor de óleo e metal corroído."
  },
  "lista_locais": [
    {
      "nome": "O Armazém Afundado dos Ferros-Velhos",
      "descricao": "A umidade é palpável aqui, o ar pesado com o cheiro pungente de ferrugem e peixe podre vindo do porto. A luz fraca das lâmpadas de óleo ilumina pilhas de caixas industriais e maquinário obsoleto. O som constante do gotejar d'água e o ranger do metal contra concreto criam uma atmosfera opressora. Superfícies úmidas e escorregadias cobrem o chão.\n\n",
      "tags": "roubado, industrial, úmido, escuro",
      "funcao": "Inicial",
      "ancora_geografica": "Situado nas profundezas da zona portuária, o Armazém Afundado é o ponto de partida visível, a ferida aberta na paisagem urbana. Conecta-se à Orla Encharcada através de um túnel de drenagem parcialmente colapsado, e é frequentemente envolto pela névoa salina que emana do mar.\n"
    },
    {
      "nome": "O Mercado das Pulgas da Sucata",
      "descricao": "Um labirinto caótico de tendas improvisadas e barracas oscilantes. O ar é uma mistura sufocante de fumaça de carvão, óleo de motor queimado e odores adocicados de comida de rua duvidosa. O burburinho de centenas de vozes, gritos de vendedores e o tilintar constante de sucata formam uma cacofonia incessante. O chão é um mosaico de metal retorcido, pneus velhos e detritos urbanos.\n\n",
      "tags": "caótico, movimentado, sucata, comércio",
      "funcao": "Intermediario",
      "ancora_geografica": "Aninhado nos arredores industrializados, o Mercado das Pulgas da Sucata é um bolsão de atividade humana febril que se estende a partir dos becos sujos que levam do Armazém Afundado. O som constante da forja da 'Oficina do Tio Gus' pode ser ouvido dos limites do mercado, e o cheiro de borracha queimada paira no ar vindo da próxima pista de corridas de sucata.\n"
    },
    {
      "nome": "A Oficina do Tio Gus",
      "descricao": "O som estrondoso de martelos em metal e o chiado agudo de solda dominam este local. A oficina exala um odor forte de óleo, graxa e metal aquecido. Faíscas dançam no ar rarefeito iluminado por fornalhas incandescentes e lampiões improvisados. O chão é uma tapeçaria de metal retorcido, ferramentas espalhadas, peças de motor e manchas de óleo.\n\n",
      "tags": "oficina, barulhento, cheiroso, mecânico",
      "funcao": "Intermediario",
      "ancora_geografica": "Localizada adjacente ao Mercado das Pulgas da Sucata, a Oficina do Tio Gus serve como um centro de atividade mecânica bruta. Ouve-se o eco do barulho do mercado através das paredes de metal batido, e fumaça da forja ocasionalmente sobe, obscurecendo a vista da Torre de Vigia distante.\n"
    },
    {
      "nome": "O Bar 'O Cilindro Ruidoso'",
      "descricao": "Um refúgio sombrio e barulhento, onde o cheiro de cerveja derramada, suor e fumaça de charuto preenche o ar. A música alta e distorcida de um gramofone desafinado mal consegue abafar as conversas ríspidas e os gritos ocasionais. A iluminação é precária, com luzes piscantes e sombras densas. O chão está pegajoso e os bancos de madeira gastos.\n\n",
      "tags": "bar, bêbado, fumo, sombrio",
      "funcao": "Intermediario",
      "ancora_geografica": "Servindo como um ponto de parada crucial nas rotas de tráfego do 'Refúgio', O Cilindro Ruidoso está estrategicamente localizado entre a Mansão de Mortem e as áreas de mercado. O som de motores de carros batendo e a poeira levantada pela 'Pista de Obstáculos' podem ser sentidos nas proximidades, e o luar fraco que penetra pelas janelas sujas reflete a silhueta da Torre de Vigia.\n"
    },
    {
      "nome": "A Mansão de \"Mandíbula\" Mortem",
      "descricao": "Um oásis de opulência reluzente em meio à decadência industrial. O ar é rarefeito e perfumado com fragrâncias caras e o leve cheiro de ozônio de máquinas elétricas. Discussões abafadas e o tilintar de vidro ecoam nos corredores ornamentados. A iluminação é controlada e suave, destacando obras de arte sombrias e móveis luxuosos. Pisos de mármore polido e tapetes grossos.\n\n",
      "tags": "poder, luxo, intriga, rico",
      "funcao": "Intermediario",
      "ancora_geografica": "Dominando a paisagem construída, a Mansão de Mortem situa-se em uma colina com vista para o porto e para a maior parte do 'Refúgio', agindo como um ponto de referência visual. Um portão de ferro forjado imponente a separa do resto da cidade, e os caminhos que levam à Mansão são patrulhados, conectando-se diretamente às vias principais que levam ao Bar e à Torre de Vigia.\n"
    },
    {
      "nome": "O Laboratório de Química Clandestino de Silas",
      "descricao": "Um antro de perigo latente, onde o ar é saturado com o cheiro acre de produtos químicos voláteis e um leve odor metálico, quase ozônio. Os sons são um gotejamento constante, o zumbido baixo de equipamentos elétricos e, ocasionalmente, um silvo agudo de vapor. A luz aqui é geralmente fraca, vinda de lâmpadas de segurança e o brilho etéreo de reagentes em recipientes de vidro. Bancadas de metal arranhadas e superfícies pegajosas.\n\n",
      "tags": "secreto, perigoso, químico, experimental",
      "funcao": "Climax",
      "ancora_geografica": "Escondido nas entranhas do 'Refúgio', o laboratório clandestino de Silas está disfarçado em um anexo esquecido dos antigos depósitos de carvão, próximo à área conhecida como 'Escombros'. O acesso é feito através de um duto de ventilação esquecido da Oficina do Tio Gus ou por uma passagem secreta no subsolo da Mansão de Mortem, com o cheiro mais pungente de óleo da área portuária frequentemente infiltrando-se em seus esconderijos.\n"
    },
    {
      "nome": "A Arena de Lutas 'O Martelo Quebrado'",
      "descricao": "Um caldeirão estrondoso de gritos da multidão, o baque surdo de corpos se chocando e o uivo de metal retorcido. O ar é espesso com o cheiro de suor, sangue e poeira. As luzes de holofotes caem sobre a areia batida, onde as sombras dançam selvagemente. O chão da arena é um caos de areia compactada, restos de metal e manchas escuras.\n\n",
      "tags": "luta, brutal, público, perigoso",
      "funcao": "Climax",
      "ancora_geografica": "Ancorada no coração do distrito industrial e desolado, a Arena 'O Martelo Quebrado' é um ponto nevrálgico de violência concentrada, um destino final para muitos na sociedade do 'Refúgio'. Ela se conecta aos Escombros por passarelas instáveis e túneis abertos, e o som distante da Torre de Vigia soa como um lamento de guerra, odores de ozônio e metal queimado flutuam de seu interior.\n"
    },
    {
      "nome": "A Torre de Vigia Gótica",
      "descricao": "O vento uiva incessantemente em torno desta estrutura imponente, carregando o cheiro salgado do oceano e o fedor adocicado de combustível industrial. Os sons são de metal rangendo sob a tensão e o eco distante do porto. A iluminação é esparsa, vinda de luzes de navegação intermitentes e o brilho pálido da lua. Superfícies de metal frio e concreto descascado.\n\n",
      "tags": "vigia, estratégico, alto, ventoso",
      "funcao": "Climax",
      "ancora_geografica": "Erguendo-se como um guardião sombrio sobre o 'Refúgio', a Torre de Vigia Gótica oferece uma visão panorâmica de toda a área portuária e suas facções. Ela está conectada ao Mercado das Pulgas por uma ponte de carga exposta e é visível de quase todos os locais, embora as rotas diretas para o seu topo sejam perigosamente precárias, levando-a aos céus acima da Mansão de Mortem e de muitos dos esconderijos menos óbvios na base.\n"
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
* **Subgêneros:** Noir, Ação Frenética, Drama de Baixo Nível
* **Escopo Geográfico:** Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.
* **Arquétipo:** A Busca
* **Foco Narrativo:** A Urgência Noir sob a eterna poluição industrial: Uma corrida contra a madrugada onde cada sombra oculta traição e cada pista leva a um beco sem saída em meio ao fedor de óleo e metal corroído.

### 2. Dados dos Locais (Step 1)
>>> DADOS DOS LOCAIS:
> **O Armazém Afundado dos Ferros-Velhos**
  - Descricao: A umidade é palpável aqui, o ar pesado com o cheiro pungente de ferrugem e peixe podre vindo do porto. A luz fraca das lâmpadas de óleo ilumina pilhas de caixas industriais e maquinário obsoleto. O som constante do gotejar d'água e o ranger do metal contra concreto criam uma atmosfera opressora. Superfícies úmidas e escorregadias cobrem o chão.


  - Tags: roubado, industrial, úmido, escuro
  - Funcao: Inicial
  - Ancora geografica: Situado nas profundezas da zona portuária, o Armazém Afundado é o ponto de partida visível, a ferida aberta na paisagem urbana. Conecta-se à Orla Encharcada através de um túnel de drenagem parcialmente colapsado, e é frequentemente envolto pela névoa salina que emana do mar.


> **O Mercado das Pulgas da Sucata**
  - Descricao: Um labirinto caótico de tendas improvisadas e barracas oscilantes. O ar é uma mistura sufocante de fumaça de carvão, óleo de motor queimado e odores adocicados de comida de rua duvidosa. O burburinho de centenas de vozes, gritos de vendedores e o tilintar constante de sucata formam uma cacofonia incessante. O chão é um mosaico de metal retorcido, pneus velhos e detritos urbanos.


  - Tags: caótico, movimentado, sucata, comércio
  - Funcao: Intermediario
  - Ancora geografica: Aninhado nos arredores industrializados, o Mercado das Pulgas da Sucata é um bolsão de atividade humana febril que se estende a partir dos becos sujos que levam do Armazém Afundado. O som constante da forja da 'Oficina do Tio Gus' pode ser ouvido dos limites do mercado, e o cheiro de borracha queimada paira no ar vindo da próxima pista de corridas de sucata.


> **A Oficina do Tio Gus**
  - Descricao: O som estrondoso de martelos em metal e o chiado agudo de solda dominam este local. A oficina exala um odor forte de óleo, graxa e metal aquecido. Faíscas dançam no ar rarefeito iluminado por fornalhas incandescentes e lampiões improvisados. O chão é uma tapeçaria de metal retorcido, ferramentas espalhadas, peças de motor e manchas de óleo.


  - Tags: oficina, barulhento, cheiroso, mecânico
  - Funcao: Intermediario
  - Ancora geografica: Localizada adjacente ao Mercado das Pulgas da Sucata, a Oficina do Tio Gus serve como um centro de atividade mecânica bruta. Ouve-se o eco do barulho do mercado através das paredes de metal batido, e fumaça da forja ocasionalmente sobe, obscurecendo a vista da Torre de Vigia distante.


> **O Bar 'O Cilindro Ruidoso'**
  - Descricao: Um refúgio sombrio e barulhento, onde o cheiro de cerveja derramada, suor e fumaça de charuto preenche o ar. A música alta e distorcida de um gramofone desafinado mal consegue abafar as conversas ríspidas e os gritos ocasionais. A iluminação é precária, com luzes piscantes e sombras densas. O chão está pegajoso e os bancos de madeira gastos.


  - Tags: bar, bêbado, fumo, sombrio
  - Funcao: Intermediario
  - Ancora geografica: Servindo como um ponto de parada crucial nas rotas de tráfego do 'Refúgio', O Cilindro Ruidoso está estrategicamente localizado entre a Mansão de Mortem e as áreas de mercado. O som de motores de carros batendo e a poeira levantada pela 'Pista de Obstáculos' podem ser sentidos nas proximidades, e o luar fraco que penetra pelas janelas sujas reflete a silhueta da Torre de Vigia.


> **A Mansão de "Mandíbula" Mortem**
  - Descricao: Um oásis de opulência reluzente em meio à decadência industrial. O ar é rarefeito e perfumado com fragrâncias caras e o leve cheiro de ozônio de máquinas elétricas. Discussões abafadas e o tilintar de vidro ecoam nos corredores ornamentados. A iluminação é controlada e suave, destacando obras de arte sombrias e móveis luxuosos. Pisos de mármore polido e tapetes grossos.


  - Tags: poder, luxo, intriga, rico
  - Funcao: Intermediario
  - Ancora geografica: Dominando a paisagem construída, a Mansão de Mortem situa-se em uma colina com vista para o porto e para a maior parte do 'Refúgio', agindo como um ponto de referência visual. Um portão de ferro forjado imponente a separa do resto da cidade, e os caminhos que levam à Mansão são patrulhados, conectando-se diretamente às vias principais que levam ao Bar e à Torre de Vigia.


> **O Laboratório de Química Clandestino de Silas**
  - Descricao: Um antro de perigo latente, onde o ar é saturado com o cheiro acre de produtos químicos voláteis e um leve odor metálico, quase ozônio. Os sons são um gotejamento constante, o zumbido baixo de equipamentos elétricos e, ocasionalmente, um silvo agudo de vapor. A luz aqui é geralmente fraca, vinda de lâmpadas de segurança e o brilho etéreo de reagentes em recipientes de vidro. Bancadas de metal arranhadas e superfícies pegajosas.


  - Tags: secreto, perigoso, químico, experimental
  - Funcao: Climax
  - Ancora geografica: Escondido nas entranhas do 'Refúgio', o laboratório clandestino de Silas está disfarçado em um anexo esquecido dos antigos depósitos de carvão, próximo à área conhecida como 'Escombros'. O acesso é feito através de um duto de ventilação esquecido da Oficina do Tio Gus ou por uma passagem secreta no subsolo da Mansão de Mortem, com o cheiro mais pungente de óleo da área portuária frequentemente infiltrando-se em seus esconderijos.


> **A Arena de Lutas 'O Martelo Quebrado'**
  - Descricao: Um caldeirão estrondoso de gritos da multidão, o baque surdo de corpos se chocando e o uivo de metal retorcido. O ar é espesso com o cheiro de suor, sangue e poeira. As luzes de holofotes caem sobre a areia batida, onde as sombras dançam selvagemente. O chão da arena é um caos de areia compactada, restos de metal e manchas escuras.


  - Tags: luta, brutal, público, perigoso
  - Funcao: Climax
  - Ancora geografica: Ancorada no coração do distrito industrial e desolado, a Arena 'O Martelo Quebrado' é um ponto nevrálgico de violência concentrada, um destino final para muitos na sociedade do 'Refúgio'. Ela se conecta aos Escombros por passarelas instáveis e túneis abertos, e o som distante da Torre de Vigia soa como um lamento de guerra, odores de ozônio e metal queimado flutuam de seu interior.


> **A Torre de Vigia Gótica**
  - Descricao: O vento uiva incessantemente em torno desta estrutura imponente, carregando o cheiro salgado do oceano e o fedor adocicado de combustível industrial. Os sons são de metal rangendo sob a tensão e o eco distante do porto. A iluminação é esparsa, vinda de luzes de navegação intermitentes e o brilho pálido da lua. Superfícies de metal frio e concreto descascado.


  - Tags: vigia, estratégico, alto, ventoso
  - Funcao: Climax
  - Ancora geografica: Erguendo-se como um guardião sombrio sobre o 'Refúgio', a Torre de Vigia Gótica oferece uma visão panorâmica de toda a área portuária e suas facções. Ela está conectada ao Mercado das Pulgas por uma ponte de carga exposta e é visível de quase todos os locais, embora as rotas diretas para o seu topo sejam perigosamente precárias, levando-a aos céus acima da Mansão de Mortem e de muitos dos esconderijos menos óbvios na base.


### 3. Contexto da Trama
* **Argumento:** Em uma cidade portuária sombria e industrial, sob o véu pesado da noite Dieselpunk, uma carga de 'cristais de éter' (combustível de alta octanagem para máquinas de guerra) foi roubada do armazém da gangue 'Os Ferros-Velhos'. A gangue rival, 'A Sombra Metálica', é a principal suspeita. Se a carga não for recuperada antes do amanhecer, a frágil trégua entre as facções será quebrada, mergulhando a cidade em uma guerra aberta e sangrenta. Na verdade, a carga não foi roubada pela Sombra Metálica, mas sim por um membro dissidente dos Ferros-Velhos que busca expor a corrupção interna e o uso indevido dos cristais para projetos militares secretos, armando uma armadilha para incriminar a gangue rival e deflagrar o conflito que ele secretamente deseja.
* **Premissa Evidente:** Vocês são contratados (ou coagidos) pelos Ferros-Velhos para recuperar uma carga valiosa de cristais de éter roubada de seus armazéns. Eles suspeitam que a gangue rival, A Sombra Metálica, é a responsável. Vocês têm até o amanhecer para achar a carga, ou a cidade afundará em uma guerra sangrenta entre as gangues.
* **Premissa Oculta:** A carga não foi roubada pela Sombra Metálica. Foi roubada por um membro dos próprios Ferros-Velhos, o engenheiro Silas, que planejou o roubo para incriminar a Sombra Metálica e forçar uma guerra. Ele quer usar o caos para expor os planos secretos do líder dos Ferros-Velhos de vender a carga para uma potência estrangeira, ou usá-la em experimentos perigosos.

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
  "descricao_frente": "Na noite Dieselpunk, onde a poluição industrial tinge o céu de um perpétuo entardecer, uma carga vital de cristais de éter foi roubada. A tensão entre as gangues 'Os Ferros-Velhos' e 'A Sombra Metálica' está no ponto de ruptura. Com a madrugada se aproximando, cada sombra esconde mais do que traição; ela esconde a verdade por trás de um roubo orquestrado que pode mergulhar o Refúgio em uma guerra total.",
  "elenco": [
    {
      "nome": "Mandíbula Mortem",
      "papel_funcao": "Líder dos Ferros-Velhos",
      "detalhe_marcante": "Tem um sorriso fixo e insincero, mostrando dentes de metal polido ao falar.",
      "conviccao": "Vejo o Refúgio como meu playground pessoal; a ordem é mantida pela força e meu controle absoluto. A guerra é apenas outra ferramenta para expandir meu império.",
      "contraste": "Coleciona relógios de bolso antigos e raros, lembranças de uma vida mais simples que ele nunca teve."
    },
    {
      "nome": "Chave",
      "papel_funcao": "Chefe de Segurança dos Ferros-Velhos, responsável pela 'recuperação'",
      "detalhe_marcante": "Usa um tapa-olho feito de sucata e uma voz rouca que parece raspar metal.",
      "conviccao": "A ordem é a prioridade máxima. Qualquer um que ameace a estabilidade, especialmente os rivais, deve ser silenciado. Os Ferros-Velhos são a única coisa que impede o caos total.",
      "contraste": "Tem uma predileção por poesias ruins que ele recita para si mesmo em momentos de estresse."
    },
    {
      "nome": "Silas 'O Engenhoso'",
      "papel_funcao": "Engenheiro dissidente dos Ferros-Velhos, o verdadeiro ladrão",
      "detalhe_marcante": "Tem mãos manchadas de graxa que se movem com uma precisão perturbadora, e um olhar que parece sempre analisar tudo.",
      "conviccao": "A corrupção internalizada é um veneno pior que qualquer guerra iminente. Silas acredita que a única maneira de expor a podridão dos Ferros-Velhos e seus planos nefastos é forçar um confronto, mesmo que isso signifique manipular a situação.",
      "contraste": "Cuida secretamente de um pequeno jardim de plantas mecânicas que ele mesmo projetou e construiu, pequenas flores de metal que desabrocham com vapor."
    },
    {
      "nome": "Vex",
      "papel_funcao": "Líder da Sombra Metálica",
      "detalhe_marcante": "Usa um monóculo cravejado de sucata e um grito de guerra estridente.",
      "conviccao": "Os Ferros-Velhos oprimen a todos com suas máquinas e sua ganância. É hora de arrancar o poder deles e reescrever as regras para que o povo comum possa prosperar.",
      "contraste": "Tem uma fraqueza secreta por filhotes de cães de rua, a quem ele alimenta com sobras de comida duvidosa."
    }
  ],
  "perigos": [
    {
      "nome": "A Desconfiança Generalizada",
      "tipo": "Organização",
      "impulso": "Governo Corrupto: Manter o status quo.",
      "ameaca_verdade": "Desafia a noção de que os jogadores podem confiar em alguém ou em suas informações. Cada pista pode ser uma armadilha e cada aliado potencial pode trair.",
      "local_vinculado": "O Refúgio (Geral)",
      "rastro_destruicao": "Falas sussurradas em becos escuros, olhares furtivos e a constante sensação de ser observado. Os jogadores sentem que todos estão contra eles.",
      "acao_iminente": "Agentes dos Ferros-Velhos e da Sombra Metálica começarão a 'patrulhar' ativamente as áreas chave, interrogando qualquer um que pareça suspeito e bloqueando rotas de acesso importantes."
    },
    {
      "nome": "A Corrida Contra o Amanhecer",
      "tipo": "Horda",
      "impulso": "Criaturas Humanoides: Crescer, multiplicar e consumir.",
      "ameaca_verdade": "Ameaça a própria capacidade dos heróis de agir. A falta de tempo pressiona, força decisões ruins e limita o alcance de suas ações.",
      "local_vinculado": "O Mercado das Pulgas da Sucata / A Arena 'O Martelo Quebrado'",
      "rastro_destruicao": "O burburinho agitado do mercado se transforma em pânico incipiente. A poeira na arena está sendo levantada pelas patas ansiosas de corredores improváveis, que se preparam para a sua própria 'corrida'.",
      "acao_iminente": "O primeiro raio de sol começará a romper o horizonte. As patrulhas de ambas as gangues se tornarão mais agressivas, e vendedores e cidadãos começarão a se recolher em suas casas, fechando os acessos e aumentando a dificuldade de movimentação."
    },
    {
      "nome": "A Manipulação de Silas",
      "tipo": "Organização",
      "impulso": "Cabala: Absorver aqueles que estão no poder, crescer.",
      "ameaca_verdade": "Desafia a justiça. Os jogadores podem estar lutando por um lado que, no fundo, está tão corrompido quanto o outro, ou servindo aos propósitos de um manipulador ainda mais perigoso.",
      "local_vinculado": "O Laboratório de Química Clandestino de Silas / Oficina do Tio Gus",
      "rastro_destruicao": "Um novo rastro de evidências plantadas aparece no Armazém Afundado, implicando a Sombra Metálica. Mensagens codificadas com planos de teste de armas secretas são sussurradas nos túneis.",
      "acao_iminente": "Silas ativará um dispositivo de distração em uma parte remota do Refúgio para desviar a atenção das patrulhas e da Sombra Metálica de seu laboratório, permitindo que ele finalize seus planos de manipulação final."
    }
  ],
  "desastre_iminente": {
    "tipo_desastre": "Caos",
    "descricao": "Se os cristais de éter não forem recuperados e a verdade não for exposta, a guerra aberta entre Os Ferros-Velhos e A Sombra Metálica irromperá. O Refúgio se tornará um campo de batalha brutal, com civis sendo pegos no fogo cruzado, a infraestrutura industrial desmoronando e a autoridade de Mandíbula Mortem, ou quem quer que sobreviva, será baseada puramente em terror e destruição. Silas, se não contido, usará o caos para implementar seus próprios experimentos perigosos ou vender a tecnologia para potências exteriores, condenando o Refúgio a um futuro ainda mais sombrio."
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
* **Subgêneros:** Noir, Ação Frenética, Drama de Baixo Nível
* **Escopo Geográfico:** Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.

### 2. Contexto da Trama
* **Argumento:** Em uma cidade portuária sombria e industrial, sob o véu pesado da noite Dieselpunk, uma carga de 'cristais de éter' (combustível de alta octanagem para máquinas de guerra) foi roubada do armazém da gangue 'Os Ferros-Velhos'. A gangue rival, 'A Sombra Metálica', é a principal suspeita. Se a carga não for recuperada antes do amanhecer, a frágil trégua entre as facções será quebrada, mergulhando a cidade em uma guerra aberta e sangrenta. Na verdade, a carga não foi roubada pela Sombra Metálica, mas sim por um membro dissidente dos Ferros-Velhos que busca expor a corrupção interna e o uso indevido dos cristais para projetos militares secretos, armando uma armadilha para incriminar a gangue rival e deflagrar o conflito que ele secretamente deseja.
* **Premissa Evidente:** Vocês são contratados (ou coagidos) pelos Ferros-Velhos para recuperar uma carga valiosa de cristais de éter roubada de seus armazéns. Eles suspeitam que a gangue rival, A Sombra Metálica, é a responsável. Vocês têm até o amanhecer para achar a carga, ou a cidade afundará em uma guerra sangrenta entre as gangues.
* **Premissa Oculta:** A carga não foi roubada pela Sombra Metálica. Foi roubada por um membro dos próprios Ferros-Velhos, o engenheiro Silas, que planejou o roubo para incriminar a Sombra Metálica e forçar uma guerra. Ele quer usar o caos para expor os planos secretos do líder dos Ferros-Velhos de vender a carga para uma potência estrangeira, ou usá-la em experimentos perigosos.
* **Arquétipos Permitidos:** Músculo: Você é grande, pesado. Machucar e fazer façanhas físicas é com você., Cabeça: Pensamento ágil, consegue operar sistemas e máquinas antigas., Volante: Atrás de um volante, não há igual. Você é uma fera das estradas., Vigia: Olhos atentos e sempre no horizonte. Consegue atirar muito bem., Boca: Sempre sabe o que dizer. Carisma em pessoa. Mesmo que isso traga problemas., Novato: Nunca conheceu um mundo que não esse. Quer provar seu valor para os seus.

### 3. Dados da Fase 1 (Estrutura)
* **Arquétipo Selecionado:** A Busca
* **Foco Narrativo:** A Urgência Noir sob a eterna poluição industrial: Uma corrida contra a madrugada onde cada sombra oculta traição e cada pista leva a um beco sem saída em meio ao fedor de óleo e metal corroído.

>>> LISTA DE LOCAIS (Referência para Localização dos Presságios):
> **O Armazém Afundado dos Ferros-Velhos**
  - Descricao: A umidade é palpável aqui, o ar pesado com o cheiro pungente de ferrugem e peixe podre vindo do porto. A luz fraca das lâmpadas de óleo ilumina pilhas de caixas industriais e maquinário obsoleto. O som constante do gotejar d'água e o ranger do metal contra concreto criam uma atmosfera opressora. Superfícies úmidas e escorregadias cobrem o chão.


  - Tags: roubado, industrial, úmido, escuro
  - Funcao: Inicial
  - Ancora geografica: Situado nas profundezas da zona portuária, o Armazém Afundado é o ponto de partida visível, a ferida aberta na paisagem urbana. Conecta-se à Orla Encharcada através de um túnel de drenagem parcialmente colapsado, e é frequentemente envolto pela névoa salina que emana do mar.


> **O Mercado das Pulgas da Sucata**
  - Descricao: Um labirinto caótico de tendas improvisadas e barracas oscilantes. O ar é uma mistura sufocante de fumaça de carvão, óleo de motor queimado e odores adocicados de comida de rua duvidosa. O burburinho de centenas de vozes, gritos de vendedores e o tilintar constante de sucata formam uma cacofonia incessante. O chão é um mosaico de metal retorcido, pneus velhos e detritos urbanos.


  - Tags: caótico, movimentado, sucata, comércio
  - Funcao: Intermediario
  - Ancora geografica: Aninhado nos arredores industrializados, o Mercado das Pulgas da Sucata é um bolsão de atividade humana febril que se estende a partir dos becos sujos que levam do Armazém Afundado. O som constante da forja da 'Oficina do Tio Gus' pode ser ouvido dos limites do mercado, e o cheiro de borracha queimada paira no ar vindo da próxima pista de corridas de sucata.


> **A Oficina do Tio Gus**
  - Descricao: O som estrondoso de martelos em metal e o chiado agudo de solda dominam este local. A oficina exala um odor forte de óleo, graxa e metal aquecido. Faíscas dançam no ar rarefeito iluminado por fornalhas incandescentes e lampiões improvisados. O chão é uma tapeçaria de metal retorcido, ferramentas espalhadas, peças de motor e manchas de óleo.


  - Tags: oficina, barulhento, cheiroso, mecânico
  - Funcao: Intermediario
  - Ancora geografica: Localizada adjacente ao Mercado das Pulgas da Sucata, a Oficina do Tio Gus serve como um centro de atividade mecânica bruta. Ouve-se o eco do barulho do mercado através das paredes de metal batido, e fumaça da forja ocasionalmente sobe, obscurecendo a vista da Torre de Vigia distante.


> **O Bar 'O Cilindro Ruidoso'**
  - Descricao: Um refúgio sombrio e barulhento, onde o cheiro de cerveja derramada, suor e fumaça de charuto preenche o ar. A música alta e distorcida de um gramofone desafinado mal consegue abafar as conversas ríspidas e os gritos ocasionais. A iluminação é precária, com luzes piscantes e sombras densas. O chão está pegajoso e os bancos de madeira gastos.


  - Tags: bar, bêbado, fumo, sombrio
  - Funcao: Intermediario
  - Ancora geografica: Servindo como um ponto de parada crucial nas rotas de tráfego do 'Refúgio', O Cilindro Ruidoso está estrategicamente localizado entre a Mansão de Mortem e as áreas de mercado. O som de motores de carros batendo e a poeira levantada pela 'Pista de Obstáculos' podem ser sentidos nas proximidades, e o luar fraco que penetra pelas janelas sujas reflete a silhueta da Torre de Vigia.


> **A Mansão de "Mandíbula" Mortem**
  - Descricao: Um oásis de opulência reluzente em meio à decadência industrial. O ar é rarefeito e perfumado com fragrâncias caras e o leve cheiro de ozônio de máquinas elétricas. Discussões abafadas e o tilintar de vidro ecoam nos corredores ornamentados. A iluminação é controlada e suave, destacando obras de arte sombrias e móveis luxuosos. Pisos de mármore polido e tapetes grossos.


  - Tags: poder, luxo, intriga, rico
  - Funcao: Intermediario
  - Ancora geografica: Dominando a paisagem construída, a Mansão de Mortem situa-se em uma colina com vista para o porto e para a maior parte do 'Refúgio', agindo como um ponto de referência visual. Um portão de ferro forjado imponente a separa do resto da cidade, e os caminhos que levam à Mansão são patrulhados, conectando-se diretamente às vias principais que levam ao Bar e à Torre de Vigia.


> **O Laboratório de Química Clandestino de Silas**
  - Descricao: Um antro de perigo latente, onde o ar é saturado com o cheiro acre de produtos químicos voláteis e um leve odor metálico, quase ozônio. Os sons são um gotejamento constante, o zumbido baixo de equipamentos elétricos e, ocasionalmente, um silvo agudo de vapor. A luz aqui é geralmente fraca, vinda de lâmpadas de segurança e o brilho etéreo de reagentes em recipientes de vidro. Bancadas de metal arranhadas e superfícies pegajosas.


  - Tags: secreto, perigoso, químico, experimental
  - Funcao: Climax
  - Ancora geografica: Escondido nas entranhas do 'Refúgio', o laboratório clandestino de Silas está disfarçado em um anexo esquecido dos antigos depósitos de carvão, próximo à área conhecida como 'Escombros'. O acesso é feito através de um duto de ventilação esquecido da Oficina do Tio Gus ou por uma passagem secreta no subsolo da Mansão de Mortem, com o cheiro mais pungente de óleo da área portuária frequentemente infiltrando-se em seus esconderijos.


> **A Arena de Lutas 'O Martelo Quebrado'**
  - Descricao: Um caldeirão estrondoso de gritos da multidão, o baque surdo de corpos se chocando e o uivo de metal retorcido. O ar é espesso com o cheiro de suor, sangue e poeira. As luzes de holofotes caem sobre a areia batida, onde as sombras dançam selvagemente. O chão da arena é um caos de areia compactada, restos de metal e manchas escuras.


  - Tags: luta, brutal, público, perigoso
  - Funcao: Climax
  - Ancora geografica: Ancorada no coração do distrito industrial e desolado, a Arena 'O Martelo Quebrado' é um ponto nevrálgico de violência concentrada, um destino final para muitos na sociedade do 'Refúgio'. Ela se conecta aos Escombros por passarelas instáveis e túneis abertos, e o som distante da Torre de Vigia soa como um lamento de guerra, odores de ozônio e metal queimado flutuam de seu interior.


> **A Torre de Vigia Gótica**
  - Descricao: O vento uiva incessantemente em torno desta estrutura imponente, carregando o cheiro salgado do oceano e o fedor adocicado de combustível industrial. Os sons são de metal rangendo sob a tensão e o eco distante do porto. A iluminação é esparsa, vinda de luzes de navegação intermitentes e o brilho pálido da lua. Superfícies de metal frio e concreto descascado.


  - Tags: vigia, estratégico, alto, ventoso
  - Funcao: Climax
  - Ancora geografica: Erguendo-se como um guardião sombrio sobre o 'Refúgio', a Torre de Vigia Gótica oferece uma visão panorâmica de toda a área portuária e suas facções. Ela está conectada ao Mercado das Pulgas por uma ponte de carga exposta e é visível de quase todos os locais, embora as rotas diretas para o seu topo sejam perigosamente precárias, levando-a aos céus acima da Mansão de Mortem e de muitos dos esconderijos menos óbvios na base.


### 4. Dados da Fase 2 (Ameaças e Elenco)
Use estes dados para definir QUEM causa os presságios.

>>> ELENCO PRINCIPAL:
> **Mandíbula Mortem**
  - Papel funcao: Líder dos Ferros-Velhos
  - Detalhe marcante: Tem um sorriso fixo e insincero, mostrando dentes de metal polido ao falar.
  - Conviccao: Vejo o Refúgio como meu playground pessoal; a ordem é mantida pela força e meu controle absoluto. A guerra é apenas outra ferramenta para expandir meu império.
  - Contraste: Coleciona relógios de bolso antigos e raros, lembranças de uma vida mais simples que ele nunca teve.

> **Chave**
  - Papel funcao: Chefe de Segurança dos Ferros-Velhos, responsável pela 'recuperação'
  - Detalhe marcante: Usa um tapa-olho feito de sucata e uma voz rouca que parece raspar metal.
  - Conviccao: A ordem é a prioridade máxima. Qualquer um que ameace a estabilidade, especialmente os rivais, deve ser silenciado. Os Ferros-Velhos são a única coisa que impede o caos total.
  - Contraste: Tem uma predileção por poesias ruins que ele recita para si mesmo em momentos de estresse.

> **Silas 'O Engenhoso'**
  - Papel funcao: Engenheiro dissidente dos Ferros-Velhos, o verdadeiro ladrão
  - Detalhe marcante: Tem mãos manchadas de graxa que se movem com uma precisão perturbadora, e um olhar que parece sempre analisar tudo.
  - Conviccao: A corrupção internalizada é um veneno pior que qualquer guerra iminente. Silas acredita que a única maneira de expor a podridão dos Ferros-Velhos e seus planos nefastos é forçar um confronto, mesmo que isso signifique manipular a situação.
  - Contraste: Cuida secretamente de um pequeno jardim de plantas mecânicas que ele mesmo projetou e construiu, pequenas flores de metal que desabrocham com vapor.

> **Vex**
  - Papel funcao: Líder da Sombra Metálica
  - Detalhe marcante: Usa um monóculo cravejado de sucata e um grito de guerra estridente.
  - Conviccao: Os Ferros-Velhos oprimen a todos com suas máquinas e sua ganância. É hora de arrancar o poder deles e reescrever as regras para que o povo comum possa prosperar.
  - Contraste: Tem uma fraqueza secreta por filhotes de cães de rua, a quem ele alimenta com sobras de comida duvidosa.

>>> PERIGOS ATIVOS:
> **A Desconfiança Generalizada**
  - Tipo: Organização
  - Impulso: Governo Corrupto: Manter o status quo.
  - Ameaca verdade: Desafia a noção de que os jogadores podem confiar em alguém ou em suas informações. Cada pista pode ser uma armadilha e cada aliado potencial pode trair.
  - Local vinculado: O Refúgio (Geral)
  - Rastro destruicao: Falas sussurradas em becos escuros, olhares furtivos e a constante sensação de ser observado. Os jogadores sentem que todos estão contra eles.
  - Acao iminente: Agentes dos Ferros-Velhos e da Sombra Metálica começarão a 'patrulhar' ativamente as áreas chave, interrogando qualquer um que pareça suspeito e bloqueando rotas de acesso importantes.

> **A Corrida Contra o Amanhecer**
  - Tipo: Horda
  - Impulso: Criaturas Humanoides: Crescer, multiplicar e consumir.
  - Ameaca verdade: Ameaça a própria capacidade dos heróis de agir. A falta de tempo pressiona, força decisões ruins e limita o alcance de suas ações.
  - Local vinculado: O Mercado das Pulgas da Sucata / A Arena 'O Martelo Quebrado'
  - Rastro destruicao: O burburinho agitado do mercado se transforma em pânico incipiente. A poeira na arena está sendo levantada pelas patas ansiosas de corredores improváveis, que se preparam para a sua própria 'corrida'.
  - Acao iminente: O primeiro raio de sol começará a romper o horizonte. As patrulhas de ambas as gangues se tornarão mais agressivas, e vendedores e cidadãos começarão a se recolher em suas casas, fechando os acessos e aumentando a dificuldade de movimentação.

> **A Manipulação de Silas**
  - Tipo: Organização
  - Impulso: Cabala: Absorver aqueles que estão no poder, crescer.
  - Ameaca verdade: Desafia a justiça. Os jogadores podem estar lutando por um lado que, no fundo, está tão corrompido quanto o outro, ou servindo aos propósitos de um manipulador ainda mais perigoso.
  - Local vinculado: O Laboratório de Química Clandestino de Silas / Oficina do Tio Gus
  - Rastro destruicao: Um novo rastro de evidências plantadas aparece no Armazém Afundado, implicando a Sombra Metálica. Mensagens codificadas com planos de teste de armas secretas são sussurradas nos túneis.
  - Acao iminente: Silas ativará um dispositivo de distração em uma parte remota do Refúgio para desviar a atenção das patrulhas e da Sombra Metálica de seu laboratório, permitindo que ele finalize seus planos de manipulação final.

* **Desastre Iminente (Game Over):** Caos - Se os cristais de éter não forem recuperados e a verdade não for exposta, a guerra aberta entre Os Ferros-Velhos e A Sombra Metálica irromperá. O Refúgio se tornará um campo de batalha brutal, com civis sendo pegos no fogo cruzado, a infraestrutura industrial desmoronando e a autoridade de Mandíbula Mortem, ou quem quer que sobreviva, será baseada puramente em terror e destruição. Silas, se não contido, usará o caos para implementar seus próprios experimentos perigosos ou vender a tecnologia para potências exteriores, condenando o Refúgio a um futuro ainda mais sombrio.

### 5. Matriz de Controle de Informação
Conecte os presságios aos segredos abaixo (Camada de Informação).

>>> SEGREDOS DA CAMPANHA:
  - Titulo: A Natureza da Carga
  - A verdade: Os 'cristais de éter' são compostos instáveis, perigosos de manusear e com potencial destrutivo muito maior do que o combustível de guerra declarado. Eles são a base para uma arma experimental secreta.
  - A expectativa: Uma carga valiosa de combustível de alta octanagem, de grande importância estratégica para as gangues.
  - A camuflagem: A carga está em caixas seladas e identificada apenas como 'combustível especial'. A urgência em recuperá-la impede uma análise detalhada. Informes iniciais dos Ferros-Velhos falam apenas do seu valor como 'combustível'.
  - O gatilho: Um acidente envolvendo a carga (vazamento, explosão parcial, aquecimento extremo) ou uma investigação química detalhada após a recuperação.
  - A revelacao: Os jogadores descobrem a verdadeira natureza perigosa e o potencial destrutivo dos cristais, que vão além de simples combustível.
  - Id: 1

  - Titulo: O Verdadeiro Ladrão
  - A verdade: Silas, um engenheiro descontente dos Ferros-Velhos, é o responsável pelo roubo. Ele orquestrou tudo para incriminar a Sombra Metálica e iniciar uma guerra que ele acredita ser necessária para expor os planos mais sombrios de seu próprio líder.
  - A expectativa: A gangue Sombra Metálica é a culpada pelo roubo, agindo por rivalidade e ganância.
  - A camuflagem: Silas é um figura periférica conhecida por sua inteligência e dissidência sutil. Ele não aparece como um antagonista direto, mas suas ações indiretas (alertas falsos, pistas plantadas) confundem a investigação. Os Ferros-Velhos apontam diretamente para a Sombra Metálica.
  - O gatilho: Investigação dos locais de origem e do modus operandi do roubo; interrogatório de membros menores dos Ferros-Velhos que possam ter visto Silas; rastreamento de tecnologia especializada usada no roubo.
  - A revelacao: Os jogadores descobrem que o verdadeiro ladrão é um 'insider' com motivos próprios, e que a Sombra Metálica pode ter sido vítima de uma armação.
  - Id: 2

  - Titulo: A Falsa Guerra
  - A verdade: O líder dos Ferros-Velhos, "Mandíbula" Mortem, deseja a guerra não apenas para eliminá-la como rival, mas para encobrir seu próprio tráfico dos cristais de éter para uma potência estrangeira ou para financiar experimentos perigosos em segredo.
  - A expectativa: A guerra entre gangues é uma consequência inevitável do roubo, motivada pela honra, território e pela quebra da trégua.
  - A camuflagem: As declarações inflamadas de "Mandíbula" Mortem sobre vingança e a honra da gangue mascaram suas verdadeiras intenções. Os planos de guerra parecem um resultado direto do roubo, sem menção a agendas ocultas para aquisição ilícita.
  - O gatilho: Descobrir comunicações secretas ou transações financeiras dos Ferros-Velhos; interceptar negociações com compradores externos; encontrar evidências de planos de contingência para a "guerra" que beneficiam exclusivamente o líder.
  - A revelacao: Os jogadores percebem que a guerra pode ser uma manobra orquestrada por um dos líderes para seu próprio benefício, em vez de uma reação genuína ao roubo.
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
      "meta_estrutura": "O Chamado",
      "local_sugerido": "O Armazém Afundado dos Ferros-Velhos",
      "o_pressagio": "O cheiro de ozônio e metal queimado paira no ar úmido do Armazém Afundado. Caixas industriais estão viradas, contendo apenas poeira e o rastro de um líquido iridescente que emana um calor tênue. O líder dos Ferros-Velhos, Mandíbula Mortem, ou seu leal, mas intimidante, chefe de segurança Chave, o jogador para uma reunião urgente. Ele exige a recuperação imediata da carga roubada de 'cristais de éter' antes do nascer do sol, caso contrário, a trégua com a Sombra Metálica se estilhaçará em mil pedaços.",
      "argumento_arco_historia": "Mandíbula Mortem (ou Chave, se Mortem estiver ocupado, agindo sob suas ordens explícitas) convoca os jogadores ao Armazém Afundado, um local que eles sabem ter sido o alvo do roubo. A noite avança rapidamente, e a pressão para recuperar os cristais é imensa. A aparência de caos e destruição no local é apenas o prelúdio para a tarefa que lhes é dada: encontrar a carga e, idealmente, identificar os culpados antes do amanhecer, sob a ameaça direta de guerra.",
      "premissas_arco_historia": {
        "evidente": "Um grande carregamento de 'cristais de éter', vital para as operações dos Ferros-Velhos, foi roubado. Os jogadores são contratados para recuperá-lo o mais rápido possível, com a implicação clara de que a Sombra Metálica é a culpada e que a falha levará ao caos total na cidade.",
        "oculta": "A cena do roubo foi provocada intencionalmente. Os cristais de éter não são apenas combustível, mas sim componentes instáveis de uma arma secreta, e a facilidade com que foram levados levanta suspeitas sobre uma possível ajuda interna ou uma encenação sutil para incriminar a Sombra Metálica."
      },
      "camada_informacao": {
        "id_matriz": 1,
        "conexao_explicada": "O cenário do roubo, com a carga valiosa e a urgência em recuperá-la, estabelece a premissa de que os 'cristais de éter' são apenas um combustível de alta octanagem. A aparência de uma carga valiosa e estratégica é apresentada como fato, ocultando sua verdadeira natureza perigosa e o potencial destrutivo de seu uso."
      }
    },
    {
      "ordem": 2,
      "meta_estrutura": "A Jornada",
      "local_sugerido": "O Mercado das Pulgas da Sucata",
      "o_pressagio": "Seguindo uma pista inicial, os jogadores se aventuram no labirinto caótico do Mercado das Pulgas da Sucata. Entre as barracas improvisadas e a fumaça sufocante, eles encontram um informante relutante ou um vendedor suspeito que afirma ter visto membros da Sombra Metálica agindo furtivamente na noite do roubo, carregando caixas que pareciam pesadas e emitiam um brilho tênue. No entanto, o informante, visivelmente assustado, sussurra que algo parecia errado, que a 'energia' que emanava das caixas não era a de simples contrabando.",
      "argumento_arco_historia": "Os jogadores investigam uma pista que os leva ao Mercado das Pulgas da Sucata. Seu objetivo é obter mais informações sobre o roubo dos cristais de éter. Lá, eles encontram um NPC (talvez um informante de Chave, ou alguém assustado com a busca de Silas) que os direciona para a Sombra Metálica, mas introduz uma nota de estranheza sobre a carga ou os envolvidos. A 'Corrida Contra o Amanhecer' já é um fator aqui, com a agitação no mercado e as tensões aumentando.",
      "premissas_arco_historia": {
        "evidente": "A pista aponta para a Sombra Metálica como a responsável, com testemunhas (ou pelo menos, um testemunho confuso) descrevendo seus membros realizando algo suspeito na noite do roubo. A tensão aumenta à medida que o tempo para o amanhecer diminui.",
        "oculta": "O testemunho, embora incriminando a Sombra Metálica, também contém um detalhe perturbador sobre a natureza da carga que foi roubada (seu brilho, sua energia peculiar) ou o comportamento incomum dos envolvidos, sugerindo que algo mais está em jogo do que uma simples guerrinha de gangues."
      },
      "camada_informacao": {
        "id_matriz": 2,
        "conexao_explicada": "A 'desconfiança generalizada' no mercado, combinada com uma pista que é apresentada como incriminatória, mas carrega um detalhe estranho, começa a plantar sementes de dúvida. O rastro de destruição do mercado, com o burburinho agitado se tornando pânico, sugere que há mais do que apenas o roubo em jogo."
      }
    },
    {
      "ordem": 3,
      "meta_estrutura": "Frustração (Barreira)",
      "local_sugerido": "A Oficina do Tio Gus",
      "o_pressagio": "Ao seguir uma linha de investigação ou tentar obter mais informações, os jogadores se deparam com uma reviravolta chocante. Em uma visita à Oficina do Tio Gus, um mecânico conhecido por todos na área, eles podem encontrar evidências plantadas (uma pequena peça específica da Sombra Metálica deixada 'acidentalmente', um recibo forjado) que incriminam os rivais. Ou, pior, eles podem encontrar o próprio Silas, disfarçado de um mecânico auxiliar, oferecendo 'ajuda' que os induz a erro. Se confrontado, Silas pode tentar uma fuga rápida, revelando ter habilidades que não condizem com um simples engenheiro, ou pode ser pego sabotando um de seus próprios veículos para parecer um ataque da Sombra Metálica.",
      "argumento_arco_historia": "Neste ponto, Silas (sob o disfarce de 'ajuda' ou como o perpetrador de uma armadilha) ativamente trabalha para incriminar a Sombra Metálica e desviar a atenção da verdadeira natureza da carga. A Oficina do Tio Gus serve como um local onde essa manipulação pode ser executada. O perigo de Silas pode se manifestar através de um ataque contra os jogadores disfarçado de incidente com a Sombra Metálica, ou ele pode simplesmente ser visto plantando evidências. A 'Manipulação de Silas' como perigo ativo está em pleno andamento.",
      "premissas_arco_historia": {
        "evidente": "As pistas coletadas parecem conclusivas: a Sombra Metálica preparou uma armadilha, com evidências sendo deliberadamente deixadas para implicá-los ainda mais. A ação iminente de Silas, visando desacreditar ou neutralizar os jogadores, pode se manifestar como uma tentativa de sabotagem ou um confronto direto com falsos culpados.",
        "oculta": "A verdade é que o culpado é um 'insider' (Silas), que está usando as habilidades de engenharia e seu conhecimento 'dos Ferros-Velhos' para incriminar a gangue rival. As 'evidências' são plantadas, e o confronto real é uma distração orquestrada para mascarar a verdadeira agenda de Silas ou a natureza da carga."
      },
      "camada_informacao": {
        "id_matriz": 2,
        "conexao_explicada": "A revelação de que o culpado é um 'insider' acontece aqui, com Silas sendo o fetiche. As evidências plantadas fortalecem a ideia de que a Sombra Metálica é a vilã, mas a intervenção de Silas introduz a dúvida sobre a narrativa estabelecida. O rastro de destruição da manipulação de Silas fica evidente com as evidências plantadas."
      }
    },
    {
      "ordem": 4,
      "meta_estrutura": "O Pesadelo",
      "local_sugerido": "A Mansão de \"Mandíbula\" Mortem",
      "o_pressagio": "Investigando mais a fundo ou seguindo uma nova pista (talvez relacionada ao destino dos cristais), os jogadores podem encontrar uma forma de acessar ou observar a Mansão de \"Mandíbula\" Mortem. Eles podem testemunhar, ou interceptar comunicações secretas, que revelam o verdadeiro plano de Mortem: a guerra iminente não é uma resposta ao roubo, mas um pretexto para encobrir seu próprio tráfico dos cristais de éter para uma potência estrangeira, ou para financiar experimentos perigosos com eles, sem a interferência de rivais ou da lei. A informação é apresentada de forma fragmentada, mas perturbadora, sugerindo uma conspiração muito maior do que uma simples guerra de gangues.",
      "argumento_arco_historia": "Os jogadores obtêm informações cruciais sobre a verdadeira motivação de Mandíbula Mortem. Isso pode ser através de espionagem na Mansão de Mortem, interceptação de comunicações, ou interrogando um membro subalterno dos Ferros-Velhos que se sente desiludido. O objetivo é expor que a própria gangue Ferros-Velhos tem seus próprios planos nefastos, que vão além da simples disputa territorial, e que a guerra é um benefício para eles. A 'Falsa Guerra' é o tema aqui.",
      "premissas_arco_historia": {
        "evidente": "Fica claro que 'Mandíbula' Mortem não agiu apenas por vingança. Ele vê a guerra como uma oportunidade de ouro para encobrir suas próprias transações secretas e para avançar em seus projetos pessoais usando os cristais de éter. A credibilidade da Sombra Metálica como única culpada é questionada.",
        "oculta": "O líder dos Ferros-Velhos está ativamente manipulando o conflito para proveito próprio, usando os cristais como uma ferramenta para negociações secretas ou para financiar experimentos perigosos, revelando que a guerra pode ser uma fachada para um esquema de poder mais sinistro e egoísta."
      },
      "camada_informacao": {
        "id_matriz": 3,
        "conexao_explicada": "A descoberta das motivações ocultas de Mandíbula Mortem revela a verdade sobre a 'Falsa Guerra'. A expectativa de que a guerra é uma consequência do roubo é quebrada. A 'Camuflagem' de ele querer a guerra como pretexto para seus planos é exposta, e a possibilidade de tráfico ou experimentos secretos é lançada."
      }
    },
    {
      "ordem": 5,
      "meta_estrutura": "Completude",
      "local_sugerido": "O Laboratório de Química Clandestino de Silas",
      "o_pressagio": "Com o amanhecer se aproximando rapidamente e as tensões no auge, os jogadores são levados (pela lógica da trama ou por uma pista final deixada por Silas, que pode querer que seu plano seja exposto de verdade) ao Laboratório de Química Clandestino de Silas. Lá, eles o encontram finalizando seu plano. Ele pode estar prestes a detonar uma diversão para encobrir a fuga de algo, ou ativando o que resta de sua manipulação de modo que a culpa recaia totalmente sobre a Sombra Metálica. Há uma chance de confrontá-lo, descobrir sua motivação por trás da manipulação, e talvez um vislumbre dos cristais de éter em seu estado mais volátil e perigoso, em meio aos recipientes de produtos químicos fumegantes.",
      "argumento_arco_historia": "Este é o clímax do arcabouço de Silas. Os jogadores o encontram em seu laboratório secreto, onde ele gerencia os estágios finais de seu plano. A 'Ação Iminente' de Silas, um dispositivo de distração para mascarar a verdade, está em pleno efeito. Os jogadores têm a oportunidade de confrontá-lo, entender sua visão distorcida de justiça e talvez obter a prova final sobre a manipulação, a natureza dos cristais e a verdadeira culpabilidade que recai sobre os Ferros-Velhos.",
      "premissas_arco_historia": {
        "evidente": "Silas está no centro de toda a confusão, agindo como um agente do caos. Ele pode ser confrontado ou observado enquanto tenta executar a última fase de sua armadilha e manipulação, com a iminência do amanhecer e da guerra total como pano de fundo.",
        "oculta": "Silas, o engenheiro dissidente, revela sua verdadeira motivação: expor a corrupção tanto de Mortem quanto, potencialmente, da gangue que ele incriminou. A 'vitória' dele seria a revelação da verdade, custe o que custar, e o confronto final pode revelar a instabilidade dos próprios cristais nas mãos de qualquer um."
      },
      "camada_informacao": {
        "id_matriz": 2,
        "conexao_explicada": "O confronto final com Silas revela a manipulação, validando a 'Revelação' de que o verdadeiro ladrão era um 'insider' com motivos complexos. Isso também pode correlacionar com a 'Natureza da Carga', pois o laboratório de Silas é o local ideal para descobrir o quão instáveis e perigosos os cristais realmente são, especialmente em um ambiente controlado por ele."
      }
    }
  ],
  "perguntas_dramatica": [
    "Até onde os jogadores estão dispostos a ir para manter a paz, ou para instigar a guerra, quando descobrem que ambos os lados envolvidos na disputa são corruptos e que um número significativo de inocentes pode ser pego no fogo cruzado?",
    "Como a descoberta da verdadeira natureza dos cristais de éter afetará a confiança dos jogadores em seus empregadores ou em seus aliados, especialmente se eles forem forçados a usar ou a proteger essa commodity volátil?",
    "Será que a busca pela verdade e a exposição dos planos secretos dos líderes das gangues justificarão o caos e a violência que eles desencadeiam, ou os jogadores se tornarão responsáveis pela própria destruição que buscavam impedir?"
  ]
}
```
