# Relatório: Teste Completo: Trama -> Frente -> Arco
**Data:** 2026_01_19_23_04 | **Status:** ✅ Sucesso

## 📊 Métricas de Execução

| Métrica | 1. Trama | 2. Frente Step 1 | 3. Frente Step 2 | 4. Frente Step 3 | 5. Arco História | Total |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Tempo Total** | 7.93s | 9.48s | 7.32s | 16.19s | 14.02s | **54.93s** |
| **Tokens Entrada** | 877 | 2830 | 3729 | 6780 | 3790 | **18006** |
| **Tokens Saída** | 1733 | 1935 | 1430 | 3498 | 2932 | **11528** |
| **Tokens Total** | 2610 | 4765 | 5159 | 10278 | 6722 | **29534** |
| **Custo Estimado** | $0.000781 | $0.001057 | $0.000945 | $0.002077 | $0.001552 | **$0.006412** |

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
      "Ação Frenética"
    ],
    "escopo": "Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.",
    "justificativa_escopo": "A ameaça de guerra entre gangues e o roubo de uma carga valiosa se encaixam perfeitamente em um ambiente confinado como um assentamento isolado, onde as tensões podem escalar rapidamente e o tempo é crucial.",
    "justificativa_estilo": "A combinação de um roubo com prazo apertado e a consequência de guerra entre gangues evoca a atmosfera sombria e tensa do Noir, enquanto a urgência em recuperar a carga sugere momentos de Ação Frenética com perseguições e confrontos."
  },
  "argumento": {
    "texto": "Na noite fria e ventosa que precede o amanhecer, a estação de processamento de minerais de 'Fagulha Negra', um assentamento isolado nas terras baldias, está à beira do caos. Uma carga valiosa de 'Éter Condensado', um recurso essencial para a tecnologia dieselpunk, foi roubada do cofre principal, não por uma gangue rival, mas por um membro da própria administração local, o Chefe de Segurança Grigor Volkov. Volkov planeja vender o Éter a uma facção externa para financiar sua fuga e iniciar uma nova vida longe das disputas internas, fingindo que o roubo foi obra da gangue 'Os Corvos de Ferro' para desviar a atenção e incriminar seus rivais, garantindo que a inevitável guerra entre gangues o beneficie, eliminando concorrentes no futuro para o controle das rotas da região.",
    "justificativa": "O 'onde' é a estação 'Fagulha Negra'. O 'quando' é a noite que precede o amanhecer. O 'quem' são os jogadores, a administração da estação, o Chefe de Segurança Grigor Volkov, e as gangues 'Os Corvos de Ferro' e uma facção externa. O 'por que' de Volkov é financiar sua fuga incriminando rivais e enfraquecendo a oposição. O 'como' é o roubo orquestrado para parecer obra de outra gangue e a subsequente tensão que isso gera."
  },
  "premissas": {
    "evidente": {
      "texto": "Uma carga vital de 'Éter Condensado' foi roubada do cofre principal da estação 'Fagulha Negra'. Se não for recuperada antes do amanhecer, a estação se tornará alvo de represálias imediatas por parte da violenta gangue rival 'Os Corvos de Ferro', mergulhando o assentamento em uma guerra sangrenta que ninguém sobreviverá.",
      "funcao": "Instigar os jogadores a agir com urgência, focando na recuperação da carga e na prevenção da guerra iminente, sem revelar a verdadeira natureza do roubo ou os motivos por trás dele."
    },
    "oculta": {
      "texto": "O roubo não foi realizado pela gangue rival, mas sim pelo próprio Chefe de Segurança da estação, Grigor Volkov. Ele planeja vender o Éter Condensado a uma facção externa, usando a acusação falsa contra 'Os Corvos de Ferro' como distração para encobrir seu crime, ganhar tempo para sua fuga e neutralizar seus rivais no futuro, fomentando uma guerra que ele espera que o beneficie.",
      "funcao": "Revelar a traição interna e a manipulação de Volkov, mudando o foco da missão de simples recuperação para confronto com um traidor e desmantelamento de um plano maior, subvertendo a expectativa de uma simples caça a ladrões."
    },
    "justificativa": "A premissa evidente estabelece a urgência e o conflito externo esperado (guerra entre gangues). A premissa oculta introduz o elemento de traição e manipulação interna, transformando a natureza do problema e os antagonistas em potencial."
  },
  "matriz_controle_informacao": {
    "itens": [
      {
        "titulo": "Identidade do Ladrão",
        "a_verdade": "O Chefe de Segurança, Grigor Volkov, roubou a carga.",
        "a_expectativa": "A gangue 'Os Corvos de Ferro' roubou a carga.",
        "a_camuflagem": "As evidências iniciais foram plantadas por Volkov para incriminar 'Os Corvos de Ferro' (impressões digitais falsificadas, marcas de botas genéricas). Ele também pode ter espalhado rumores ou desinformação.",
        "o_gatilho": "Investigar o local do roubo com atenção aos detalhes (ex: análise forense das impressões digitais, rastreamento de um veículo específico), interrogar funcionários que trabalham sob Volkov.",
        "a_revelacao": "Descobrir que as evidências são falsas e que as ações de Volkov são suspeitamente convenientes para a fuga."
      },
      {
        "titulo": "O Destino da Carga",
        "a_verdade": "A carga está sendo preparada para ser vendida a uma facção externa por Volkov.",
        "a_expectativa": "A carga foi levada pela gangue 'Os Corvos de Ferro' para ser usada em seus domínios.",
        "a_camuflagem": "Informações limitadas sobre o paradeiro da carga, com Volkov mantendo controle sobre quaisquer pistas sólidas. Pode haver falsos rastros ou rumores sobre a localização.",
        "o_gatilho": "Interceptar comunicações de Volkov com a facção externa, rastrear o esconderijo temporário da carga, ou interrogar um cúmplice de Volkov.",
        "a_revelacao": "Pistas que levam à carga e à negociação em andamento com a facção externa, revelando o plano de Volkov de vender em vez de usar ou esconder a carga para si."
      },
      {
        "titulo": "Motivação de Volkov",
        "a_verdade": "Volkov quer fugir e usar a venda do Éter para financiar uma nova vida e eliminar rivais.",
        "a_expectativa": "Volkov (ou a gangue) roubou a carga para obter poder imediato ou para usá-la em benefício próprio na guerra entre gangues.",
        "a_camuflagem": "Volkov age de forma a parecer um líder preocupado e eficiente, desviando a atenção de seus planos pessoais. Ele usa a ameaça da guerra como cortina de fumaça.",
        "o_gatilho": "Descobrir os planos de fuga de Volkov (passagens compradas, um veículo escondido, economias secretas), encontrar evidências de contato com a facção externa fora do contexto de segurança da estação.",
        "a_revelacao": "A percepção de que Volkov está agindo por interesse próprio para escapar, e não para ganhos de guerra ou poder local."
      }
    ],
    "justificativa": "Esses itens da matriz ajudam a gerenciar a revelação gradual de que o roubo não foi obra de uma gangue externa, mas sim de um ato traiçoeiro interno por parte de Volkov. A expectativa inicial (gangues) é gradualmente substituída pela verdade (traição interna, fuga pessoal), criando surpresa e um dilema moral para os jogadores."
  }
}
```

## 2. 2. Frente Step 1 (Módulo: `step1_front_archetype`)
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
* **Subgêneros:** Noir, Ação Frenética
* **Escopo Geográfico:** Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.
* **Pool de Tipos de Locais (Inspiração):** Arena de Lutas, Ferro velho, Fila da ração, Armazém de comida, Mercado de pulgas, Bar movimentado, Mansão de um senhor de armas, Festival de Música, Torre de Vigia, Pista de Obstáculos, Escombros, Oficina de carros, Laboratório de química, Ferro Velho

### 2. A Alma da História
* **Argumento:** Na noite fria e ventosa que precede o amanhecer, a estação de processamento de minerais de 'Fagulha Negra', um assentamento isolado nas terras baldias, está à beira do caos. Uma carga valiosa de 'Éter Condensado', um recurso essencial para a tecnologia dieselpunk, foi roubada do cofre principal, não por uma gangue rival, mas por um membro da própria administração local, o Chefe de Segurança Grigor Volkov. Volkov planeja vender o Éter a uma facção externa para financiar sua fuga e iniciar uma nova vida longe das disputas internas, fingindo que o roubo foi obra da gangue 'Os Corvos de Ferro' para desviar a atenção e incriminar seus rivais, garantindo que a inevitável guerra entre gangues o beneficie, eliminando concorrentes no futuro para o controle das rotas da região.
* **Premissa Evidente (Missão):** Uma carga vital de 'Éter Condensado' foi roubada do cofre principal da estação 'Fagulha Negra'. Se não for recuperada antes do amanhecer, a estação se tornará alvo de represálias imediatas por parte da violenta gangue rival 'Os Corvos de Ferro', mergulhando o assentamento em uma guerra sangrenta que ninguém sobreviverá.
* **Premissa Oculta (Twist):** O roubo não foi realizado pela gangue rival, mas sim pelo próprio Chefe de Segurança da estação, Grigor Volkov. Ele planeja vender o Éter Condensado a uma facção externa, usando a acusação falsa contra 'Os Corvos de Ferro' como distração para encobrir seu crime, ganhar tempo para sua fuga e neutralizar seus rivais no futuro, fomentando uma guerra que ele espera que o beneficie.

### 3. Segredos da Campanha (Matriz)
Use estes segredos para garantir que os locais contenham pistas ou conexões temáticas com a verdade maior:
  - Titulo: Identidade do Ladrão
  - A verdade: O Chefe de Segurança, Grigor Volkov, roubou a carga.
  - A expectativa: A gangue 'Os Corvos de Ferro' roubou a carga.
  - A camuflagem: As evidências iniciais foram plantadas por Volkov para incriminar 'Os Corvos de Ferro' (impressões digitais falsificadas, marcas de botas genéricas). Ele também pode ter espalhado rumores ou desinformação.
  - O gatilho: Investigar o local do roubo com atenção aos detalhes (ex: análise forense das impressões digitais, rastreamento de um veículo específico), interrogar funcionários que trabalham sob Volkov.
  - A revelacao: Descobrir que as evidências são falsas e que as ações de Volkov são suspeitamente convenientes para a fuga.

  - Titulo: O Destino da Carga
  - A verdade: A carga está sendo preparada para ser vendida a uma facção externa por Volkov.
  - A expectativa: A carga foi levada pela gangue 'Os Corvos de Ferro' para ser usada em seus domínios.
  - A camuflagem: Informações limitadas sobre o paradeiro da carga, com Volkov mantendo controle sobre quaisquer pistas sólidas. Pode haver falsos rastros ou rumores sobre a localização.
  - O gatilho: Interceptar comunicações de Volkov com a facção externa, rastrear o esconderijo temporário da carga, ou interrogar um cúmplice de Volkov.
  - A revelacao: Pistas que levam à carga e à negociação em andamento com a facção externa, revelando o plano de Volkov de vender em vez de usar ou esconder a carga para si.

  - Titulo: Motivação de Volkov
  - A verdade: Volkov quer fugir e usar a venda do Éter para financiar uma nova vida e eliminar rivais.
  - A expectativa: Volkov (ou a gangue) roubou a carga para obter poder imediato ou para usá-la em benefício próprio na guerra entre gangues.
  - A camuflagem: Volkov age de forma a parecer um líder preocupado e eficiente, desviando a atenção de seus planos pessoais. Ele usa a ameaça da guerra como cortina de fumaça.
  - O gatilho: Descobrir os planos de fuga de Volkov (passagens compradas, um veículo escondido, economias secretas), encontrar evidências de contato com a facção externa fora do contexto de segurança da estação.
  - A revelacao: A percepção de que Volkov está agindo por interesse próprio para escapar, e não para ganhos de guerra ou poder local.

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
    "meta_estrutura_resumo": "1. Tentação -> 2. Fase do Sonho (O Crime Compensa) -> 3. A Frustração (Consequências) -> 4. O Pesadelo (Perda de Controle) -> 5. Destruição.",
    "foco_narrativo": "Noir Dieselpunk de Paranoia e Traição: Uma atmosfera de desconfiança onde a linha entre herói e vilão se torna turva, sob a constante ameaça de explosões iminentes e o fedor de combustível e poluição."
  },
  "lista_locais": [
    {
      "nome": "Posto de Controle da Cratera",
      "descricao": "Onde o vento uiva através de chapas de metal enferrujadas e faíscas dançam preguiçosamente de um gerador moribundo. O ar é pesado com o cheiro de óleo queimado e ozônio, misturado ao odor metálico de sangue seco. Este é o primeiro ponto de contato com a 'Fagulha Negra', uma estação escavada em uma antiga cratera de impacto, com torres de vigia improvisadas que se projetam precariamente contra o céu tempestuoso.",
      "tags": "Dieselpunk, Noir, Fronteira, Vigilância, Perigo Iminente",
      "funcao": "Inicial",
      "ancora_geografica": "Situado na entrada principal da estação 'Fagulha Negra', ligando o deserto escaldante exterior a todas as rotas internas da base. O acesso é feito por uma ponte pênsil instável sobre um abismo, com postos de guarda improvisados de sucata ao redor."
    },
    {
      "nome": "Mercado Sombrio das Quebradas",
      "descricao": "Um labirinto de barracas improvisadas sob lonas rasgadas, onde o murmúrio de barganhas se mistura ao som discordante de uma caixa de música quebrada. O cheiro de carne defumada e solventes químicos paira no ar denso. Luzes fracas de lampiões a gás pingam sombras sinistras sobre rostos desconfiados.",
      "tags": "Mercado Negro, Intriga, Dieselpunk, Comunidade, Sobrevivência",
      "funcao": "Intermediario",
      "ancora_geografica": "Aninhado nos níveis inferiores da estação, acessível por elevadores de carga ruidosos e escadarias escorregadias. Ouve-se o zumbido constante das máquinas de processamento vindas de cima, e o cheiro pungente de combustível de alto octanagem emana da Oficina dos 'Corvos de Ferro' próxima."
    },
    {
      "nome": "Oficina do Inferno sobre Rodas",
      "descricao": "Explosões esporádicas de soldas ecoam neste espaço cavernoso, iluminado por um brilho laranja intermitente. O cheiro pungente de metal derretido e graxa saturada de óleo enche o ar. Sucata de veículos modificados e peças sobressalentes formam pilhas caóticas, com o ruído constante de ferramentas pneumáticas.",
      "tags": "Dieselpunk, Oficina, Ação, Perigo Mecânico, 'Os Corvos de Ferro'",
      "funcao": "Intermediario",
      "ancora_geografica": "Localizada no distrito industrial da estação, adjacente ao Mercado e sob as principais tubulações de processamento de minerais. O acesso é feito por entradas de serviço discretas e becos estreitos, com a constante vibração do motor de um triturador de sucata impulsionando a estrutura."
    },
    {
      "nome": "Depósito de Ração 'Fome Eterna'",
      "descricao": "As prateleiras metálicas rangem sob o peso de sacos sujos de grãos e conservas de aspecto duvidoso. Um cheiro agridoce de mofo e conservantes sintéticos domina o ambiente. O silêncio é tenso, pontuado apenas pelos rangidos do metal e o ocasional suspiro de desespero de quem espera.",
      "tags": "Ração, Escassez, Desespero, Dieselpunk, Isolado",
      "funcao": "Intermediario",
      "ancora_geografica": "Um anexo dos níveis de habitação, acessível por corredores metálicos estreitos e escadas de emergência. O chão frio e metálico reflete a pouca luz que entra pelas frestas, e o eco de passos parece amplificado pelo vazio dos corredores circundantes."
    },
    {
      "nome": "O Cofre Vazio",
      "descricao": "Onde o ar está estranhamente frio e imóvel, com um leve odor de metal polido e pânico contido. As paredes do cofre, outrora impenetráveis, agora exibem sinais de manipulação cuidadosa, não de força bruta. A iluminação é fraca e artificial, projetando sombras longas e distorcidas.",
      "tags": "Roubo, Intrigas, Dieselpunk, Segredo, Confronto Imediato",
      "funcao": "Intermediario",
      "ancora_geografica": "Central na administração da estação, ligado diretamente aos escritórios de Grigor Volkov por um túnel de acesso secreto. Ouve-se o zumbido distante dos sistemas de ventilação da sede principal, e o som abafado do tráfego interno da estação se propaga pelas paredes."
    },
    {
      "nome": "Laboratório de Sintetização de Éter",
      "descricao": "Fervilhando com o silvo de vapor e o zumbido de maquinaria experimental, este laboratório pulsa com uma energia instável. O ar é denso com o cheiro acre de produtos químicos e um leve aroma etéreo de sucesso. Tubos de vidro borbulham com líquidos brilhantes sob luzes de laboratório sinistras.",
      "tags": "Ciência, Perigo Químico, Dieselpunk, Segredo, Criação",
      "funcao": "Climax",
      "ancora_geografica": "Localizado em um anexo mais profundo e isolado da estação, diretamente sob a torre de controle. O acesso é restrito, guardado por sistemas de segurança automatizados e passagens de serviço que se conectam aos túneis subterrâneos. O cheiro de ozônio e resíduos químicos emana com força para os corredores vizinhos."
    },
    {
      "nome": "Torre das Sombras de Grigor",
      "descricao": "Um pináculo solitário de metal e concreto, onde o vento uiva mais forte. A vista panorâmica é obscurecida por nuvens de fuligem, mas oferece um vislumbre do deserto implacável lá fora. O cheiro de café queimado e cigarros baratos paira no ar de seu escritório desordenado, repleto de mapas de rotas de fuga.",
      "tags": "Comando, Traição, Dieselpunk, Paranoia, Controle",
      "funcao": "Climax",
      "ancora_geografica": "Dominando a paisagem da estação, conectada aos níveis inferiores por um elevador de serviço privado e uma escada de emergência externa exposta aos elementos. O som dos rádios de comunicação, tanto oficiais quanto clandestinos, ecoa fracamente através das paredes de metal, e a vista da cidade se estende até o horizonte distante."
    },
    {
      "nome": "Terminal de Carga Oeste",
      "descricao": "Um vasto cemitério de contêineres enferrujados, onde o som metálico do metal batendo uns nos outros ecoa incessantemente sob o céu cinzento. O ar é impregnado com o cheiro de sal marinho esquecido, poeira e combustível diesel barato. As sombras são longas e traiçoeiras, escondendo potenciais emboscadas.",
      "tags": "Logística, Comércio, Dieselpunk, Perigo Oculto, Negociação",
      "funcao": "Climax",
      "ancora_geografica": "Localizado na periferia da estação, onde as principais rotas de suprimento se encontram com o deserto. Conectado a outras áreas por vias de serviço de terra batida e um trilho de carga abandonado que serpenteia para o sul. O som distante de motores de veículos pesados e o apito de apocalipse de um trem de carga que se aproxima marcam a paisagem sonora."
    }
  ]
}
```

