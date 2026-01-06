# Relatório de Teste: Módulo FRENTE_AVENTURA
**Data:** 24/12/2025 15:47:05
---

## Passo 1

Gerando Trama Real (Dependência)...

## Output Trama (Input para Frente)

```json
{
  "analysis": "A sabotagem do combustível é o ponto de partida, mas a busca por um refúgio é o objetivo imediato. A consequência de ficar sem combustível é a morte, criando uma urgência dramática. A camada oculta pode envolver um sabotador, uma conspiração para controlar o refúgio, ou uma força maior que causa a escassez de combustível. Os locais serão usados para progredir da mentira para a verdade.",
  "title": "A Longa Estrada para o Refúgio",
  "tags": [
    "Dieselpunk",
    "Mistério",
    "Sobrevivência"
  ],
  "scope": [
    "Fila da ração / Armazém de comida",
    "Oficina de carros / Laboratório de química",
    "Torre de Vigia / Pista de Obstáculos / Escombros"
  ],
  "evident_premise": "As reservas de combustível foram sabotadas, e o grupo precisa desesperadamente de combustível para alcançar o Refúgio. Eles devem ir ao armazém de comida para conseguir um pouco de combustível e, depois, consertar um veículo na oficina. A viagem é perigosa, e eles precisam se manter firmes durante o percurso.",
  "hidden_premise": "A sabotagem foi orquestrada por um grupo que controla o Refúgio, visando eliminar aqueles que podem ameaçar seu poder. Eles usam uma arma química experimental, testada no combustível, que causa uma morte lenta e dolorosa. Se os jogadores conseguirem chegar ao Refúgio, estarão infectados, selando seu destino.",
  "connection": "A análise do combustível na oficina revela traços da arma química. A descoberta de documentos escondidos no armazém e na torre de vigia revela a conspiração. A pista chave é a necessidade de combustível e a morte que ele causa."
}
```

