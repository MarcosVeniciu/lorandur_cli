# Relatório: Teste Completo: Trama & Frente Pipeline (Com Respostas)
**Data:** 2026_01_12_19_42 | **Status:** ✅ Sucesso

## 📊 Métricas de Execução

| Métrica | 1. Trama | 2. Front Arquiteto | 3. Front World | 4. Front Story | Total |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tempo Total** | 13.61s | 14.85s | 10.27s | 19.02s | **57.74s** |
| **Tokens Entrada** | 877 | 3301 | 4295 | 7844 | **16317** |
| **Tokens Saída** | 2923 | 3191 | 2297 | 4193 | **12604** |
| **Tokens Total** | 3800 | 6492 | 6592 | 12037 | **28921** |
| **Custo Estimado** | $0.001257 | $0.001607 | $0.001348 | $0.002462 | **$0.006673** |

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
    "justificativa_escopo": "A trama de recuperar uma carga roubada antes do amanhecer, com a ameaça de guerra entre gangues, se encaixa perfeitamente em um escopo local. Isso permite focar a ação em um assentamento ou base específica, onde as consequências de uma guerra de gangues teriam um impacto imediato e contido, facilitando a intriga social e a exploração de disputas de poder.",
    "justificativa_estilo": "A combinação de roubo de carga valiosa, a urgência do prazo (antes do amanhecer) e a ameaça de guerra entre gangues cria um cenário clássico de Noir, com um suspense crescente e a promessa de ação explícita. O gênero Dieselpunk adiciona uma camada de tecnologia retrofuturista e um ambiente industrial pesado, ideal para perseguições urbanas e conflitos táticos."
  },
  "argumento": {
    "texto": "Na labiríntica 'Oficina Subterrânea', um complexo industrial abandonado que serve como ponto de encontro e mercado negro de peças nos confins do Distrito 7, uma carga inestimável composta por componentes raros de um protótipo aéreo foi roubada do receptador local, 'Silas, O Químico'. O roubo foi executado pelos 'Espectros', uma gangue secundária que opera nas sombras, não por ganância, mas para evitar que a carga caia nas mãos da ascendente 'Legião de Ferro'. Se os jogadores não recuperarem a carga antes do amanhecer, a Legião de Ferro usará o incidente como pretexto para aniquilar os Espectros e Silas, iniciando uma guerra aberta que mergulhará o Distrito 7 no caos, com potencial para se espalhar para outros setores da cidade.",
    "justificativa": "O argumento define o 'Quem' (jogadores, Espectros, Legião de Ferro, Silas, Silas), o 'Onde' (Oficina Subterrânea, Distrito 7), o 'Quando' (noite até amanhecer), e o 'Por Quê' (a carga é crucial para um protótipo e sua posse é a faísca para uma guerra maior). A motivação oculta dos Espectros (impedir o mal maior) contrasta com a premissa inicial de um simples roubo."
  },
  "premissas": {
    "evidente": {
      "texto": "Vocês foram contratados por Silas, O Químico, um receptador de tecnologia sombrio, para recuperar uma carga de componentes de alto valor roubada de seu esconderijo na Oficina Subterrânea. O tempo está se esgotando; a carga precisa estar de volta antes que o sol nasça, ou Silas promete consequências terríveis para quem falhar. As informações preliminares sugerem que os ladrões são uma gangue menor e sem importância, facilmente subjugável.",
      "funcao": "Esta é a missão superficial que os jogadores recebem, focando na urgência e em um alvo aparentemente simples (recuperar a carga de uma gangue menor), direcionando suas ações iniciais para a caça à carga e eliminando a 'ameaça' de gangue."
    },
    "oculta": {
      "texto": "A carga roubada (componentes raros de protótipo aéreo) não é valiosa por si só, mas sim pela tecnologia que ela desbloqueia ou pela capacidade de sabotagem que representa. Os Espectros roubaram a carga para impedir que a Liga de Ferro a use para iniciar uma guerra territorial e eliminar qualquer oposição. Silas, o Químico, trabalhava em conluio com a Liga de Ferro, mas foi traído. A 'guerra entre gangues rivais' é um plano maior da Liga de Ferro para consolidar poder na cidade, usando este roubo como desculpa para uma ofensiva. Recuperar a carga pode significar entregá-la a Silas (potencialmente para a Liga), entregá-la aos Espectros (garantindo sua sobrevivência, mas atrasando o plano da Liga), ou descobrir uma terceira via para neutralizar o poder da Liga.",
      "funcao": "Revela a verdadeira natureza do conflito, a complexidade das alianças (Silas não confia em ninguém) e o verdadeiro perigo por trás da carga, transformando uma simples recuperação em um dilema moral e estratégico."
    },
    "justificativa": "A premissa evidente oferece um objetivo claro e direto, enquanto a premissa oculta subverte as expectativas iniciais, introduzindo um conflito de interesses mais profundo, personagens com motivações ocultas e um perigo maior do que o inicialmente aparente."
  },
  "matriz_controle_informacao": {
    "itens": [
      {
        "titulo": "A Verdadeira Natureza da Carga",
        "a_verdade": "Os componentes roubados são peças-chave para um novo sistema de armamento aéreo 'silencioso' que a Liga de Ferro planeja usar para subjugar os distritos rivais e consolidar seu controle sobre a cidade.",
        "a_expectativa": "Os jogadores acreditam que a carga é apenas 'valiosa' no sentido de dinheiro ou poder de barganha para Silas. Eles a veem como um item tecnológico de alto mercado negro.",
        "a_camuflagem": "A carga está em um contêiner discreto, marcado apenas com um número de série genérico. Silas descreve a carga vagamente como 'coisas que fazem os céus tremerem', sem especificar para quem ou para quê.",
        "o_gatilho": "Investigar o contêiner onde a carga original estava armazenada, encontrar anotações ou planos parciais de Silas sobre seu destino, ou interrogar um membro capturado dos Espectros que revela o propósito militar.",
        "a_revelacao": "Os jogadores descobrem que estão lidando com a peça central de uma arma de guerra, e que a 'guerra de gangues' é um plano mais sinistro para justificar a ascensão de uma nova força militar corporativa ou de gangue.",
        "id": 1
      },
      {
        "titulo": "A Traição de Silas",
        "a_verdade": "Silas, O Químico, não é apenas um receptador; ele era o intermediário original da Liga de Ferro para os componentes. Os Espectros o roubaram não só para frustrar a Liga, mas também como retaliação por um acordo anterior não cumprido por Silas, que resultou em baixas para os Espectros.",
        "a_expectativa": "Os jogadores consideram Silas uma vítima legítima, um empresário sombrio sendo explorado por gangues, e que precisa da carga de volta para seu próprio 'negócio'.",
        "a_camuflagem": "Silas parece genuinamente perturbado e preocupado com a perda. Ele pode omitir detalhes sobre sua própria participação no esquema da Liga de Ferro, ou atribuir a culpa inteiramente às gangues.",
        "o_gatilho": "Encontrar evidências de comunicação entre Silas e a Liga de Ferro, rastrear o rastro de dinheiro ou subornos de Silas, ou ouvir sussurros de informantes no submundo sobre a verdadeira lealdade de Silas.",
        "a_revelacao": "Os jogadores descobrem que Silas é um traidor de múltiplas partes, que estava colaborando com a Liga de Ferro e que o roubo teve um motivo mais profundo relacionado a vingança dos Espectros por ações passadas de Silas em nome da Liga.",
        "id": 2
      },
      {
        "titulo": "Os Verdadeiros Culpados (e Inocentes)",
        "a_verdade": "A 'guerra entre gangues' iminente é um plano orquestrado pela Liga de Ferro. Os Espectros, embora sejam ladrões, estão agindo por desespero e para impedir a Liga, não para iniciar um conflito em larga escala. A verdadeira ameaça à paz (e à cidade) é a Liga de Ferro, que quer que os Espectros e Silas sejam destruídos para criar um vácuo de poder que eles possam preencher.",
        "a_expectativa": "Os jogadores acreditam que a ameaça de 'guerra entre gangues rivais' é uma consequência direta e inevitável do roubo, e que eles precisam controlar ou eliminar de um dos lados (provavelmente os Espectros) para evitar a escalada.",
        "a_camuflagem": "O incidente é apresentado como um conflito turfista comum. A presença e a influência da Liga de Ferro são sutis, operando nas sombras ou através de intermediários, não aparecendo como um jogador principal inicialmente.",
        "o_gatilho": "Testemunhar o comportamento altamente organizado e coordenado dos 'espectros' (que podem ser mercenários contratados pela Liga para incriminar os Espectros reais) ou obter informações de um contato de inteligência que revela o plano da Liga de Ferro para a 'pacificação' do Distrito 7.",
        "a_revelacao": "Os jogadores percebem que a luta contra os Espectros ou a recuperação da carga para Silas não resolverá o problema; é a Liga de Ferro a mente por trás da violência, e neutralizá-los é a única maneira de evitar a verdadeira guerra.",
        "id": 3
      }
    ],
    "justificativa": "A matriz detalha os principais pontos de virada e mistérios da aventura. Cada item apresenta uma expectativa superficial que os jogadores provavelmente terão, a verdade oculta que subverte essa expectativa, como essa verdade está disfarçada, o que precisa acontecer para revelá-la e qual será a revelação em si. Isso permite ao Mestre gerenciar o fluxo de informações e criar momentos de surpresa e quebra de expectativas."
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
* **Subgêneros:** Noir, Ação Frenética
* **Escopo Geográfico:** Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.
* **Pool de Tipos de Locais (Inspiração):** Arena de Lutas, Ferro velho, Fila da ração, Armazém de comida, Mercado de pulgas, Bar movimentado, Mansão de um senhor de armas, Festival de Música, Torre de Vigia, Pista de Obstáculos, Escombros, Oficina de carros, Laboratório de química, Ferro Velho

### 2. A Alma da História
* **Argumento:** Na labiríntica 'Oficina Subterrânea', um complexo industrial abandonado que serve como ponto de encontro e mercado negro de peças nos confins do Distrito 7, uma carga inestimável composta por componentes raros de um protótipo aéreo foi roubada do receptador local, 'Silas, O Químico'. O roubo foi executado pelos 'Espectros', uma gangue secundária que opera nas sombras, não por ganância, mas para evitar que a carga caia nas mãos da ascendente 'Legião de Ferro'. Se os jogadores não recuperarem a carga antes do amanhecer, a Legião de Ferro usará o incidente como pretexto para aniquilar os Espectros e Silas, iniciando uma guerra aberta que mergulhará o Distrito 7 no caos, com potencial para se espalhar para outros setores da cidade.
* **Premissa Evidente (Missão):** Vocês foram contratados por Silas, O Químico, um receptador de tecnologia sombrio, para recuperar uma carga de componentes de alto valor roubada de seu esconderijo na Oficina Subterrânea. O tempo está se esgotando; a carga precisa estar de volta antes que o sol nasça, ou Silas promete consequências terríveis para quem falhar. As informações preliminares sugerem que os ladrões são uma gangue menor e sem importância, facilmente subjugável.
* **Premissa Oculta (Twist):** A carga roubada (componentes raros de protótipo aéreo) não é valiosa por si só, mas sim pela tecnologia que ela desbloqueia ou pela capacidade de sabotagem que representa. Os Espectros roubaram a carga para impedir que a Liga de Ferro a use para iniciar uma guerra territorial e eliminar qualquer oposição. Silas, o Químico, trabalhava em conluio com a Liga de Ferro, mas foi traído. A 'guerra entre gangues rivais' é um plano maior da Liga de Ferro para consolidar poder na cidade, usando este roubo como desculpa para uma ofensiva. Recuperar a carga pode significar entregá-la a Silas (potencialmente para a Liga), entregá-la aos Espectros (garantindo sua sobrevivência, mas atrasando o plano da Liga), ou descobrir uma terceira via para neutralizar o poder da Liga.

### 3. Segredos da Campanha (Matriz)
Use estes segredos para garantir que os locais contenham pistas ou conexões temáticas com a verdade maior:
  - Titulo: A Verdadeira Natureza da Carga
  - A verdade: Os componentes roubados são peças-chave para um novo sistema de armamento aéreo 'silencioso' que a Liga de Ferro planeja usar para subjugar os distritos rivais e consolidar seu controle sobre a cidade.
  - A expectativa: Os jogadores acreditam que a carga é apenas 'valiosa' no sentido de dinheiro ou poder de barganha para Silas. Eles a veem como um item tecnológico de alto mercado negro.
  - A camuflagem: A carga está em um contêiner discreto, marcado apenas com um número de série genérico. Silas descreve a carga vagamente como 'coisas que fazem os céus tremerem', sem especificar para quem ou para quê.
  - O gatilho: Investigar o contêiner onde a carga original estava armazenada, encontrar anotações ou planos parciais de Silas sobre seu destino, ou interrogar um membro capturado dos Espectros que revela o propósito militar.
  - A revelacao: Os jogadores descobrem que estão lidando com a peça central de uma arma de guerra, e que a 'guerra de gangues' é um plano mais sinistro para justificar a ascensão de uma nova força militar corporativa ou de gangue.
  - Id: 1

  - Titulo: A Traição de Silas
  - A verdade: Silas, O Químico, não é apenas um receptador; ele era o intermediário original da Liga de Ferro para os componentes. Os Espectros o roubaram não só para frustrar a Liga, mas também como retaliação por um acordo anterior não cumprido por Silas, que resultou em baixas para os Espectros.
  - A expectativa: Os jogadores consideram Silas uma vítima legítima, um empresário sombrio sendo explorado por gangues, e que precisa da carga de volta para seu próprio 'negócio'.
  - A camuflagem: Silas parece genuinamente perturbado e preocupado com a perda. Ele pode omitir detalhes sobre sua própria participação no esquema da Liga de Ferro, ou atribuir a culpa inteiramente às gangues.
  - O gatilho: Encontrar evidências de comunicação entre Silas e a Liga de Ferro, rastrear o rastro de dinheiro ou subornos de Silas, ou ouvir sussurros de informantes no submundo sobre a verdadeira lealdade de Silas.
  - A revelacao: Os jogadores descobrem que Silas é um traidor de múltiplas partes, que estava colaborando com a Liga de Ferro e que o roubo teve um motivo mais profundo relacionado a vingança dos Espectros por ações passadas de Silas em nome da Liga.
  - Id: 2

  - Titulo: Os Verdadeiros Culpados (e Inocentes)
  - A verdade: A 'guerra entre gangues' iminente é um plano orquestrado pela Liga de Ferro. Os Espectros, embora sejam ladrões, estão agindo por desespero e para impedir a Liga, não para iniciar um conflito em larga escala. A verdadeira ameaça à paz (e à cidade) é a Liga de Ferro, que quer que os Espectros e Silas sejam destruídos para criar um vácuo de poder que eles possam preencher.
  - A expectativa: Os jogadores acreditam que a ameaça de 'guerra entre gangues rivais' é uma consequência direta e inevitável do roubo, e que eles precisam controlar ou eliminar de um dos lados (provavelmente os Espectros) para evitar a escalada.
  - A camuflagem: O incidente é apresentado como um conflito turfista comum. A presença e a influência da Liga de Ferro são sutis, operando nas sombras ou através de intermediários, não aparecendo como um jogador principal inicialmente.
  - O gatilho: Testemunhar o comportamento altamente organizado e coordenado dos 'espectros' (que podem ser mercenários contratados pela Liga para incriminar os Espectros reais) ou obter informações de um contato de inteligência que revela o plano da Liga de Ferro para a 'pacificação' do Distrito 7.
  - A revelacao: Os jogadores percebem que a luta contra os Espectros ou a recuperação da carga para Silas não resolverá o problema; é a Liga de Ferro a mente por trás da violência, e neutralizá-los é a única maneira de evitar a verdadeira guerra.
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
    "meta_estrutura_resumo": "1. O Chamado (contratados por Silas para recuperar carga roubada). 2. A Jornada (rastrear os Espectros pelo Distrito 7, enfrentando perigos). 3. Chegada e Frustração (encontrar os Espectros e a carga, mas a verdade sobre o roubo e os motivos se revela, criando uma nova barreira). 4. Provações Finais (confrontar os verdadeiros conspiradores ou fazer escolhas morais difíceis). 5. O Objetivo (recuperar a carga, neutralizar a ameaça da Liga de Ferro ou garantir uma paz precária antes do amanhecer).",
    "foco_narrativo": "Mistura Noir Dieselpunk e Ação Frenética: Uma investigação tensa e rápida em um submundo industrial sombrio, onde cada beco pode esconder um perigo mortal ou uma pista crucial, tudo sob a ameaça iminente de uma guerra brutal."
  },
  "lista_locais": [
    {
      "nome": "Portal Enferrujado da Oficina",
      "descricao": "A entrada principal para a Oficina Subterrânea. Uma estrutura colossal de metal riscado e corroído, com portões maciços que rangem com o vento incessante. O ar aqui cheira a graxa antiga e a chuva ácida, com o som distante e abafado de maquinaria em funcionamento e gritos ocasionais que ecoam das profundezas. Luzes incandescentes piscam erraticamente, lançando sombras dançantes sobre as poças oleosas.",
      "tags": "Entrada, Industrial, Subterrâneo, Sombrio",
      "funcao": "Inicial",
      "ancora_geografica": "Este portal é a única entrada terrestre significativa para a Oficina Subterrânea, localizado em um bolsão isolado de escombros e estaleiros abandonados, no limite do Distrito 7. O chão de metal desgastado se funde com a terra lamacenta do exterior, e o ruído do tráfego da cidade distante é quase inaudível aqui, substituído pelo gotejar constante de fluidos desconhecidos e o vento uivante através das brechas."
    },
    {
      "nome": "O Mercado das Sombras",
      "descricao": "Um labirinto caótico de barracas improvisadas e contêineres empilhados, iluminado por lâmpadas a cartucho e projetores improvisados. O ar é denso com fumaça de cachimbos, o cheiro de comida de rua duvidosa e o tom metálico de peças de máquinas sendo negociadas. Sussurros de negócios ilícitos se misturam com o barulho de mercadores vendendo desde componentes de motores até implantes cibernéticos questionáveis. É o coração pulsante do comércio negro na Oficina.",
      "tags": "Mercado Negro, Social, Intriga, Comércio",
      "funcao": "Intermediario",
      "ancora_geografica": "Localizado logo após os túneis iniciais da Entrada Enferrujada, o Mercado das Sombras se estende por um vasto espaço aberto dentro da Oficina. Ele é circundado por antigas docas de carga e armazéns, conectando-se a eles por passarelas metálicas instáveis e escadas de serviço corroídas. O som vibrante do mercado se mistura com o eco dos guindastes ociosos nos armazéns adjacentes."
    },
    {
      "nome": "Armazém 7B: O Vazio Refrigerado",
      "descricao": "Um espaço sinistro e silencioso onde o frio persiste mesmo no calor opressivo das entranhas da Oficina. O ar cheira a metal gelado, ozônio e algo levemente químico que ressoa com o 'gatilho' secreto. Luzes fluorescentes piscam sobre prateleiras metálicas vazias e uma poucos contêineres de transporte lacrados. O som predominante é o zumbido baixo e constante dos sistemas de refrigeração arcaicos, que parecem estar lutando para manter a temperatura.",
      "tags": "Armazém, Frio, Pista, Escondido",
      "funcao": "Intermediario",
      "ancora_geografica": "Aninhado entre o Mercado das Sombras e os Laboratórios de Química, o Armazém 7B é acessível por uma única porta de aço maciço e uma passagem de serviço estreita que leva aos fundos do Mercado. O som dos ventiladores de exaustão do laboratório vizinho é fracamente audível através das paredes bem isoladas, e o chão de concreto rachado abriga pequenas nascentes gotejantes de condensação."
    },
    {
      "nome": "Os Trens Fantasma do Setor C",
      "descricao": "Um trecho de trilhos de carga esquecido que serpenteia através de áreas abandonadas da Oficina. A escuridão aqui é quase total, quebrada apenas por ocasionalmente frestas de luz que penetram através de buracos no teto, revelando vagões enferrujados e derruídos. O ar é parado, mofado e carrega o cheiro de ferrugem e óleo velho. O silêncio é opressor, apenas pontuado pelo rangido ocasional de metal se acomodando ou o correr de algo pequeno e indesejado nas sombras.",
      "tags": "Passagem, Perigo, Escombros, Abandonado",
      "funcao": "Intermediario",
      "ancora_geografica": "Os trilhos dos Trens Fantasma formam uma 'veia' abandonada que conecta a área de carga do Mercado das Sombras às zonas mais profundas e perigosas da Oficina. Eles passam por baixo de pilares massivos de sustentação e ao lado de fábricas desativadas, com pontes de serviço precárias oferecendo acesso a níveis superiores, e túneis de drenagem parcialmente bloqueados levando a áreas mais baixas."
    },
    {
      "nome": "O Ninho dos Espectros",
      "descricao": "Antigo maquinário de fundição retorcido e abandonado que foi transformado em um covil improvisado. Chamas irregulares de fogueiras iluminam um espaço claustrofóbico, onde sucata e peças roubadas formam barricadas rudimentares. O ar aqui é carregado com o cheiro acre de metal queimado, suor e desespero. Gritos de comandos curtos e o clangor metálico de armas indicam que este é um local de ação e confronto.",
      "tags": "Covil, Gangue, Confronto, Perigo",
      "funcao": "Intermediario",
      "ancora_geografica": "Escondido no labirinto de 'Escombros e Indústrias Desativadas' que compõem o Setor C, o Ninho dos Espectros é acessível apenas por caminhos tortuosos entre máquinas enferrujadas e pilhas de sucata em desmoronamento. Um túnel de ventilação colapsado leva diretamente para dentro de sua área principal, e a saída mais 'segura' se abre para uma rampa de serviço que desce em direção aos Trens Fantasma."
    },
    {
      "nome": "Laboratório de Química 'O Alquimista'",
      "descricao": "Um espaço surpreendentemente organizado, mas sinistro, onde o cheiro pungente de produtos químicos reage com o odor metálico de Silas. Equipamentos de laboratório de alta tecnologia, muitos deles antigos, estão dispostos em bancadas de aço polido. Tubos borbulham com líquidos coloridos e venenosos, e mapas detalhados da cidade são espalhados sobre uma mesa central sob uma luz potente e fria. Este é o reino de Silas, a mente por trás de muitos negócios obscuros.",
      "tags": "Laboratório, Científico, Pista, Conspiração",
      "funcao": "Climax",
      "ancora_geografica": "O Laboratório de Silas é uma adição bem protegida ao 'complexo' da Oficina Subterrânea, localizado em um nível mais alto, acessível por um elevador de carga privado que parte do Mercado das Sombras ou através de uma passagem secreta ligada a um antigo escritório de engenharia. O som do zumbido dos sistemas de segurança e ventilação é constante, e a vista das luzes distantes da cidade, quando visível através de pequenas janelas reforçadas, contrasta com a escuridão industrial abaixo."
    },
    {
      "nome": "A Plataforma de Lançamento Esquecida",
      "descricao": "Uma área vasta e aberta nas entranhas da Oficina, outrora destinada ao lançamento de aeronaves ou foguetes, agora dominada por estruturas metálicas gigantescas e corroídas, tubulações de vapor e plataformas de observação em ruínas. O ar é quente, úmido e carrega o cheiro de óleo de motor e ozônio de equipamento elétrico. Uma sensação de grandeza perdida e abandono paira aqui, misturada com a tensão de um impasse iminente.",
      "tags": "Abertura, Combate, Confronto, Estratégico",
      "funcao": "Climax",
      "ancora_geografica": "Esta plataforma é o ponto mais baixo e central da Oficina, acessível por rampas maciças que descem do Mercado das Sombras e dos túneis adjacentes. Um rio de esgoto industrial corre por um lado, e as paredes monumentais da própria Oficina se erguem em todos os outros lados, repletas de escadas de serviço e passarelas que observam o campo de batalha. É um coliseu natural dentro da estrutura industrial."
    },
    {
      "nome": "Torre de Vigia do Distrito 7",
      "descricao": "Uma torre de controle cênica e dilapidada, com uma vista panorâmica sobre os telhados da Oficina e a paisagem urbana escura do Distrito 7 ao amanhecer. A sala de controle está cheia de painéis de instrumentos quebrados e mapas rasgados, iluminados pela luz crescente do sol. O ar é limpo, mas frio, com o cheiro de metal enferrujado e a promessa de um novo dia. É um ponto de observação estratégico, onde as consequências da batalha podem ser vistas se consolidando.",
      "tags": "Observação, Estratégico, Consequência, Fim",
      "funcao": "Climax",
      "ancora_geografica": "Situada no ponto mais alto acessível dentro do complexo da Oficina, ou emergindo diretamente dele, a Torre de Vigia domina a paisagem. Está conectada à rede de corredores de serviço superiores e a passagens de manutenção que levam a outras partes elevadas da Oficina. Abaixo dela, estendem-se as entranhas industriais, e à distância, os contornos dos outros distritos da cidade começam a tomar forma sob a luz do amanhecer."
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
* **Subgêneros:** Noir, Ação Frenética
* **Escopo Geográfico:** Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.
* **Arquétipo:** A Busca
* **Foco Narrativo:** Mistura Noir Dieselpunk e Ação Frenética: Uma investigação tensa e rápida em um submundo industrial sombrio, onde cada beco pode esconder um perigo mortal ou uma pista crucial, tudo sob a ameaça iminente de uma guerra brutal.

### 2. Dados dos Locais (Step 1)
>>> DADOS DOS LOCAIS:
> **Portal Enferrujado da Oficina**
  - Descricao: A entrada principal para a Oficina Subterrânea. Uma estrutura colossal de metal riscado e corroído, com portões maciços que rangem com o vento incessante. O ar aqui cheira a graxa antiga e a chuva ácida, com o som distante e abafado de maquinaria em funcionamento e gritos ocasionais que ecoam das profundezas. Luzes incandescentes piscam erraticamente, lançando sombras dançantes sobre as poças oleosas.
  - Tags: Entrada, Industrial, Subterrâneo, Sombrio
  - Funcao: Inicial
  - Ancora geografica: Este portal é a única entrada terrestre significativa para a Oficina Subterrânea, localizado em um bolsão isolado de escombros e estaleiros abandonados, no limite do Distrito 7. O chão de metal desgastado se funde com a terra lamacenta do exterior, e o ruído do tráfego da cidade distante é quase inaudível aqui, substituído pelo gotejar constante de fluidos desconhecidos e o vento uivante através das brechas.

> **O Mercado das Sombras**
  - Descricao: Um labirinto caótico de barracas improvisadas e contêineres empilhados, iluminado por lâmpadas a cartucho e projetores improvisados. O ar é denso com fumaça de cachimbos, o cheiro de comida de rua duvidosa e o tom metálico de peças de máquinas sendo negociadas. Sussurros de negócios ilícitos se misturam com o barulho de mercadores vendendo desde componentes de motores até implantes cibernéticos questionáveis. É o coração pulsante do comércio negro na Oficina.
  - Tags: Mercado Negro, Social, Intriga, Comércio
  - Funcao: Intermediario
  - Ancora geografica: Localizado logo após os túneis iniciais da Entrada Enferrujada, o Mercado das Sombras se estende por um vasto espaço aberto dentro da Oficina. Ele é circundado por antigas docas de carga e armazéns, conectando-se a eles por passarelas metálicas instáveis e escadas de serviço corroídas. O som vibrante do mercado se mistura com o eco dos guindastes ociosos nos armazéns adjacentes.

> **Armazém 7B: O Vazio Refrigerado**
  - Descricao: Um espaço sinistro e silencioso onde o frio persiste mesmo no calor opressivo das entranhas da Oficina. O ar cheira a metal gelado, ozônio e algo levemente químico que ressoa com o 'gatilho' secreto. Luzes fluorescentes piscam sobre prateleiras metálicas vazias e uma poucos contêineres de transporte lacrados. O som predominante é o zumbido baixo e constante dos sistemas de refrigeração arcaicos, que parecem estar lutando para manter a temperatura.
  - Tags: Armazém, Frio, Pista, Escondido
  - Funcao: Intermediario
  - Ancora geografica: Aninhado entre o Mercado das Sombras e os Laboratórios de Química, o Armazém 7B é acessível por uma única porta de aço maciço e uma passagem de serviço estreita que leva aos fundos do Mercado. O som dos ventiladores de exaustão do laboratório vizinho é fracamente audível através das paredes bem isoladas, e o chão de concreto rachado abriga pequenas nascentes gotejantes de condensação.

> **Os Trens Fantasma do Setor C**
  - Descricao: Um trecho de trilhos de carga esquecido que serpenteia através de áreas abandonadas da Oficina. A escuridão aqui é quase total, quebrada apenas por ocasionalmente frestas de luz que penetram através de buracos no teto, revelando vagões enferrujados e derruídos. O ar é parado, mofado e carrega o cheiro de ferrugem e óleo velho. O silêncio é opressor, apenas pontuado pelo rangido ocasional de metal se acomodando ou o correr de algo pequeno e indesejado nas sombras.
  - Tags: Passagem, Perigo, Escombros, Abandonado
  - Funcao: Intermediario
  - Ancora geografica: Os trilhos dos Trens Fantasma formam uma 'veia' abandonada que conecta a área de carga do Mercado das Sombras às zonas mais profundas e perigosas da Oficina. Eles passam por baixo de pilares massivos de sustentação e ao lado de fábricas desativadas, com pontes de serviço precárias oferecendo acesso a níveis superiores, e túneis de drenagem parcialmente bloqueados levando a áreas mais baixas.

> **O Ninho dos Espectros**
  - Descricao: Antigo maquinário de fundição retorcido e abandonado que foi transformado em um covil improvisado. Chamas irregulares de fogueiras iluminam um espaço claustrofóbico, onde sucata e peças roubadas formam barricadas rudimentares. O ar aqui é carregado com o cheiro acre de metal queimado, suor e desespero. Gritos de comandos curtos e o clangor metálico de armas indicam que este é um local de ação e confronto.
  - Tags: Covil, Gangue, Confronto, Perigo
  - Funcao: Intermediario
  - Ancora geografica: Escondido no labirinto de 'Escombros e Indústrias Desativadas' que compõem o Setor C, o Ninho dos Espectros é acessível apenas por caminhos tortuosos entre máquinas enferrujadas e pilhas de sucata em desmoronamento. Um túnel de ventilação colapsado leva diretamente para dentro de sua área principal, e a saída mais 'segura' se abre para uma rampa de serviço que desce em direção aos Trens Fantasma.

> **Laboratório de Química 'O Alquimista'**
  - Descricao: Um espaço surpreendentemente organizado, mas sinistro, onde o cheiro pungente de produtos químicos reage com o odor metálico de Silas. Equipamentos de laboratório de alta tecnologia, muitos deles antigos, estão dispostos em bancadas de aço polido. Tubos borbulham com líquidos coloridos e venenosos, e mapas detalhados da cidade são espalhados sobre uma mesa central sob uma luz potente e fria. Este é o reino de Silas, a mente por trás de muitos negócios obscuros.
  - Tags: Laboratório, Científico, Pista, Conspiração
  - Funcao: Climax
  - Ancora geografica: O Laboratório de Silas é uma adição bem protegida ao 'complexo' da Oficina Subterrânea, localizado em um nível mais alto, acessível por um elevador de carga privado que parte do Mercado das Sombras ou através de uma passagem secreta ligada a um antigo escritório de engenharia. O som do zumbido dos sistemas de segurança e ventilação é constante, e a vista das luzes distantes da cidade, quando visível através de pequenas janelas reforçadas, contrasta com a escuridão industrial abaixo.

> **A Plataforma de Lançamento Esquecida**
  - Descricao: Uma área vasta e aberta nas entranhas da Oficina, outrora destinada ao lançamento de aeronaves ou foguetes, agora dominada por estruturas metálicas gigantescas e corroídas, tubulações de vapor e plataformas de observação em ruínas. O ar é quente, úmido e carrega o cheiro de óleo de motor e ozônio de equipamento elétrico. Uma sensação de grandeza perdida e abandono paira aqui, misturada com a tensão de um impasse iminente.
  - Tags: Abertura, Combate, Confronto, Estratégico
  - Funcao: Climax
  - Ancora geografica: Esta plataforma é o ponto mais baixo e central da Oficina, acessível por rampas maciças que descem do Mercado das Sombras e dos túneis adjacentes. Um rio de esgoto industrial corre por um lado, e as paredes monumentais da própria Oficina se erguem em todos os outros lados, repletas de escadas de serviço e passarelas que observam o campo de batalha. É um coliseu natural dentro da estrutura industrial.

> **Torre de Vigia do Distrito 7**
  - Descricao: Uma torre de controle cênica e dilapidada, com uma vista panorâmica sobre os telhados da Oficina e a paisagem urbana escura do Distrito 7 ao amanhecer. A sala de controle está cheia de painéis de instrumentos quebrados e mapas rasgados, iluminados pela luz crescente do sol. O ar é limpo, mas frio, com o cheiro de metal enferrujado e a promessa de um novo dia. É um ponto de observação estratégico, onde as consequências da batalha podem ser vistas se consolidando.
  - Tags: Observação, Estratégico, Consequência, Fim
  - Funcao: Climax
  - Ancora geografica: Situada no ponto mais alto acessível dentro do complexo da Oficina, ou emergindo diretamente dele, a Torre de Vigia domina a paisagem. Está conectada à rede de corredores de serviço superiores e a passagens de manutenção que levam a outras partes elevadas da Oficina. Abaixo dela, estendem-se as entranhas industriais, e à distância, os contornos dos outros distritos da cidade começam a tomar forma sob a luz do amanhecer.

### 3. Contexto da Trama
* **Argumento:** Na labiríntica 'Oficina Subterrânea', um complexo industrial abandonado que serve como ponto de encontro e mercado negro de peças nos confins do Distrito 7, uma carga inestimável composta por componentes raros de um protótipo aéreo foi roubada do receptador local, 'Silas, O Químico'. O roubo foi executado pelos 'Espectros', uma gangue secundária que opera nas sombras, não por ganância, mas para evitar que a carga caia nas mãos da ascendente 'Legião de Ferro'. Se os jogadores não recuperarem a carga antes do amanhecer, a Legião de Ferro usará o incidente como pretexto para aniquilar os Espectros e Silas, iniciando uma guerra aberta que mergulhará o Distrito 7 no caos, com potencial para se espalhar para outros setores da cidade.
* **Premissa Evidente:** Vocês foram contratados por Silas, O Químico, um receptador de tecnologia sombrio, para recuperar uma carga de componentes de alto valor roubada de seu esconderijo na Oficina Subterrânea. O tempo está se esgotando; a carga precisa estar de volta antes que o sol nasça, ou Silas promete consequências terríveis para quem falhar. As informações preliminares sugerem que os ladrões são uma gangue menor e sem importância, facilmente subjugável.
* **Premissa Oculta:** A carga roubada (componentes raros de protótipo aéreo) não é valiosa por si só, mas sim pela tecnologia que ela desbloqueia ou pela capacidade de sabotagem que representa. Os Espectros roubaram a carga para impedir que a Liga de Ferro a use para iniciar uma guerra territorial e eliminar qualquer oposição. Silas, o Químico, trabalhava em conluio com a Liga de Ferro, mas foi traído. A 'guerra entre gangues rivais' é um plano maior da Liga de Ferro para consolidar poder na cidade, usando este roubo como desculpa para uma ofensiva. Recuperar a carga pode significar entregá-la a Silas (potencialmente para a Liga), entregá-la aos Espectros (garantindo sua sobrevivência, mas atrasando o plano da Liga), ou descobrir uma terceira via para neutralizar o poder da Liga.

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
  "descricao_frente": "Nas profundezas do Dieselpunk Noir da Oficina Subterrânea, uma corrida contra o tempo se inicia. A busca por componentes roubados de um protótipo aéreo é o palco para uma intriga mortal, onde gangues rivais e mentes ardilosas jogam um jogo perigoso. O alvorecer trará não apenas a luz do dia, mas a potencial aniquilação e o caos desenfreado para o Distrito 7, a menos que a carga seja recuperada e a verdade venha à tona.",
  "elenco": [
    {
      "nome": "Silas, O Químico",
      "papel_funcao": "Receptor de Tecnologia e Mestre de Conspirações",
      "detalhe_marcante": "Seus dedos grossos e manchados de produtos químicos manipulam pipetas e componentes eletrônicos com a mesma delicadeza de quem tece seda.",
      "conviccao": "A ordem e o progresso só podem existir sob controle absoluto. Ele acredita que o caos atual da cidade justifica métodos drásticos para impor sua própria visão de 'estabilidade técnica'.",
      "contraste": "Quando não está em seu laboratório, ele veste um avental de couro impecável e passa horas em um pequeno museu de autômatos antigos, restaurando peças com reverência."
    },
    {
      "nome": "Kael, Líder dos Espectros",
      "papel_funcao": "Líder da Gangue Espectros",
      "detalhe_marcante": "Sempre usa um cachecol improvisado feito de fios elétricos coloridos, que protege parte do seu rosto corroído por produtos químicos industriais.",
      "conviccao": "A Legião de Ferro representa a tirania que esmagou seu bairro. Ele roubou a carga para que a Legião não pudesse usá-la como desculpa para exterminar seu povo e a resistência que ele representa.",
      "contraste": "Embora pense em táticas de guerrilha, ele adora alimentar os ratos que vivem nas entranhas da Oficina, tratando-os como mensageiros secretos."
    },
    {
      "nome": "Comandante Valerius da Legião de Ferro",
      "papel_funcao": "Líder da Facção Militar Ascendente",
      "detalhe_marcante": "Seu punho direito é um canhão de plasma customizado, que ele usa para 'destacar' pontos cruciais em mapas de operações, muitas vezes incriminando inocentes.",
      "conviccao": "A sociedade se desintegrou pela fraqueza. Ele acredita que apenas a força bruta e a total supressão da dissidência podem restaurar a ordem e a 'paz' que ele almeja para a cidade.",
      "contraste": "Possui uma coleção de discos de jazz antigos, que ouve apenas em privado, sonhando com um futuro onde as artes possam florescer de verdade."
    }
  ],
  "perigos": [
    {
      "nome": "A Emboscada dos Espectros",
      "tipo": "Horda",
      "impulso": "Crescer em força e destruir",
      "ameaca_verdade": "A gangue Espectros demonstra que a ordem imposta pela Legião de Ferro é tão brutal quanto o 'caos' que ela alega combater, forçando os heróis a questionar quem são os verdadeiros vilões.",
      "local_vinculado": "O Ninho dos Espectros",
      "rastro_destruicao": "Os poucos contêineres de carga recuperados pelos Espectros estão enterrados em sucata e pilhas de peças roubadas no Ninho, suas marcas de roubo são óbvias, e o local está fortificado.",
      "acao_iminente": "Armar emboscadas usando os corredores tortuosos em torno de seu covil e usar drones improvisados para espalhar desinformação sobre a localização exata da carga."
    },
    {
      "nome": "A Teia de Silas",
      "tipo": "Organização",
      "impulso": "Controlar através da influência e pactos",
      "ameaca_verdade": "A manipulação de Silas desafia a ideia de que a 'boa vontade' ou 'contratos' podem existir, mostrando como a confiança é apenas uma ferramenta para controle, minando a fé em alianças.",
      "local_vinculado": "Laboratório de Química 'O Alquimista'",
      "rastro_destruicao": "Os mapas e intrincados diagramas nas paredes do laboratório de Silas detalham as rotas de contrabando, os pactos com gangues menores e planos de contingência para a 'coleta' da carga supostamente roubada.",
      "acao_iminente": "Enviar agentes disfarçados ou mercenários para recuperar a carga por conta própria, eliminando quem estiver em seu caminho e tentando incriminar os Espectros ou os heróis."
    },
    {
      "nome": "A Mão Firme da Legião de Ferro",
      "tipo": "Governo Corrupto",
      "impulso": "Manter o status quo",
      "ameaca_verdade": "A Legião demonstra que a 'lei' e a 'ordem' são armas para opressão e expansão territorial, questionando se a justiça pode existir sob um regime autoritário.",
      "local_vinculado": "Torre de Vigia do Distrito 7",
      "rastro_destruicao": "Marcos de patrulha intensificada ao redor da Oficina e do Distrito 7. Veículos blindados da Legião de Ferro patrulham as fronteiras, e a comunicação com a cidade externa está sendo rigidamente monitorada.",
      "acao_iminente": "Desencadear uma operação de 'limpeza' brutal em toda a Oficina Subterrânea, derrubando quaisquer gangues ou indivíduos que se oponham à sua chegada e utilizando o roubo como justificativa para um ataque em larga escala."
    }
  ],
  "desastre_iminente": {
    "tipo_desastre": "Tirania",
    "descricao": "A Legião de Ferro, usando o roubo como pretexto e a desordem como desculpa, inicia uma campanha massiva de aniquilação. A Oficina Subterrânea é submergida em fogo e aço, seus habitantes caçados e eliminados. Silas é capturado e forçado a entregar todos os seus segredos tecnológicos. Kael e os Espectros são exterminados, ou pior, forçados a se tornarem escravos na nova ordem. O Distrito 7 se torna um território militarizado, a liberdade é extinta, e a sombra da Legião de Ferro se estende para o resto da cidade, prometendo uma era de controle absoluto e opressão sem fim."
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
* **Subgêneros:** Noir, Ação Frenética
* **Escopo Geográfico:** Nível 2 (Escopo Local - O Refúgio): A trama ocorre em um assentamento isolado ou base, focando em disputas de poder, defesa de perímetro ou intriga social.

### 2. Contexto da Trama
* **Argumento:** Na labiríntica 'Oficina Subterrânea', um complexo industrial abandonado que serve como ponto de encontro e mercado negro de peças nos confins do Distrito 7, uma carga inestimável composta por componentes raros de um protótipo aéreo foi roubada do receptador local, 'Silas, O Químico'. O roubo foi executado pelos 'Espectros', uma gangue secundária que opera nas sombras, não por ganância, mas para evitar que a carga caia nas mãos da ascendente 'Legião de Ferro'. Se os jogadores não recuperarem a carga antes do amanhecer, a Legião de Ferro usará o incidente como pretexto para aniquilar os Espectros e Silas, iniciando uma guerra aberta que mergulhará o Distrito 7 no caos, com potencial para se espalhar para outros setores da cidade.
* **Premissa Evidente:** Vocês foram contratados por Silas, O Químico, um receptador de tecnologia sombrio, para recuperar uma carga de componentes de alto valor roubada de seu esconderijo na Oficina Subterrânea. O tempo está se esgotando; a carga precisa estar de volta antes que o sol nasça, ou Silas promete consequências terríveis para quem falhar. As informações preliminares sugerem que os ladrões são uma gangue menor e sem importância, facilmente subjugável.
* **Premissa Oculta:** A carga roubada (componentes raros de protótipo aéreo) não é valiosa por si só, mas sim pela tecnologia que ela desbloqueia ou pela capacidade de sabotagem que representa. Os Espectros roubaram a carga para impedir que a Liga de Ferro a use para iniciar uma guerra territorial e eliminar qualquer oposição. Silas, o Químico, trabalhava em conluio com a Liga de Ferro, mas foi traído. A 'guerra entre gangues rivais' é um plano maior da Liga de Ferro para consolidar poder na cidade, usando este roubo como desculpa para uma ofensiva. Recuperar a carga pode significar entregá-la a Silas (potencialmente para a Liga), entregá-la aos Espectros (garantindo sua sobrevivência, mas atrasando o plano da Liga), ou descobrir uma terceira via para neutralizar o poder da Liga.
* **Arquétipos Permitidos:** Músculo: Você é grande, pesado. Machucar e fazer façanhas físicas é com você., Cabeça: Pensamento ágil, consegue operar sistemas e máquinas antigas., Volante: Atrás de um volante, não há igual. Você é uma fera das estradas., Vigia: Olhos atentos e sempre no horizonte. Consegue atirar muito bem., Boca: Sempre sabe o que dizer. Carisma em pessoa. Mesmo que isso traga problemas., Novato: Nunca conheceu um mundo que não esse. Quer provar seu valor para os seus.

### 3. Dados da Fase 1 (Estrutura)
* **Arquétipo Selecionado:** A Busca
* **Foco Narrativo:** Mistura Noir Dieselpunk e Ação Frenética: Uma investigação tensa e rápida em um submundo industrial sombrio, onde cada beco pode esconder um perigo mortal ou uma pista crucial, tudo sob a ameaça iminente de uma guerra brutal.

>>> LISTA DE LOCAIS (Referência para Localização dos Presságios):
> **Portal Enferrujado da Oficina**
  - Descricao: A entrada principal para a Oficina Subterrânea. Uma estrutura colossal de metal riscado e corroído, com portões maciços que rangem com o vento incessante. O ar aqui cheira a graxa antiga e a chuva ácida, com o som distante e abafado de maquinaria em funcionamento e gritos ocasionais que ecoam das profundezas. Luzes incandescentes piscam erraticamente, lançando sombras dançantes sobre as poças oleosas.
  - Tags: Entrada, Industrial, Subterrâneo, Sombrio
  - Funcao: Inicial
  - Ancora geografica: Este portal é a única entrada terrestre significativa para a Oficina Subterrânea, localizado em um bolsão isolado de escombros e estaleiros abandonados, no limite do Distrito 7. O chão de metal desgastado se funde com a terra lamacenta do exterior, e o ruído do tráfego da cidade distante é quase inaudível aqui, substituído pelo gotejar constante de fluidos desconhecidos e o vento uivante através das brechas.

> **O Mercado das Sombras**
  - Descricao: Um labirinto caótico de barracas improvisadas e contêineres empilhados, iluminado por lâmpadas a cartucho e projetores improvisados. O ar é denso com fumaça de cachimbos, o cheiro de comida de rua duvidosa e o tom metálico de peças de máquinas sendo negociadas. Sussurros de negócios ilícitos se misturam com o barulho de mercadores vendendo desde componentes de motores até implantes cibernéticos questionáveis. É o coração pulsante do comércio negro na Oficina.
  - Tags: Mercado Negro, Social, Intriga, Comércio
  - Funcao: Intermediario
  - Ancora geografica: Localizado logo após os túneis iniciais da Entrada Enferrujada, o Mercado das Sombras se estende por um vasto espaço aberto dentro da Oficina. Ele é circundado por antigas docas de carga e armazéns, conectando-se a eles por passarelas metálicas instáveis e escadas de serviço corroídas. O som vibrante do mercado se mistura com o eco dos guindastes ociosos nos armazéns adjacentes.

> **Armazém 7B: O Vazio Refrigerado**
  - Descricao: Um espaço sinistro e silencioso onde o frio persiste mesmo no calor opressivo das entranhas da Oficina. O ar cheira a metal gelado, ozônio e algo levemente químico que ressoa com o 'gatilho' secreto. Luzes fluorescentes piscam sobre prateleiras metálicas vazias e uma poucos contêineres de transporte lacrados. O som predominante é o zumbido baixo e constante dos sistemas de refrigeração arcaicos, que parecem estar lutando para manter a temperatura.
  - Tags: Armazém, Frio, Pista, Escondido
  - Funcao: Intermediario
  - Ancora geografica: Aninhado entre o Mercado das Sombras e os Laboratórios de Química, o Armazém 7B é acessível por uma única porta de aço maciço e uma passagem de serviço estreita que leva aos fundos do Mercado. O som dos ventiladores de exaustão do laboratório vizinho é fracamente audível através das paredes bem isoladas, e o chão de concreto rachado abriga pequenas nascentes gotejantes de condensação.

> **Os Trens Fantasma do Setor C**
  - Descricao: Um trecho de trilhos de carga esquecido que serpenteia através de áreas abandonadas da Oficina. A escuridão aqui é quase total, quebrada apenas por ocasionalmente frestas de luz que penetram através de buracos no teto, revelando vagões enferrujados e derruídos. O ar é parado, mofado e carrega o cheiro de ferrugem e óleo velho. O silêncio é opressor, apenas pontuado pelo rangido ocasional de metal se acomodando ou o correr de algo pequeno e indesejado nas sombras.
  - Tags: Passagem, Perigo, Escombros, Abandonado
  - Funcao: Intermediario
  - Ancora geografica: Os trilhos dos Trens Fantasma formam uma 'veia' abandonada que conecta a área de carga do Mercado das Sombras às zonas mais profundas e perigosas da Oficina. Eles passam por baixo de pilares massivos de sustentação e ao lado de fábricas desativadas, com pontes de serviço precárias oferecendo acesso a níveis superiores, e túneis de drenagem parcialmente bloqueados levando a áreas mais baixas.

> **O Ninho dos Espectros**
  - Descricao: Antigo maquinário de fundição retorcido e abandonado que foi transformado em um covil improvisado. Chamas irregulares de fogueiras iluminam um espaço claustrofóbico, onde sucata e peças roubadas formam barricadas rudimentares. O ar aqui é carregado com o cheiro acre de metal queimado, suor e desespero. Gritos de comandos curtos e o clangor metálico de armas indicam que este é um local de ação e confronto.
  - Tags: Covil, Gangue, Confronto, Perigo
  - Funcao: Intermediario
  - Ancora geografica: Escondido no labirinto de 'Escombros e Indústrias Desativadas' que compõem o Setor C, o Ninho dos Espectros é acessível apenas por caminhos tortuosos entre máquinas enferrujadas e pilhas de sucata em desmoronamento. Um túnel de ventilação colapsado leva diretamente para dentro de sua área principal, e a saída mais 'segura' se abre para uma rampa de serviço que desce em direção aos Trens Fantasma.

> **Laboratório de Química 'O Alquimista'**
  - Descricao: Um espaço surpreendentemente organizado, mas sinistro, onde o cheiro pungente de produtos químicos reage com o odor metálico de Silas. Equipamentos de laboratório de alta tecnologia, muitos deles antigos, estão dispostos em bancadas de aço polido. Tubos borbulham com líquidos coloridos e venenosos, e mapas detalhados da cidade são espalhados sobre uma mesa central sob uma luz potente e fria. Este é o reino de Silas, a mente por trás de muitos negócios obscuros.
  - Tags: Laboratório, Científico, Pista, Conspiração
  - Funcao: Climax
  - Ancora geografica: O Laboratório de Silas é uma adição bem protegida ao 'complexo' da Oficina Subterrânea, localizado em um nível mais alto, acessível por um elevador de carga privado que parte do Mercado das Sombras ou através de uma passagem secreta ligada a um antigo escritório de engenharia. O som do zumbido dos sistemas de segurança e ventilação é constante, e a vista das luzes distantes da cidade, quando visível através de pequenas janelas reforçadas, contrasta com a escuridão industrial abaixo.

> **A Plataforma de Lançamento Esquecida**
  - Descricao: Uma área vasta e aberta nas entranhas da Oficina, outrora destinada ao lançamento de aeronaves ou foguetes, agora dominada por estruturas metálicas gigantescas e corroídas, tubulações de vapor e plataformas de observação em ruínas. O ar é quente, úmido e carrega o cheiro de óleo de motor e ozônio de equipamento elétrico. Uma sensação de grandeza perdida e abandono paira aqui, misturada com a tensão de um impasse iminente.
  - Tags: Abertura, Combate, Confronto, Estratégico
  - Funcao: Climax
  - Ancora geografica: Esta plataforma é o ponto mais baixo e central da Oficina, acessível por rampas maciças que descem do Mercado das Sombras e dos túneis adjacentes. Um rio de esgoto industrial corre por um lado, e as paredes monumentais da própria Oficina se erguem em todos os outros lados, repletas de escadas de serviço e passarelas que observam o campo de batalha. É um coliseu natural dentro da estrutura industrial.

> **Torre de Vigia do Distrito 7**
  - Descricao: Uma torre de controle cênica e dilapidada, com uma vista panorâmica sobre os telhados da Oficina e a paisagem urbana escura do Distrito 7 ao amanhecer. A sala de controle está cheia de painéis de instrumentos quebrados e mapas rasgados, iluminados pela luz crescente do sol. O ar é limpo, mas frio, com o cheiro de metal enferrujado e a promessa de um novo dia. É um ponto de observação estratégico, onde as consequências da batalha podem ser vistas se consolidando.
  - Tags: Observação, Estratégico, Consequência, Fim
  - Funcao: Climax
  - Ancora geografica: Situada no ponto mais alto acessível dentro do complexo da Oficina, ou emergindo diretamente dele, a Torre de Vigia domina a paisagem. Está conectada à rede de corredores de serviço superiores e a passagens de manutenção que levam a outras partes elevadas da Oficina. Abaixo dela, estendem-se as entranhas industriais, e à distância, os contornos dos outros distritos da cidade começam a tomar forma sob a luz do amanhecer.

### 4. Dados da Fase 2 (Ameaças e Elenco)
Use estes dados para definir QUEM causa os presságios.

>>> ELENCO PRINCIPAL:
> **Silas, O Químico**
  - Papel funcao: Receptor de Tecnologia e Mestre de Conspirações
  - Detalhe marcante: Seus dedos grossos e manchados de produtos químicos manipulam pipetas e componentes eletrônicos com a mesma delicadeza de quem tece seda.
  - Conviccao: A ordem e o progresso só podem existir sob controle absoluto. Ele acredita que o caos atual da cidade justifica métodos drásticos para impor sua própria visão de 'estabilidade técnica'.
  - Contraste: Quando não está em seu laboratório, ele veste um avental de couro impecável e passa horas em um pequeno museu de autômatos antigos, restaurando peças com reverência.

> **Kael, Líder dos Espectros**
  - Papel funcao: Líder da Gangue Espectros
  - Detalhe marcante: Sempre usa um cachecol improvisado feito de fios elétricos coloridos, que protege parte do seu rosto corroído por produtos químicos industriais.
  - Conviccao: A Legião de Ferro representa a tirania que esmagou seu bairro. Ele roubou a carga para que a Legião não pudesse usá-la como desculpa para exterminar seu povo e a resistência que ele representa.
  - Contraste: Embora pense em táticas de guerrilha, ele adora alimentar os ratos que vivem nas entranhas da Oficina, tratando-os como mensageiros secretos.

> **Comandante Valerius da Legião de Ferro**
  - Papel funcao: Líder da Facção Militar Ascendente
  - Detalhe marcante: Seu punho direito é um canhão de plasma customizado, que ele usa para 'destacar' pontos cruciais em mapas de operações, muitas vezes incriminando inocentes.
  - Conviccao: A sociedade se desintegrou pela fraqueza. Ele acredita que apenas a força bruta e a total supressão da dissidência podem restaurar a ordem e a 'paz' que ele almeja para a cidade.
  - Contraste: Possui uma coleção de discos de jazz antigos, que ouve apenas em privado, sonhando com um futuro onde as artes possam florescer de verdade.

>>> PERIGOS ATIVOS:
> **A Emboscada dos Espectros**
  - Tipo: Horda
  - Impulso: Crescer em força e destruir
  - Ameaca verdade: A gangue Espectros demonstra que a ordem imposta pela Legião de Ferro é tão brutal quanto o 'caos' que ela alega combater, forçando os heróis a questionar quem são os verdadeiros vilões.
  - Local vinculado: O Ninho dos Espectros
  - Rastro destruicao: Os poucos contêineres de carga recuperados pelos Espectros estão enterrados em sucata e pilhas de peças roubadas no Ninho, suas marcas de roubo são óbvias, e o local está fortificado.
  - Acao iminente: Armar emboscadas usando os corredores tortuosos em torno de seu covil e usar drones improvisados para espalhar desinformação sobre a localização exata da carga.

> **A Teia de Silas**
  - Tipo: Organização
  - Impulso: Controlar através da influência e pactos
  - Ameaca verdade: A manipulação de Silas desafia a ideia de que a 'boa vontade' ou 'contratos' podem existir, mostrando como a confiança é apenas uma ferramenta para controle, minando a fé em alianças.
  - Local vinculado: Laboratório de Química 'O Alquimista'
  - Rastro destruicao: Os mapas e intrincados diagramas nas paredes do laboratório de Silas detalham as rotas de contrabando, os pactos com gangues menores e planos de contingência para a 'coleta' da carga supostamente roubada.
  - Acao iminente: Enviar agentes disfarçados ou mercenários para recuperar a carga por conta própria, eliminando quem estiver em seu caminho e tentando incriminar os Espectros ou os heróis.

> **A Mão Firme da Legião de Ferro**
  - Tipo: Governo Corrupto
  - Impulso: Manter o status quo
  - Ameaca verdade: A Legião demonstra que a 'lei' e a 'ordem' são armas para opressão e expansão territorial, questionando se a justiça pode existir sob um regime autoritário.
  - Local vinculado: Torre de Vigia do Distrito 7
  - Rastro destruicao: Marcos de patrulha intensificada ao redor da Oficina e do Distrito 7. Veículos blindados da Legião de Ferro patrulham as fronteiras, e a comunicação com a cidade externa está sendo rigidamente monitorada.
  - Acao iminente: Desencadear uma operação de 'limpeza' brutal em toda a Oficina Subterrânea, derrubando quaisquer gangues ou indivíduos que se oponham à sua chegada e utilizando o roubo como justificativa para um ataque em larga escala.

* **Desastre Iminente (Game Over):** Tirania - A Legião de Ferro, usando o roubo como pretexto e a desordem como desculpa, inicia uma campanha massiva de aniquilação. A Oficina Subterrânea é submergida em fogo e aço, seus habitantes caçados e eliminados. Silas é capturado e forçado a entregar todos os seus segredos tecnológicos. Kael e os Espectros são exterminados, ou pior, forçados a se tornarem escravos na nova ordem. O Distrito 7 se torna um território militarizado, a liberdade é extinta, e a sombra da Legião de Ferro se estende para o resto da cidade, prometendo uma era de controle absoluto e opressão sem fim.

### 5. Matriz de Controle de Informação
Conecte os presságios aos segredos abaixo (Camada de Informação).

>>> SEGREDOS DA CAMPANHA:
  - Titulo: A Verdadeira Natureza da Carga
  - A verdade: Os componentes roubados são peças-chave para um novo sistema de armamento aéreo 'silencioso' que a Liga de Ferro planeja usar para subjugar os distritos rivais e consolidar seu controle sobre a cidade.
  - A expectativa: Os jogadores acreditam que a carga é apenas 'valiosa' no sentido de dinheiro ou poder de barganha para Silas. Eles a veem como um item tecnológico de alto mercado negro.
  - A camuflagem: A carga está em um contêiner discreto, marcado apenas com um número de série genérico. Silas descreve a carga vagamente como 'coisas que fazem os céus tremerem', sem especificar para quem ou para quê.
  - O gatilho: Investigar o contêiner onde a carga original estava armazenada, encontrar anotações ou planos parciais de Silas sobre seu destino, ou interrogar um membro capturado dos Espectros que revela o propósito militar.
  - A revelacao: Os jogadores descobrem que estão lidando com a peça central de uma arma de guerra, e que a 'guerra de gangues' é um plano mais sinistro para justificar a ascensão de uma nova força militar corporativa ou de gangue.
  - Id: 1

  - Titulo: A Traição de Silas
  - A verdade: Silas, O Químico, não é apenas um receptador; ele era o intermediário original da Liga de Ferro para os componentes. Os Espectros o roubaram não só para frustrar a Liga, mas também como retaliação por um acordo anterior não cumprido por Silas, que resultou em baixas para os Espectros.
  - A expectativa: Os jogadores consideram Silas uma vítima legítima, um empresário sombrio sendo explorado por gangues, e que precisa da carga de volta para seu próprio 'negócio'.
  - A camuflagem: Silas parece genuinamente perturbado e preocupado com a perda. Ele pode omitir detalhes sobre sua própria participação no esquema da Liga de Ferro, ou atribuir a culpa inteiramente às gangues.
  - O gatilho: Encontrar evidências de comunicação entre Silas e a Liga de Ferro, rastrear o rastro de dinheiro ou subornos de Silas, ou ouvir sussurros de informantes no submundo sobre a verdadeira lealdade de Silas.
  - A revelacao: Os jogadores descobrem que Silas é um traidor de múltiplas partes, que estava colaborando com a Liga de Ferro e que o roubo teve um motivo mais profundo relacionado a vingança dos Espectros por ações passadas de Silas em nome da Liga.
  - Id: 2

  - Titulo: Os Verdadeiros Culpados (e Inocentes)
  - A verdade: A 'guerra entre gangues' iminente é um plano orquestrado pela Liga de Ferro. Os Espectros, embora sejam ladrões, estão agindo por desespero e para impedir a Liga, não para iniciar um conflito em larga escala. A verdadeira ameaça à paz (e à cidade) é a Liga de Ferro, que quer que os Espectros e Silas sejam destruídos para criar um vácuo de poder que eles possam preencher.
  - A expectativa: Os jogadores acreditam que a ameaça de 'guerra entre gangues rivais' é uma consequência direta e inevitável do roubo, e que eles precisam controlar ou eliminar de um dos lados (provavelmente os Espectros) para evitar a escalada.
  - A camuflagem: O incidente é apresentado como um conflito turfista comum. A presença e a influência da Liga de Ferro são sutis, operando nas sombras ou através de intermediários, não aparecendo como um jogador principal inicialmente.
  - O gatilho: Testemunhar o comportamento altamente organizado e coordenado dos 'espectros' (que podem ser mercenários contratados pela Liga para incriminar os Espectros reais) ou obter informações de um contato de inteligência que revela o plano da Liga de Ferro para a 'pacificação' do Distrito 7.
  - A revelacao: Os jogadores percebem que a luta contra os Espectros ou a recuperação da carga para Silas não resolverá o problema; é a Liga de Ferro a mente por trás da violência, e neutralizá-los é a única maneira de evitar a verdadeira guerra.
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
      "meta_estrutura": "O Chamado: O evento que torna ficar em casa impossível (um roubo)",
      "local_sugerido": "Portal Enferrujado da Oficina",
      "o_pressagio": "O ar de diesel e ozônio na entrada da Oficina Subterrânea é cortado por uma voz rouca e desesperada. Silas, O Químico, visivelmente abalado, mas com um brilho calculista nos olhos, oferece uma recompensa generosa aos heróis para recuperar uma carga de componentes de protótipo aéreo roubada. Ele enfatiza a urgência: antes do amanhecer, um ataque em larga escala acontecerá, e a perda da carga apenas acelerará o desastre.",
      "argumento_arco_historia": "Silas, agindo de acordo com seus planos com a Liga de Ferro (Matriz 2), orquestrou o 'roubo' para usar como pretexto contra os Espectros e para testar as águas. Ele encena o desespero na entrada principal da Oficina, atraindo os heróis para que recuperem a carga, possivelmente alimentando sua paranoia ou tentando incriminá-los caso falhem. O roubo em si foi executado discretamente pelos Espectros, sob ordens de Kael (Matriz 3), para frustrar os planos da Liga.",
      "premissas_arco_historia": {
        "evidente": "Vocês foram contratados como mercenários por um receptador sombrio, Silas, para recuperar tecnologia valiosa roubada por uma gangue inferior. O tempo é essencial, e o perigo aparente são os Espectros e as consequências da FALHA.",
        "oculta": "O 'roubo' foi um jogo de Silas para iniciar um conflito, e a carga tem um propósito militar muito mais sombrio do que Silas revela. A verdadeira ameaça não é a gangue, mas quem está manipulando o incidente para desestabilizar o Distrito 7."
      },
      "camada_informacao": {
        "id_matriz": 2,
        "conexao_explicada": "O desespero e a urgência de Silas parecem genuínos, mas a menção de 'consequências terríveis' e um 'ataque em larga escala' (sem especificar de quem) podem ser um primeiro indício de sua capacidade de manipulação e de como ele pode estar jogando ambos os lados, levantando suspeitas sobre sua verdadeira lealdade."
      }
    },
    {
      "ordem": 2,
      "meta_estrutura": "A Jornada: O mundo se expande. O Presságio introduz perigos nos caminhos.",
      "local_sugerido": "O Mercado das Sombras",
      "o_pressagio": "Ao adentrarem o labiríntico Mercado das Sombras em busca de pistas, os heróis encontram uma cena de tensão crescente. Os comerciantes estão apavorados, negociando em voz baixa. De repente, luzes de busca varrem o local, e mercenários com uniformes brancos e cinzas (sutis, mas distintivos, não a armadura completa da Legião ainda) executam um 'redistribuição forçada' de bens, intimidando e 'requisitando' itens. Um Sussurro é ouvido: 'A Liga está limpando as bordas antes de avançar'.",
      "argumento_arco_historia": "A 'limpeza' no Mercado das Sombras é uma operação de inteligência e intimidação orquestrada pela Liga de Ferro (Matriz 3) para testar as defesas da Oficina, identificar potenciais rivais e coletar informações sobre o terreno e as gangues menores. Não é um confronto direto com os Espectros ainda, mas uma demonstração de força calculada para criar medo e instabilidade, complicando a vida de Silas e dos heróis, e direcionando a atenção para os Espectros como os 'causadores' do problema.",
      "premissas_arco_historia": {
        "evidente": "Os heróis investigam o mercado negro em busca da carga, mas são apanhados no meio de uma 'operação de segurança' liderada por uma facção desconhecida, que apreende mercadorias e intimida mercadores. A missão aparente é evitar serem detectados ou presos, e continuar a busca pela carga.",
        "oculta": "Os 'agentes de segurança' não são apenas bandidos comuns; são da Liga de Ferro, testando o terreno para uma ofensiva maior. Eles podem estar disfarçados ou operando sob um codinome para evitar confronto direto com Silas ou para não revelar sua mão contra os Espectros ainda. A pressão não é puramente sobre a carga, mas sobre o controle do distrito."
      },
      "camada_informacao": {
        "id_matriz": 3,
        "conexao_explicada": "A presença dessas forças 'disfarçadas' sugere que o conflito não é um simples confronto entre Silas e os Espectros, mas que uma terceira força (a Liga de Ferro) está orquestrando ou se beneficiando do caos, com planos muito maiores do que os heróis inicialmente entenderam."
      }
    },
    {
      "ordem": 3,
      "meta_estrutura": "Frustração (Barreira): o caminho é bloqueado. O Presságio é um revés significativo ou a perda de um refúgio.",
      "local_sugerido": "O Ninho dos Espectros",
      "o_pressagio": "Rastros levam os heróis a um antigo maquinário de fundição abandonado, o 'Ninho dos Espectros'. No entanto, ao se aproximarem, são recebidos por uma barragem de fogo de armas improvisadas e explosivos rudimentares. Perto das barricadas de sucata, eles encontram um dos contêineres roubados de Silas, brutalmente danificado e escancarado, espalhando componentes espalhados e quebrados pela lama. Kael, o líder dos Espectros, aparece brevemente em uma passarela superior, gritando que não entregarão nada à 'máfia da Liga' ou seus cães de aluguel, antes de sumir com seu pessoal.",
      "argumento_arco_historia": "Kael e os Espectros, sabendo que Silas os traiu e que a Liga de Ferro está chegando, decidiram destruir parte da carga para impedir que caísse nas mãos erradas (Matriz 1) e usar seu covil como ponto de resistência. Eles estão lutando pela sobrevivência e defendendo seu território de Silas ('os cães de aluguel') e da Liga. Os heróis são forçados a uma escolha brutal: tentar tomar o que resta da carga aos Espectros em um confronto direto, isolando-os ainda mais e alimentando a narrativa da Liga, ou tentar uma abordagem menos combativa, mas arriscando perder mais tempo e a carga.",
      "premissas_arco_historia": {
        "evidente": "Os heróis encontram Kael e os Espectros defendendo seu covil, com parte da carga destruída. Kael os considera mercenários de Silas ou cães de aluguel da Liga e os ataca. A missão aparente é superar os Espectros, recuperar a carga restante e lidar com Kael.",
        "oculta": "Os Espectros não são os vilões principais; eles estão agindo por desespero contra a Liga de Ferro e a traição de Silas. Destruir parcialmente a carga foi um ato de desafio, não de malícia. Kael está defendendo seu povo e tentando impedir que a carga seja usada como arma da Liga, revelando a complexidade moral da situação."
      },
      "camada_informacao": {
        "id_matriz": 1,
        "conexao_explicada": "A destruição parcial da carga e a declaração de Kael sobre não querer que ela caia nas mãos da 'máfia da Liga' sugere que o valor da carga não é o que Silas apregoa. Os heróis podem descobrir que estão lidando com peças de um 'sistema de armamento' sombrio, e que a 'guerra entre gangues' é um plano maior para justificar a ascensão da Liga de Ferro."
      }
    },
    {
      "ordem": 4,
      "meta_estrutura": "Provações Finais: O destino está à vista, mas é mortal.",
      "local_sugerido": "Laboratório de Química 'O Alquimista'",
      "o_pressagio": "Os heróis rastreiam Silas até seu laboratório, apenas para encontrá-lo em meio a uma armadilha de seus próprios dispositivos de segurança. Ele se revela traiçoeiro, mas não um inimigo forte em combate direto. Ele confessa ter orquestrado o roubo com a Liga, mas que foi traído por eles e que os Espectros sabiam de sua colaboração e tinham motivos próprios para o roubo (Matriz 2). Ele implora aos heróis para que recuperem a carga restante (talvez prometendo que ele pode 'neutralizá-la' para eles) ou para que o ajudem a escapar, enquanto a Legião de Ferro, alertada por Silas como plano B, começa a cercar a Oficina e enviar patrulhas pesadas.",
      "argumento_arco_historia": "Silas, acuado, tenta manipular os heróis uma última vez. Ele revela parte da verdade sobre a colaboração com a Liga e o roubo planejado, mas omite que a carga é uma arma. Sua intenção é que os heróis ou recuperem a carga para ele (para que ele possa entregá-la de volta à Liga, completando seu 'trato' e obtendo proteção) ou que ele escape, deixando os heróis lutarem contra a Liga. A chegada antecipada da Legião de Ferro (Matriz 3), que Silas alertou, transforma o laboratório em uma zona de perigo iminente, onde os heróis precisam lidar com Silas e a escalada da ameaça da Liga.",
      "premissas_arco_historia": {
        "evidente": "Ao encontrar Silas, os heróis descobrem que ele não é uma vítima, mas um traidor que trabalhou com a Liga. Ele oferece uma barganha: ajude-o a recuperar a carga 'para neutralizar' a ameaça, ou ajude-o a escapar enquanto a Legião de Ferro cerca o local. A missão aparente é lidar com Silas e a ameaça iminente da Legião.",
        "oculta": "A carga é uma arma da Liga de Ferro que Silas ajudou a desenvolver. A 'neutralização' que ele propõe é na verdade uma forma de entregá-la de volta à Liga para consolidar seu acordo. A Legião de Ferro está agindo com base em informações de Silas, que está tentando vender aos seus opressores, e os heróis estão no centro de sua teia de traição."
      },
      "camada_informacao": {
        "id_matriz": 2,
        "conexao_explicada": "A confissão de Silas sobre sua colaboração com a Liga e a traição mútua entre ele e a Liga esclarece a profundidade de suas manipulações (Matriz 2). A consciência de que Silas está ligado à Liga e que ele quer a carga de volta 'para neutralizar' a ameaça (o que é uma mentira) expõe a verdade sobre a natureza da carga e o papel de Silas em fornecê-la para a Liga."
      }
    },
    {
      "ordem": 5,
      "meta_estrutura": "O Objetivo: O prêmio está ao alcance. O Presságio é a última salvaguarda ou o despertar do guardião final.",
      "local_sugerido": "A Plataforma de Lançamento Esquecida",
      "o_pressagio": "O rastro dos componentes restantes da carga, ou a tentativa de Silas de levá-los para um local seguro, leva os heróis à Plataforma de Lançamento Esquecida. Lá, a Legião de Ferro, liderada pelo Comandante Valerius, já prepara a 'operação de limpeza' final. Eles utilizam um pequeno grupo de 'Espectros' capturados (ou mercenários disfarçados de Espectros) para encenar um confronto, justificando assim a aniquilação total iminente. A carga, ou o que restou dela, está em posse de Valerius ou em um veículo de transporte da Liga, pronto para ser levado, consolidando o poder da Legião. Kael, se ainda vivo, pode ter uma última chance de aparecer para proteger seu povo ou fazer um sacrifício final.",
      "argumento_arco_historia": "Esta é a última resistência e a revelação final. A Legião de Ferro emprega uma força de elite e um plano de desinformação para justificar sua ofensiva massiva. Valerius pretende usar a carga (Matriz 1) como peça central para o seu poder, e a aniquilação da Oficina é para silenciar todas as testemunhas e consolidar o controle. Os heróis devem decidir se lutam para impedir a Legião (e ganhar o prêmio da liberdade ou impedir a arma), salvá-los dos Espectros restantes (se for o caso), ou lidar com Silas e a carga final. O 'guardião final' aqui é a própria Legião de Ferro, em toda a sua glória tirânica.",
      "premissas_arco_historia": {
        "evidente": "Os heróis chegam ao local onde a carga final está, encontrando a Legião de Ferro pronta para iniciar uma guerra brutal, usando supostos confrontos de gangues como pretexto. A missão aparente é recuperar a carga, salvar os Espectros, ou simplesmente sobreviver ao ataque da Legião. A 'vitória' seria pegar a carga e escapar.",
        "oculta": "Recuperar a carga não é o fim; é a prova de que os heróis podem parar ou expor a verdadeira ameaça: a escala da ambição destrutiva da Legião de Ferro e a arma que ela pretende usar. A verdadeira vitória seria expor o plano da Liga e potencialmente usar a própria carga para desmantelar seu poder, em vez de apenas fugir com ela."
      },
      "camada_informacao": {
        "id_matriz": 3,
        "conexao_explicada": "A cena na Plataforma de Lançamento é a confirmação máxima de que a 'guerra entre gangues' era um falso pretexto orquestrado pela Legião de Ferro. Valerius e seus homens demonstram o objetivo final da Liga: controle total, utilizando a carga (arma secreta) como a garantia desse controle. A 'verdade maior' é exposta na face do poder militar bruto da Liga, que vê os Espectros e Silas apenas como obstáculos a serem removidos para o 'progresso'. A ação dos heróis aqui definirá se a Legião de Ferro consolida sua tirania (Desastre Iminente) ou se a verdade é exposta."
      }
    }
  ],
  "perguntas_dramatica": [
    "Será que a busca por 'componentes raros' levará os heróis a serem cúmplices involuntários na ascensão de uma nova tirania, ou eles conseguirão desmantelar o plano da Legião antes que a guerra total consuma o Distrito 7?",
    "Diante da corrupção de Silas e da brutalidade da Legião de Ferro, será que a 'ordem' que os jogadores buscam só pode ser alcançada através de meios moralmente ambíguos, ou existe uma linha clara que separa os heróis dos monstros que caçam?",
    "Se a verdadeira ameaça for a Liga de Ferro, como os heróis podem provar a culpabilidade de uma organização que criminaliza seus próprios oponentes e controla a informação, e quais sacrifícios serão necessários para trazer a verdade à luz em meio ao conflito Dieselpunk?"
  ]
}
```
