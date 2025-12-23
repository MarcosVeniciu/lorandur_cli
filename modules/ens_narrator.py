import json
from model_llm import llm_client
from utils.xml_parser import extract_all_tags

# --- INSTRUÇÃO DE SISTEMA (ENS V2.1) ---
SYSTEM_INSTRUCTION = """
VOCÊ É: O Narrador Literário (ENS - Engine de Narrativa Silenciosa).
SUA FUNÇÃO: Transformar resoluções táticas em prosa imersiva e atuar como Detetive de Incerteza.

### 1. HIERARQUIA DE COMANDO ###
- [SISTEMA_ANPA] é a verdade absoluta sobre o resultado da ação (Sucesso/Falha).
- Você decide o "Flavor" (Descrição), mas nunca muda a mecânica.

### 2. DIRETRIZES DE ESTILO (V2.1) ###
A. SHOW, DON'T TELL: Use sentidos (som, cheiro, luz) em vez de explicar sentimentos.
B. NPC VIVO: Se houver NPC, use a tag <npc>.
C. PRINCÍPIO DA PREGUIÇA: Não repita descrições de cenário se o jogador apenas falou algo trivial. Seja conciso.

### 3. O DETETIVE DE INCERTEZA (ORÁCULO) ###
Se o jogador fizer uma PERGUNTA sobre um fato NÃO definido no contexto (ex: "A porta está trancada?", "Tem alguém na janela?", "O baú tem armadilha?"):
- NÃO INVENTE A RESPOSTA.
- Pare a narração imediatamente e acione o Oráculo.
- Output: <sistema>{ "event_trigger": "ORACLE_CONSULT", "oracle_params": { "question": "A pergunta do jogador?" } }</sistema>

### 4. ESTRUTURA DE RESPOSTA (XML) ###
<pensamento>
1. Verificar se é uma pergunta de Oráculo.
2. Se não, ler o resultado do ANPA.
3. Planejar a descrição sensorial.
</pensamento>

<narrator>Prosa descritiva.</narrator>
<npc name="NOME">Fala do personagem.</npc>
<sistema>{ "event_trigger": "...", "oracle_params": ... }</sistema>
"""

class ENSNarrator:
    def __init__(self):
        pass

    def generate(self, player_input: str, game_state: dict, action_success: bool, history: list = []) -> dict:
        """
        Gera a narração final baseada no contexto e na decisão do ANPA.
        """
        # 1. Extração de Contexto
        scene = game_state.get('state', {}).get('current_scene_context', {})
        npc = scene.get('npc_active', {})
        
        # 2. Histórico Recente (Limitado para manter foco)
        recent_history = history[-3:] if history else ["Início da cena."]
        history_str = "\n".join(recent_history)
        
        # 3. Montagem do Prompt
        user_content = f"""
        ### CONTEXTO DA CENA ###
        [LOCAL]: {scene.get('location_name', 'Desconhecido')}
        [OBJETIVO]: {scene.get('scene_objective', 'Explorar')}
        [DETALHE OCULTO]: {scene.get('hidden_info', 'Nenhum')}
        
        ### NPC PRESENTE ###
        [NOME]: {npc.get('name', 'Ninguém')}
        [ARQUÉTIPO]: {npc.get('archetype', 'Genérico')}
        [DESCRIÇÃO]: {npc.get('description', 'Sem detalhes visuais.')}
        
        ### AÇÃO DO JOGADOR ###
        Input: "{player_input}"
        
        ### VERDADE TÁTICA (ANPA) ###
        O sistema de regras determinou: {'SUCESSO' if action_success else 'FALHA'}
        (Se houver detalhes específicos do ANPA no histórico abaixo, siga-os).
        
        ### HISTÓRICO RECENTE ###
        {history_str}
        """

        messages = [
            {"role": "system", "content": SYSTEM_INSTRUCTION},
            {"role": "user", "content": user_content}
        ]

        # Temperatura 0.85 para criatividade narrativa, mas instrução rígida para Oráculo
        response_text = llm_client.send_prompt(messages, temperature=0.85)
        
        # 4. Parsing e Tratamento de Erros
        tags = extract_all_tags(response_text)
        
        # Fallback se a IA esquecer XML
        if not tags and response_text and len(response_text.strip()) > 0:
            tags['narrator'] = response_text.strip()
            tags['sistema_dict'] = {}
            
        # Parse do JSON de sistema
        if 'sistema' in tags:
            try:
                # Limpa quebras de linha para evitar erro de JSON
                clean_json = tags['sistema'].replace('\n', ' ')
                tags['sistema_dict'] = json.loads(clean_json)
            except json.JSONDecodeError:
                tags['sistema_dict'] = {}
        else:
            tags['sistema_dict'] = {}
                
        return tags