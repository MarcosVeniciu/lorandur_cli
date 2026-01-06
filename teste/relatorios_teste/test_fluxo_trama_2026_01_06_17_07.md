# Relatório de Teste: Fluxo de Trama V5
**Data:** 2026_01_06_17_07

## 📊 Métricas de Execução
| Métrica | Valor |
| :--- | :--- |
| **Tempo Total** | 12.97s |
| **Tokens Entrada** | 841 |
| **Tokens Saída** | 3135 |
| **Tokens Total** | 3976 |
| **Custo Estimado** | $0.001338 |
| **Stop Reason** | stop |

**Módulo:** core_trama_generator

## 1. Contexto Enviado
### System Prompt
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

### User Prompt
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

## 2. Resposta Recebida (Output JSON)
```json
{
  "configuracao_aventura": {
    "genero_principal": "Dieselpunk",
    "subgeneros_selecionados": [
      "Noir",
      "Ação Frenética",
      "Thriller"
    ],
    "escopo_selecionado": "Nível 2 (Escopo Local - O Refúgio)",
    "justificativa_escopo": "A urgência de recuperar a carga antes do amanhecer e a ameaça iminente de uma guerra de gangues localizada tornam um cenário contido e denso o ideal. Este escopo permite uma investigação focada, interações intensas e confrontos imediatos dentro de um perímetro definido, aumentando a tensão sob o limite de tempo.",
    "justificativa_estilo": "A combinação de Dieselpunk com uma carga roubada, um prazo apertado e a consequência de uma guerra de gangues sugere uma narrativa sombria e cheia de suspense. O Noir se manifesta na investigação e na corrupção subjacente, a Ação Frenética nos confrontos e perseguições com a tecnologia da era, e o Thriller na pressão do tempo e na revelação de conspirações perigosas."
  },
  "argumento": {
    "texto": "Na metrópole industrial de Neo-Veridia, uma carga de 'combustível experimental de alta octanagem' (a verdade oculta é que se trata de um componente para uma arma sônica devastadora) foi roubada de um armazém seguro no Distrito Industrial. A cidade está sob a tensão da iminente guerra entre as gangues rivais dos 'Serpentes de Ferro' e as 'Abutres de Cromo', que se acusam mutuamente pelo roubo. Se a carga não for recuperada antes do amanhecer, a guerra irromperá, mergulhando a cidade em caos e permitindo que uma facção corrupta dentro da Guarda da Cidade (os verdadeiros ladrões) tome o controle, vendendo a arma para potências estrangeiras ou usando-a para consolidar seu próprio poder.",
    "justificativa": "O argumento estabelece o Quem (gangues rivais, Guarda da Cidade corrupta), Onde (Distrito Industrial de Neo-Veridia), Quando (antes do amanhecer), Por que (motivação de poder e lucro da facção corrupta, usando a guerra de gangues como cobertura) e Como (roubo orquestrado, manipulação das gangues para criar a crise)."
  },
  "premissas": {
    "evidente": {
      "texto": "Uma carga de combustível experimental crucial para a infraestrutura da cidade foi roubada. As gangues rivais 'Serpentes de Ferro' e 'Abutres de Cromo' estão à beira de um conflito aberto. Os jogadores são contratados para recuperar a carga antes do nascer do sol, evitando assim uma guerra civil que devastaria Neo-Veridia.",
      "funcao": "Estabelece a missão superficial e o senso de urgência, direcionando os jogadores para a investigação das gangues rivais como os principais suspeitos."
    },
    "oculta": {
      "texto": "O roubo foi um trabalho interno orquestrado por uma facção desonesta da Guarda da Cidade. O objetivo não é apenas roubar o 'combustível', mas sim um componente de arma sônica avançada, que eles planejam vender ou usar para impor sua própria ordem após o caos da guerra de gangues fabricada.",
      "funcao": "Revela a verdadeira natureza da conspiração, subvertendo a expectativa de que o conflito seja apenas entre gangues e expondo a corrupção nas instituições."
    },
    "justificativa": "A premissa evidente foca na ameaça imediata e nos suspeitos óbvios, enquanto a premissa oculta introduz o twist principal que muda a natureza da ameaça e os verdadeiros antagonistas."
  },
  "matriz_controle_informacao": {
    "itens": [
      {
        "titulo": "A Verdadeira Natureza da Carga",
        "a_verdade": "A carga roubada não é combustível, mas sim o protótipo de um amplificador de arma sônica, capaz de causar destruição em larga escala.",
        "a_expectativa": "É um combustível experimental de alta octanagem, valioso pela sua potência energética.",
        "a_camuflagem": "A embalagem é genérica e as etiquetas foram deliberadamente danificadas. Relatos iniciais (e boatos espalhados pelos conspiradores) a descrevem apenas como um 'combustível especial'.",
        "o_gatilho": "Análise forense dos resíduos encontrados no local do roubo, interceptação de comunicações sobre o destino da carga, ou interrogar um membro da gangue que tenha visto a carga.",
        "a_revelacao": "A carga é um componente de arma, e sua verdadeira finalidade é muito mais sinistra e perigosa do que se pensava inicialmente.",
        "id": 1
      },
      {
        "titulo": "O Ladrão Interior",
        "a_verdade": "O roubo foi um trabalho interno, orquestrado por uma facção da Guarda da Cidade que planeja usar a carga para seus próprios fins (venda ou controle).",
        "a_expectativa": "Uma das gangues rivais (Serpentes de Ferro ou Abutres de Cromo) é a responsável pelo roubo, agindo por conta própria.",
        "a_camuflagem": "Evidências plantadas que incriminam as gangues, membros da Guarda da Cidade agindo de forma suspeita ou deliberadamente enganando os investigadores, comunicações interceptadas entre gangues que são falsas ou manipuladas.",
        "o_gatilho": "Encontrar equipamento especializado (como ferramentas de arrombamento de alta tecnologia ou uniformes parciais) que não pertence a nenhuma das gangues conhecidas, rastrear a rota de fuga até uma instalação da Guarda da Cidade, ou um informante da Guarda da Cidade se arriscar a revelar a verdade.",
        "a_revelacao": "A Guarda da Cidade, ou uma parte dela, está envolvida diretamente no roubo e na manipulação da situação.",
        "id": 2
      },
      {
        "titulo": "A Guerra Fabricada",
        "a_verdade": "A escalada para a guerra entre as gangues é artificialmente provocada pelos conspiradores para criar o caos necessário para a execução de seu plano.",
        "a_expectativa": "As gangues estão genuinamente à beira da guerra devido à desconfiança mútua e à perda da carga.",
        "a_camuflagem": "Pequenos confrontos simulados entre gangues que parecem ser provocados pelas próprias gangues, 'vazamentos' de informações falsas que aumentam a tensão, ou sabotagens que parecem ser atos de retaliação gangues vs. gangues.",
        "o_gatilho": "Testemunhar uma provocação que parece 'pouco natural' ou coordenada demais, encontrar um agente terceiro (não pertencente a nenhuma gangue) incitando a violência, ou descobrir planos que visam especificamente aumentar a hostilidade entre os grupos.",
        "a_revelacao": "A guerra de gangues iminente é uma farsa orquestrada para servir a um propósito maior, e não um conflito orgânico.",
        "id": 3
      }
    ],
    "justificativa": "Esta matriz gerencia as principais quebras de expectativa: a natureza da carga, a identidade do verdadeiro culpado e a artificialidade da guerra de gangues. Cada item oferece uma pista para a verdade oculta, escondida sob uma suposição mais simples, com gatilhos claros para a revelação."
  }
}
```

### 3. Análise Rápida (Schema V3.0)
- **Escopo:** Nível 2 (Escopo Local - O Refúgio)
- **Subgêneros:** Noir, Ação Frenética, Thriller
- **Premissa Evidente:** Uma carga de combustível experimental crucial para a infraestrutura da cidade foi roubada. As gangues rivais 'Serpentes de Ferro' e 'Abutres de Cromo' estão à beira de um conflito aberto. Os jogadores são contratados para recuperar a carga antes do nascer do sol, evitando assim uma guerra civil que devastaria Neo-Veridia.
- **Premissa Oculta:** O roubo foi um trabalho interno orquestrado por uma facção desonesta da Guarda da Cidade. O objetivo não é apenas roubar o 'combustível', mas sim um componente de arma sônica avançada, que eles planejam vender ou usar para impor sua própria ordem após o caos da guerra de gangues fabricada.

#### Matriz de Informação (Item 1):
- **A Verdadeira Natureza da Carga:** É um combustível experimental de alta octanagem, valioso pela sua potência energética. -> *A carga roubada não é combustível, mas sim o protótipo de um amplificador de arma sônica, capaz de causar destruição em larga escala.*