## 3. 3. Frente Step 2 (Módulo: `step2_front_worldbuilder`)
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
* **Subgêneros:** Noir, Ação Frenética
* **Escopo Geográfico:** Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.
* **Arquétipo:** Tragédia
* **Foco Narrativo:** Noir Dieselpunk de Paranoia e Traição: Uma atmosfera de desconfiança onde a linha entre herói e vilão se torna turva, sob a constante ameaça de explosões iminentes e o fedor de combustível e poluição.

### 2. Dados dos Locais (Step 1)
>>> DADOS DOS LOCAIS:
> **Posto de Controle da Cratera**
  - Descricao: Onde o vento uiva através de chapas de metal enferrujadas e faíscas dançam preguiçosamente de um gerador moribundo. O ar é pesado com o cheiro de óleo queimado e ozônio, misturado ao odor metálico de sangue seco. Este é o primeiro ponto de contato com a 'Fagulha Negra', uma estação escavada em uma antiga cratera de impacto, com torres de vigia improvisadas que se projetam precariamente contra o céu tempestuoso.
  - Tags: Dieselpunk, Noir, Fronteira, Vigilância, Perigo Iminente
  - Funcao: Inicial
  - Ancora geografica: Situado na entrada principal da estação 'Fagulha Negra', ligando o deserto escaldante exterior a todas as rotas internas da base. O acesso é feito por uma ponte pênsil instável sobre um abismo, com postos de guarda improvisados de sucata ao redor.

> **Mercado Sombrio das Quebradas**
  - Descricao: Um labirinto de barracas improvisadas sob lonas rasgadas, onde o murmúrio de barganhas se mistura ao som discordante de uma caixa de música quebrada. O cheiro de carne defumada e solventes químicos paira no ar denso. Luzes fracas de lampiões a gás pingam sombras sinistras sobre rostos desconfiados.
  - Tags: Mercado Negro, Intriga, Dieselpunk, Comunidade, Sobrevivência
  - Funcao: Intermediario
  - Ancora geografica: Aninhado nos níveis inferiores da estação, acessível por elevadores de carga ruidosos e escadarias escorregadias. Ouve-se o zumbido constante das máquinas de processamento vindas de cima, e o cheiro pungente de combustível de alto octanagem emana da Oficina dos 'Corvos de Ferro' próxima.

> **Oficina do Inferno sobre Rodas**
  - Descricao: Explosões esporádicas de soldas ecoam neste espaço cavernoso, iluminado por um brilho laranja intermitente. O cheiro pungente de metal derretido e graxa saturada de óleo enche o ar. Sucata de veículos modificados e peças sobressalentes formam pilhas caóticas, com o ruído constante de ferramentas pneumáticas.
  - Tags: Dieselpunk, Oficina, Ação, Perigo Mecânico, 'Os Corvos de Ferro'
  - Funcao: Intermediario
  - Ancora geografica: Localizada no distrito industrial da estação, adjacente ao Mercado e sob as principais tubulações de processamento de minerais. O acesso é feito por entradas de serviço discretas e becos estreitos, com a constante vibração do motor de um triturador de sucata impulsionando a estrutura.

> **Depósito de Ração 'Fome Eterna'**
  - Descricao: As prateleiras metálicas rangem sob o peso de sacos sujos de grãos e conservas de aspecto duvidoso. Um cheiro agridoce de mofo e conservantes sintéticos domina o ambiente. O silêncio é tenso, pontuado apenas pelos rangidos do metal e o ocasional suspiro de desespero de quem espera.
  - Tags: Ração, Escassez, Desespero, Dieselpunk, Isolado
  - Funcao: Intermediario
  - Ancora geografica: Um anexo dos níveis de habitação, acessível por corredores metálicos estreitos e escadas de emergência. O chão frio e metálico reflete a pouca luz que entra pelas frestas, e o eco de passos parece amplificado pelo vazio dos corredores circundantes.

