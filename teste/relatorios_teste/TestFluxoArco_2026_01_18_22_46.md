# Relatório: Teste Pipeline Completo: Trama -> Frente -> Arco
**Data:** 2026_01_18_22_46 | **Status:** ✅ Sucesso

## 📊 Métricas de Execução

| Métrica | 1. Trama | 2. Front Arquiteto | 3. Front World | 4. Front Story | 5. Arco História | Total |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Tempo Total** | 8.61s | 8.85s | 5.60s | 14.35s | 32.70s | **70.11s** |
| **Tokens Entrada** | 877 | 3147 | 3988 | 7137 | 3902 | **19051** |
| **Tokens Saída** | 2081 | 2134 | 1301 | 3519 | 7917 | **16952** |
| **Tokens Total** | 2958 | 5281 | 5289 | 10656 | 11819 | **36003** |
| **Custo Estimado** | $0.000920 | $0.001168 | $0.000919 | $0.002121 | $0.003557 | **$0.008686** |

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
    "justificativa_escopo": "A trama de recuperação de carga sob pressão temporal e a iminência de guerra entre gangues se encaixam perfeitamente em um ambiente confinado como um refúgio isolado, onde as consequências de uma falha são imediatas e palpáveis. Isso permite um foco em intrigas e na defesa contra ameaças internas e externas.",
    "justificativa_estilo": "A combinação de 'carga roubada', 'recuperar antes do amanhecer' e 'guerra entre gangues' em um cenário Dieselpunk evoca um clima de urgência e desespero. Elementos de Noir, com seus mistérios, personagens sombrios e moralidade ambígua, se misturam à ação frenética prometida pela perseguição e pelo conflito iminente entre facções."
  },
  "argumento": {
    "texto": "Em \"O Fim da Linha\", um assentamento Dieselpunk isolado e decadente, a carga roubada não é um simples carregamento, mas sim um protótipo de arma experimental desenvolvido por uma das gangues rivais, a \"Ferro-Velho\". Roubada pelo grupo mercenário \"Corvos Mecânicos\", a carga foi vendida a uma terceira facção, os \"Sombras Aéreas\", que planejam usá-la para subjugar o assentamento e iniciar a guerra declarada pelo título. Os jogadores são contratados pela gangue \"Ferro-Velho\" para recuperar o protótipo antes que o sol nasça, para evitar retaliação e manter o tênue equilíbrio de poder no \"Fim da Linha\". A motivação oculta da \"Ferro-Velho\" é, na verdade, que eles próprios planejavam vender o protótipo, mas foram traídos pelos Corvos Mecânicos. Os Sombras Aéreas, por sua vez, foram manipulados a comprar algo que pensavam ser diferente, e a guerra iminente é a consequência desse engodo.",
    "justificativa": "A trama gira em torno de um roubo que desencadeia uma crise, e em um cenário Dieselpunk, a carga ganha um peso tecnológico e estratégico. O escopo local do 'Refúgio' reforça a ideia de um local isolado onde a lei é ditada pela força e a decadência é palpável. O 'Por quê' envolve traição e manipulação entre as facções, com os jogadores inicialmente alheios a essa camada mais profunda de engano."
  },
  "premissas": {
    "evidente": {
      "texto": "Um carregamento valioso de componentes para as máquinas que mantêm \"O Fim da Linha\" funcionando foi roubado. Se não for recuperado antes do amanhecer, a gangue \"Ferro-Velho\" não conseguirá manter suas defesas, levando a um ataque das gangues rivais e a uma guerra total no assentamento.",
      "funcao": "Estabelece a urgência e o objetivo imediato. Cria a expectativa de uma missão de recuperação direta e a ameaça de conflito aberto."
    },
    "oculta": {
      "texto": "O carregamento roubado é, na verdade, um protótipo de arma experimental perigosa. Foi roubado pelos mercenários \"Corvos Mecânicos\" dos presumidos donos originais (\"Ferro-Velho\"), e não é um mero acessório para manter as máquinas. Os \"Sombras Aéreas\" compraram essa arma sem saber de sua verdadeira natureza ou potencial destrutivo, e sua ativação pelo amanhecer deflagrará a guerra, não a manutenção do assentamento. A \"Ferro-Velho\" quer o protótipo de volta não só para evitar a guerra, mas também para recuperar seu investimento e manter seu segredo de que eles mesmos planejavam vendê-lo para terceiros.",
      "funcao": "Subverte a expectativa de uma simples recuperação de peças. Revela o envolvimento de mais facções e a natureza perigosa da carga, adicionando camadas de intriga, traição e perigo químico/tecnológico."
    },
    "justificativa": "As premissas criam um 'gancho' de urgência e serviço (Evidente), e um 'twist' que revela a verdadeira natureza do perigo e a complexidade dos atores envolvidos (Oculta). Essa dicotomia é essencial para o gênero Noir e a gestão de mistérios."
  },
  "matriz_controle_informacao": {
    "itens": [
      {
        "titulo": "A Ordem da Carga",
        "a_verdade": "A carga não é de suprimentos essenciais, mas sim um protótipo de arma que a gangue Ferro-Velho deveria ter sob controle.",
        "a_expectativa": "A carga é composta por peças cruciais para a sobrevivência do assentamento, roubadas por bandidos comuns.",
        "a_camuflagem": "A embalagem da carga é genérica e pode conter qualquer tipo de material industrial. Os lacres da Ferro-Velho foram rasgados. O contato que contratou os jogadores usa termos vagos como 'componentes vitais'.",
        "o_gatilho": "Encontrar a carga escondida ou interceptar uma comunicação sobre o 'protótipo' ou o número de série da arma.",
        "a_revelacao": "Ao inspecionar a carga, os jogadores descobrem que ela contém um canhão de energia instável ou um dispositivo de dispersão de gás tóxico, claramente não sendo 'peças de manutenção'.",
        "id": 1
      },
      {
        "titulo": "Os Verdadeiros Compradores",
        "a_verdade": "Os 'Sombras Aéreas' são os compradores da arma, mas foram enganados quanto à sua natureza e potência.",
        "a_expectativa": "Os Sombras Aéreas são os compradores da carga roubada, planejando usá-la para iniciar a guerra contra a Ferro-Velho.",
        "a_camuflagem": "A negociação conhecida é com os Corvos Mecânicos. Os Sombras Aéreas são mencionados com medo como compradores 'agressivos' ou 'desesperados'. Em seu esconderijo (se visitado), pode haver planos de infraestrutura, sugerindo um uso defensivo ou de controle, não de destruição em massa.",
        "o_gatilho": "Interceptar uma comunicação direta entre os Corvos Mecânicos e os Sombras Aéreas, ou interrogar um membro dos Corvos Mecânicos que conheça o comprador.",
        "a_revelacao": "A comunicação revela que os Sombras Aéreas foram informados que estavam comprando tecnologia para 'restaurar a ordem' ou 'proteger o assentamento', e não para um ataque devastador. Eles estão tão surpresos quanto os outros com o poder da arma e podem expressar hesitação em usá-la, ou um pedido de ajuda para entender o que compraram.",
        "id": 2
      },
      {
        "titulo": "O Traficante Original",
        "a_verdade": "Os Corvos Mecânicos não roubaram a carga para si, mas sim a roubaram de sua guardiã original (a Ferro-Velho) para vendê-la a terceiros.",
        "a_expectativa": "Os Corvos Mecânicos são a gangue que roubou a carga e está tentando vendê-la para iniciar uma guerra.",
        "a_camuflagem": "Os Corvos Mecânicos são abordados como os ladrões e vendedores. Suas motivações parecem ser puramente ganância ou poder. A Ferro-Velho age como vítima inicial. A verdade só aparece se os jogadores investigarem mais a fundo a origem da carga.",
        "o_gatilho": "Encontrar a base dos Corvos Mecânicos e evidências de que eles não estavam 'em posse' da carga, mas que a 'adquiriram' de outra fonte, possivelmente após um confronto anterior com a própria Ferro-Velho.",
        "a_revelacao": "Eles descobrem logística e rotas de aquisição que indicam que a carga era originalmente da Ferro-Velho, que foi quem deu a posse aos Corvos Mecânicos ou que um esquema de \"roubo e revenda\" interno foi orquestrado pela própria Ferro-Velho e deu errado.",
        "id": 3
      }
    ],
    "justificativa": "Estes três pontos de intriga visam minar as suposições iniciais dos jogadores sobre a natureza da carga, os compradores e os ladrões. Eles adicionam camadas de traição, manipulação e perigo que são cruciais para o tom Noir e a gestão de mistérios, levando a uma revelação mais complexa do que um simples conflito de gangues."
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
* **Argumento:** Em "O Fim da Linha", um assentamento Dieselpunk isolado e decadente, a carga roubada não é um simples carregamento, mas sim um protótipo de arma experimental desenvolvido por uma das gangues rivais, a "Ferro-Velho". Roubada pelo grupo mercenário "Corvos Mecânicos", a carga foi vendida a uma terceira facção, os "Sombras Aéreas", que planejam usá-la para subjugar o assentamento e iniciar a guerra declarada pelo título. Os jogadores são contratados pela gangue "Ferro-Velho" para recuperar o protótipo antes que o sol nasça, para evitar retaliação e manter o tênue equilíbrio de poder no "Fim da Linha". A motivação oculta da "Ferro-Velho" é, na verdade, que eles próprios planejavam vender o protótipo, mas foram traídos pelos Corvos Mecânicos. Os Sombras Aéreas, por sua vez, foram manipulados a comprar algo que pensavam ser diferente, e a guerra iminente é a consequência desse engodo.
* **Premissa Evidente (Missão):** Um carregamento valioso de componentes para as máquinas que mantêm "O Fim da Linha" funcionando foi roubado. Se não for recuperado antes do amanhecer, a gangue "Ferro-Velho" não conseguirá manter suas defesas, levando a um ataque das gangues rivais e a uma guerra total no assentamento.
* **Premissa Oculta (Twist):** O carregamento roubado é, na verdade, um protótipo de arma experimental perigosa. Foi roubado pelos mercenários "Corvos Mecânicos" dos presumidos donos originais ("Ferro-Velho"), e não é um mero acessório para manter as máquinas. Os "Sombras Aéreas" compraram essa arma sem saber de sua verdadeira natureza ou potencial destrutivo, e sua ativação pelo amanhecer deflagrará a guerra, não a manutenção do assentamento. A "Ferro-Velho" quer o protótipo de volta não só para evitar a guerra, mas também para recuperar seu investimento e manter seu segredo de que eles mesmos planejavam vendê-lo para terceiros.

### 3. Segredos da Campanha (Matriz)
Use estes segredos para garantir que os locais contenham pistas ou conexões temáticas com a verdade maior:
  - Titulo: A Ordem da Carga
  - A verdade: A carga não é de suprimentos essenciais, mas sim um protótipo de arma que a gangue Ferro-Velho deveria ter sob controle.
  - A expectativa: A carga é composta por peças cruciais para a sobrevivência do assentamento, roubadas por bandidos comuns.
  - A camuflagem: A embalagem da carga é genérica e pode conter qualquer tipo de material industrial. Os lacres da Ferro-Velho foram rasgados. O contato que contratou os jogadores usa termos vagos como 'componentes vitais'.
  - O gatilho: Encontrar a carga escondida ou interceptar uma comunicação sobre o 'protótipo' ou o número de série da arma.
  - A revelacao: Ao inspecionar a carga, os jogadores descobrem que ela contém um canhão de energia instável ou um dispositivo de dispersão de gás tóxico, claramente não sendo 'peças de manutenção'.
  - Id: 1

  - Titulo: Os Verdadeiros Compradores
  - A verdade: Os 'Sombras Aéreas' são os compradores da arma, mas foram enganados quanto à sua natureza e potência.
  - A expectativa: Os Sombras Aéreas são os compradores da carga roubada, planejando usá-la para iniciar a guerra contra a Ferro-Velho.
  - A camuflagem: A negociação conhecida é com os Corvos Mecânicos. Os Sombras Aéreas são mencionados com medo como compradores 'agressivos' ou 'desesperados'. Em seu esconderijo (se visitado), pode haver planos de infraestrutura, sugerindo um uso defensivo ou de controle, não de destruição em massa.
  - O gatilho: Interceptar uma comunicação direta entre os Corvos Mecânicos e os Sombras Aéreas, ou interrogar um membro dos Corvos Mecânicos que conheça o comprador.
  - A revelacao: A comunicação revela que os Sombras Aéreas foram informados que estavam comprando tecnologia para 'restaurar a ordem' ou 'proteger o assentamento', e não para um ataque devastador. Eles estão tão surpresos quanto os outros com o poder da arma e podem expressar hesitação em usá-la, ou um pedido de ajuda para entender o que compraram.
  - Id: 2

  - Titulo: O Traficante Original
  - A verdade: Os Corvos Mecânicos não roubaram a carga para si, mas sim a roubaram de sua guardiã original (a Ferro-Velho) para vendê-la a terceiros.
  - A expectativa: Os Corvos Mecânicos são a gangue que roubou a carga e está tentando vendê-la para iniciar uma guerra.
  - A camuflagem: Os Corvos Mecânicos são abordados como os ladrões e vendedores. Suas motivações parecem ser puramente ganância ou poder. A Ferro-Velho age como vítima inicial. A verdade só aparece se os jogadores investigarem mais a fundo a origem da carga.
  - O gatilho: Encontrar a base dos Corvos Mecânicos e evidências de que eles não estavam 'em posse' da carga, mas que a 'adquiriram' de outra fonte, possivelmente após um confronto anterior com a própria Ferro-Velho.
  - A revelacao: Eles descobrem logística e rotas de aquisição que indicam que a carga era originalmente da Ferro-Velho, que foi quem deu a posse aos Corvos Mecânicos ou que um esquema de "roubo e revenda" interno foi orquestrado pela própria Ferro-Velho e deu errado.
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
    "meta_estrutura_resumo": "1. O Chamado (Contratados pela Ferro-Velho) -> 2. A Jornada (Investigando os Corvos Mecânicos e Sombras Aéreas) -> 3. Chegada e Frustração (Percebendo a natureza da carga e a manipulação) -> 4. Provações Finais (Confronto para recuperar a arma) -> 5. O Objetivo (Recuperar a arma e lidar com as consequências).",
    "foco_narrativo": "Dieselpunk Noir de Sobrevivência: Uma corrida contra o tempo na penumbra de um assentamento decrépito, onde a confiança é uma moeda rara e cada sombra pode esconder um traidor ou uma ameaça igualmente letal. A tensão é palpável, com o cheiro de óleo queimado e a promessa de violência no ar."
  },
  "lista_locais": [
    {
      "nome": "O Muelle dos Corvos",
      "descricao": "Um emaranhado retorcido de metal enferrujado e plataformas precárias sobre um canal escuro. O ar está impregnado com o cheiro pungente de óleo de motor e peixe podre. O barulho incessante de engrenagens rangendo e o eco de vozes agudas vindas dos escritórios improvisados criam uma cacofonia constante. A poeira metálica e a ferrugem cobrem tudo com um manto áspero e oleoso.",
      "tags": "Ferro velho, Base de mercenários, Sujo, Perigoso",
      "funcao": "Inicial",
      "ancora_geografica": "Localizado nos confins externos do 'Fim da Linha', onde os restos de hangares aéreos naufragados formam a base dos Corvos Mecânicos. O acesso é feito por túneis de serviço abandonados que serpenteiam sob as docas principais, com a opção de escalada perigosa pelas estruturas metálicas enferrujadas."
    },
    {
      "nome": "O Barracão da Ração",
      "descricao": "Uma fila serpenteante se estende por um corredor estreito com paredes de metal amassado e sujo. O cheiro de ração sintética e suor humano paira no ar pesado e abafado. O som de passos arrastados e murmúrios impacientes compõem a trilha sonora, pontuado pelo som metálico ocasional de um dispensador de comida sendo forçado. A iluminação fraca e intermitente de lâmpadas desgastadas revela rostos cansados e desconfiados.",
      "tags": "Fila da ração, Pobreza, Sobrevivência, Social",
      "funcao": "Intermediario",
      "ancora_geografica": "Situado no coração do assentamento, este barracão é um nó vital de transporte. As passagens que levam a ele desembocam diretamente dos túneis de saneamento do Mercado de Pulgas, e sua saída oposta se abre para becos estreitos que levam às oficinas de carros."
    },
    {
      "nome": "O Mercado das Engrenagens",
      "descricao": "Um labirinto caótico de barracas improvisadas cobertas por lonas esfarrapadas, empilhadas em volta de uma clareira central poeirenta. O ar pulsa com uma mistura de odores – especiarias exóticas, metal aquecido, fumaça de solda e o cheiro acre de combustível derramado. O barulho é ensurdecedor: gritos de vendedores, marteladas em metal, o ronco de motores de teste e o tilintar incessante de moedas.",
      "tags": "Mercado de pulgas, Comércio, Caos, Social",
      "funcao": "Intermediario",
      "ancora_geografica": "O centro nervoso do 'Fim da Linha'. O Mercado está conectado a quase todas as áreas por vielas claustrofóbicas e túneis de manutenção. A Torre de Vigia domina o céu acima dele, e seus esgotos levam diretamente para o Muelle dos Corvos e para os níveis inferiores da Oficina de Carros."
    },
    {
      "nome": "O Refeitório dos 'Sombras'",
      "descricao": "Um salão cavernoso, outrora um armazém, agora decorado com símbolos arcaicos pintados a spray nas paredes de metal empoeiradas. O cheiro de especiarias fortes e bebida barata paira no ar rarefeito. Sons de conversas abafadas e o tinir de copos criam uma atmosfera tensa e vigilante. A iluminação é escassa, projetando longas sombras dançantes.",
      "tags": "Bar movimentado, Esconderijo, Facção, Reserva",
      "funcao": "Intermediario",
      "ancora_geografica": "Abaixo da Mansão dos Ferro-Velho, acessível por um elevador de carga oculto no Mercado das Engrenagens. As passagens de ventilação deste salão conectam-se discretamente às redes de esgoto que circundam a Torre de Vigia, permitindo acessos furtivos."
    },
    {
      "nome": "A Arena da Sucata",
      "descricao": "Um anfiteatro improvisado feito de sucata automotiva empilhada e carcaças de máquinas antigas. O ar está espesso com o cheiro de óleo queimado, suor e a eletricidade estática de ferimentos recentes. O rugido da multidão, gritos de dor e o som estrondoso de metal contra metal são ensurdecedores. Uma fina camada de poeira de metal cobre o chão e as arquibancadas improvisadas.",
      "tags": "Arena de Lutas, Brutal, Violento, Espetáculo",
      "funcao": "Intermediario",
      "ancora_geografica": "Aninhada nas profundezas do Ferro Velho. A Arena é acessada por túneis subterrâneos que se ramificam a partir dos escombros mais densos, emergindo diretamente no centro da pista de combate. Vias de serviço enferrujadas e precárias levam a plataformas de observação elevadas."
    },
    {
      "nome": "O Depósito Zehn",
      "descricao": "Um labirinto de prateleiras altas e metálicas cheias de caixas industriais genéricas, imaculadamente organizadas e etiquetadas, um contraste gritante com o resto do assentamento. O ar está filtrado, com um leve cheiro de ozônio e plástico novo. O silêncio aqui é quase opressor, quebrado apenas pelo zumbido baixo de sistemas de ventilação e pelo clique ocasional de um scanner.",
      "tags": "Armazém, Segurança, Contenção, Secreto",
      "funcao": "Climax",
      "ancora_geografica": "Escondido sob a Mansão dos Ferro-Velho, com acesso principal por um elevador de carga secreto que parte do Mercado das Engrenagens. As paredes do depósito se conectam em profundidade com os túneis de serviço esquecidos que levam aos níveis inferiores da Torre de Vigia."
    },
    {
      "nome": "Torre de Vigia da Aurora",
      "descricao": "Uma estrutura imponente de metal e concreto reforçado, perfurando o céu noturno. O ar aqui no topo é frio e rarefeito, com um cheiro metálico persistente de emissões de máquinas e poeira transportada pelo vento. O silêncio é quebrado apenas pelo uivo do vento e pelo zumbido constante de poderosos focos de luz e sistemas de comunicação. As vistas panorâmicas sobre o assentamento são espetaculares, mas opressoras.",
      "tags": "Torre de Vigia, Controle, Posicionamento estratégico, Vantagem",
      "funcao": "Climax",
      "ancora_geografica": "Dominando o horizonte, esta torre é o ponto mais alto do 'Fim da Linha'. Seu acesso primário é através de um elevador blindado no centro do assentamento. Escadas de serviço enferrujadas e túneis de acesso subsecretos conectam-se aos esgotos coletivos e à estrutura da Mansão dos Ferro-Velho."
    },
    {
      "nome": "O Laboratório da Fraude",
      "descricao": "Um espaço claustrofóbico e improvisado, repleto de mesas de trabalho cobertas por ferramentas, fios soltos e aparelhos de teste rudimentares. O ar é pesado com o cheiro acre de produtos químicos voláteis, óleo de motor exposto e metal aquecido. O som constante de faíscas, o zumbido de geradores instáveis e o borbulhar de líquidos em tubos de ensaio criam um ambiente de perigo iminente.",
      "tags": "Laboratório de química, Perigo, Oficina improvisada, Investigação",
      "funcao": "Climax",
      "ancora_geografica": "Escondido nas entranhas do Ferro Velho, acessível por uma entrada disfarçada dentro de um dos túneis de descarte de resíduos da Arena da Sucata. O laboratório está conectado, por meio de dutos de ventilação estreitos e esquecidos, aos níveis inferiores da Torre de Vigia."
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
* **Foco Narrativo:** Dieselpunk Noir de Sobrevivência: Uma corrida contra o tempo na penumbra de um assentamento decrépito, onde a confiança é uma moeda rara e cada sombra pode esconder um traidor ou uma ameaça igualmente letal. A tensão é palpável, com o cheiro de óleo queimado e a promessa de violência no ar.

### 2. Dados dos Locais (Step 1)
>>> DADOS DOS LOCAIS:
> **O Muelle dos Corvos**
  - Descricao: Um emaranhado retorcido de metal enferrujado e plataformas precárias sobre um canal escuro. O ar está impregnado com o cheiro pungente de óleo de motor e peixe podre. O barulho incessante de engrenagens rangendo e o eco de vozes agudas vindas dos escritórios improvisados criam uma cacofonia constante. A poeira metálica e a ferrugem cobrem tudo com um manto áspero e oleoso.
  - Tags: Ferro velho, Base de mercenários, Sujo, Perigoso
  - Funcao: Inicial
  - Ancora geografica: Localizado nos confins externos do 'Fim da Linha', onde os restos de hangares aéreos naufragados formam a base dos Corvos Mecânicos. O acesso é feito por túneis de serviço abandonados que serpenteiam sob as docas principais, com a opção de escalada perigosa pelas estruturas metálicas enferrujadas.

> **O Barracão da Ração**
  - Descricao: Uma fila serpenteante se estende por um corredor estreito com paredes de metal amassado e sujo. O cheiro de ração sintética e suor humano paira no ar pesado e abafado. O som de passos arrastados e murmúrios impacientes compõem a trilha sonora, pontuado pelo som metálico ocasional de um dispensador de comida sendo forçado. A iluminação fraca e intermitente de lâmpadas desgastadas revela rostos cansados e desconfiados.
  - Tags: Fila da ração, Pobreza, Sobrevivência, Social
  - Funcao: Intermediario
  - Ancora geografica: Situado no coração do assentamento, este barracão é um nó vital de transporte. As passagens que levam a ele desembocam diretamente dos túneis de saneamento do Mercado de Pulgas, e sua saída oposta se abre para becos estreitos que levam às oficinas de carros.

> **O Mercado das Engrenagens**
  - Descricao: Um labirinto caótico de barracas improvisadas cobertas por lonas esfarrapadas, empilhadas em volta de uma clareira central poeirenta. O ar pulsa com uma mistura de odores – especiarias exóticas, metal aquecido, fumaça de solda e o cheiro acre de combustível derramado. O barulho é ensurdecedor: gritos de vendedores, marteladas em metal, o ronco de motores de teste e o tilintar incessante de moedas.
  - Tags: Mercado de pulgas, Comércio, Caos, Social
  - Funcao: Intermediario
  - Ancora geografica: O centro nervoso do 'Fim da Linha'. O Mercado está conectado a quase todas as áreas por vielas claustrofóbicas e túneis de manutenção. A Torre de Vigia domina o céu acima dele, e seus esgotos levam diretamente para o Muelle dos Corvos e para os níveis inferiores da Oficina de Carros.

> **O Refeitório dos 'Sombras'**
  - Descricao: Um salão cavernoso, outrora um armazém, agora decorado com símbolos arcaicos pintados a spray nas paredes de metal empoeiradas. O cheiro de especiarias fortes e bebida barata paira no ar rarefeito. Sons de conversas abafadas e o tinir de copos criam uma atmosfera tensa e vigilante. A iluminação é escassa, projetando longas sombras dançantes.
  - Tags: Bar movimentado, Esconderijo, Facção, Reserva
  - Funcao: Intermediario
  - Ancora geografica: Abaixo da Mansão dos Ferro-Velho, acessível por um elevador de carga oculto no Mercado das Engrenagens. As passagens de ventilação deste salão conectam-se discretamente às redes de esgoto que circundam a Torre de Vigia, permitindo acessos furtivos.

> **A Arena da Sucata**
  - Descricao: Um anfiteatro improvisado feito de sucata automotiva empilhada e carcaças de máquinas antigas. O ar está espesso com o cheiro de óleo queimado, suor e a eletricidade estática de ferimentos recentes. O rugido da multidão, gritos de dor e o som estrondoso de metal contra metal são ensurdecedores. Uma fina camada de poeira de metal cobre o chão e as arquibancadas improvisadas.
  - Tags: Arena de Lutas, Brutal, Violento, Espetáculo
  - Funcao: Intermediario
  - Ancora geografica: Aninhada nas profundezas do Ferro Velho. A Arena é acessada por túneis subterrâneos que se ramificam a partir dos escombros mais densos, emergindo diretamente no centro da pista de combate. Vias de serviço enferrujadas e precárias levam a plataformas de observação elevadas.

> **O Depósito Zehn**
  - Descricao: Um labirinto de prateleiras altas e metálicas cheias de caixas industriais genéricas, imaculadamente organizadas e etiquetadas, um contraste gritante com o resto do assentamento. O ar está filtrado, com um leve cheiro de ozônio e plástico novo. O silêncio aqui é quase opressor, quebrado apenas pelo zumbido baixo de sistemas de ventilação e pelo clique ocasional de um scanner.
  - Tags: Armazém, Segurança, Contenção, Secreto
  - Funcao: Climax
  - Ancora geografica: Escondido sob a Mansão dos Ferro-Velho, com acesso principal por um elevador de carga secreto que parte do Mercado das Engrenagens. As paredes do depósito se conectam em profundidade com os túneis de serviço esquecidos que levam aos níveis inferiores da Torre de Vigia.

> **Torre de Vigia da Aurora**
  - Descricao: Uma estrutura imponente de metal e concreto reforçado, perfurando o céu noturno. O ar aqui no topo é frio e rarefeito, com um cheiro metálico persistente de emissões de máquinas e poeira transportada pelo vento. O silêncio é quebrado apenas pelo uivo do vento e pelo zumbido constante de poderosos focos de luz e sistemas de comunicação. As vistas panorâmicas sobre o assentamento são espetaculares, mas opressoras.
  - Tags: Torre de Vigia, Controle, Posicionamento estratégico, Vantagem
  - Funcao: Climax
  - Ancora geografica: Dominando o horizonte, esta torre é o ponto mais alto do 'Fim da Linha'. Seu acesso primário é através de um elevador blindado no centro do assentamento. Escadas de serviço enferrujadas e túneis de acesso subsecretos conectam-se aos esgotos coletivos e à estrutura da Mansão dos Ferro-Velho.

> **O Laboratório da Fraude**
  - Descricao: Um espaço claustrofóbico e improvisado, repleto de mesas de trabalho cobertas por ferramentas, fios soltos e aparelhos de teste rudimentares. O ar é pesado com o cheiro acre de produtos químicos voláteis, óleo de motor exposto e metal aquecido. O som constante de faíscas, o zumbido de geradores instáveis e o borbulhar de líquidos em tubos de ensaio criam um ambiente de perigo iminente.
  - Tags: Laboratório de química, Perigo, Oficina improvisada, Investigação
  - Funcao: Climax
  - Ancora geografica: Escondido nas entranhas do Ferro Velho, acessível por uma entrada disfarçada dentro de um dos túneis de descarte de resíduos da Arena da Sucata. O laboratório está conectado, por meio de dutos de ventilação estreitos e esquecidos, aos níveis inferiores da Torre de Vigia.

### 3. Contexto da Trama
* **Argumento:** Em "O Fim da Linha", um assentamento Dieselpunk isolado e decadente, a carga roubada não é um simples carregamento, mas sim um protótipo de arma experimental desenvolvido por uma das gangues rivais, a "Ferro-Velho". Roubada pelo grupo mercenário "Corvos Mecânicos", a carga foi vendida a uma terceira facção, os "Sombras Aéreas", que planejam usá-la para subjugar o assentamento e iniciar a guerra declarada pelo título. Os jogadores são contratados pela gangue "Ferro-Velho" para recuperar o protótipo antes que o sol nasça, para evitar retaliação e manter o tênue equilíbrio de poder no "Fim da Linha". A motivação oculta da "Ferro-Velho" é, na verdade, que eles próprios planejavam vender o protótipo, mas foram traídos pelos Corvos Mecânicos. Os Sombras Aéreas, por sua vez, foram manipulados a comprar algo que pensavam ser diferente, e a guerra iminente é a consequência desse engodo.
* **Premissa Evidente:** Um carregamento valioso de componentes para as máquinas que mantêm "O Fim da Linha" funcionando foi roubado. Se não for recuperado antes do amanhecer, a gangue "Ferro-Velho" não conseguirá manter suas defesas, levando a um ataque das gangues rivais e a uma guerra total no assentamento.
* **Premissa Oculta:** O carregamento roubado é, na verdade, um protótipo de arma experimental perigosa. Foi roubado pelos mercenários "Corvos Mecânicos" dos presumidos donos originais ("Ferro-Velho"), e não é um mero acessório para manter as máquinas. Os "Sombras Aéreas" compraram essa arma sem saber de sua verdadeira natureza ou potencial destrutivo, e sua ativação pelo amanhecer deflagrará a guerra, não a manutenção do assentamento. A "Ferro-Velho" quer o protótipo de volta não só para evitar a guerra, mas também para recuperar seu investimento e manter seu segredo de que eles mesmos planejavam vendê-lo para terceiros.

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
  "descricao_frente": "Em 'O Fim da Linha', um assentamento Dieselpunk noir isolado e decrépito, uma carga roubada — um protótipo de arma experimental — precipita uma corrida contra o tempo antes do amanhecer. As gangues rivais se preparam para a guerra, enquanto a verdade por trás do objeto roubado e as motivações ocultas de cada facção se desdobram em meio à poeira, óleo e desconfiança.",
  "elenco": [
    {
      "nome": "Vex, Mestre dos Corvos Mecânicos",
      "papel_funcao": "Líder Mercenário",
      "detalhe_marcante": "Usa um monóculo com uma lente fumê que reflete o ambiente como vidro quebrado.",
      "conviccao": "A sobrevivência através da astúcia. O lucro é a única lei e ele é seu maior adorador.",
      "contraste": "Tem um carinho especial por pássaros metálicos que ele mesmo construiu, murmurando-lhes segredos que ninguém mais ouve."
    },
    {
      "nome": "Silas 'O Gato' Ferro-Velho",
      "papel_funcao": "Capo da Ferro-Velho",
      "detalhe_marcante": "Sempre carrega uma chave inglesa antiga e polida, que ele usa para gesticular mais do que para consertar.",
      "conviccao": "A ordem é mantida pelo controle. O protótipo é a ferramenta perfeita para impor a paz pela força, sob seu comando.",
      "contraste": "Um exímio cozinheiro de guisados exóticos, que ele insiste em compartilhar com estranhos antes de traí-los."
    },
    {
      "nome": "Lyra, a Oradora das Sombras",
      "papel_funcao": "Líder dos Sombras Aéreas",
      "detalhe_marcante": "Sua voz tem uma ressonância metálica, como se viesse de um alto-falante defeituoso.",
      "conviccao": "A libertação virá através da purificação. A guerra é um mal necessário para forjar um novo começo.",
      "contraste": "Costuma citar poesia antiga e esquecida durante momentos de extrema violência."
    }
  ],
  "perigos": [
    {
      "nome": "A Rede de Contrabando dos Corvos Mecânicos",
      "tipo": "Organização",
      "impulso": "Expandir através da influência e pactos.",
      "ameaca_verdade": "Eles provam que a lealdade é uma fraqueza, vendendo qualquer um por um preço melhor. A confiança é uma moeda morta.",
      "local_vinculado": "O Muelle dos Corvos",
      "rastro_destruicao": "As docas agora são um campo de caça, com armadilhas improvisadas e guardas armados à espreita nas sombras metálicas. Barcos abandonados servem de esconderijos.",
      "acao_iminente": "Ajustar as rotas de fuga e emboscadas em torno daqueles que buscam o protótipo, priorizando a segurança de Vex e seus lacaios mais leais."
    },
    {
      "nome": "A Fome e a Desconfiança no Barracão",
      "tipo": "Social",
      "impulso": "Aumentar o descontentamento e a agitação.",
      "ameaca_verdade": "Eles demonstram que a própria sobrevivência exige atos desesperados e desleais. Cada pessoa é uma potencial ameaça ou um recurso a ser explorado.",
      "local_vinculado": "O Barracão da Ração",
      "rastro_destruicao": "As filas se tornaram mais longas e violentas, com pequenos furtos e brigas constantes pela escassez de ração. A atmosfera é pesada de fome e ressentimento.",
      "acao_iminente": "Explorar a tensão crescente para incitar motins ou criar diversões que desviem a atenção dos jogadores para a crise da ração."
    },
    {
      "nome": "O Protótipo 'Aurora'",
      "tipo": "Inimigo Arcano",
      "impulso": "Buscar poder destrutivo a qualquer custo.",
      "ameaca_verdade": "A promessa de poder absoluto corrompe. O protótipo, se ativado, mostra que a tecnologia pode facilmente se tornar uma arma de aniquilação contra qualquer um, inclusive os heróis.",
      "local_vinculado": "O Depósito Zehn",
      "rastro_destruicao": "A área ao redor do Depósito Zehn emana uma estranha energia residual, com pequenos curtos-circuitos e mal funcionamento em eletrônicos próximos. As prateleiras do depósito começaram a tremer.",
      "acao_iminente": "Começar a emitir pulsos de energia instáveis que podem sobrecarregar sistemas próximos, ou se ativar parcialmente, causando danos colaterais severos para quem estiver por perto."
    }
  ],
  "desastre_iminente": {
    "tipo_desastre": "Destruição",
    "descricao": "Se os jogadores falharem, o protótipo 'Aurora' será ativado antes do amanhecer. Sua detonação ou uso descontrolado causará uma explosão massiva que obliterará o coração do assentamento 'O Fim da Linha', resultando em destruição total, morte generalizada e o início de uma guerra caótica pela sobrevivência nos escombros fumegantes."
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
* **Argumento:** Em "O Fim da Linha", um assentamento Dieselpunk isolado e decadente, a carga roubada não é um simples carregamento, mas sim um protótipo de arma experimental desenvolvido por uma das gangues rivais, a "Ferro-Velho". Roubada pelo grupo mercenário "Corvos Mecânicos", a carga foi vendida a uma terceira facção, os "Sombras Aéreas", que planejam usá-la para subjugar o assentamento e iniciar a guerra declarada pelo título. Os jogadores são contratados pela gangue "Ferro-Velho" para recuperar o protótipo antes que o sol nasça, para evitar retaliação e manter o tênue equilíbrio de poder no "Fim da Linha". A motivação oculta da "Ferro-Velho" é, na verdade, que eles próprios planejavam vender o protótipo, mas foram traídos pelos Corvos Mecânicos. Os Sombras Aéreas, por sua vez, foram manipulados a comprar algo que pensavam ser diferente, e a guerra iminente é a consequência desse engodo.
* **Premissa Evidente:** Um carregamento valioso de componentes para as máquinas que mantêm "O Fim da Linha" funcionando foi roubado. Se não for recuperado antes do amanhecer, a gangue "Ferro-Velho" não conseguirá manter suas defesas, levando a um ataque das gangues rivais e a uma guerra total no assentamento.
* **Premissa Oculta:** O carregamento roubado é, na verdade, um protótipo de arma experimental perigosa. Foi roubado pelos mercenários "Corvos Mecânicos" dos presumidos donos originais ("Ferro-Velho"), e não é um mero acessório para manter as máquinas. Os "Sombras Aéreas" compraram essa arma sem saber de sua verdadeira natureza ou potencial destrutivo, e sua ativação pelo amanhecer deflagrará a guerra, não a manutenção do assentamento. A "Ferro-Velho" quer o protótipo de volta não só para evitar a guerra, mas também para recuperar seu investimento e manter seu segredo de que eles mesmos planejavam vendê-lo para terceiros.
* **Arquétipos Permitidos:** Músculo: Você é grande, pesado. Machucar e fazer façanhas físicas é com você., Cabeça: Pensamento ágil, consegue operar sistemas e máquinas antigas., Volante: Atrás de um volante, não há igual. Você é uma fera das estradas., Vigia: Olhos atentos e sempre no horizonte. Consegue atirar muito bem., Boca: Sempre sabe o que dizer. Carisma em pessoa. Mesmo que isso traga problemas., Novato: Nunca conheceu um mundo que não esse. Quer provar seu valor para os seus.

### 3. Dados da Fase 1 (Estrutura)
* **Arquétipo Selecionado:** A Busca
* **Foco Narrativo:** Dieselpunk Noir de Sobrevivência: Uma corrida contra o tempo na penumbra de um assentamento decrépito, onde a confiança é uma moeda rara e cada sombra pode esconder um traidor ou uma ameaça igualmente letal. A tensão é palpável, com o cheiro de óleo queimado e a promessa de violência no ar.

>>> LISTA DE LOCAIS (Referência para Localização dos Presságios):
> **O Muelle dos Corvos**
  - Descricao: Um emaranhado retorcido de metal enferrujado e plataformas precárias sobre um canal escuro. O ar está impregnado com o cheiro pungente de óleo de motor e peixe podre. O barulho incessante de engrenagens rangendo e o eco de vozes agudas vindas dos escritórios improvisados criam uma cacofonia constante. A poeira metálica e a ferrugem cobrem tudo com um manto áspero e oleoso.
  - Tags: Ferro velho, Base de mercenários, Sujo, Perigoso
  - Funcao: Inicial
  - Ancora geografica: Localizado nos confins externos do 'Fim da Linha', onde os restos de hangares aéreos naufragados formam a base dos Corvos Mecânicos. O acesso é feito por túneis de serviço abandonados que serpenteiam sob as docas principais, com a opção de escalada perigosa pelas estruturas metálicas enferrujadas.

> **O Barracão da Ração**
  - Descricao: Uma fila serpenteante se estende por um corredor estreito com paredes de metal amassado e sujo. O cheiro de ração sintética e suor humano paira no ar pesado e abafado. O som de passos arrastados e murmúrios impacientes compõem a trilha sonora, pontuado pelo som metálico ocasional de um dispensador de comida sendo forçado. A iluminação fraca e intermitente de lâmpadas desgastadas revela rostos cansados e desconfiados.
  - Tags: Fila da ração, Pobreza, Sobrevivência, Social
  - Funcao: Intermediario
  - Ancora geografica: Situado no coração do assentamento, este barracão é um nó vital de transporte. As passagens que levam a ele desembocam diretamente dos túneis de saneamento do Mercado de Pulgas, e sua saída oposta se abre para becos estreitos que levam às oficinas de carros.

> **O Mercado das Engrenagens**
  - Descricao: Um labirinto caótico de barracas improvisadas cobertas por lonas esfarrapadas, empilhadas em volta de uma clareira central poeirenta. O ar pulsa com uma mistura de odores – especiarias exóticas, metal aquecido, fumaça de solda e o cheiro acre de combustível derramado. O barulho é ensurdecedor: gritos de vendedores, marteladas em metal, o ronco de motores de teste e o tilintar incessante de moedas.
  - Tags: Mercado de pulgas, Comércio, Caos, Social
  - Funcao: Intermediario
  - Ancora geografica: O centro nervoso do 'Fim da Linha'. O Mercado está conectado a quase todas as áreas por vielas claustrofóbicas e túneis de manutenção. A Torre de Vigia domina o céu acima dele, e seus esgotos levam diretamente para o Muelle dos Corvos e para os níveis inferiores da Oficina de Carros.

> **O Refeitório dos 'Sombras'**
  - Descricao: Um salão cavernoso, outrora um armazém, agora decorado com símbolos arcaicos pintados a spray nas paredes de metal empoeiradas. O cheiro de especiarias fortes e bebida barata paira no ar rarefeito. Sons de conversas abafadas e o tinir de copos criam uma atmosfera tensa e vigilante. A iluminação é escassa, projetando longas sombras dançantes.
  - Tags: Bar movimentado, Esconderijo, Facção, Reserva
  - Funcao: Intermediario
  - Ancora geografica: Abaixo da Mansão dos Ferro-Velho, acessível por um elevador de carga oculto no Mercado das Engrenagens. As passagens de ventilação deste salão conectam-se discretamente às redes de esgoto que circundam a Torre de Vigia, permitindo acessos furtivos.

> **A Arena da Sucata**
  - Descricao: Um anfiteatro improvisado feito de sucata automotiva empilhada e carcaças de máquinas antigas. O ar está espesso com o cheiro de óleo queimado, suor e a eletricidade estática de ferimentos recentes. O rugido da multidão, gritos de dor e o som estrondoso de metal contra metal são ensurdecedores. Uma fina camada de poeira de metal cobre o chão e as arquibancadas improvisadas.
  - Tags: Arena de Lutas, Brutal, Violento, Espetáculo
  - Funcao: Intermediario
  - Ancora geografica: Aninhada nas profundezas do Ferro Velho. A Arena é acessada por túneis subterrâneos que se ramificam a partir dos escombros mais densos, emergindo diretamente no centro da pista de combate. Vias de serviço enferrujadas e precárias levam a plataformas de observação elevadas.

> **O Depósito Zehn**
  - Descricao: Um labirinto de prateleiras altas e metálicas cheias de caixas industriais genéricas, imaculadamente organizadas e etiquetadas, um contraste gritante com o resto do assentamento. O ar está filtrado, com um leve cheiro de ozônio e plástico novo. O silêncio aqui é quase opressor, quebrado apenas pelo zumbido baixo de sistemas de ventilação e pelo clique ocasional de um scanner.
  - Tags: Armazém, Segurança, Contenção, Secreto
  - Funcao: Climax
  - Ancora geografica: Escondido sob a Mansão dos Ferro-Velho, com acesso principal por um elevador de carga secreto que parte do Mercado das Engrenagens. As paredes do depósito se conectam em profundidade com os túneis de serviço esquecidos que levam aos níveis inferiores da Torre de Vigia.

> **Torre de Vigia da Aurora**
  - Descricao: Uma estrutura imponente de metal e concreto reforçado, perfurando o céu noturno. O ar aqui no topo é frio e rarefeito, com um cheiro metálico persistente de emissões de máquinas e poeira transportada pelo vento. O silêncio é quebrado apenas pelo uivo do vento e pelo zumbido constante de poderosos focos de luz e sistemas de comunicação. As vistas panorâmicas sobre o assentamento são espetaculares, mas opressoras.
  - Tags: Torre de Vigia, Controle, Posicionamento estratégico, Vantagem
  - Funcao: Climax
  - Ancora geografica: Dominando o horizonte, esta torre é o ponto mais alto do 'Fim da Linha'. Seu acesso primário é através de um elevador blindado no centro do assentamento. Escadas de serviço enferrujadas e túneis de acesso subsecretos conectam-se aos esgotos coletivos e à estrutura da Mansão dos Ferro-Velho.

> **O Laboratório da Fraude**
  - Descricao: Um espaço claustrofóbico e improvisado, repleto de mesas de trabalho cobertas por ferramentas, fios soltos e aparelhos de teste rudimentares. O ar é pesado com o cheiro acre de produtos químicos voláteis, óleo de motor exposto e metal aquecido. O som constante de faíscas, o zumbido de geradores instáveis e o borbulhar de líquidos em tubos de ensaio criam um ambiente de perigo iminente.
  - Tags: Laboratório de química, Perigo, Oficina improvisada, Investigação
  - Funcao: Climax
  - Ancora geografica: Escondido nas entranhas do Ferro Velho, acessível por uma entrada disfarçada dentro de um dos túneis de descarte de resíduos da Arena da Sucata. O laboratório está conectado, por meio de dutos de ventilação estreitos e esquecidos, aos níveis inferiores da Torre de Vigia.

### 4. Dados da Fase 2 (Ameaças e Elenco)
Use estes dados para definir QUEM causa os presságios.

>>> ELENCO PRINCIPAL:
> **Vex, Mestre dos Corvos Mecânicos**
  - Papel funcao: Líder Mercenário
  - Detalhe marcante: Usa um monóculo com uma lente fumê que reflete o ambiente como vidro quebrado.
  - Conviccao: A sobrevivência através da astúcia. O lucro é a única lei e ele é seu maior adorador.
  - Contraste: Tem um carinho especial por pássaros metálicos que ele mesmo construiu, murmurando-lhes segredos que ninguém mais ouve.

> **Silas 'O Gato' Ferro-Velho**
  - Papel funcao: Capo da Ferro-Velho
  - Detalhe marcante: Sempre carrega uma chave inglesa antiga e polida, que ele usa para gesticular mais do que para consertar.
  - Conviccao: A ordem é mantida pelo controle. O protótipo é a ferramenta perfeita para impor a paz pela força, sob seu comando.
  - Contraste: Um exímio cozinheiro de guisados exóticos, que ele insiste em compartilhar com estranhos antes de traí-los.

> **Lyra, a Oradora das Sombras**
  - Papel funcao: Líder dos Sombras Aéreas
  - Detalhe marcante: Sua voz tem uma ressonância metálica, como se viesse de um alto-falante defeituoso.
  - Conviccao: A libertação virá através da purificação. A guerra é um mal necessário para forjar um novo começo.
  - Contraste: Costuma citar poesia antiga e esquecida durante momentos de extrema violência.

>>> PERIGOS ATIVOS:
> **A Rede de Contrabando dos Corvos Mecânicos**
  - Tipo: Organização
  - Impulso: Expandir através da influência e pactos.
  - Ameaca verdade: Eles provam que a lealdade é uma fraqueza, vendendo qualquer um por um preço melhor. A confiança é uma moeda morta.
  - Local vinculado: O Muelle dos Corvos
  - Rastro destruicao: As docas agora são um campo de caça, com armadilhas improvisadas e guardas armados à espreita nas sombras metálicas. Barcos abandonados servem de esconderijos.
  - Acao iminente: Ajustar as rotas de fuga e emboscadas em torno daqueles que buscam o protótipo, priorizando a segurança de Vex e seus lacaios mais leais.

> **A Fome e a Desconfiança no Barracão**
  - Tipo: Social
  - Impulso: Aumentar o descontentamento e a agitação.
  - Ameaca verdade: Eles demonstram que a própria sobrevivência exige atos desesperados e desleais. Cada pessoa é uma potencial ameaça ou um recurso a ser explorado.
  - Local vinculado: O Barracão da Ração
  - Rastro destruicao: As filas se tornaram mais longas e violentas, com pequenos furtos e brigas constantes pela escassez de ração. A atmosfera é pesada de fome e ressentimento.
  - Acao iminente: Explorar a tensão crescente para incitar motins ou criar diversões que desviem a atenção dos jogadores para a crise da ração.

> **O Protótipo 'Aurora'**
  - Tipo: Inimigo Arcano
  - Impulso: Buscar poder destrutivo a qualquer custo.
  - Ameaca verdade: A promessa de poder absoluto corrompe. O protótipo, se ativado, mostra que a tecnologia pode facilmente se tornar uma arma de aniquilação contra qualquer um, inclusive os heróis.
  - Local vinculado: O Depósito Zehn
  - Rastro destruicao: A área ao redor do Depósito Zehn emana uma estranha energia residual, com pequenos curtos-circuitos e mal funcionamento em eletrônicos próximos. As prateleiras do depósito começaram a tremer.
  - Acao iminente: Começar a emitir pulsos de energia instáveis que podem sobrecarregar sistemas próximos, ou se ativar parcialmente, causando danos colaterais severos para quem estiver por perto.

* **Desastre Iminente (Game Over):** Destruição - Se os jogadores falharem, o protótipo 'Aurora' será ativado antes do amanhecer. Sua detonação ou uso descontrolado causará uma explosão massiva que obliterará o coração do assentamento 'O Fim da Linha', resultando em destruição total, morte generalizada e o início de uma guerra caótica pela sobrevivência nos escombros fumegantes.

### 5. Matriz de Controle de Informação
Conecte os presságios aos segredos abaixo (Camada de Informação).

>>> SEGREDOS DA CAMPANHA:
  - Titulo: A Ordem da Carga
  - A verdade: A carga não é de suprimentos essenciais, mas sim um protótipo de arma que a gangue Ferro-Velho deveria ter sob controle.
  - A expectativa: A carga é composta por peças cruciais para a sobrevivência do assentamento, roubadas por bandidos comuns.
  - A camuflagem: A embalagem da carga é genérica e pode conter qualquer tipo de material industrial. Os lacres da Ferro-Velho foram rasgados. O contato que contratou os jogadores usa termos vagos como 'componentes vitais'.
  - O gatilho: Encontrar a carga escondida ou interceptar uma comunicação sobre o 'protótipo' ou o número de série da arma.
  - A revelacao: Ao inspecionar a carga, os jogadores descobrem que ela contém um canhão de energia instável ou um dispositivo de dispersão de gás tóxico, claramente não sendo 'peças de manutenção'.
  - Id: 1

  - Titulo: Os Verdadeiros Compradores
  - A verdade: Os 'Sombras Aéreas' são os compradores da arma, mas foram enganados quanto à sua natureza e potência.
  - A expectativa: Os Sombras Aéreas são os compradores da carga roubada, planejando usá-la para iniciar a guerra contra a Ferro-Velho.
  - A camuflagem: A negociação conhecida é com os Corvos Mecânicos. Os Sombras Aéreas são mencionados com medo como compradores 'agressivos' ou 'desesperados'. Em seu esconderijo (se visitado), pode haver planos de infraestrutura, sugerindo um uso defensivo ou de controle, não de destruição em massa.
  - O gatilho: Interceptar uma comunicação direta entre os Corvos Mecânicos e os Sombras Aéreas, ou interrogar um membro dos Corvos Mecânicos que conheça o comprador.
  - A revelacao: A comunicação revela que os Sombras Aéreas foram informados que estavam comprando tecnologia para 'restaurar a ordem' ou 'proteger o assentamento', e não para um ataque devastador. Eles estão tão surpresos quanto os outros com o poder da arma e podem expressar hesitação em usá-la, ou um pedido de ajuda para entender o que compraram.
  - Id: 2

  - Titulo: O Traficante Original
  - A verdade: Os Corvos Mecânicos não roubaram a carga para si, mas sim a roubaram de sua guardiã original (a Ferro-Velho) para vendê-la a terceiros.
  - A expectativa: Os Corvos Mecânicos são a gangue que roubou a carga e está tentando vendê-la para iniciar uma guerra.
  - A camuflagem: Os Corvos Mecânicos são abordados como os ladrões e vendedores. Suas motivações parecem ser puramente ganância ou poder. A Ferro-Velho age como vítima inicial. A verdade só aparece se os jogadores investigarem mais a fundo a origem da carga.
  - O gatilho: Encontrar a base dos Corvos Mecânicos e evidências de que eles não estavam 'em posse' da carga, mas que a 'adquiriram' de outra fonte, possivelmente após um confronto anterior com a própria Ferro-Velho.
  - A revelacao: Eles descobrem logística e rotas de aquisição que indicam que a carga era originalmente da Ferro-Velho, que foi quem deu a posse aos Corvos Mecânicos ou que um esquema de "roubo e revenda" interno foi orquestrado pela própria Ferro-Velho e deu errado.
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
      "local_sugerido": "O Muelle dos Corvos",
      "o_pressagio": "A noite cai pesada sobre O Fim da Linha, e com ela o silêncio ansioso que precede a tempestade. O sol ainda não se pôs, mas as luzes de alerta já piscam fracamente. Um mensageiro desesperado, com a roupa rasgada e o rosto marcado pelo pânico, chega até os jogadores. Ele relata que o carregamento de 'componentes vitais' foi roubado, e que as defesas do assentamento entrarão em colapso ao amanhecer. A 'Ferro-Velho' oferece uma recompensa generosa para a recuperação imediata, antes que as gangues rivais aproveitem a fraqueza.",
      "argumento_arco_historia": "Silas 'O Gato' Ferro-Velho, sentindo a iminência de ser pego em sua própria cilada, contrata os jogadores na noite em que o protótipo 'Aurora' foi tecnicamente roubado pelos Corvos Mecânicos (a mando implicito da Ferro-Velho). Ele os envia para o Muelle dos Corvos, base dos mercenários, para recuperar o protótipo. O objetivo imediato é evitar que a Ferro-Velho sofra retaliação e mantenha seu segredo de venda.",
      "premissas_arco_historia": {
        "evidente": "Os jogadores são contratados por Silas 'O Gato' Ferro-Velho para recuperar um carregamento roubado que é vital para a manutenção das defesas do assentamento antes do amanhecer. A natureza do carregamento é descrita como 'componentes vitais', e a ameaça iminente é um ataque das gangues rivais.",
        "oculta": "O carregamento é na verdade o protótipo de arma 'Aurora', roubado pelos Corvos Mecânicos a pedido da própria Ferro-Velho, que planejava vendê-lo secretamente. Silas quer o protótipo de volta não só para evitar a retaliação, mas para esconder seu esquema de venda e evitar que outros descubram seu envolvimento."
      },
      "camada_informacao": {
        "id_matriz": 3,
        "conexao_explicada": "Este presságio estabelece a narrativa inicial onde a Ferro-Velho age como vítima. Ao se dirigirem ao Muelle dos Corvos, os jogadores podem encontrar evidências da logística de 'aquisição' da carga pelos Corvos Mecânicos, sugerindo que eles não a possuíam originalmente, e pistas sobre a origem da carga podendo ser a Ferro-Velho, preparando o terreno para a revelação do 'Traficante Original'."
      }
    },
    {
      "ordem": 2,
      "meta_estrutura": "A Jornada",
      "local_sugerido": "O Barracão da Ração",
      "o_pressagio": "Enquanto os jogadores se preparam para investigar o Muelle dos Corvos, uma comoção irrompe no Barracão da Ração. Uma multidão faminta e desesperada, sentindo a fragilidade do poder central com o roubo da carga (que acreditam ser de suprimentos), entra em conflito. Guardas da Ferro-Velho tentam manter a ordem com brutalidade, aumentando a tensão. A escassez de alimentos e a desconfiança generalizada tornam o assentamento um barril de pólvora, e a luta pela sobrevivência expõe a fragilidade social que o protótipo e a guerra iminente irão exacerbar.",
      "argumento_arco_historia": "A agitação no Barracão da Ração é uma consequência direta da atenção desviada para o roubo da 'carga vital'. A ausência de patrulhas eficazes e a percepção de fraqueza criam uma oportunidade para os famintos expressarem seu descontentamento. Os Corvos Mecânicos, percebendo a distração, utilizam o caos para movimentar o protótipo em segurança ou fortalecer suas posições, enquanto a Ferro-Velho, focada em recuperar o protótipo, ignora a crise social crescente.",
      "premissas_arco_historia": {
        "evidente": "Uma revolta pela escassez de ração ocorre no Barracão da Ração, ameaçando a estabilidade do assentamento. Os jogadores podem ser forçados a intervir ou lidar com as consequências dessa crise social que se agrava enquanto buscam o protótipo.",
        "oculta": "A revolta é exacerbada pela distração causada pelo roubo da carga, que a Ferro-Velho usou como desculpa para mobilizar seus guardas e recursos, enfraquecendo a segurança do Barracão. A verdade é que a fome e a desconfiança são ferramentas que os Corvos Mecânicos (ou Vex) podem explorar, demonstrando que a própria sobrevivência em O Fim da Linha exige atos desesperados e desleais."
      },
      "camada_informacao": {
        "id_matriz": 5,
        "conexao_explicada": "O foco na 'Fome e Desconfiança no Barracão' demonstra como a lei do mais forte prevalece em O Fim da Linha. Este presságio reforça a ideia de que a confiança é uma moeda morta e que a sobrevivência exige atos desesperados, alinhando-se com a Ameaça Verdadeira da Rede de Contrabando dos Corvos Mecânicos. Ao testemunhar ou participar dessa revolta, os jogadores ganham uma compreensão mais profunda do desespero que permeia O Fim da Linha e como eventos como o roubo do protótipo podem desencadear esses conflitos sociais."
      }
    },
    {
      "ordem": 3,
      "meta_estrutura": "Frustração (Barreira)",
      "local_sugerido": "O Refeitório dos 'Sombras'",
      "o_pressagio": "Ao rastrear os rumores e pistas sobre o destino da carga roubada, os jogadores chegam ao Refeitório dos 'Sombras'. Eles interceptam uma comunicação tensa entre Lyra, a Oradora das Sombras, e um contato dos Corvos Mecânicos. Lyra expressa descontentamento e surpresa com a natureza da 'tecnologia de restauração da ordem' que adquiriu, indicando que esperava algo para defender o assentamento, não um dispositivo de guerra. A voz dela ecoa com confusão e uma crescente suspeita, revelando que os Sombras Aéreas foram enganados sobre o que compraram.",
      "argumento_arco_historia": "Vex, Mestre dos Corvos Mecânicos, está negociando a venda do protótipo 'Aurora' com Lyra das Sombras Aéreas. No entanto, Vex subestimou a astúcia de Lyra e sua capacidade de questionar a natureza do 'produto'. A comunicação interceptada revela a desinformação plantada por Vex sobre o protótipo, levando Lyra a suspeitar. A Ferro-Velho (representada pelos jogadores) pode usar essa informação para expor o engano de Vex ou tentar negociar com os Sombras Aéreas.",
      "premissas_arco_historia": {
        "evidente": "Os jogadores interceptam uma comunicação entre Lyra, a líder dos Sombras Aéreas, e os Corvos Mecânicos. Lyra demonstra preocupação e confusão sobre a 'tecnologia de restauração da ordem' que adquiriu, sugerindo que foi enganada sobre seu uso e poder.",
        "oculta": "Os Sombras Aéreas foram manipulados pelos Corvos Mecânicos (e, por extensão, pela Ferro-Velho) a comprar o protótipo 'Aurora' sem saber de sua verdadeira natureza destrutiva. Lyra esperava uma arma defensiva ou de controle, não um dispositivo de guerra para iniciar uma aniquilação em massa, o que a coloca em uma posição moralmente dúbia e cheia de incertezas sobre como proceder."
      },
      "camada_informacao": {
        "id_matriz": 2,
        "conexao_explicada": "Este presságio revela diretamente a 'Verdade Maior' sobre 'Os Verdadeiros Compradores'. A comunicação interceptada com Lyra expõe explicitamente que os Sombras Aéreas foram enganados sobre a natureza destrutiva do protótipo. Isso desmente a expectativa de que eles eram compradores agressivos em busca de guerra e introduz a complicação de que foram manipulados, abrindo a possibilidade de que não sejam os verdadeiros vilões nesta parte da trama."
      }
    },
    {
      "ordem": 4,
      "meta_estrutura": "O Pesadelo",
      "local_sugerido": "O Depósito Zehn",
      "o_pressagio": "Os jogadores finalmente localizam o protótipo 'Aurora' no Depósito Zehn, o local de contenção secreto da Ferro-Velho. Ao se aproximarem, notam que a área emana uma energia estranha e instável. Pequenos curtos-circuitos e mau funcionamento de equipamentos eletrônicos tornam-se evidentes. As prateleiras do depósito começam a vibrar, e um zumbido crescente indica que o protótipo está começando a emitir pulsos de energia perigosos, prestes a se ativar de forma incontrolável e devastadora.",
      "argumento_arco_historia": "Após serem enganados e perceberem que a Ferro-Velho e os Corvos Mecânicos estão envolvidos em um esquema de venda que deu errado, os jogadores rastreiam o protótipo 'Aurora' até o Depósito Zehn, uma instalação de alta segurança da Ferro-Velho. Silas 'O Gato' Ferro-Velho, em desespero para recuperar seu investimento e manter a 'ordem', tenta ativar o protótipo prematuramente ou os lacaios de Silas (ou Vex) tentam desativá-lo de forma perigosa, desencadeando sua instabilidade. O objetivo é impedir a ativação ou conter a explosão iminente.",
      "premissas_arco_historia": {
        "evidente": "Os jogadores encontram o protótipo 'Aurora' no Depósito Zehn, mas ele está se tornando perigosamente instável, emitindo energia prejudicial e causando falhas eletrônicas. Parece que o próprio protótipo está prestes a explodir ou ativar-se de forma catastrófica.",
        "oculta": "A instabilidade do protótipo é resultado tanto de sua natureza inerentemente perigosa quanto das tentativas desesperadas de Silas (ou de Vex) de controlá-lo, manipulá-lo ou desativá-lo de forma imprudente. O protótipo não é apenas uma arma; é uma força destrutiva que a tecnologia, em sua busca por poder absoluto, pode se tornar contra todos."
      },
      "camada_informacao": {
        "id_matriz": 1,
        "conexao_explicada": "Este presságio foca no 'Protótipo Aurora' e seu perigo iminente, ligando-se diretamente à 'A Ordem da Carga'. Ao encontrar o protótipo instável, os jogadores descobrem que ele não é um simples componente, mas sim um canhão de energia destrutivo ou um dispositivo de dispersão tóxica, revelando a verdade sobre o conteúdo da carga e desmascarando a camuflagem genérica utilizada pela Ferro-Velho."
      }
    },
    {
      "ordem": 5,
      "meta_estrutura": "Fuga da Morte/Vitória",
      "local_sugerido": "Torre de Vigia da Aurora",
      "o_pressagio": "Com o protótipo 'Aurora' prestes a detonar ou ser ativado de forma irrefreável, os jogadores precisam correr contra o tempo. A Torre de Vigia da Aurora, com seus poderosos holofotes e sistemas de comunicação, é o local mais estratégico para tentar desviar, conter ou ao menos alertar o assentamento sobre o desastre iminente. Silas 'O Gato' Ferro-Velho e Vex, Mestres dos Corvos Mecânicos, podem ambos estar presentes na torre, usando-a como ponto de controle para seus planos distorcidos, transformando-a no palco final para impedir a aniquilação total ou a guerra caótica pela sobrevivência nos escombros.",
      "argumento_arco_historia": "O clímax ocorre na Torre de Vigia da Aurora, enquanto o protótipo 'Aurora' está prestes a ser ativado (ou detonar). Os jogadores devem confrontar Silas ou Vex (ou ambos, caso se tornem inimigos mútuos) que possivelmente usam a Torre de Vigia para coordenar os eventos finais ou tentar conter o protótipo de forma a seu favor. O objetivo é impedir a ativação total do protótipo, desviar sua energia, ou desmantelá-lo antes que o amanhecer traga a destruição total do assentamento.",
      "premissas_arco_historia": {
        "evidente": "A situação atingiu o ponto crítico. Os jogadores devem correr para a Torre de Vigia da Aurora para impedir a ativação final do protótipo 'Aurora', que trará destruição total. Eles podem encontrar Silas ou Vex controlando a torre para seus próprios fins nefastos ou tentando controlar o caos. A guerra iminente é uma certeza se falharem.",
        "oculta": "Tanto Silas quanto Vex podem estar na Torre de Vigia, não apenas como antagonistas, mas como peças em um jogo maior de engano. Silas pode tentar 'salvar' o protótipo para sua própria venda futura, enquanto Vex pode ter manipulado ambos os lados para chegar a esse ponto. A verdadeira luta é para impedir que a tecnologia de busca por poder, representada pelo protótipo, consuma O Fim da Linha em uma espiral de destruição mútua e caos."
      },
      "camada_informacao": {
        "id_matriz": 1,
        "conexao_explicada": "Este presságio representa o confronto final com a ameaça do 'Protótipo Aurora' e a revelação final de 'A Ordem da Carga'. A luta para impedir sua ativação total na Torre de Vigia da Aurora é o clímax da descoberta dos jogadores sobre a verdadeira natureza da carga roubada. O sucesso ou fracasso aqui determinará se a verdade sobre o protótipo se tornará aparente para todos ou se o assentamento será reduzido a escombros, cumprindo o Desastre Iminente."
      }
    }
  ],
  "perguntas_dramatica": [
    "Será que Silas 'O Gato' Ferro-Velho conseguirá manter o controle sobre O Fim da Linha através da força bruta e da manipulação, ou sua traição o consumirá?",
    "Em um mundo onde a confiança é uma moeda morta, os jogadores conseguirão forjar alianças inesperadas com os 'Sombras Aéreas' ou outros grupos marginalizados para sobreviver e talvez até mesmo curar as feridas de O Fim da Linha?",
    "Até onde os jogadores estarão dispostos a ir – quais princípios éticos ou morals estarão dispostos a sacrificar – para recuperar o protótipo 'Aurora' e sobreviver à noite mais longa de suas vidas em O Fim da Linha?"
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
* **Argumento Geral:** Em "O Fim da Linha", um assentamento Dieselpunk isolado e decadente, a carga roubada não é um simples carregamento, mas sim um protótipo de arma experimental desenvolvido por uma das gangues rivais, a "Ferro-Velho". Roubada pelo grupo mercenário "Corvos Mecânicos", a carga foi vendida a uma terceira facção, os "Sombras Aéreas", que planejam usá-la para subjugar o assentamento e iniciar a guerra declarada pelo título. Os jogadores são contratados pela gangue "Ferro-Velho" para recuperar o protótipo antes que o sol nasça, para evitar retaliação e manter o tênue equilíbrio de poder no "Fim da Linha". A motivação oculta da "Ferro-Velho" é, na verdade, que eles próprios planejavam vender o protótipo, mas foram traídos pelos Corvos Mecânicos. Os Sombras Aéreas, por sua vez, foram manipulados a comprar algo que pensavam ser diferente, e a guerra iminente é a consequência desse engodo.
* **Foco Narrativo:** Dieselpunk Noir de Sobrevivência: Uma corrida contra o tempo na penumbra de um assentamento decrépito, onde a confiança é uma moeda rara e cada sombra pode esconder um traidor ou uma ameaça igualmente letal. A tensão é palpável, com o cheiro de óleo queimado e a promessa de violência no ar.

### 2. Elementos Disponíveis
>>> ELENCO:
> **Vex, Mestre dos Corvos Mecânicos**
  - Papel funcao: Líder Mercenário
  - Detalhe marcante: Usa um monóculo com uma lente fumê que reflete o ambiente como vidro quebrado.
  - Conviccao: A sobrevivência através da astúcia. O lucro é a única lei e ele é seu maior adorador.
  - Contraste: Tem um carinho especial por pássaros metálicos que ele mesmo construiu, murmurando-lhes segredos que ninguém mais ouve.

> **Silas 'O Gato' Ferro-Velho**
  - Papel funcao: Capo da Ferro-Velho
  - Detalhe marcante: Sempre carrega uma chave inglesa antiga e polida, que ele usa para gesticular mais do que para consertar.
  - Conviccao: A ordem é mantida pelo controle. O protótipo é a ferramenta perfeita para impor a paz pela força, sob seu comando.
  - Contraste: Um exímio cozinheiro de guisados exóticos, que ele insiste em compartilhar com estranhos antes de traí-los.

> **Lyra, a Oradora das Sombras**
  - Papel funcao: Líder dos Sombras Aéreas
  - Detalhe marcante: Sua voz tem uma ressonância metálica, como se viesse de um alto-falante defeituoso.
  - Conviccao: A libertação virá através da purificação. A guerra é um mal necessário para forjar um novo começo.
  - Contraste: Costuma citar poesia antiga e esquecida durante momentos de extrema violência.

>>> PERIGOS:
> **A Rede de Contrabando dos Corvos Mecânicos**
  - Tipo: Organização
  - Impulso: Expandir através da influência e pactos.
  - Ameaca verdade: Eles provam que a lealdade é uma fraqueza, vendendo qualquer um por um preço melhor. A confiança é uma moeda morta.
  - Local vinculado: O Muelle dos Corvos
  - Rastro destruicao: As docas agora são um campo de caça, com armadilhas improvisadas e guardas armados à espreita nas sombras metálicas. Barcos abandonados servem de esconderijos.
  - Acao iminente: Ajustar as rotas de fuga e emboscadas em torno daqueles que buscam o protótipo, priorizando a segurança de Vex e seus lacaios mais leais.

> **A Fome e a Desconfiança no Barracão**
  - Tipo: Social
  - Impulso: Aumentar o descontentamento e a agitação.
  - Ameaca verdade: Eles demonstram que a própria sobrevivência exige atos desesperados e desleais. Cada pessoa é uma potencial ameaça ou um recurso a ser explorado.
  - Local vinculado: O Barracão da Ração
  - Rastro destruicao: As filas se tornaram mais longas e violentas, com pequenos furtos e brigas constantes pela escassez de ração. A atmosfera é pesada de fome e ressentimento.
  - Acao iminente: Explorar a tensão crescente para incitar motins ou criar diversões que desviem a atenção dos jogadores para a crise da ração.

> **O Protótipo 'Aurora'**
  - Tipo: Inimigo Arcano
  - Impulso: Buscar poder destrutivo a qualquer custo.
  - Ameaca verdade: A promessa de poder absoluto corrompe. O protótipo, se ativado, mostra que a tecnologia pode facilmente se tornar uma arma de aniquilação contra qualquer um, inclusive os heróis.
  - Local vinculado: O Depósito Zehn
  - Rastro destruicao: A área ao redor do Depósito Zehn emana uma estranha energia residual, com pequenos curtos-circuitos e mal funcionamento em eletrônicos próximos. As prateleiras do depósito começaram a tremer.
  - Acao iminente: Começar a emitir pulsos de energia instáveis que podem sobrecarregar sistemas próximos, ou se ativar parcialmente, causando danos colaterais severos para quem estiver por perto.

>>> LOCAIS:
> **O Muelle dos Corvos**
  - Descricao: Um emaranhado retorcido de metal enferrujado e plataformas precárias sobre um canal escuro. O ar está impregnado com o cheiro pungente de óleo de motor e peixe podre. O barulho incessante de engrenagens rangendo e o eco de vozes agudas vindas dos escritórios improvisados criam uma cacofonia constante. A poeira metálica e a ferrugem cobrem tudo com um manto áspero e oleoso.
  - Tags: Ferro velho, Base de mercenários, Sujo, Perigoso
  - Funcao: Inicial
  - Ancora geografica: Localizado nos confins externos do 'Fim da Linha', onde os restos de hangares aéreos naufragados formam a base dos Corvos Mecânicos. O acesso é feito por túneis de serviço abandonados que serpenteiam sob as docas principais, com a opção de escalada perigosa pelas estruturas metálicas enferrujadas.

> **O Barracão da Ração**
  - Descricao: Uma fila serpenteante se estende por um corredor estreito com paredes de metal amassado e sujo. O cheiro de ração sintética e suor humano paira no ar pesado e abafado. O som de passos arrastados e murmúrios impacientes compõem a trilha sonora, pontuado pelo som metálico ocasional de um dispensador de comida sendo forçado. A iluminação fraca e intermitente de lâmpadas desgastadas revela rostos cansados e desconfiados.
  - Tags: Fila da ração, Pobreza, Sobrevivência, Social
  - Funcao: Intermediario
  - Ancora geografica: Situado no coração do assentamento, este barracão é um nó vital de transporte. As passagens que levam a ele desembocam diretamente dos túneis de saneamento do Mercado de Pulgas, e sua saída oposta se abre para becos estreitos que levam às oficinas de carros.

> **O Mercado das Engrenagens**
  - Descricao: Um labirinto caótico de barracas improvisadas cobertas por lonas esfarrapadas, empilhadas em volta de uma clareira central poeirenta. O ar pulsa com uma mistura de odores – especiarias exóticas, metal aquecido, fumaça de solda e o cheiro acre de combustível derramado. O barulho é ensurdecedor: gritos de vendedores, marteladas em metal, o ronco de motores de teste e o tilintar incessante de moedas.
  - Tags: Mercado de pulgas, Comércio, Caos, Social
  - Funcao: Intermediario
  - Ancora geografica: O centro nervoso do 'Fim da Linha'. O Mercado está conectado a quase todas as áreas por vielas claustrofóbicas e túneis de manutenção. A Torre de Vigia domina o céu acima dele, e seus esgotos levam diretamente para o Muelle dos Corvos e para os níveis inferiores da Oficina de Carros.

> **O Refeitório dos 'Sombras'**
  - Descricao: Um salão cavernoso, outrora um armazém, agora decorado com símbolos arcaicos pintados a spray nas paredes de metal empoeiradas. O cheiro de especiarias fortes e bebida barata paira no ar rarefeito. Sons de conversas abafadas e o tinir de copos criam uma atmosfera tensa e vigilante. A iluminação é escassa, projetando longas sombras dançantes.
  - Tags: Bar movimentado, Esconderijo, Facção, Reserva
  - Funcao: Intermediario
  - Ancora geografica: Abaixo da Mansão dos Ferro-Velho, acessível por um elevador de carga oculto no Mercado das Engrenagens. As passagens de ventilação deste salão conectam-se discretamente às redes de esgoto que circundam a Torre de Vigia, permitindo acessos furtivos.

> **A Arena da Sucata**
  - Descricao: Um anfiteatro improvisado feito de sucata automotiva empilhada e carcaças de máquinas antigas. O ar está espesso com o cheiro de óleo queimado, suor e a eletricidade estática de ferimentos recentes. O rugido da multidão, gritos de dor e o som estrondoso de metal contra metal são ensurdecedores. Uma fina camada de poeira de metal cobre o chão e as arquibancadas improvisadas.
  - Tags: Arena de Lutas, Brutal, Violento, Espetáculo
  - Funcao: Intermediario
  - Ancora geografica: Aninhada nas profundezas do Ferro Velho. A Arena é acessada por túneis subterrâneos que se ramificam a partir dos escombros mais densos, emergindo diretamente no centro da pista de combate. Vias de serviço enferrujadas e precárias levam a plataformas de observação elevadas.

> **O Depósito Zehn**
  - Descricao: Um labirinto de prateleiras altas e metálicas cheias de caixas industriais genéricas, imaculadamente organizadas e etiquetadas, um contraste gritante com o resto do assentamento. O ar está filtrado, com um leve cheiro de ozônio e plástico novo. O silêncio aqui é quase opressor, quebrado apenas pelo zumbido baixo de sistemas de ventilação e pelo clique ocasional de um scanner.
  - Tags: Armazém, Segurança, Contenção, Secreto
  - Funcao: Climax
  - Ancora geografica: Escondido sob a Mansão dos Ferro-Velho, com acesso principal por um elevador de carga secreto que parte do Mercado das Engrenagens. As paredes do depósito se conectam em profundidade com os túneis de serviço esquecidos que levam aos níveis inferiores da Torre de Vigia.

> **Torre de Vigia da Aurora**
  - Descricao: Uma estrutura imponente de metal e concreto reforçado, perfurando o céu noturno. O ar aqui no topo é frio e rarefeito, com um cheiro metálico persistente de emissões de máquinas e poeira transportada pelo vento. O silêncio é quebrado apenas pelo uivo do vento e pelo zumbido constante de poderosos focos de luz e sistemas de comunicação. As vistas panorâmicas sobre o assentamento são espetaculares, mas opressoras.
  - Tags: Torre de Vigia, Controle, Posicionamento estratégico, Vantagem
  - Funcao: Climax
  - Ancora geografica: Dominando o horizonte, esta torre é o ponto mais alto do 'Fim da Linha'. Seu acesso primário é através de um elevador blindado no centro do assentamento. Escadas de serviço enferrujadas e túneis de acesso subsecretos conectam-se aos esgotos coletivos e à estrutura da Mansão dos Ferro-Velho.

> **O Laboratório da Fraude**
  - Descricao: Um espaço claustrofóbico e improvisado, repleto de mesas de trabalho cobertas por ferramentas, fios soltos e aparelhos de teste rudimentares. O ar é pesado com o cheiro acre de produtos químicos voláteis, óleo de motor exposto e metal aquecido. O som constante de faíscas, o zumbido de geradores instáveis e o borbulhar de líquidos em tubos de ensaio criam um ambiente de perigo iminente.
  - Tags: Laboratório de química, Perigo, Oficina improvisada, Investigação
  - Funcao: Climax
  - Ancora geografica: Escondido nas entranhas do Ferro Velho, acessível por uma entrada disfarçada dentro de um dos túneis de descarte de resíduos da Arena da Sucata. O laboratório está conectado, por meio de dutos de ventilação estreitos e esquecidos, aos níveis inferiores da Torre de Vigia.

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
    "titulo_arco": "A Sombra do Protótipo Aurora",
    "arquetipo_enredo": "A Busca",
    "curva_emocional": "Do Bem-estar à Queda (com elementos de Homem no Buraco)",
    "argumento_arco": "Os jogadores são contratados pela gangue 'Ferro-Velho' para recuperar um protótipo de arma roubado, o 'Aurora', antes do amanhecer. O que pensam ser uma simples tarefa de recuperação se revela uma teia de traições entre gangues: os 'Corvos Mecânicos' roubaram o protótipo da 'Ferro-Velho' para vendê-lo aos 'Sombras Aéreas', mas foram ludibriados sobre a verdadeira natureza e intenção de Vex e dos Corvos. Os Sombras Aéreas, acreditando ter adquirido uma arma de 'purificação', estão prestes a usá-la para iniciar uma guerra. Os jogadores precisarão navegar por essa rede de enganos, lidar com a fome crescente no assentamento e evitar que o protótipo caia em mãos erradas ou seja ativado, o que poderia destruir o 'Fim da Linha'.",
    "premissas_arco": {
      "evidente": "Recuperar um protótipo de arma roubado da gangue Ferro-Velho e devolvê-lo antes do amanhecer, silenciando uma ameaça iminente.",
      "oculta": "A venda do protótipo é uma trama de Vex para incriminar a Ferro-Velho e/ou desestabilizar o 'Fim da Linha', enquanto os Sombras Aéreas são peões em um jogo de poder maior, e o protótipo em si representa uma ameaça existencial para todos no assentamento."
    }
  },
  "lista_cenas": [
    {
      "numero": 1,
      "titulo": "A Oferta na Neblina",
      "fase_do_enredo": "O Chamado",
      "tipo_detalhamento": "Detalhado",
      "conteudo_cena": {
        "argumento_resumido": "Os jogadores são convocados, talvez por um intermediário desconfiado, para uma reunião secreta com Silas 'O Gato' Ferro-Velho no Muelle dos Corvos. Ele lhes oferece uma recompensa generosa para recuperar um 'item valioso' roubado seus pela gangue Corvos Mecânicos, antes que algo pior aconteça.",
        "objetivo_narrativo": "Apresentar a missão principal, o cliente (Silas e a Ferro-Velho), o primeiro alvo (Corvos Mecânicos) e o local inicial da ação, estabelecendo o tom noir e a urgência da trama contra o tempo (antes de amanhecer). Estabelecer um dos perigos sociais do assentamento: a desconfiança e a escassez de recursos que levam a negócios perigosos. Introduzir Silas como uma figura de poder ambíguo e a Ferro-Velho como fonte primária de contato, mas com motivações próprias já suspeitas devido ao argumento geral da campanha. Definir o prazo implícito (amanhecer). Comparar a oferta da recompensa com a precariedade dos moradores para demonstrar a disparidade de poder e recursos no local (ligação com A Fome e a Desconfiança no Barracão). Fornecer a Silas seu contraste culinário para subtilizar sua natureza traiçoeira, talvez oferecendo um guisado para os jogadores antes do pacto ou logo após, com um tempero que sugere manipulação. Explicar que Silas considera a posse do protótipo como seu direito e meio para impor ordem, em vez de uma arma para comércio, mostrando sua convicção. Mencionar que a gangue 'Corvos Mecânicos' roubou o 'item', ligando-o à Rede de Contrabando dos Corvos Mecânicos e ao local vinculado (O Muelle dos Corvos). A incerteza sobre o que exatamente foi roubado, e por que Silas está tão desesperado, pode ser outro ponto de tensão, ligando ao Protótipo 'Aurora'. Detalhar o ambiente do Muelle dos Corvos com focos na sujeira, óleo, barulho e a atmosfera perigosa, além de mencionar os barcos abandonados como possíveis esconderijos/locais de encontro, conforme a descrição da Rede de Contrabando dos Corvos Mecânicos. Mencionar as armadilhas improvisadas e guardas à espreita. A conversa com Silas pode incluir uma menção velada à necessidade de manter a paz e o equilíbrio no 'Fim da Linha', o que ele pretende fazer com o protótipo (seu desejo de controle), contudo, ele dirá que o protótipo é uma 'ferramenta de paz' para incutir os jogadores a pensarem que ele é o 'mal menor', o que é um ponto de conflito para os jogadores se eles tentarem entender as motivações. O monóculo de Vex pode ser descrito em um reflexo rápido se os jogadores tentarem espiar ou se uma reunião for interrompida, ou se Vex for mencionado como o líder dos Corvos. Silas, com sua chave inglesa, pode estar polindo-a obsessivamente enquanto fala, uma demonstração de nervosismo ou arrogância. O Protótipo 'Aurora' e seu efeito sobre eletrônicos pode ser sugerido por um breve mau funcionamento da iluminação ou equipamento de comunicação dos jogadores durante a reunião, ou pela descrição de que 'a noite está mais estranha do que o normal'. A luta iminente que os Corvos preparam com a Rede de Contrabando dos Corvos Mecânicos pode ser um presságio no discurso de Silas ao mencionar o perigo de confrontá-los em seu território, o Muelle dos Corvos. No final, Silas dará aos jogadores uma localização aproximada onde os 'Corvos Mecânicos' costumam fazer suas trocas ou esconderijos, como uma área do Muelle dos Corvos com barcos abandonados ou docas específicas, apontando para a próxima cena como um local de emboscada ou investigação, preparando o terreno para que os jogadores tomem uma iniciativa de busca ou infiltração dentro do Muelle dos Corvos, ou talvez para um local mais afastado e específico vinculado aos Corvos Mecânicos, como um armazém abandonado na periferia do Muelle dos Corvos onde supostamente o item foi levado. Mencionar que os Corvos estão ajustando rotas de fuga e emboscadas, e que ele pode ter uma desinformação sobre o paradeiro exato, mas que está localizado em seu território é crucial. A ameaça que os Corvos Mecânicos representam para a confiança e a lealdade será evidenciada pela maneira como Silas fala deles e pede aos jogadores que recuperem o item com discrição, implicando que os Corvos não hesitarão em vender a informação ou armar uma emboscada. O cheiro de óleo de motor e peixe podre do Muelle dos Corvos, a cacofonia de engrenagens, o eco de vozes agudas e a poeira metálica serão detalhados. Silas oferecerá um guisado exótico como um gesto de 'boa vontade' ou de 'boa sorte'. Ele pode mencionar que 'a noite está agitada', e que 'o item' é sensível, talvez insinuando sua natureza tecnológica ou perigosa. Silas pode revelar que os Corvos Mecânicos são conhecidos por usarem armadilhas improvisadas em seus territórios, como nas docas e barcos abandonados. A ambição de Silas de usar o protótipo para impor ordem, e não para vender, será dita com cuidado para não revelar completamente a verdade, mas para deixar os jogadores confusos sobre as intenções da Ferro-Velho. O Protótipo 'Aurora' pode ter um nome que Silas usa de forma genérica, como 'a carga' ou 'o artefato', mas sua descrição pode insinuar que ele é poderoso e instável. Silas pode ter uma preocupação específica com Vex, mencionando seu monóculo como um detalhe que o marca, aumentando a desconfiança dos jogadores sobre a situação real. A ação iminente dos Corvos Mecânicos de ajustar rotas de fuga e emboscadas pode ser uma pista para os jogadores sobre a dificuldade da missão. A fome e a desconfiança no Barracão da Ração podem ser mencionadas por Silas como algo que ele quer 'acabar', e o protótipo é a solução para a 'desordem' que a escassez causa. O Protótipo 'Aurora' pode ser o motivo pelo qual o chão do Depósito Zehn (o local de armazenamento original antes do roubo) pode estar inerte, apesar do protótipo não estar mais lá, com pequenos curtos-circuitos e mal funcionamento em eletrônicos próximos, sugerindo uma 'radiação' remanescente ou instabilidade. Silas pode mencionar que os Corvos 'não hesitarão em se livrar de quem atrapalhar', o que se alinha com a \"ameaça verdade\" deles: \"Eles provam que a lealdade é uma fraqueza, vendendo qualquer um por um preço melhor. A confiança é uma moeda morta.\". Ele pode também afirmar que o Protótipo é a chave para a paz, para ele, o que conecta diretamente com o seu contrato com a Ferro-Velho e sua convicção: \"A ordem é mantida pelo controle. O protótipo é a ferramenta perfeita para impor a paz pela força, sob seu comando.\". A ambiguidade é a chave aqui, deixando os jogadores desconfiados tanto da Ferro-Velho quanto dos Corvos Mecânicos. A Fome e a Desconfiança no Barracão da Ração são a contrapartida social que Silas quer resolver, e o protótipo sendo a arma definitiva para controlar a todos. O cheiro de óleo e peixe podre, a cacofonia de engrenagens, o eco de vozes agudas e a poeira metálica criam uma atmosfera rica para a primeira cena. Silas usa sua chave inglesa para gesticular e para ressaltar seus pontos, mas também pode oferecer um guisado exótico para os jogadores antes de partirem, como um gesto de boa sorte ou como forma de amolecê-los para o que vier. O protótipo, para Silas, não é apenas para vender, ele é a ferramenta de controle para impor a paz que o assentaento tanto carece. O Perigo da Rede de Contrabando dos Corvos Mecânicos é o obstáculo imediato, e Silas os descreve como caçadores traiçoeiros sempre à espreita nesse tipo de território para aqueles que buscam o protótipo, e que eles prioritizam a segurança de Vex, o líder deles, e seus lacaios mais leais. A ambientação do Muelle dos Corvos, com seus barcos abandonados, armadilhas improvisadas e guardas armados, será o palco para a primeira confrontação velada ou explícita. A desconfiança nos jogadores é implícita, pois uma gangue rival está contratando-os para roubar de outra gangue. A fome no Barracão da Ração é um pano de fundo constante para a luta pela sobrevivência, e Silas pode mencionar que a desordem que a fome causa é um problema que ele pretende resolver, mas que seu método será pelo controle, não pela distribuição igualitária. O Protótipo 'Aurora' pode ser descrito por Silas como algo que irá 'trazer ordem' e 'acabar com a anarquia', e que por isso é essencial recuperá-lo, insinuando um poder de contenção, mas com uma conotação de imposição que sugere mais do que apenas uma arma padrão. Ele pode mencionar, de forma dissimulada, que 'os Corvos não sabem o que têm em mãos' ou 'eles roubaram algo que não entendem', e isso é um presságio para a ameaça do Protótipo 'Aurora'. Liamus e sua poesia não têm função aqui, mas Vex e seu monóculo são cruciais para a identidade dos Corvos. Silas estará mais preocupado com o ganho da Ferro-Velho e o controle que o protótipo lhe trará do que com as consequências gerais. O cheiro de óleo, peixe podre e a cacofonia de engrenagens e vozes agudas criam uma atmosfera densa. A poeira metálica no ar e a ferrugem nas estruturas completam o cenário. A chave inglesa de Silas sempre em punho, ele a usa para esfregar nervosamente para enfatizar seus pontos. O café, caso seja servido, terá o gosto forte e amargo, como o próprio 'Fim da Linha'. O protótipo pode ser referido por Silas como um 'pacificador', o que é uma mentira óbvia para quem conhece o contexto. A Rede de Contrabando dos Corvos Mecânicos é o perigo imediato, com armadilhas improvisadas, guardas e um foco na segurança de Vex. As docas e os barcos abandonados são seus esconderijos. A segunda razão para Silas ter problemas é a 'Fome e a Desconfiança no Barracão', citando que o protótipo poderia acabar com a desordem, mas seu interesse é o controle, não a generosidade. O Protótipo 'Aurora' é a fonte do problema, a tecnologia que pode destruir tudo, e Silas a quer para 'restaurar a ordem'. Seus pulsos de energia instáveis podem ser um dos rumores que Silas ouviu ou deliberadamente mente. O toque de Vex com pássaros metálicos pode ser algo que Silas ironiza ou apenas menciona como um detalhe estranho do líder rival. O fato de Silas ter contratado os jogadores para recuperar um protótipo da Ferro-Velho, mas seu objetivo final ser a ordem através do controle, é um mistério que ele constrói. O motivo da Ferro-Velho por trás da contratação é que eles mesmos planejavam vender o protótipo (o ganho financeiro), mas foram traídos pelos Corvos Mecânicos. Os jogadores são, portanto, um meio para Silas recuperar um objeto que ele pretende usar para seus próprios fins (controle, não venda) e não para a Ferro-Velho como um todo. Silas o chama de 'protótipo' e não 'arma', uma sutileza para minimiazar a ameaça. Ele garante que a gangue dos Corvos Mecânicos usa armadilhas e que a segurança de Vex é primordial para eles. O cheiro pungente de óleo de motor e peixe podre, o emaranhado de metal enferrujado e o barulho incessante de engrenagens criam um cenário memorável. Silas, com suas frases curtas e o uso constante da chave inglesa, impõe um ar de autoridade, mas também de insegurança. A promessa de lucro, para os jogadores, vem em conflito com o risco, mas a descrição da Rede de Contrabando dos Corvos Mecânicos e suas ações iminentes servem como um aviso claro. A fome é a justificativa de Silas para o uso do protótipo para impor a ordem, o que ele chama de 'pacificação'. Ele dirá isso de forma convincente, mas a descrição do Perigo 'Protótipo Aurora' e suas ameaças de aniquilação contradiz essa narrativa. O fato de Silas descrever Vex com seu monóculo de vidro quebrado é um detalhe importante para os jogadores identificarem o líder dos Corvos se o virem. Silas menciona que o protótipo pode não estar seguro nos esconderijos dos Corvos Mecânicos, especificamente nos barcos abandonados, e que eles sabem que o item é valioso para qualquer um que busque o protótipo. E se ele for ativado, a aniquilação pode ser generalizada. Liamus e sua poesia não têm papel neste momento, mas Silas pode falar de sua própria 'ordem' de forma poética, mas brutal. O protótipo que Vex roubou é uma ameaça que pode sobrecarregar sistemas e causar danos colaterais severos. A oferta de Silas é clara: dinheiro em troca do protótipo. O Muelle dos Corvos é sujo, perigoso e cheio de ferro velho. A desconfiança é alta em torno desse local. O gatinho metálico de Vex, caso seja mencionado, será uma forma de estranheza no líder dos Corvos, algo que Silas pode achar patético ou sinistro. Silas pode ter um sorriso de escárnio ao falar dos Corvos, indicando uma rivalidade profunda e talvez um sentimento de superioridade. O Barracão da Ração é um lembrete constante da escassez no lugar, e Silas o usa para justificar a necessidade de 'ordem' através do protótipo. Ele dirá que 'o povo precisa de uma mão forte para sair da miséria', e o protótipo é essa mão. A ameaça do Protótipo 'Aurora' é a principal preocupação, uma arma que 'busca poder destrutivo a qualquer custo' e que pode ser a ruína para todos. Silas pode ter um olhar furtivo para fora, como se estivesse preocupado com o tempo, acentuando a urgência. Ele garante que os Corvos Mecânicos não são bonzinhos, e que a Rede de Contrabando deles os torna perigosos, especialmente se eles priorizam a segurança de Vex. A ação iminente deles de ajustar rotas de fuga e emboscadas prova que eles estão se preparando para uma reação. Silas pode oferecer um pedaço de seu guisado de 'segredo' para os jogadores, o que pode até ser bom, mas um lembrete de sua natureza traiçoeira. Ele sabe que os jogadores podem desconfiar dele, mas o dinheiro é um persuasor forte em 'O Fim da Linha'. A ameaça de A Fome e a Desconfiança no Barracão é um fantasma que assombra Silas e o motiva a recuperar o protótipo, vendo-o como a única forma de conter o caos. O Protótipo 'Aurora' não é um simples artefato, é uma arma de aniquilação que pode ser a ruína de todos, algo que Silas sabe, mas que minimiza para os jogadores. Ele pode mencionar que Vex tem um fraquinho por animais mecânicos, algo estranho que serve para humanizar (ou desumanizar) o líder inimigo. Silas não tem problema em mentir ou omitir a verdade para alcançar seus objetivos. Ele diz a verdade sobre a necessidade de recuperar o protótipo, mas não sobre as suas próprias intenções. O Muelle dos Corvos é deveras perigoso, cheio de armadilhas e guardas à espreita em barcos abandonados. O cheiro de óleo de motor e peixe podre paira no ar. Silas gesticula com sua chave inglesa polida enquanto fala, um objeto que ele usa mais para impressionar do que para consertar. Ele promete que a Ferro-Velho dará aos jogadores uma generosa recompensa por recuperar o Protótipo 'Aurora'. Silas pode sugerir que o protótipo não é apenas uma arma, mas algo capaz de 'restaurar a ordem', o que é a sua primeira mentira. A Fome e a Desconfiança no Barracão servem como pano de fundo para a motivação de Silas: ele quer o protótipo para impor essa ordem. Ele menciona que os Corvos Mecânicos são conhecidos por sua rede de contrabando, e que as docas são território deles, com armadilhas e guardas à espreita. O protótipo pode estar em um barco abandonado, um dos esconderijos de Vex. Silas garante que a Ferro-Velho é uma gangue a ser respeitada, e que se os jogadores tiverem sucesso, eles terão uma fatia do pastel no 'Fim da Linha'.  O Protótipo 'Aurora' é o cerne da trama, uma arma que pode ser usada para aniquilação. Silas pode sussurrar sobre a 'instabilidade' do protótipo, insinuando perigo, mas também o descreve como 'a chave para o controle absoluto'. A frase com a qual Silas encerra o trato: 'Venham com o protótipo AMANHÃ, e o Fim da Linha será nosso. Falhem, e a noite cairá sobre todos nós.' Ele pode oferecer um guisado para os jogadores, e o cheiro é exótico, talvez com ingredientes que eles não identificam, sugerindo sua culinária para traidores. A desconfiança no Barracão da Ração é um problema social que Silas diz querer resolver, mas através do controle imposto pelo protótipo. O Protótipo 'Aurora' é a solução utópica que Silas apresenta, uma arma de purificação e contenção. A Rede de Contrabando dos Corvos Mecânicos é um labirinto de perigos e armadilhas, especialmente se Vex estiver no controle. Silas é a figura central deste encontro, com sua chave inglesa polida e seu discurso calculista. Ele quer o protótipo para consolidar seu poder e 'trazer ordem' ao 'Fim da Linha'. O monóculo de Vex é mencionado como um detalhe distintivo do líder dos Corvos, talvez como um pedaço de vidro quebrado, reflexivo e perigoso. Silas pode ter um toque teatral em seu discurso, como um comediante macabro, prometendo segurança e prosperidade. A Fome no Barracão da Ração é um problema que os civis enfrentam, e Silas se apresenta como o salvador através do protótipo, mas seu interesse real é o controle. O cheiro de óleo de motor e peixe podre é avassalador. O Protótipo 'Aurora' é o objeto de desejo, uma arma que pode sobrecarregar sistemas e causar danos colaterais severos. Silas mente sobre o propósito do protótipo. O Muelle dos Corvos é um local de risco, com armadilhas e emboscadas, e os Corvos Mecânicos parecem ter antecipado a busca pelo protótipo. Silas oferece uma recompensa significativa, mas o risco é igualmente alto, especialmente considerando a natureza do Protótipo e as intenções ocultas dos envolvidos. Silas, com sua chave inglesa, está pronto para lidar com qualquer um que cruze seu caminho. A promessa de uma 'noite que mudará o Fim da Linha para sempre' é feita, insinuando a importância vital do protótipo. A Rede de Contrabando dos Corvos Mecânicos opera em rotas de fuga ajustadas e emboscadas, e a segurança de Vex é a prioridade. Silas quer o protótipo para a Ferro-Velho, mas suas intenções são apenas dele. A Fome e a Desconfiança no Barracão indicam a necessidade de ordem que Silas quer impor. O Protótipo 'Aurora' é um artefato de poder destrutivo que promete a aniquilação de qualquer um que o possua ou o enfrente. A conversa de Silas é emoldurada pela promessa de riqueza e pela ameaça velada de fracasso. O Muelle dos Corvos, sendo o local de ação principal para recuperar o protótipo, é descrito como sujo e perigoso, repleto de sucata e com a ameaça constante de emboscadas por parte dos Corvos Mecânicos. Um aspecto marcante de Silas é seu aparente prazer em cozinhar, oferecendo um guisado exótico. O protótipo é referido genericamente como 'carga' ou 'item'. Os Sombras Aéreas não são mencionados diretamente nesta cena, mas a urgência em recuperar o protótipo antes do nascer do sol sugere que outra facção pode estar interessada nele. Silas, com sua chave inglesa, é a personificação da ameaça e da promessa. A Fome e a Desconfiança no Barracão são o pano de fundo para as ambições de Silas de impor sua 'ordem'. A Rede de Contrabando dos Corvos Mecânicos é descrita como um campo de caça, com armadilhas e perigos em cada esquina. Silas garante que o protótipo não é tão simples quanto parece, insinuando seu poder e potencial destrutivo. A desconfiança é fomentada, pois Silas é ambiguo e motivado por algo além do simples lucro, o controle. A fome no barracão é um problema que ele quer resolver, mas com autoridade, não com compaixão. O protótipo é a ferramenta que ele usará para esse fim, e ele não hesitará em usar a violência para consegui-lo."
      }
    },
    {
      "numero": 2,
      "titulo": "Na Teia dos Corvos",
      "fase_do_enredo": "A Aventura",
      "tipo_detalhamento": "Detalhado",
      "conteudo_cena": {
        "argumento_resumido": "Os jogadores se infiltram no Muelle dos Corvos, buscando pistas sobre onde o protótipo 'Aurora' foi levado. Eles se deparam com a segurança improvisada dos Corvos Mecânicos, o ambiente perigoso das docas e a possibilidade de encontrar mercenários leais a Vex. Podem encontrar sinais da rede de contrabando, armadilhas, e possivelmente um contato que pode ajudar (ou trair) os jogadores.",
        "objetivo_narrativo": "Permitir que os jogadores explorem um dos principais domínios de uma facção rival e enfrentem suas defesas. Introduzir os perigos associados à Rede de Contrabando dos Corvos Mecânicos. Fornecer pistas sobre o paradeiro do protótipo ou sobre quem mais esteve envolvido na troca. Dar aos jogadores a oportunidade de usar habilidades de furtividade, combate ou investigação. Apresentar uma amostra da astúcia de Vex através de suas defesas e táticas. Subtilmente sugerir que o protótipo não é um item comum, talvez através de algum equipamento eletrônico danificado na área, quebrando um dispositivo ou uma comunicação captada que se refere à 'energia estranha' ou 'pulsos'. Detalhar o local do Muelle dos Corvos com a descrição focada no emaranhado retorcido de metal enferrujado, plataformas precárias, o cheiro pungente de óleo de motor e peixe podre, a cacofonia de engrenagens e vozes agudas, e a poeira metálica e ferrugem que cobrem tudo. Mencionar os barcos abandonados como esconderijos e os túneis de serviço como acessos, conforme a descrição da Rede de Contrabando. Evidenciar a ameaça verdadeira dos Corvos: \"Eles provam que a lealdade é uma fraqueza, vendendo qualquer um por um preço melhor. A confiança é uma moeda morta.\" Isso será demonstrado através de encontros com mercenários desconfiados ou que tentam vender informações. A ação iminente dos Corvos ('Ajustar as rotas de fuga e emboscadas') deve ser visível através de patrulhas mais frequentes, sinais de armadilhas novas ou guardas em posições defensivas elevadas (em hangares naufragados). A ideia de que Vex e seus lacaios mais leais são a prioridade pode ser vista na forte segurança em torno de certas áreas ou em patrulhas que parecem 'proteger' algo ou alguém internamente. O protótipo pode ser mencionado em conversas interceptadas entre mercenários como 'a carga de Vex' ou 'algo energizado' que está sendo movido, mas o destino exato é incerto, talvez para o Depósito Zehn ou para um ponto de encontro com os Sombras Aéreas no Refeitório dos 'Sombras' (embora eles não saibam que é para eles). Um detalhe curioso pode ser um pássaro metálico, um dos brinquedos de Vex, que está em guarda em um local incomum, talvez emitindo um som sutil ou observando as ações dos jogadores. Outro detalhe curioso seria um dispositivo de comunicação improvisado emitindo fragmentos de áudio em loop, talvez a voz de Vex falando sobre 'eficiência' ou a necessidade de 'esconder a carga dos curiosos'. A presença de equipamentos eletrônicos quebrados ou com mau funcionamento em áreas próximas a onde o protótipo poderia ter sido manuseado insinuaria sua 'ameaça verdade' como Inimigo Arcano. Um gancho para a próxima cena poderia ser a descoberta de um mapa rudimentar de um dos mercenários, indicando uma rota de fuga para o Mercado das Engrenagens, ou a menção de um encontro futuro entre os Corvos Mecânicos e os 'compradores' em uma área mais central do assentamento, como o Mercado das Engrenagens, onde podem estar negociando a entrega final ou onde o protótipo foi levado temporariamente. Pode haver um encontro com um mercenário fugitivo ou assustado que pode ser pressionado a fornecer informações em troca de proteção ou passagem segura, ligando à Rede de Contrabando dos Corvos Mecânicos. O ar pesado com óleo de motor e peixe podre, os sons de engrenagens rangeendo e vozes agudas, a poeira metálica e a ferrugem cobrindo tudo criarão a atmosfera. Os jogadores precisarão navegar por armadilhas, guardas ocultos e possivelmente confrontos táticos em meio à sucata e aos barcos abandonados. A lealdade dos mercenários é questionável, e eles podem estar mais dispostos a vender informações ou a atacar por um preço melhor. Podem encontrar um dos pássaros metálicos de Vex, um sentinela silencioso, ou um comunicador com a voz de Vex gravada, detalhando planos vagos. O Perigo da Rede de Contrabando dos Corvos Mecânicos é a ameaça central, refletida em patrulhas, armadilhas e um senso de vigilância constante. A 'ameaça verdade' deles de que lealdade é fraqueza será palpável, pois podem haver rivais dentro da própria gangue que os jogadores podem explorar, ou mercenários que podem ser subornados. A ação iminente de ajustar rotas de fuga e emboscadas será evidenciada pela movimentação suspeita e pela presença inesperada de guardas. A prioridade de Vex e seus lacaios pode ser percebida pela segurança reforçada em torno de escritórios improvisados ou áreas de armazenamento específicas. O Protótipo 'Aurora' pode ser insinuado pela descoberta de detritos metálicos com vestígios de energia incomum em uma área de confronto, ou por um dispositivo eletrônico de comunicação dos Corvos que apresenta falhas devido à proximidade do protótipo. A ligação com a Fome e a Desconfiança no Barracão da Ração pode ser feita se os jogadores encontrarem mercenários desiludidos que falam sobre a escassez e como isso os torna mais propensos a trair por uma refeição ou um bom pagamento, o que reforça que a confiança é uma moeda morta para os Corvos."
      }
    },
    {
      "numero": 3,
      "titulo": "O Mercado Negro e as Vendas",
      "fase_do_enredo": "A Prova",
      "tipo_detalhamento": "Esboco",
      "conteudo_cena": {
        "argumento_resumido": "Seguindo as pistas do Muelle dos Corvos, os jogadores chegam ao Mercado das Engrenagens para procurar informações sobre o destino do protótipo. Eles podem precisar interagir com vendedores, informantes duvidosos ou até mesmo testemunhar uma transação secreta ou uma disputa entre gangues menores, que pode envolver Vex ou seus contatos."
      }
    },
    {
      "numero": 4,
      "titulo": "O Refeitório e as Confissões",
      "fase_do_enredo": "A Frustração",
      "tipo_detalhamento": "Esboco",
      "conteudo_cena": {
        "argumento_resumido": "Investigando mais a fundo, os jogadores descobrem que o protótipo pode ter sido negociado com os 'Sombras Aéreas'. Eles se dirigem ao Refeitório dos 'Sombras' para tentar obter informações, possivelmente encontrando Lyra ou seus tenentes e ouvindo fragmentos de sua filosofia sobre libertação e purificação, o que pode levantar dúvidas sobre o uso que eles darão ao protótipo."
      }
    },
    {
      "numero": 5,
      "titulo": "A Corrupção da Arena",
      "fase_do_enredo": "A Frustração",
      "tipo_detalhamento": "Esboco",
      "conteudo_cena": {
        "argumento_resumido": "Em busca de um ponto de acesso ou de informação sobre os Sombras Aéreas ou sobre o protótipo, os jogadores podem se deparar com a Arena da Sucata, onde a violência e o desespero são espetáculo. Podem encontrar um mercenário ferido, um informante desesperado que tem informações sobre o protótipo ou sobre os Sombras Aéreas, talvez até um pequeno engajamento com capangas da arena que estão agindo de forma mais agressiva devido à instabilidade do protótipo próximo."
      }
    },
    {
      "numero": 6,
      "titulo": "O Confronto no Depósito",
      "fase_do_enredo": "O Clímax",
      "tipo_detalhamento": "Esboco",
      "conteudo_cena": {
        "argumento_resumido": "As pistas levam ao Depósito Zehn, onde o protótipo 'Aurora' está guardado ou sendo preparado para uso. Os jogadores enfrentam o perigo iminente do próprio protótipo, que pode começar a emitir pulsos de energia instáveis, causando danos colaterais e sobrecarregando sistemas próximos. Podem ter que lidar com guardas leais à Ferro-Velho (que não sabem do plano real de Silas) ou com os próprios Corvos Mecânicos que tentam recuperar o protótipo deles."
      }
    },
    {
      "numero": 7,
      "titulo": "A Torre de Vigia e a Guerra Iminente",
      "fase_do_enredo": "O Clímax",
      "tipo_detalhamento": "Esboco",
      "conteudo_cena": {
        "argumento_resumido": "Se os jogadores não conseguirem desativar ou conter o protótipo no Depósito Zehn, eles podem testemunhar os Sombras Aéreas, liderados por Lyra, tentando ativá-lo ou transportá-lo para a Torre de Vigia, de onde planejam iniciar a guerra com o assentamento. Os jogadores precisam impedir a ativação completa ou a projeção de sua energia destrutiva."
      }
    },
    {
      "numero": 8,
      "titulo": "O Laboratório da Fraude e o Desenlace",
      "fase_do_enredo": "A Resolução",
      "tipo_detalhamento": "Esboco",
      "conteudo_cena": {
        "argumento_resumido": "Os jogadores podem descobrir o que realmente é o protótipo e como ele foi modificado ou como caiu em mãos erradas ao investigar o que restou do plano original ou encontrar pistas em um laboratório improvisado (o Laboratório da Fraude). Dependendo de suas ações, eles podem desativar o protótipo, usá-lo contra uma das facções, ou expor a verdade sobre Silas, Vex e Lyra, impactando o futuro do 'Fim da Linha'."
      }
    }
  ]
}
```
