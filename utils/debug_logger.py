import os
import json
import re
from datetime import datetime

class DebugLogger:
    def __init__(self, scenario_name: str):
        # Cria a pasta de logs se não existir
        self.log_dir = "Logger/game_logger"
        os.makedirs(self.log_dir, exist_ok=True)

        # Sanitização robusta do nome do arquivo
        # 1. Remove caracteres inválidos como : / \ ? * " < > |
        # 2. Substitui espaços por _
        clean_name = re.sub(r'[<>:"/\\|?*]', '', scenario_name)
        sanitized_name = clean_name.replace(" ", "_").lower()
        
        # Timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        self.filepath = f"{self.log_dir}/log_{sanitized_name}_{timestamp}.md"

        # Inicializa o arquivo com Cabeçalho
        self._write_header(scenario_name)

    def _write_header(self, scenario_name: str):
        with open(self.filepath, "w", encoding="utf-8") as f:
            f.write(f"# SESSÃO DE DEBUG: {scenario_name}\n")
            f.write(f"**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            f.write("---\n\n")

    def log_turn(self, turn_count: int, player_input: str, rule_verdict: dict, roll_result: dict, ens_output: dict):
        """
        Registra o ciclo completo de um turno.
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        with open(self.filepath, "a", encoding="utf-8") as f:
            # Cabeçalho do Turno
            f.write(f"## [{timestamp}] Turno {turn_count}\n")
            f.write(f"**Input do Jogador:** `{player_input}`\n\n")

            # 1. Análise de Regras (Arbiter)
            f.write("### 1. Verificador de Regras\n")
            f.write(f"- **Gatilho:** `{rule_verdict.get('trigger')}`\n")
            f.write(f"- **Condição:** `{rule_verdict.get('condition')}`\n")
            f.write(f"- **Análise da IA:** _{rule_verdict.get('analysis', 'N/A')}_\n\n")

            # 2. Resultado Mecânico (Dados)
            f.write("### 2. Mecânica (Dados)\n")
            if roll_result['rolled']:
                f.write(f"- **Dados:** {roll_result['dice_value']}\n")
                f.write(f"- **Resultado:** **{'SUCESSO' if roll_result['success'] else 'FALHA'}**\n")
            else:
                f.write("- _Sem rolagem de dados._\n")
            f.write("\n")

            # 3. Narrativa (ENS)
            f.write("### 3. Narrativa (ENS)\n")
            
            # Pensamento (Chain of Thought)
            if 'pensamento' in ens_output:
                f.write("**Pensamento da IA:**\n")
                f.write(f"> {ens_output['pensamento']}\n\n")
            
            # Saídas Visuais
            if 'narrator' in ens_output:
                f.write("**Narrador:**\n")
                f.write(f"```text\n{ens_output['narrator']}\n```\n")
            
            if 'npc' in ens_output:
                f.write("**NPC:**\n")
                f.write(f"```text\n{ens_output['npc']}\n```\n")

            # Sistema (JSON)
            if 'sistema' in ens_output:
                f.write("**Output de Sistema (Raw):**\n")
                f.write(f"```json\n{ens_output['sistema']}\n```\n")
            elif 'sistema_dict' in ens_output:
                f.write("**Output de Sistema (Dict):**\n")
                f.write(f"```json\n{json.dumps(ens_output['sistema_dict'], indent=2, ensure_ascii=False)}\n```\n")

            f.write("\n---\n")

    def log_error(self, message: str):
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write(f"## [ERRO CRÍTICO] {datetime.now().strftime('%H:%M:%S')}\n")
            f.write(f"```\n{message}\n```\n---\n")