> **O Cofre Vazio**
  - Descricao: Onde o ar está estranhamente frio e imóvel, com um leve odor de metal polido e pânico contido. As paredes do cofre, outrora impenetráveis, agora exibem sinais de manipulação cuidadosa, não de força bruta. A iluminação é fraca e artificial, projetando sombras longas e distorcidas.
  - Tags: Roubo, Intrigas, Dieselpunk, Segredo, Confronto Imediato
  - Funcao: Intermediario
  - Ancora geografica: Central na administração da estação, ligado diretamente aos escritórios de Grigor Volkov por um túnel de acesso secreto. Ouve-se o zumbido distante dos sistemas de ventilação da sede principal, e o som abafado do tráfego interno da estação se propaga pelas paredes.

> **Laboratório de Sintetização de Éter**
  - Descricao: Fervilhando com o silvo de vapor e o zumbido de maquinaria experimental, este laboratório pulsa com uma energia instável. O ar é denso com o cheiro acre de produtos químicos e um leve aroma etéreo de sucesso. Tubos de vidro borbulham com líquidos brilhantes sob luzes de laboratório sinistras.
  - Tags: Ciência, Perigo Químico, Dieselpunk, Segredo, Criação
  - Funcao: Climax
  - Ancora geografica: Localizado em um anexo mais profundo e isolado da estação, diretamente sob a torre de controle. O acesso é restrito, guardado por sistemas de segurança automatizados e passagens de serviço que se conectam aos túneis subterrâneos. O cheiro de ozônio e resíduos químicos emana com força para os corredores vizinhos.

> **Torre das Sombras de Grigor**
  - Descricao: Um pináculo solitário de metal e concreto, onde o vento uiva mais forte. A vista panorâmica é obscurecida por nuvens de fuligem, mas oferece um vislumbre do deserto implacável lá fora. O cheiro de café queimado e cigarros baratos paira no ar de seu escritório desordenado, repleto de mapas de rotas de fuga.
  - Tags: Comando, Traição, Dieselpunk, Paranoia, Controle
  - Funcao: Climax
  - Ancora geografica: Dominando a paisagem da estação, conectada aos níveis inferiores por um elevador de serviço privado e uma escada de emergência externa exposta aos elementos. O som dos rádios de comunicação, tanto oficiais quanto clandestinos, ecoa fracamente através das paredes de metal, e a vista da cidade se estende até o horizonte distante.

> **Terminal de Carga Oeste**
  - Descricao: Um vasto cemitério de contêineres enferrujados, onde o som metálico do metal batendo uns nos outros ecoa incessantemente sob o céu cinzento. O ar é impregnado com o cheiro de sal marinho esquecido, poeira e combustível diesel barato. As sombras são longas e traiçoeiras, escondendo potenciais emboscadas.
  - Tags: Logística, Comércio, Dieselpunk, Perigo Oculto, Negociação
  - Funcao: Climax
  - Ancora geografica: Localizado na periferia da estação, onde as principais rotas de suprimento se encontram com o deserto. Conectado a outras áreas por vias de serviço de terra batida e um trilho de carga abandonado que serpenteia para o sul. O som distante de motores de veículos pesados e o apito de apocalipse de um trem de carga que se aproxima marcam a paisagem sonora.

