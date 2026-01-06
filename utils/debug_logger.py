import os
import json
from datetime import datetime
from typing import Any

class DebugLogger:
    """
    Sistema de Logs em Markdown para a Engine Lorandur.
    Gera relatórios legíveis para humanos em lorandur_cli/Logger/game_logger/
    """
    
    def __init__(self, scenario_name: str = "System"):
        # Garante que o diretório de logs exista relativo a este arquivo
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.log_dir = os.path.join(base_dir, "Logger", "game_logger")
        os.makedirs(self.log_dir, exist_ok=True)
        
        # Cria um nome de arquivo seguro
        date_str = datetime.now().strftime("%Y-%m-%d")
        safe_name = "".join([c for c in scenario_name if c.isalnum() or c in (' ', '_', '-')]).strip().replace(' ', '_').lower()
        
        # Se for System, usa um log rotativo ou único por execução. Aqui usamos timestamp para evitar conflito.
        if scenario_name == "System":
            timestamp = datetime.now().strftime("%H-%M-%S")
            self.filepath = os.path.join(self.log_dir, f"log_SYSTEM_{date_str}_{timestamp}.md")
        else:
            # Para cenários, tentamos manter um arquivo por dia ou sessão
            self.filepath = os.path.join(self.log_dir, f"log_{safe_name}_{date_str}.md")
        
        # Inicializa o arquivo se ele não existir
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                f.write(f"# Log de Sessão: {scenario_name}\n")
                f.write(f"**Data:** {date_str}\n")
                f.write(f"**Inicio:** {datetime.now().strftime('%H:%M:%S')}\n\n")
                f.write("---\n\n")

    def log_step(self, step_name: str, status: str, data: Any = None):
        """Registra um passo importante da execução."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        try:
            with open(self.filepath, 'a', encoding='utf-8') as f:
                f.write(f"## [{timestamp}] {step_name}\n")
                f.write(f"**Status:** {status}\n")
                
                if data is not None:
                    f.write("\n```json\n")
                    # default=str ajuda a serializar objetos que não são nativos do JSON
                    f.write(json.dumps(data, indent=2, ensure_ascii=False, default=str))
                    f.write("\n```\n")
                
                f.write("\n---\n")
        except Exception as e:
            print(f"[Logger Error] Falha ao escrever log: {e}")

    def log_error(self, step_name: str, error_msg: str):
        """Registra um erro destacado."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        try:
            with open(self.filepath, 'a', encoding='utf-8') as f:
                f.write(f"## [{timestamp}] ❌ ERRO CRÍTICO: {step_name}\n")
                f.write(f"**Detalhes:** {error_msg}\n")
                f.write("\n---\n")
        except Exception as e:
            print(f"[Logger Error] Falha ao escrever erro: {e}")