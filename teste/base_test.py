import unittest
import os
import sys
import time
import json
import logging
from datetime import datetime

# Ajuste de path para rodar a partir da pasta teste/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_controller import GameController
from engine.sync_manager import SyncManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("BaseTest")

class BaseFlowTest(unittest.TestCase):
    """
    Template base para testes de fluxo do Lorandur.
    Gerencia:
    - Setup do Controller
    - Rastreamento de métricas por etapa
    - Geração padronizada de relatório Markdown
    """

    def setUp(self):
        self.controller = GameController()
        logger.info("[SETUP] Sincronizando módulos...")
        SyncManager().sync_all()
        
        self.metrics_history = []  # Lista para guardar métricas de cada passo
        self.start_time_global = time.time()
        self.test_name = self.__class__.__name__

    def track_step(self, step_name: str, duration: float, debug_data: dict = None):
        """
        Registra as métricas de um módulo/etapa executada.
        Tenta pegar os dados de uso do último prompt executado pelo executor.
        """
        if not debug_data:
            debug_data = self.controller.module_executor.last_prompt_debug or {}
        
        usage = debug_data.get('usage', {})
        
        # Tenta pegar custo direto da API (se houver campo customizado) ou calcula
        # Preços Flash 2.0 (Exemplo - Ajuste conforme API real se não vier no JSON)
        price_input = 0.10
        price_output = 0.40
        
        prompt_tokens = usage.get('prompt_tokens', 0)
        completion_tokens = usage.get('completion_tokens', 0)
        total_tokens = usage.get('total_tokens', 0)
        
        # Se a API retornasse 'total_cost' usaríamos aqui. Como fallback, calculamos:
        estimated_cost = (prompt_tokens / 1_000_000 * price_input) + \
                         (completion_tokens / 1_000_000 * price_output)

        self.metrics_history.append({
            "name": step_name,
            "duration": duration,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": total_tokens,
            "cost": estimated_cost,
            "debug_data": debug_data, # Guarda prompt/response para o relatório
            "module_id": debug_data.get('module_id', 'Unknown')
        })

    def _get_module_source(self, module_filename):
        """Lê o arquivo fonte do módulo para exibir prompts no relatório."""
        try:
            root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
            path = os.path.join(root_path, "modules_source", module_filename)
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception:
            pass
        return {}

    def generate_report(self, title: str, status: str = "✅ Sucesso"):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M")
        root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        report_dir = os.path.join(root_path, "teste", "relatorios_teste")
        os.makedirs(report_dir, exist_ok=True)
        
        filename = os.path.join(report_dir, f"{self.test_name}_{timestamp}.md")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Relatório: {title}\n")
            f.write(f"**Data:** {timestamp} | **Status:** {status}\n\n")

            # === TABELA DE MÉTRICAS DINÂMICA ===
            f.write("## 📊 Métricas de Execução\n\n")
            
            # Cabeçalho
            headers = ["Métrica"] + [step['name'] for step in self.metrics_history] + ["Total"]
            f.write("| " + " | ".join(headers) + " |\n")
            f.write("| " + " | ".join([":---"] * len(headers)) + " |\n")

            # Totais
            t_duration = sum(s['duration'] for s in self.metrics_history)
            t_input = sum(s['prompt_tokens'] for s in self.metrics_history)
            t_output = sum(s['completion_tokens'] for s in self.metrics_history)
            t_total = sum(s['total_tokens'] for s in self.metrics_history)
            t_cost = sum(s['cost'] for s in self.metrics_history)

            # Linhas
            # Tempo
            row_time = [f"{s['duration']:.2f}s" for s in self.metrics_history]
            f.write(f"| **Tempo Total** | {' | '.join(row_time)} | **{t_duration:.2f}s** |\n")
            
            # Tokens Entrada
            row_in = [str(s['prompt_tokens']) for s in self.metrics_history]
            f.write(f"| **Tokens Entrada** | {' | '.join(row_in)} | **{t_input}** |\n")
            
            # Tokens Saída
            row_out = [str(s['completion_tokens']) for s in self.metrics_history]
            f.write(f"| **Tokens Saída** | {' | '.join(row_out)} | **{t_output}** |\n")
            
            # Tokens Total
            row_tot = [str(s['total_tokens']) for s in self.metrics_history]
            f.write(f"| **Tokens Total** | {' | '.join(row_tot)} | **{t_total}** |\n")
            
            # Custo
            row_cost = [f"${s['cost']:.6f}" for s in self.metrics_history]
            f.write(f"| **Custo Estimado** | {' | '.join(row_cost)} | **${t_cost:.6f}** |\n")

            f.write("\n---\n")

            # === DETALHES DE CADA PASSO ===
            for i, step in enumerate(self.metrics_history):
                debug = step['debug_data']
                mod_id = step['module_id']
                
                f.write(f"\n## {i+1}. {step['name']} (Módulo: `{mod_id}`)\n")
                
                # Detalhes Técnicos (Collapsible)
                f.write("<details>\n<summary><strong>⚙️ Ver Prompts & Request</strong></summary>\n\n")
                f.write(f"**System Prompt:**\n```text\n{debug.get('system', 'N/A')}\n```\n")
                f.write(f"**User Prompt:**\n```text\n{debug.get('user', 'N/A')}\n```\n")
                if debug.get('schema'):
                     f.write(f"**Schema Enviado:**\n```json\n{json.dumps(debug.get('schema'), indent=2, ensure_ascii=False)}\n```\n")
                f.write("</details>\n\n")

                # === NOVA SEÇÃO: RESPOSTA DA LLM ===
                # Renderiza a resposta se ela tiver sido passada para o track_step
                response_content = debug.get('response_content')
                if response_content:
                    f.write("### 🤖 Resposta do Modelo\n")
                    f.write(f"```json\n{json.dumps(response_content, indent=2, ensure_ascii=False)}\n```\n")
                else:
                    f.write("> *Nenhuma resposta registrada para este passo.*\n")
            
            print(f"\n>>> Relatório gerado: {filename}")