### 🤖 Interação LLM: Geração Frente
**Prompt Enviado:**
- **SYSTEM:**
```text

VOCÊ É: Um Game Designer de RPG especialista em "Frentes de Aventura" (Dungeon World/Apocalypse World).
SUA TAREFA: Criar a mecânica de antagonismo baseada na Trama fornecida.

ESTRUTURA:
1. PERIGO (Danger): Use a 'Premissa Oculta' da trama para definir o verdadeiro vilão/ameaça.
2. DESGRAÇA (Doom): O "Bad Ending" se o vilão vencer.
3. PRESSÁGIOS SOMBRIOS (Grim Portents): 3 a 5 passos lógicos que levam ao Doom. 
   - O primeiro presságio deve estar ligado à 'Premissa Evidente' (o que já está acontecendo).
4. RELÓGIOS (Cabo de Guerra):
   - Ameaça (6 segmentos): O avanço do vilão.
   - Resolução (4 segmentos): O objetivo do herói para vencer.

```
- **USER:**
```text

        ### DADOS DO CENÁRIO ###
        [GÊNERO]: Dieselpunk: Estrada da Fúria

        ### TRAMA APROVADA ###
        
        [TÍTULO]: A Longa Estrada para o Refúgio
        [TAGS]: Dieselpunk, Mistério, Sobrevivência
        [ESCOPO]: Fila da ração / Armazém de comida, Oficina de carros / Laboratório de química, Torre de Vigia / Pista de Obstáculos / Escombros
        [PREMISSA EVIDENTE (O SINTOMA)]: As reservas de combustível foram sabotadas, e o grupo precisa desesperadamente de combustível para alcançar o Refúgio. Eles devem ir ao armazém de comida para conseguir um pouco de combustível e, depois, consertar um veículo na oficina. A viagem é perigosa, e eles precisam se manter firmes durante o percurso.
        [PREMISSA OCULTA (A DOENÇA/VILÃO)]: A sabotagem foi orquestrada por um grupo que controla o Refúgio, visando eliminar aqueles que podem ameaçar seu poder. Eles usam uma arma química experimental, testada no combustível, que causa uma morte lenta e dolorosa. Se os jogadores conseguirem chegar ao Refúgio, estarão infectados, selando seu destino.
        

        Construa a Frente de Aventura agora.
        
```
**Resposta Recebida:**
✅ **Sucesso** (4.20s | Tokens: In 511 / Out 498)
```json
{
  "danger": {
    "name": "Os Guardiões do Refúgio",
    "type": "Facção",
    "impulse": "Manter o poder e eliminar ameaças.",
    "description": "Um grupo que controla o Refúgio, usando a violência e o medo para manter sua posição. Eles envenenam o combustível para eliminar potenciais desafiantes."
  },
  "doom": "Os personagens chegam ao Refúgio, mas já estão infectados com a arma química. A morte lenta e dolorosa se espalha, e eles se tornam mais uma vítima do sistema corrupto que tentaram escapar.",
  "grim_portents": [
    {
      "index": 1,
      "description": "O combustível continua a falhar, os veículos quebram e a viagem se torna cada vez mais lenta.",
      "visible_sign": "Fumaça preta e cheiro estranho saindo dos veículos."
    },
    {
      "index": 2,
      "description": "Pessoas começam a apresentar sintomas estranhos: tosse, dores de cabeça, fadiga extrema.",
      "visible_sign": "Pessoas tossindo sangue e desmaiando repentinamente."
    },
    {
      "index": 3,
      "description": "O Refúgio envia batedores, oferecendo ajuda, mas na verdade estão monitorando e isolando os sobreviventes.",
      "visible_sign": "Veículos do Refúgio patrulham a estrada, oferecendo 'ajuda'."
    },
    {
      "index": 4,
      "description": "Os sintomas se agravam, a morte é iminente, e os personagens descobrem a traição.",
      "visible_sign": "Alucinações, órgãos falhando, e a verdade sobre o combustível envenenado é revelada."
    }
  ],
  "clocks": {
    "threat_clock_name": "A Propagação da Toxina",
    "threat_clock_max": 6,
    "resolution_clock_name": "A Busca pela Cura",
    "resolution_clock_max": 4
  }
}
```
---
## 🏁 Resultado Final do Módulo
```json
{
  "danger": {
    "name": "Os Guardiões do Refúgio",
    "type": "Facção",
    "impulse": "Manter o poder e eliminar ameaças.",
    "description": "Um grupo que controla o Refúgio, usando a violência e o medo para manter sua posição. Eles envenenam o combustível para eliminar potenciais desafiantes."
  },
  "doom": "Os personagens chegam ao Refúgio, mas já estão infectados com a arma química. A morte lenta e dolorosa se espalha, e eles se tornam mais uma vítima do sistema corrupto que tentaram escapar.",
  "grim_portents": [
    {
      "index": 1,
      "description": "O combustível continua a falhar, os veículos quebram e a viagem se torna cada vez mais lenta.",
      "visible_sign": "Fumaça preta e cheiro estranho saindo dos veículos."
    },
    {
      "index": 2,
      "description": "Pessoas começam a apresentar sintomas estranhos: tosse, dores de cabeça, fadiga extrema.",
      "visible_sign": "Pessoas tossindo sangue e desmaiando repentinamente."
    },
    {
      "index": 3,
      "description": "O Refúgio envia batedores, oferecendo ajuda, mas na verdade estão monitorando e isolando os sobreviventes.",
      "visible_sign": "Veículos do Refúgio patrulham a estrada, oferecendo 'ajuda'."
    },
    {
      "index": 4,
      "description": "Os sintomas se agravam, a morte é iminente, e os personagens descobrem a traição.",
      "visible_sign": "Alucinações, órgãos falhando, e a verdade sobre o combustível envenenado é revelada."
    }
  ],
  "clocks": {
    "threat_clock_name": "A Propagação da Toxina",
    "threat_clock_max": 6,
    "resolution_clock_name": "A Busca pela Cura",
    "resolution_clock_max": 4
  }
}
```