### 3. Contexto da Trama
* **Argumento:** Na noite fria e ventosa que precede o amanhecer, a estação de processamento de minerais de 'Fagulha Negra', um assentamento isolado nas terras baldias, está à beira do caos. Uma carga valiosa de 'Éter Condensado', um recurso essencial para a tecnologia dieselpunk, foi roubada do cofre principal, não por uma gangue rival, mas por um membro da própria administração local, o Chefe de Segurança Grigor Volkov. Volkov planeja vender o Éter a uma facção externa para financiar sua fuga e iniciar uma nova vida longe das disputas internas, fingindo que o roubo foi obra da gangue 'Os Corvos de Ferro' para desviar a atenção e incriminar seus rivais, garantindo que a inevitável guerra entre gangues o beneficie, eliminando concorrentes no futuro para o controle das rotas da região.
* **Premissa Evidente:** Uma carga vital de 'Éter Condensado' foi roubada do cofre principal da estação 'Fagulha Negra'. Se não for recuperada antes do amanhecer, a estação se tornará alvo de represálias imediatas por parte da violenta gangue rival 'Os Corvos de Ferro', mergulhando o assentamento em uma guerra sangrenta que ninguém sobreviverá.
* **Premissa Oculta:** O roubo não foi realizado pela gangue rival, mas sim pelo próprio Chefe de Segurança da estação, Grigor Volkov. Ele planeja vender o Éter Condensado a uma facção externa, usando a acusação falsa contra 'Os Corvos de Ferro' como distração para encobrir seu crime, ganhar tempo para sua fuga e neutralizar seus rivais no futuro, fomentando uma guerra que ele espera que o beneficie.

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
  "descricao_frente": "Na sombria e poluída Fagulha Negra, a paranoia reina soberana. O roubo de Éter Condensado do cofre principal não é apenas um crime, mas um catalisador para a traição, que ameaça desmantelar o decrépito assentamento de dentro para fora. As faíscas do conflito iminente ecoam mais alto do que o zumbido dos geradores moribundos, e a linha entre a busca por justiça e a sobrevivência se torna cada vez mais turva.",
  "elenco": [
    {
      "nome": "Grigor Volkov",
      "papel_funcao": "Chefe de Segurança da Fagulha Negra",
      "detalhe_marcante": "Tem o hábito de polir constantemente o cano de sua pistola automática com um lenço de seda, um gesto que exala uma calma ameaçadora.",
      "conviccao": "O poder é a única lei que importa; ele manipula o sistema para seu próprio ganho e fuga, acreditando que a sobrevivência dos mais fortes é o único caminho.",
      "contraste": "Apesar de sua frieza calculista, ele mantém um quadro de seus filhos em seu escritório, olhando para ele frequentemente com uma expressão de saudade."
    },
    {
      "nome": "Os Corvos de Ferro",
      "papel_funcao": "Gangue Rival / Ameaça Externa",
      "detalhe_marcante": "Usam implantes mecânicos toscos e barulhentos em seus membros, tornando seus ataques previsíveis, mas brutalmente eficientes.",
      "conviccao": "Domínio territorial e controle dos recursos; eles acreditam que a força bruta e o medo são os únicos meios de prosperidade e ordem em sua visão de mundo.",
      "contraste": "Seu líder, um brutamontes com um braço prostético coberto de adereços metálicos, é conhecido por organizar competições de poesia improvisada para seus membros em segredo."
    },
    {
      "nome": "Conselheiros da Fagulha Negra",
      "papel_funcao": "Burocratas e Facções Internas",
      "detalhe_marcante": "Nenhum se lembra de seus nomes, mas todos têm um código de cores em suas roupas para identificar sua afiliação, agindo em silêncio e espalhando rumores.",
      "conviccao": "Manter o status quo e garantir sua própria segurança e privilégios, independentemente do custo para os outros.",
      "contraste": "À noite, muitos se reúnem clandestinamente para trocar histórias sobre os dias em que a Fagulha Negra era um lugar de esperança."
    }
  ],
  "perigos": [
    {
      "nome": "A Rede de Informantes de Volkov",
      "tipo": "Organização Religiosa",
      "impulso": "Estabelecer e seguir doutrinas.",
      "ameaca_verdade": "Eles minam a ideia de confiança e lealdade, mostrando que qualquer um pode ser um traidor por um preço, destruindo a força da comunidade.",
      "local_vinculado": "Mercado Sombrio das Quebradas",
      "rastro_destruicao": "Os acordos feitos aqui são sussurrados, com olhares nervosos e pagamentos feitos em cantos escuros, onde a desconfiança é palpável.",
      "acao_iminente": "Volkov está prestes a usar seus informantes para espalhar falsas evidências e incriminar permanentemente os Corvos de Ferro pelo roubo, garantindo que a guerra comece ao amanhecer."
    },
    {
      "nome": "A Escalada da Violência dos Corvos de Ferro",
      "tipo": "Horda",
      "impulso": "Crescer em força e destruir.",
      "ameaca_verdade": "A gangue representa a brutalidade desenfreada que ameaça engolir a Fagulha Negra, desafiando a ideia de que a ordem pode ser mantida sem violência ou autoridade.",
      "local_vinculado": "Oficina do Inferno sobre Rodas",
      "rastro_destruicao": "A oficina está um caos de metal retorcido e marcas de batalha recentes, com veículos em chamas abandonados e um rastro de destruição que leva para fora.",
      "acao_iminente": "Os Corvos de Ferro pretendem incendiar a Oficina, destruindo a capacidade de reparo da estação e usando o fogo como cortina de fumaça para lançar seu ataque inicial contra os postos de guarda."
    },
    {
      "nome": "A Instabilidade do Laboratório de Éter",
      "tipo": "Lugar Amaldiçoado",
      "impulso": "Ser controlado ou domado.",
      "ameaca_verdade": "O laboratório é um símbolo do progresso perigoso e instável que levou a Fagulha Negra ao seu estado atual, mostrando que a busca por poder tecnológico pode ter um custo catastrófico.",
      "local_vinculado": "Laboratório de Sintetização de Éter",
      "rastro_destruicao": "Vazamentos químicos têm corroído o metal circundante, e explosões menores criaram crateras irregulares nos corredores de acesso, com sinais de evacuação apressada.",
      "acao_iminente": "Uma reação em cadeia iminente no laboratório ameaça causar uma explosão massiva que devastaria a seção administrativa e vital da estação, tornando a fuga de Volkov impossível ou, pior, atingindo a Torre das Sombras dele."
    }
  ],
  "desastre_iminente": {
    "tipo_desastre": "Destruição",
    "descricao": "Se o Éter Condensado não for recuperado e a verdadeira identidade do ladrão não for revelada, a Fagulha Negra será obliterada. A guerra total eclodirá entre os Corvos de Ferro e as forças de segurança (lideradas por Volkov, que orquestra o caos), culminando em uma explosão massiva do Laboratório de Éter, varrendo o assentamento do mapa e transformando-o em um monumento silencioso à traição e à autodestruição."
  }
}
```

## 4. 4. Frente Step 3 (Módulo: `step3_front_storyteller`)
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
* **Subgêneros:** Noir, Ação Frenética
* **Escopo Geográfico:** Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.

### 2. Contexto da Trama
* **Argumento:** Na noite fria e ventosa que precede o amanhecer, a estação de processamento de minerais de 'Fagulha Negra', um assentamento isolado nas terras baldias, está à beira do caos. Uma carga valiosa de 'Éter Condensado', um recurso essencial para a tecnologia dieselpunk, foi roubada do cofre principal, não por uma gangue rival, mas por um membro da própria administração local, o Chefe de Segurança Grigor Volkov. Volkov planeja vender o Éter a uma facção externa para financiar sua fuga e iniciar uma nova vida longe das disputas internas, fingindo que o roubo foi obra da gangue 'Os Corvos de Ferro' para desviar a atenção e incriminar seus rivais, garantindo que a inevitável guerra entre gangues o beneficie, eliminando concorrentes no futuro para o controle das rotas da região.
* **Premissa Evidente:** Uma carga vital de 'Éter Condensado' foi roubada do cofre principal da estação 'Fagulha Negra'. Se não for recuperada antes do amanhecer, a estação se tornará alvo de represálias imediatas por parte da violenta gangue rival 'Os Corvos de Ferro', mergulhando o assentamento em uma guerra sangrenta que ninguém sobreviverá.
* **Premissa Oculta:** O roubo não foi realizado pela gangue rival, mas sim pelo próprio Chefe de Segurança da estação, Grigor Volkov. Ele planeja vender o Éter Condensado a uma facção externa, usando a acusação falsa contra 'Os Corvos de Ferro' como distração para encobrir seu crime, ganhar tempo para sua fuga e neutralizar seus rivais no futuro, fomentando uma guerra que ele espera que o beneficie.
* **Arquétipos Permitidos:** Músculo: Você é grande, pesado. Machucar e fazer façanhas físicas é com você., Cabeça: Pensamento ágil, consegue operar sistemas e máquinas antigas., Volante: Atrás de um volante, não há igual. Você é uma fera das estradas., Vigia: Olhos atentos e sempre no horizonte. Consegue atirar muito bem., Boca: Sempre sabe o que dizer. Carisma em pessoa. Mesmo que isso traga problemas., Novato: Nunca conheceu um mundo que não esse. Quer provar seu valor para os seus.

### 3. Dados da Fase 1 (Estrutura)
* **Arquétipo Selecionado:** Tragédia
* **Foco Narrativo:** Noir Dieselpunk de Paranoia e Traição: Uma atmosfera de desconfiança onde a linha entre herói e vilão se torna turva, sob a constante ameaça de explosões iminentes e o fedor de combustível e poluição.

>>> LISTA DE LOCAIS (Referência para Localização dos Presságios):
> **Posto de Controle da Cratera**
  - Descricao: Onde o vento uiva através de chapas de metal enferrujadas e faíscas dançam preguiçosamente de um gerador moribundo. O ar é pesado com o cheiro de óleo queimado e ozônio, misturado ao odor metálico de sangue seco. Este é o primeiro ponto de contato com a 'Fagulha Negra', uma estação escavada em uma antiga cratera de impacto, com torres de vigia improvisadas que se projetam precariamente contra o céu tempestuoso.
  - Tags: Dieselpunk, Noir, Fronteira, Vigilância, Perigo Iminente
  - Funcao: Inicial
  - Ancora geografica: Situado na entrada principal da estação 'Fagulha Negra', ligando o deserto escaldante exterior a todas as rotas internas da base. O acesso é feito por uma ponte pênsil instável sobre um abismo, com postos de guarda improvisados de sucata ao redor.

> **Mercado Sombrio das Quebradas**
  - Descricao: Um labirinto de barracas improvisadas sob lonas rasgadas, onde o murmúrio de barganhas se mistura ao som discordante de uma caixa de música quebrada. O cheiro de carne defumada e solventes químicos paira no ar denso. Luzes fracas de lampiões a gás pingam sombras sinistras sobre rostos desconfiados.
  - Tags: Mercado Negro, Intriga, Dieselpunk, Comunidade, Sobrevivência
  - Funcao: Intermediario
  - Ancora geografica: Aninhado nos níveis inferiores da estação, acessível por elevadores de carga ruidosos e escadarias escorregadias. Ouve-se o zumbido constante das máquinas de processamento vindas de cima, e o cheiro pungente de combustível de alto octanagem emana da Oficina dos 'Corvos de Ferro' próxima.

> **Oficina do Inferno sobre Rodas**
  - Descricao: Explosões esporádicas de soldas ecoam neste espaço cavernoso, iluminado por um brilho laranja intermitente. O cheiro pungente de metal derretido e graxa saturada de óleo enche o ar. Sucata de veículos modificados e peças sobressalentes formam pilhas caóticas, com o ruído constante de ferramentas pneumáticas.
  - Tags: Dieselpunk, Oficina, Ação, Perigo Mecânico, 'Os Corvos de Ferro'
  - Funcao: Intermediario
  - Ancora geografica: Localizada no distrito industrial da estação, adjacente ao Mercado e sob as principais tubulações de processamento de minerais. O acesso é feito por entradas de serviço discretas e becos estreitos, com a constante vibração do motor de um triturador de sucata impulsionando a estrutura.

> **Depósito de Ração 'Fome Eterna'**
  - Descricao: As prateleiras metálicas rangem sob o peso de sacos sujos de grãos e conservas de aspecto duvidoso. Um cheiro agridoce de mofo e conservantes sintéticos domina o ambiente. O silêncio é tenso, pontuado apenas pelos rangidos do metal e o ocasional suspiro de desespero de quem espera.
  - Tags: Ração, Escassez, Desespero, Dieselpunk, Isolado
  - Funcao: Intermediario
  - Ancora geografica: Um anexo dos níveis de habitação, acessível por corredores metálicos estreitos e escadas de emergência. O chão frio e metálico reflete a pouca luz que entra pelas frestas, e o eco de passos parece amplificado pelo vazio dos corredores circundantes.

> **O Cofre Vazio**
  - Descricao: Onde o ar está estranhamente frio e imóvel, com um leve odor de metal polido e pânico contido. As paredes do cofre, outrora impenetráveis, agora exibem sinais de manipulação cuidadosa, não de força bruta. A iluminação é fraca e artificial, projetando sombras longas e distorcidas.
  - Tags: Roubo, Intrigas, Dieselpunk, Segredo, Confronto Imediato
  - Funcao: Intermediario
  - Ancora geografica: Central na administração da estação, ligado diretamente aos escritórios de Grigor Volkov por um túnel de acesso secreto. Ouve-se o zumbido distante dos sistemas de ventilação da sede principal, e o som abafado do tráfego interno da estação se propaga pelas paredes.

> **Laboratório de Sintetização de Éter**
  - Descricao: Fervilhando com o silvo de vapor e o zumbido de maquinaria experimental, este laboratório pulsa com uma energia instável. O ar é denso com o cheiro acre de produtos químicos e um leve aroma etéreo de sucesso. Tubos de vidro borbulham com líquidos brilhantes sob luzes de laboratório sinistras.
  - Tags: Ciência, Perigo Químico, Dieselpunk, Segredo, Criação
  - Funcao: Climax
  - Ancora geografica: Localizado em um anexo mais profundo e isolado da estação, diretamente sob a torre de controle. O acesso é restrito, guardado por sistemas de segurança automatizados e passagens de serviço que se conectam aos túneis subterrâneos. O cheiro de ozônio e resíduos químicos emana com força para os corredores vizinhos.

> **Torre das Sombras de Grigor**
  - Descricao: Um pináculo solitário de metal e concreto, onde o vento uiva mais forte. A vista panorâmica é obscurecida por nuvens de fuligem, mas oferece um vislumbre do deserto implacável lá fora. O cheiro de café queimado e cigarros baratos paira no ar de seu escritório desordenado, repleto de mapas de rotas de fuga.
  - Tags: Comando, Traição, Dieselpunk, Paranoia, Controle
  - Funcao: Climax
  - Ancora geografica: Dominando a paisagem da estação, conectada aos níveis inferiores por um elevador de serviço privado e uma escada de emergência externa exposta aos elementos. O som dos rádios de comunicação, tanto oficiais quanto clandestinos, ecoa fracamente através das paredes de metal, e a vista da cidade se estende até o horizonte distante.

> **Terminal de Carga Oeste**
  - Descricao: Um vasto cemitério de contêineres enferrujados, onde o som metálico do metal batendo uns nos outros ecoa incessantemente sob o céu cinzento. O ar é impregnado com o cheiro de sal marinho esquecido, poeira e combustível diesel barato. As sombras são longas e traiçoeiras, escondendo potenciais emboscadas.
  - Tags: Logística, Comércio, Dieselpunk, Perigo Oculto, Negociação
  - Funcao: Climax
  - Ancora geografica: Localizado na periferia da estação, onde as principais rotas de suprimento se encontram com o deserto. Conectado a outras áreas por vias de serviço de terra batida e um trilho de carga abandonado que serpenteia para o sul. O som distante de motores de veículos pesados e o apito de apocalipse de um trem de carga que se aproxima marcam a paisagem sonora.

### 4. Dados da Fase 2 (Ameaças e Elenco)
Use estes dados para definir QUEM causa os presságios.

>>> ELENCO PRINCIPAL:
> **Grigor Volkov**
  - Papel funcao: Chefe de Segurança da Fagulha Negra
  - Detalhe marcante: Tem o hábito de polir constantemente o cano de sua pistola automática com um lenço de seda, um gesto que exala uma calma ameaçadora.
  - Conviccao: O poder é a única lei que importa; ele manipula o sistema para seu próprio ganho e fuga, acreditando que a sobrevivência dos mais fortes é o único caminho.
  - Contraste: Apesar de sua frieza calculista, ele mantém um quadro de seus filhos em seu escritório, olhando para ele frequentemente com uma expressão de saudade.

> **Os Corvos de Ferro**
  - Papel funcao: Gangue Rival / Ameaça Externa
  - Detalhe marcante: Usam implantes mecânicos toscos e barulhentos em seus membros, tornando seus ataques previsíveis, mas brutalmente eficientes.
  - Conviccao: Domínio territorial e controle dos recursos; eles acreditam que a força bruta e o medo são os únicos meios de prosperidade e ordem em sua visão de mundo.
  - Contraste: Seu líder, um brutamontes com um braço prostético coberto de adereços metálicos, é conhecido por organizar competições de poesia improvisada para seus membros em segredo.

> **Conselheiros da Fagulha Negra**
  - Papel funcao: Burocratas e Facções Internas
  - Detalhe marcante: Nenhum se lembra de seus nomes, mas todos têm um código de cores em suas roupas para identificar sua afiliação, agindo em silêncio e espalhando rumores.
  - Conviccao: Manter o status quo e garantir sua própria segurança e privilégios, independentemente do custo para os outros.
  - Contraste: À noite, muitos se reúnem clandestinamente para trocar histórias sobre os dias em que a Fagulha Negra era um lugar de esperança.

>>> PERIGOS ATIVOS:
> **A Rede de Informantes de Volkov**
  - Tipo: Organização Religiosa
  - Impulso: Estabelecer e seguir doutrinas.
  - Ameaca verdade: Eles minam a ideia de confiança e lealdade, mostrando que qualquer um pode ser um traidor por um preço, destruindo a força da comunidade.
  - Local vinculado: Mercado Sombrio das Quebradas
  - Rastro destruicao: Os acordos feitos aqui são sussurrados, com olhares nervosos e pagamentos feitos em cantos escuros, onde a desconfiança é palpável.
  - Acao iminente: Volkov está prestes a usar seus informantes para espalhar falsas evidências e incriminar permanentemente os Corvos de Ferro pelo roubo, garantindo que a guerra comece ao amanhecer.

> **A Escalada da Violência dos Corvos de Ferro**
  - Tipo: Horda
  - Impulso: Crescer em força e destruir.
  - Ameaca verdade: A gangue representa a brutalidade desenfreada que ameaça engolir a Fagulha Negra, desafiando a ideia de que a ordem pode ser mantida sem violência ou autoridade.
  - Local vinculado: Oficina do Inferno sobre Rodas
  - Rastro destruicao: A oficina está um caos de metal retorcido e marcas de batalha recentes, com veículos em chamas abandonados e um rastro de destruição que leva para fora.
  - Acao iminente: Os Corvos de Ferro pretendem incendiar a Oficina, destruindo a capacidade de reparo da estação e usando o fogo como cortina de fumaça para lançar seu ataque inicial contra os postos de guarda.

> **A Instabilidade do Laboratório de Éter**
  - Tipo: Lugar Amaldiçoado
  - Impulso: Ser controlado ou domado.
  - Ameaca verdade: O laboratório é um símbolo do progresso perigoso e instável que levou a Fagulha Negra ao seu estado atual, mostrando que a busca por poder tecnológico pode ter um custo catastrófico.
  - Local vinculado: Laboratório de Sintetização de Éter
  - Rastro destruicao: Vazamentos químicos têm corroído o metal circundante, e explosões menores criaram crateras irregulares nos corredores de acesso, com sinais de evacuação apressada.
  - Acao iminente: Uma reação em cadeia iminente no laboratório ameaça causar uma explosão massiva que devastaria a seção administrativa e vital da estação, tornando a fuga de Volkov impossível ou, pior, atingindo a Torre das Sombras dele.

* **Desastre Iminente (Game Over):** Destruição - Se o Éter Condensado não for recuperado e a verdadeira identidade do ladrão não for revelada, a Fagulha Negra será obliterada. A guerra total eclodirá entre os Corvos de Ferro e as forças de segurança (lideradas por Volkov, que orquestra o caos), culminando em uma explosão massiva do Laboratório de Éter, varrendo o assentamento do mapa e transformando-o em um monumento silencioso à traição e à autodestruição.

### 5. Matriz de Controle de Informação
Conecte os presságios aos segredos abaixo (Camada de Informação).

>>> SEGREDOS DA CAMPANHA:
  - Titulo: Identidade do Ladrão
  - A verdade: O Chefe de Segurança, Grigor Volkov, roubou a carga.
  - A expectativa: A gangue 'Os Corvos de Ferro' roubou a carga.
  - A camuflagem: As evidências iniciais foram plantadas por Volkov para incriminar 'Os Corvos de Ferro' (impressões digitais falsificadas, marcas de botas genéricas). Ele também pode ter espalhado rumores ou desinformação.
  - O gatilho: Investigar o local do roubo com atenção aos detalhes (ex: análise forense das impressões digitais, rastreamento de um veículo específico), interrogar funcionários que trabalham sob Volkov.
  - A revelacao: Descobrir que as evidências são falsas e que as ações de Volkov são suspeitamente convenientes para a fuga.

  - Titulo: O Destino da Carga
  - A verdade: A carga está sendo preparada para ser vendida a uma facção externa por Volkov.
  - A expectativa: A carga foi levada pela gangue 'Os Corvos de Ferro' para ser usada em seus domínios.
  - A camuflagem: Informações limitadas sobre o paradeiro da carga, com Volkov mantendo controle sobre quaisquer pistas sólidas. Pode haver falsos rastros ou rumores sobre a localização.
  - O gatilho: Interceptar comunicações de Volkov com a facção externa, rastrear o esconderijo temporário da carga, ou interrogar um cúmplice de Volkov.
  - A revelacao: Pistas que levam à carga e à negociação em andamento com a facção externa, revelando o plano de Volkov de vender em vez de usar ou esconder a carga para si.

  - Titulo: Motivação de Volkov
  - A verdade: Volkov quer fugir e usar a venda do Éter para financiar uma nova vida e eliminar rivais.
  - A expectativa: Volkov (ou a gangue) roubou a carga para obter poder imediato ou para usá-la em benefício próprio na guerra entre gangues.
  - A camuflagem: Volkov age de forma a parecer um líder preocupado e eficiente, desviando a atenção de seus planos pessoais. Ele usa a ameaça da guerra como cortina de fumaça.
  - O gatilho: Descobrir os planos de fuga de Volkov (passagens compradas, um veículo escondido, economias secretas), encontrar evidências de contato com a facção externa fora do contexto de segurança da estação.
  - A revelacao: A percepção de que Volkov está agindo por interesse próprio para escapar, e não para ganhos de guerra ou poder local.

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
      "local_sugerido": "Mercado Sombrio das Quebradas",
      "o_pressagio": "No Mercado Sombrio das Quebradas, um contrabandista desesperado, com a cara marcada pelo estresse e o cheiro de solvente, aborda os jogadores. Ele oferece uma pequena quantidade de Éter Condensado, roubado 'por acidente' durante o caos do roubo principal, por uma quantia modesta. Ele jura que os Corvos de Ferro não o pegaram, e que essa pequena porção pode ser o suficiente para as necessidades de alguém, ou uma pista para algo maior, se tivessem coragem de olhar para onde o Éter realmente vai.",
      "argumento_arco_historia": "Nos becos escuros do Mercado Sombrio das Quebradas, um contrabandista de baixo escalão (influenciado por Volkov através da Rede de Informantes) tenta vender uma pequena porção do Éter Condensado roubado. Ele age sob a pressão de Volkov para espalhar o boato de que o Éter está passando pelas mãos de múltiplos intermediários, e não diretamente com a facção externa, para confundir qualquer investigação. Isso acontece durante o turno da noite, aproveitando a atmosfera de desconfiança e transações ilícitas do mercado.",
      "premissas_arco_historia": {
        "evidente": "Um pequeno roubo de Éter Condensado está sendo oportunamente vendido a preços baixos pelos becos. O contrabandista parece assustado e quer se livrar da carga rapidamente, sugerindo que os Corvos de Ferro podem estar atrás dele.",
        "oculta": "O Éter oferecido é uma isca plantada por Volkov. O contrabandista não roubou o Éter acidentalmente; ele foi instruído a vendê-lo para testar a competência dos jogadores em rastrear o material e, ao mesmo tempo, confirmar que a atenção deles estará focada na carga em si, e não no roubo ou no ladrão."
      },
      "camada_informacao": {
        "id_matriz": 2,
        "conexao_explicada": "Ao aceitar ou rastrear a pequena quantidade de Éter Condensado, os jogadores podem inadvertidamente seguir uma pista falsa plantada por Volkov. Se investigarem mais a fundo a origem do Éter, podem encontrar inconsistências que apontam para uma manipulação, começando a questionar o 'Destino da Carga' e se ela realmente foi levada pelos Corvos de Ferro."
      }
    },
    {
      "ordem": 2,
      "meta_estrutura": "O Crime Compensa",
      "local_sugerido": "Oficina do Inferno sobre Rodas",
      "o_pressagio": "Na Oficina do Inferno sobre Rodas, a atmosfera é de pânico controlado. Mecânicos e membros da gangue 'Os Corvos de Ferro' estão freneticamente tentando apagar um incêndio que começou em uma área de armazenamento de peças. No caos, um dos tenentes mais brutais dos Corvos de Ferro, ostentando um braço mecânico ruidoso, está supervisionando a destruição. Ele exibe uma segurança inabalável, gritando ordens e prometendo recompensas generosas para quem controlar as chamas rapidamente, como se o incêndio não o preocupasse, mas sim fosse uma oportunidade conveniente.",
      "argumento_arco_historia": "A Oficina do Inferno sobre Rodas está em chamas. Este evento é provocado por membros dos 'Corvos de Ferro' sob as ordens de seu tenente, que sabe que Volkov facilitou o incêndio como parte de sua estratégia para incriminar a gangue. O tenente usa o incêndio para destruir evidências de modificações ilegais em veículos que poderiam ser rastreadas até a gangue e para criar uma cortina de fumaça. O incidente ocorre na madrugada, enquanto a estação ainda está imersa na escuridão e no caos inicial do roubo aparente.",
      "premissas_arco_historia": {
        "evidente": "Um incêndio irrompeu na Oficina dos Corvos de Ferro, e a gangue, com surpreendente eficiência, está lutando para contê-lo. O líder parece mais focado em manter a ordem e recompensar seus subordinados do que em apagar o fogo, sugerindo uma desconsideração pela destruição material.",
        "oculta": "O incêndio não é acidental. Foi orquestrado em parte por Volkov para criar uma diversão e incriminar ainda mais os Corvos de Ferro. O tenente da gangue sabe disso e está usando a oportunidade para destruir provas que poderiam ligá-lo a atividades mais sombrias, além de usar a destruição como ponto de largada para o ataque planejado contra os postos de guarda periféricos da estação, simulando um ataque em larga escala."
      },
      "camada_informacao": {
        "id_matriz": 1,
        "conexao_explicada": "Ao investigar o incêndio e a reação dos Corvos de Ferro, os jogadores podem notar a estranha calma do tenente e a destruição seletiva de certos materiais. Se conseguirem acessar as áreas danificadas, podem encontrar restos de evidências que não se encaixam na narrativa de um simple incêndio, começando a desconfiar da 'Identidade do Ladrão' e perceber que as ações da gangue são reativas a um plano maior."
      }
    },
    {
      "ordem": 3,
      "meta_estrutura": "A Frustração",
      "local_sugerido": "Depósito de Ração 'Fome Eterna'",
      "o_pressagio": "No Depósito de Ração 'Fome Eterna', a fila de moradores famintos se estende pelos corredores metálicos frios. A tensão é palpável. De repente, Grigor Volkov aparece, acompanhado por alguns guardas leais. Ele anuncia com frieza que, devido ao 'ataque' dos Corvos de Ferro e ao roubo do Éter, um racionamento mais severo será imposto. Ele culpa publicamente a gangue pela escassez iminente, apontando para os rostos empobrecidos e desnutridos como prova do perigo que eles representam e da necessidade de controle absoluto.",
      "argumento_arco_historia": "Volkov utiliza o Depósito de Ração para aprofundar sua narrativa de que os Corvos de Ferro são os únicos culpados pela crise. Ele anuncia o racionamento severo, justificando-o como uma medida de segurança necessária em tempos de guerra iminente. Na realidade, ele está usando o racionamento para controlar a população, criar mais ressentimento contra a gangue e reduzir os recursos disponíveis para qualquer um que possa se opor a ele, enquanto garante que seus cúmplices tenham acesso privilegiado. Isso ocorre pela manhã, quando a população está mais vulnerável e o impacto de tal anúncio é máximo.",
      "premissas_arco_historia": {
        "evidente": "O roubo do Éter e o incêndio na oficina levaram a uma crise de suprimentos. Volkov, como Chefe de Segurança, está impondo um racionamento severo, culpando abertamente os Corvos de Ferro e enfatizando a necessidade de ordem sob seu comando para a sobrevivência de todos.",
        "oculta": "Volkov está usando a crise de suprimentos como uma ferramenta de controle e manipulação. O racionamento não é apenas uma consequência do roubo, mas uma escolha deliberada para instigar medo e dependência, além de desviar a atenção de seu próprio envolvimento. Ele está consolidando seu poder em meio ao caos, preparando o terreno para sua fuga, pois quer garantir que qualquer oposição esteja enfraquecida e desorganizada."
      },
      "camada_informacao": {
        "id_matriz": 3,
        "conexao_explicada": "Ao observar a reação de Volkov e o anúncio do racionamento, os jogadores podem começar a questionar sua 'Motivação de Volkov'. A forma como ele enquadra a culpa e a severidade das medidas podem parecer excessivas para um simples roubo, sugerindo que ele tem um objetivo mais amplo e pessoal. A verdade sobre sua fuga começará a se insinuar."
      }
    },
    {
      "ordem": 4,
      "meta_estrutura": "O Pesadelo",
      "local_sugerido": "Laboratório de Sintetização de Éter",
      "o_pressagio": "Um alarme estridente soa a partir do Laboratório de Sintetização de Éter, um som que ecoa por toda a estação 'Fagulha Negra'. O vapor escapa em redemoinhos ameaçadores e luzes piscam erraticamente. Um dos cientistas, com o rosto manchado de fuligem e em pânico, corre para encontrar os jogadores, gritando sobre uma sobrecarga incontrolável. Ele revela que a instabilidade da reação do Éter, exacerbada nos últimos dias, atingiu um ponto crítico e uma explosão massiva é iminente, ameaçando destruir a seção administrativa e, possivelmente, a Torre das Sombras de Volkov.",
      "argumento_arco_historia": "O Laboratório de Sintetização de Éter está à beira de uma explosão catastrófica. Esta crise é uma consequência direta da manipulação de Volkov com o Éter Condensado roubado; ele o expôs a condições instáveis para acelerar seus planos de venda. O cientista apavorado busca ajuda para evitar a catástrofe, que, se ocorrer, fará com que a fuga de Volkov seja impossível ou, pior, que ela mesma cause sua destruição. O evento ocorre no meio da noite, intensificando o pânico e o desespero.",
      "premissas_arco_historia": {
        "evidente": "O Laboratório de Éter está em crise, com riscos de uma explosão iminente. Os jogadores são alertados por um cientista aterrorizado que a instabilidade do processo de síntese atingiu um ponto perigoso, ameaçando destruir uma grande parte da estação. A culpa é atribuída à tecnologia perigosa.",
        "oculta": "A explosão não é um acidente tecnológico puro. É o resultado direto da manipulação e profanação do Éter Condensado roubado por Volkov. Ele forçou o processo para acelerar a transação com a facção externa, e agora a estação está em risco iminente por causa de seus planos. A catástrofe ameaça sabotar a própria fuga de Volkov, criando um dilema terrível: salvar a estação pode significar condenar o ladrão, ou deixar a explosão acontecer pode destruir tudo, inclusive a vítima de Volkov."
      },
      "camada_informacao": {
        "id_matriz": 2,
        "conexao_explicada": "A explosão iminente no Laboratório de Éter é uma consequência direta da manipulação do Éter roubado. Se os jogadores conseguirem acessar o laboratório e examinar os dados ou a própria carga de Éter, podem descobrir a causa raiz da instabilidade, percebendo que não foi um acidente, mas sim o resultado de interferência maliciosa. Isso reforçará a verdade sobre o 'Destino da Carga' e a natureza perigosa dos planos de Volkov."
      }
    },
    {
      "ordem": 5,
      "meta_estrutura": "Destruição",
      "local_sugerido": "Terminal de Carga Oeste",
      "o_pressagio": "No Terminal de Carga Oeste, os contêineres empilhados criam um labirinto antes do amanhecer. Um veículo blindado robusto, diferente de qualquer coisa usada pelos Corvos de Ferro ou pela segurança da estação, está estacionado, com sua rampa abaixada. Figuras encapuzadas estão carregando rapidamente caixas seladas no veículo. O cheiro pungente de Éter Condensado flutua no ar. Grigor Volkov, com sua pistola automática em punho e um olhar de triunfo frio, supervisiona a operação. Ele está prestes a concluir sua traição, vendendo o Éter para a facção externa e desaparecendo na vastidão do deserto.",
      "argumento_arco_historia": "A transferência final do Éter Condensado para a facção externa está ocorrendo no Terminal de Carga Oeste. Volkov está orquestrando este evento para garantir sua fuga e o pagamento. Ele usou os eventos anteriores (o roubo, o incêndio, o racionamento, a crise do laboratório) como distrações perfeitas. A tentativa de fuga ocorre pouco antes do amanhecer, com o veículo da facção externa pronto para partir para as terras baldias. Ele está agindo para não ser pego pelas consequências da explosão iminente do laboratório, se não o contiverem.",
      "premissas_arco_historia": {
        "evidente": "É o amanhecer e os Corvos de Ferro, ou cúmplices deles, estão carregando o Éter roubado em um veículo blindado, prestes a fugir com ele. Volkov, agindo como parte da segurança da estação, parece estar confrontando os ladrões, em uma tentativa desesperada de recuperar a carga roubada antes que ela desapareça para sempre.",
        "oculta": "Volkov não está tentando recuperar a carga; ele está supervisionando sua própria venda para uma facção externa. Ele está usando o confronto aparente como uma farsa. O veículo blindado não pertence aos Corvos de Ferro, mas sim aos compradores. Ele está prestes a trair tudo e todos para garantir sua própria sobrevivência e riqueza. A verdade sobre sua traição e seus planos de fuga se revela neste momento crucial."
      },
      "camada_informacao": {
        "id_matriz": 1,
        "conexao_explicada": "Este é o momento culminante onde todas as peças se encaixam. Se os jogadores chegarem ao terminal a tempo, testemunharão a tentativa de fuga de Volkov. Isso revelará a verdade sobre a 'Identidade do Ladrão', o 'Destino da Carga' e a 'Motivação de Volkov' de forma inequívoca. A cena é o gatilho final para o Desastre Imminente, se não forem detidos."
      }
    }
  ],
  "perguntas_dramatica": [
    "Em um mundo onde a conveniência e a sobrevivência ditam a moralidade, será que os jogadores sucumbirão à tentação de Grigor Volkov e venderão sua própria integridade por um ganho rápido, ou conseguirão manter seus princípios em face da corrupção generalizada?",
    "Com a verdade sobre a traição de Volkov exposta, cada aliado na Fagulha Negra torna-se um potencial traidor ou um alvo em potencial. Será que os jogadores conseguirão distinguir entre os verdadeiros aliados e aqueles que foram manipulados ou comprados por Volkov, ou a paranoia os consumirá?",
    "Diante da ameaça iminente de destruição e da inevitabilidade da guerra entre gangues, será que os jogadores conseguirão encontrar a coragem para expor a verdade sobre Grigor Volkov, arriscando desatar um caos ainda maior, ou tentarão silenciar a verdade para permitir que a Fagulha Negra morra em um silêncio caótico?"
  ]
}
```

## 5. 5. Arco História (Módulo: `step4_arc_builder`)
<details>
<summary><strong>⚙️ Ver Prompts & Request</strong></summary>

**System Prompt:**
```text
Você é um Mestre de RPG especialista e Designer Narrativo, seguindo a metodologia 'Narradores Narrados'.

# **Objetivo**
Sua tarefa é criar um **Arco de História** (uma aventura completa de curto/médio prazo) dentro da campanha. Você deve definir a estrutura emocional do arco e planejar as cenas sequenciais.

# **Instruções de Processamento**

### **1. Definição do Arco (O Esqueleto)**
* **Argumento do Arco:** Crie uma história contida que colabore com o argumento maior da campanha, mas tenha início, meio e fim próprios. Defina a **Premissa Evidente** (o que os jogadores acham que é) e a **Premissa Oculta** (o que realmente está acontecendo neste arco).
* **Arquétipo de Enredo:** Escolha um modelo (ex: 'A Busca', 'Superar o Monstro', 'Viagem e Retorno') que guiará as fases da história.
* **Curva Emocional:** Defina o movimento de tensão/bem-estar (ex: 'Do Bem-estar à Queda', 'Homem no Buraco', 'Cinderela'). O arco deve gerar movimento no gráfico de tensão da campanha.

### **2. Planejamento das Cenas (A Musculatura)**
Você deve gerar uma lista sequencial de cenas organizadas pelas **Fases do Enredo** escolhido. Não há limite de cenas, mas a história deve fluir logicamente.

**REGRA DE DETALHAMENTO (CRÍTICA):**
* **Cenas 1 e 2:** Devem ser **TOTALMENTE DETALHADAS**.
* **Cenas 3 em diante:** Devem ser apenas **ESBOÇOS (Argumentos)**.

#### **Estrutura de uma Cena Detalhada (Cenas 1 e 2):**
Para as duas primeiras cenas, preencha os seguintes campos baseados nos 3 pilares da cena:
1.  **Objetivo Narrativo:** O que essa cena cumpre na história? (ex: Apresentar o vilão, dar uma informação, gerar empatia).
2.  **O Conflito:** O problema que os jogadores devem resolver AGORA. Pode ser combate, social, exploração ou dilema moral.
3.  **O Gancho:** O elemento final que aponta ou empurra para a próxima cena.
4.  **Local:** Onde ocorre (use a lista de locais se possível).
5.  **Detalhes Curiosos:** Liste 2 ou 3 detalhes sensoriais ou específicos (nomes, cheiros, objetos estranhos) que dão vida à cena e servem de pista para a Premissa Oculta.

#### **Estrutura de uma Cena Esboço (Cena 3+):**
* **Argumento da Cena:** Um parágrafo resumindo quem, onde e o que acontece. Qual é o propósito simples desta cena na fase atual do enredo?

### **3. Orientações Gerais**
* Use o **Elenco** e os **Perigos** fornecidos para povoar o arco.
* Cada cena deve ter **um único objetivo simples**.
* Lembre-se: O planejamento é um guia, não um trilho. Crie situações, não roteiros rígidos.
```
**User Prompt:**
```text
### 1. Contexto da Campanha
* **Gênero:** Dieselpunk
* **Escopo:** Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.
* **Argumento Geral:** Na noite fria e ventosa que precede o amanhecer, a estação de processamento de minerais de 'Fagulha Negra', um assentamento isolado nas terras baldias, está à beira do caos. Uma carga valiosa de 'Éter Condensado', um recurso essencial para a tecnologia dieselpunk, foi roubada do cofre principal, não por uma gangue rival, mas por um membro da própria administração local, o Chefe de Segurança Grigor Volkov. Volkov planeja vender o Éter a uma facção externa para financiar sua fuga e iniciar uma nova vida longe das disputas internas, fingindo que o roubo foi obra da gangue 'Os Corvos de Ferro' para desviar a atenção e incriminar seus rivais, garantindo que a inevitável guerra entre gangues o beneficie, eliminando concorrentes no futuro para o controle das rotas da região.
* **Foco Narrativo:** Noir Dieselpunk de Paranoia e Traição: Uma atmosfera de desconfiança onde a linha entre herói e vilão se torna turva, sob a constante ameaça de explosões iminentes e o fedor de combustível e poluição.

### 2. Elementos Disponíveis
>>> ELENCO:
> **Grigor Volkov**
  - Papel funcao: Chefe de Segurança da Fagulha Negra
  - Detalhe marcante: Tem o hábito de polir constantemente o cano de sua pistola automática com um lenço de seda, um gesto que exala uma calma ameaçadora.
  - Conviccao: O poder é a única lei que importa; ele manipula o sistema para seu próprio ganho e fuga, acreditando que a sobrevivência dos mais fortes é o único caminho.
  - Contraste: Apesar de sua frieza calculista, ele mantém um quadro de seus filhos em seu escritório, olhando para ele frequentemente com uma expressão de saudade.

> **Os Corvos de Ferro**
  - Papel funcao: Gangue Rival / Ameaça Externa
  - Detalhe marcante: Usam implantes mecânicos toscos e barulhentos em seus membros, tornando seus ataques previsíveis, mas brutalmente eficientes.
  - Conviccao: Domínio territorial e controle dos recursos; eles acreditam que a força bruta e o medo são os únicos meios de prosperidade e ordem em sua visão de mundo.
  - Contraste: Seu líder, um brutamontes com um braço prostético coberto de adereços metálicos, é conhecido por organizar competições de poesia improvisada para seus membros em segredo.

> **Conselheiros da Fagulha Negra**
  - Papel funcao: Burocratas e Facções Internas
  - Detalhe marcante: Nenhum se lembra de seus nomes, mas todos têm um código de cores em suas roupas para identificar sua afiliação, agindo em silêncio e espalhando rumores.
  - Conviccao: Manter o status quo e garantir sua própria segurança e privilégios, independentemente do custo para os outros.
  - Contraste: À noite, muitos se reúnem clandestinamente para trocar histórias sobre os dias em que a Fagulha Negra era um lugar de esperança.

>>> PERIGOS:
> **A Rede de Informantes de Volkov**
  - Tipo: Organização Religiosa
  - Impulso: Estabelecer e seguir doutrinas.
  - Ameaca verdade: Eles minam a ideia de confiança e lealdade, mostrando que qualquer um pode ser um traidor por um preço, destruindo a força da comunidade.
  - Local vinculado: Mercado Sombrio das Quebradas
  - Rastro destruicao: Os acordos feitos aqui são sussurrados, com olhares nervosos e pagamentos feitos em cantos escuros, onde a desconfiança é palpável.
  - Acao iminente: Volkov está prestes a usar seus informantes para espalhar falsas evidências e incriminar permanentemente os Corvos de Ferro pelo roubo, garantindo que a guerra comece ao amanhecer.

> **A Escalada da Violência dos Corvos de Ferro**
  - Tipo: Horda
  - Impulso: Crescer em força e destruir.
  - Ameaca verdade: A gangue representa a brutalidade desenfreada que ameaça engolir a Fagulha Negra, desafiando a ideia de que a ordem pode ser mantida sem violência ou autoridade.
  - Local vinculado: Oficina do Inferno sobre Rodas
  - Rastro destruicao: A oficina está um caos de metal retorcido e marcas de batalha recentes, com veículos em chamas abandonados e um rastro de destruição que leva para fora.
  - Acao iminente: Os Corvos de Ferro pretendem incendiar a Oficina, destruindo a capacidade de reparo da estação e usando o fogo como cortina de fumaça para lançar seu ataque inicial contra os postos de guarda.

> **A Instabilidade do Laboratório de Éter**
  - Tipo: Lugar Amaldiçoado
  - Impulso: Ser controlado ou domado.
  - Ameaca verdade: O laboratório é um símbolo do progresso perigoso e instável que levou a Fagulha Negra ao seu estado atual, mostrando que a busca por poder tecnológico pode ter um custo catastrófico.
  - Local vinculado: Laboratório de Sintetização de Éter
  - Rastro destruicao: Vazamentos químicos têm corroído o metal circundante, e explosões menores criaram crateras irregulares nos corredores de acesso, com sinais de evacuação apressada.
  - Acao iminente: Uma reação em cadeia iminente no laboratório ameaça causar uma explosão massiva que devastaria a seção administrativa e vital da estação, tornando a fuga de Volkov impossível ou, pior, atingindo a Torre das Sombras dele.

>>> LOCAIS:
> **Posto de Controle da Cratera**
  - Descricao: Onde o vento uiva através de chapas de metal enferrujadas e faíscas dançam preguiçosamente de um gerador moribundo. O ar é pesado com o cheiro de óleo queimado e ozônio, misturado ao odor metálico de sangue seco. Este é o primeiro ponto de contato com a 'Fagulha Negra', uma estação escavada em uma antiga cratera de impacto, com torres de vigia improvisadas que se projetam precariamente contra o céu tempestuoso.
  - Tags: Dieselpunk, Noir, Fronteira, Vigilância, Perigo Iminente
  - Funcao: Inicial
  - Ancora geografica: Situado na entrada principal da estação 'Fagulha Negra', ligando o deserto escaldante exterior a todas as rotas internas da base. O acesso é feito por uma ponte pênsil instável sobre um abismo, com postos de guarda improvisados de sucata ao redor.

> **Mercado Sombrio das Quebradas**
  - Descricao: Um labirinto de barracas improvisadas sob lonas rasgadas, onde o murmúrio de barganhas se mistura ao som discordante de uma caixa de música quebrada. O cheiro de carne defumada e solventes químicos paira no ar denso. Luzes fracas de lampiões a gás pingam sombras sinistras sobre rostos desconfiados.
  - Tags: Mercado Negro, Intriga, Dieselpunk, Comunidade, Sobrevivência
  - Funcao: Intermediario
  - Ancora geografica: Aninhado nos níveis inferiores da estação, acessível por elevadores de carga ruidosos e escadarias escorregadias. Ouve-se o zumbido constante das máquinas de processamento vindas de cima, e o cheiro pungente de combustível de alto octanagem emana da Oficina dos 'Corvos de Ferro' próxima.

> **Oficina do Inferno sobre Rodas**
  - Descricao: Explosões esporádicas de soldas ecoam neste espaço cavernoso, iluminado por um brilho laranja intermitente. O cheiro pungente de metal derretido e graxa saturada de óleo enche o ar. Sucata de veículos modificados e peças sobressalentes formam pilhas caóticas, com o ruído constante de ferramentas pneumáticas.
  - Tags: Dieselpunk, Oficina, Ação, Perigo Mecânico, 'Os Corvos de Ferro'
  - Funcao: Intermediario
  - Ancora geografica: Localizada no distrito industrial da estação, adjacente ao Mercado e sob as principais tubulações de processamento de minerais. O acesso é feito por entradas de serviço discretas e becos estreitos, com a constante vibração do motor de um triturador de sucata impulsionando a estrutura.

> **Depósito de Ração 'Fome Eterna'**
  - Descricao: As prateleiras metálicas rangem sob o peso de sacos sujos de grãos e conservas de aspecto duvidoso. Um cheiro agridoce de mofo e conservantes sintéticos domina o ambiente. O silêncio é tenso, pontuado apenas pelos rangidos do metal e o ocasional suspiro de desespero de quem espera.
  - Tags: Ração, Escassez, Desespero, Dieselpunk, Isolado
  - Funcao: Intermediario
  - Ancora geografica: Um anexo dos níveis de habitação, acessível por corredores metálicos estreitos e escadas de emergência. O chão frio e metálico reflete a pouca luz que entra pelas frestas, e o eco de passos parece amplificado pelo vazio dos corredores circundantes.

> **O Cofre Vazio**
  - Descricao: Onde o ar está estranhamente frio e imóvel, com um leve odor de metal polido e pânico contido. As paredes do cofre, outrora impenetráveis, agora exibem sinais de manipulação cuidadosa, não de força bruta. A iluminação é fraca e artificial, projetando sombras longas e distorcidas.
  - Tags: Roubo, Intrigas, Dieselpunk, Segredo, Confronto Imediato
  - Funcao: Intermediario
  - Ancora geografica: Central na administração da estação, ligado diretamente aos escritórios de Grigor Volkov por um túnel de acesso secreto. Ouve-se o zumbido distante dos sistemas de ventilação da sede principal, e o som abafado do tráfego interno da estação se propaga pelas paredes.

> **Laboratório de Sintetização de Éter**
  - Descricao: Fervilhando com o silvo de vapor e o zumbido de maquinaria experimental, este laboratório pulsa com uma energia instável. O ar é denso com o cheiro acre de produtos químicos e um leve aroma etéreo de sucesso. Tubos de vidro borbulham com líquidos brilhantes sob luzes de laboratório sinistras.
  - Tags: Ciência, Perigo Químico, Dieselpunk, Segredo, Criação
  - Funcao: Climax
  - Ancora geografica: Localizado em um anexo mais profundo e isolado da estação, diretamente sob a torre de controle. O acesso é restrito, guardado por sistemas de segurança automatizados e passagens de serviço que se conectam aos túneis subterrâneos. O cheiro de ozônio e resíduos químicos emana com força para os corredores vizinhos.

> **Torre das Sombras de Grigor**
  - Descricao: Um pináculo solitário de metal e concreto, onde o vento uiva mais forte. A vista panorâmica é obscurecida por nuvens de fuligem, mas oferece um vislumbre do deserto implacável lá fora. O cheiro de café queimado e cigarros baratos paira no ar de seu escritório desordenado, repleto de mapas de rotas de fuga.
  - Tags: Comando, Traição, Dieselpunk, Paranoia, Controle
  - Funcao: Climax
  - Ancora geografica: Dominando a paisagem da estação, conectada aos níveis inferiores por um elevador de serviço privado e uma escada de emergência externa exposta aos elementos. O som dos rádios de comunicação, tanto oficiais quanto clandestinos, ecoa fracamente através das paredes de metal, e a vista da cidade se estende até o horizonte distante.

> **Terminal de Carga Oeste**
  - Descricao: Um vasto cemitério de contêineres enferrujados, onde o som metálico do metal batendo uns nos outros ecoa incessantemente sob o céu cinzento. O ar é impregnado com o cheiro de sal marinho esquecido, poeira e combustível diesel barato. As sombras são longas e traiçoeiras, escondendo potenciais emboscadas.
  - Tags: Logística, Comércio, Dieselpunk, Perigo Oculto, Negociação
  - Funcao: Climax
  - Ancora geografica: Localizado na periferia da estação, onde as principais rotas de suprimento se encontram com o deserto. Conectado a outras áreas por vias de serviço de terra batida e um trilho de carga abandonado que serpenteia para o sul. O som distante de motores de veículos pesados e o apito de apocalipse de um trem de carga que se aproxima marcam a paisagem sonora.

---

**Tarefa:** Gere o arquivo do **Arco de História Atual**. Defina o enredo, a curva emocional e a lista de cenas (Detalhe as cenas 1 e 2, esboce as restantes).
```
**Schema Enviado:**
```json
{
  "type": "object",
  "properties": {
    "cabecalho_arco": {
      "type": "object",
      "properties": {
        "titulo_arco": {
          "type": "string",
          "description": "Um título evocativo para esta aventura."
        },
        "arquetipo_enredo": {
          "type": "string",
          "description": "Ex: A Busca, Superar o Monstro, Tragédia, etc."
        },
        "curva_emocional": {
          "type": "string",
          "description": "Ex: Queda -> Ascensão (Homem no Buraco)."
        },
        "argumento_arco": {
          "type": "string",
          "description": "Resumo da história deste arco específico."
        },
        "premissas_arco": {
          "type": "object",
          "properties": {
            "evidente": {
              "type": "string",
              "description": "A missão apresentada aos jogadores."
            },
            "oculta": {
              "type": "string",
              "description": "A verdade por trás deste arco específico."
            }
          },
          "required": [
            "evidente",
            "oculta"
          ]
        }
      },
      "required": [
        "titulo_arco",
        "arquetipo_enredo",
        "curva_emocional",
        "argumento_arco",
        "premissas_arco"
      ]
    },
    "lista_cenas": {
      "type": "array",
      "description": "Lista sequencial de todas as cenas do arco.",
      "items": {
        "type": "object",
        "properties": {
          "numero": {
            "type": "integer"
          },
          "titulo": {
            "type": "string"
          },
          "fase_do_enredo": {
            "type": "string",
            "description": "Em qual etapa do arquétipo esta cena se encaixa (ex: O Chamado, A Frustração)."
          },
          "tipo_detalhamento": {
            "type": "string",
            "enum": [
              "Detalhado",
              "Esboco"
            ],
            "description": "'Detalhado' para cenas 1 e 2. 'Esboco' para as demais."
          },
          "conteudo_cena": {
            "type": "object",
            "properties": {
              "objetivo_narrativo": {
                "type": "string",
                "description": "Apenas se Detalhado. O que a cena cumpre na história."
              },
              "conflito_principal": {
                "type": "string",
                "description": "Apenas se Detalhado. O problema a ser resolvido."
              },
              "gancho": {
                "type": "string",
                "description": "Apenas se Detalhado. O que leva à próxima cena."
              },
              "local_cena": {
                "type": "string",
                "description": "Nome do local."
              },
              "detalhes_curiosos": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "description": "Apenas se Detalhado. Pistas sensoriais ou nomes específicos."
              },
              "argumento_resumido": {
                "type": "string",
                "description": "Obrigatório para todas. Se for Esboco, é o único campo preenchido."
              }
            },
            "required": [
              "argumento_resumido"
            ]
          }
        },
        "required": [
          "numero",
          "titulo",
          "fase_do_enredo",
          "tipo_detalhamento",
          "conteudo_cena"
        ]
      }
    }
  },
  "required": [
    "cabecalho_arco",
    "lista_cenas"
  ]
}
```
</details>

### 🤖 Resposta do Modelo
```json
{
  "cabecalho_arco": {
    "titulo_arco": "A Traição de Fagulha Negra",
    "arquetipo_enredo": "O Chamado Inesperado e a Queda do Herói",
    "curva_emocional": "Queda -> Ascensão (Homem no Buraco)",
    "argumento_arco": "Os jogadores são chamados para investigar o roubo de Éter Condensado em Fagulha Negra, acreditando que a gangue 'Os Corvos de Ferro' é a culpada. Logo descobrem que o Chefe de Segurança, Grigor Volkov, orquestrou o roubo para vender o recurso e fugir, incriminando a gangue. Os jogadores precisarão desvendar a teia de mentiras e traições de Volkov, enfrentando os perigos que ele cria e os resquícios da instabilidade do laboratório de éter, para impedir que a guerra entre gangues e a explosão iminente destruam a estação.",
    "premissas_arco": {
      "evidente": "Investigar o roubo de Éter Condensado e recuperar o recurso, provavelmente lidando com a gangue Corvos de Ferro.",
      "oculta": "Grigor Volkov é o verdadeiro ladrão e manipulador, usando o roubo para iniciar uma guerra e financiar sua fuga, enquanto a estação em si está à beira de um colapso devido à instabilidade do laboratório de éter."
    }
  },
  "lista_cenas": [
    {
      "numero": 1,
      "titulo": "A Chegada Desolada",
      "fase_do_enredo": "O Chamado",
      "tipo_detalhamento": "Detalhado",
      "conteudo_cena": {
        "argumento_resumido": "Os jogadores chegam à Fagulha Negra e são recebidos pelo caos inicial e pela atmosfera opressora do Posto de Controle da Cratera, onde recebem a 'missão' oficial.",
        "objetivo_narrativo": "Introduzir o cenário, apresentar a atmosfera noir/dieselpunk e estabelecer a missão inicial dos jogadores, focando no roubo do Éter Condensado e apontando para os Corvos de Ferro como os responsáveis. Gerar um senso de urgência e desconfiança inicial na estação. Apresentar o local de forma vívida e ameaçadora, estabelecendo o tom do arco de história e a presença sutil de Grigor Volkov através de seus subordinados e da segurança falha. Introduzir a ideia de que a ameaça externa (Corvos de Ferro) é iminente e perigosa, enquanto a organização interna parece corrupta ou incompetente. Preparar o terreno para a investigação, mostrando as consequências imediatas do roubo e a fragilidade da Fagulha Negra.\n\nO primeiro vislumbre da Fagulha Negra em meio a uma tempestade de areia e vento. O herói é recebido em um Posto de Controle dilapidado. Uma figura de autoridade (talvez um tenente de Volkov, desconfiado e com um ar de superioridade) informa sobre o roubo massivo de Éter Condensado e a suspeita recai sobre os Corvos de Ferro. Eles são informados que 'precisam' da ajuda dos personagens para resolver isso rápido, pois a situação já está tensa. A estação parece instável, com ruídos estranhos e uma sensação palpável de paranoia. Informação sobre o laboratório de Éter estar em mau estado e sobre a ameaça iminente dos Corvos de Ferro atacando é passada de forma evasiva. O objetivo é clara: recuperar o Éter e/ou 'resolver' o problema dos Corvos de Ferro antes que a Fagulha Negra exploda por dentro e por fora. O tenente aponta para o Mercado Sombrio como um lugar para começar a investigar a gangue ou para buscar informações sobre o Éter sumido. Menciona também que o Chefe de Segurança, Volkov, está 'ocupado' com os preparativos para a defesa da estação e não pode ser incomodado agora, mas aconselha os jogadores a relatar tudo a ele quando possível, se a missão terminar bem. O objetivo é que os jogadores se sintam pressionados pela situação e comecem a investigar a suposta ameaça externa."
      }
    },
    {
      "numero": 2,
      "titulo": "A Teia do Mercado Sombrio",
      "fase_do_enredo": "A Busca Continua",
      "tipo_detalhamento": "Detalhado",
      "conteudo_cena": {
        "argumento_resumido": "Os jogadores investigam no Mercado Sombrio das Quebradas, procurando pistas sobre o roubo e os Corvos de Ferro, mas encontram desconfiança e a manipulação de Volkov através de sua rede de informantes.",
        "objetivo_narrativo": "Revelar que a rede de Volkov está ativa no mercado, plantando informações falsas e criando o clima de paranoia. Apresentar a complexidade social da Fagulha Negra e a dificuldade em obter informações confiáveis. Gerar tensão e desconfiança nos jogadores em relação a quem procurar e em quem confiar. Apresentar o local do Mercado Sombrio como um centro de intriga e comércio ilícito, onde a verdade é vendida a preço alto. Os jogadores devem navegar entre informantes relutantes, rumores e a sutil influência da rede de Volkov. Eles podem ouvir sobre os Corvos de Ferro, mas as informações são contraditórias ou parecem projetadas para incriminá-los mais fortemente. Podem encontrar um informante que se arrisca a revelar um segredo, mas é interceptado ou silenciado de alguma forma (talvez um 'acidente' ou 'desaparecimento'), demonstrando os perigos de obter informações verdadeiras. Uma pista pode levar à Oficina do Inferno sobre Rodas, onde a gangue Corvos de Ferro tem um esconderijo, ou para um boato sobre a atividade incomum de Volkov perto do Cofre Vazio ou do Laboratório de Sintetização de Éter. Um detalhe curioso pode ser um dos Conselheiros da Fagulha Negra, com um código de cor específico, observando os jogadores de longe ou trocando um bilhete com um desses informantes, mostrando a intriga interna. Outro detalhe é o cheiro forte de um solvente incomum sendo usado para 'limpar' algo com cuidado, que pode ser usado para mascarar cheiros de metal ou para manipular o cofre. A cena culmina com os jogadores recebendo uma nova pista ou sendo forçados a uma ação precipitada, talvez devido a uma emboscada ou a um alerta sobre uma movimentação dos 'Corvos de Ferro'. O gancho pode ser um mapa rabiscado deixado por um informante para os jogadores, indicando um esconderijo dos Corvos ou um ponto de encontro secreto, ou um aviso de que a 'janela de oportunidade' para parar os Corvos está se fechando. Ou, ainda mais intrigante, o gancho pode ser um pedaço de seda de lenço que lembra o hábito de Volkov, deixado para trás por um fugaz informante. E, como uma ameaça iminente, podem ouvir que os Corvos de Ferro planejam 'acabar' com a Oficina do Inferno sobre Rodas logo mais, possivelmente como uma distração ou para consolidar suas posições."
      }
    },
    {
      "numero": 3,
      "titulo": "O Fogo da Oficina",
      "fase_do_enredo": "Respostas e Reações",
      "tipo_detalhamento": "Esboco",
      "conteudo_cena": {
        "argumento_resumido": "Os jogadores vão até a Oficina do Inferno sobre Rodas, suspeitando que seja um local ligado aos Corvos de Ferro ou ao roubo. Lá, eles podem encontrar evidências deixadas pela gangue, ou encontrar a oficina sendo atacada ou incendiada pelos Corvos de Ferro como parte de seu plano. Esta cena focará na 'Escalada da Violência dos Corvos de Ferro', introduzindo a presença física da gangue de forma brutal."
      }
    },
    {
      "numero": 4,
      "titulo": "O Silêncio do Cofre",
      "fase_do_enredo": "Respostas e Reações",
      "tipo_detalhamento": "Esboco",
      "conteudo_cena": {
        "argumento_resumido": "Investigando o local do roubo, o Cofre Vazio, os jogadores percebem que a entrada não foi forçada, sugerindo um trabalho interno. Podem encontrar vestígios sutis da manipulação de Volkov ou alguma pista que o conecte mais diretamente ao crime, contradizendo a narrativa pública. Isso pode levar à revelação da verdade sobre o envolvimento de Volkov."
      }
    },
    {
      "numero": 5,
      "titulo": "A Dança dos Conselheiros",
      "fase_do_enredo": "Julgamento",
      "tipo_detalhamento": "Esboco",
      "conteudo_cena": {
        "argumento_resumido": "Confrontados com informações conflitantes ou com a descoberta da manipulação de Volkov, os jogadores procuram os Conselheiros da Fagulha Negra para obter uma visão oficial ou contornar a segurança de Volkov. Os conselheiros, envoltos em suas intrigas internas e códigos de cores, podem oferecer informações valiosas sobre o status quo, as rivalidades internas e talvez até sobre os planos de Volkov, mas sempre com um viés para proteger seus próprios interesses."
      }
    },
    {
      "numero": 6,
      "titulo": "A Reação em Cadeia",
      "fase_do_enredo": "O Clímax",
      "tipo_detalhamento": "Esboco",
      "conteudo_cena": {
        "argumento_resumido": "Para impedir Volkov ou escapar, os jogadores precisam atravessar o perigoso Laboratório de Sintetização de Éter, que está à beira de uma explosão. Esta cena foca na 'Instabilidade do Laboratório de Éter', forçando os jogadores a lidar com um ambiente volátil e perigoso enquanto a ameaça de colapso total da Fagulha Negra se torna real. A fuga de Volkov, se não for impedida, pode ser diretamente afetada por isso."
      }
    },
    {
      "numero": 7,
      "titulo": "O Confronto na Torre",
      "fase_do_enredo": "O Clímax",
      "tipo_detalhamento": "Esboco",
      "conteudo_cena": {
        "argumento_resumido": "Os jogadores confrontam Grigor Volkov em sua Torre das Sombras, onde ele planeja sua fuga ou tenta consolidar seu controle sobre a estação. Este é o clímax da trama de traição, onde a verdade sobre seus planos (e o que ele fez com o Éter) é finalmente revelada, forçando um confronto direto e uma decisão sobre seu destino e o futuro da Fagulha Negra. A possibilidade de ele usar o Éter que roubou para financiar sua fuga, ou que a instabilidade do laboratório o leve a uma tentativa desesperada de fuga, pode ser aqui."
      }
    },
    {
      "numero": 8,
      "titulo": "Fuga ou Confronto Final",
      "fase_do_enredo": "A Resolução",
      "tipo_detalhamento": "Esboco",
      "conteudo_cena": {
        "argumento_resumido": "Dependendo das ações dos jogadores, esta cena pode focar na fuga de Volkov (talvez para o Terminal de Carga Oeste para se encontrar com compradores), no seu confronto final com os Corvos de Ferro, ou na tentativa dos jogadores de estabilizar a estação e deter a violência. O Terminal de Carga Oeste pode servir como ponto de fuga ou como local de um último embate em larga escala, onde as facções restantes da Fagulha Negra precisam se unir (ou se destruir) para sobreviver."
      }
    },
    {
      "numero": 9,
      "titulo": "Um Novo Amanhecer (ou Não)",
      "fase_do_enredo": "Resolução",
      "tipo_detalhamento": "Esboco",
      "conteudo_cena": {
        "argumento_resumido": "Epílogo do arco. Os jogadores observam as consequências de suas ações: a Fagulha Negra está salva, destruída, ou em um estado de equilíbrio precário. A ameaça dos Corvos de Ferro foi neutralizada ou apenas adiada. O destino de Volkov é decidido. A atmosfera de paranoia e traição pode ter diminuído ou se intensificado, deixando os personagens prontos para o próximo arco da campanha."
      }
    }
  ]
}
```
