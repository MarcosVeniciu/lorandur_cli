import os
import json
import time
from datetime import datetime

class TestOrchestrator:
    def __init__(self, module_name):
        self.module_name = module_name
        self.reports_dir = "teste/relatorios_teste"
        os.makedirs(self.reports_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M")
        self.filename = f"test_{module_name}_{timestamp}.md"
        self.filepath = os.path.join(self.reports_dir, self.filename)
        
        self._init_report()

    def _init_report(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write(f"# Relatório de Teste: Módulo {self.module_name.upper()}\n")
            f.write(f"**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            f.write("---\n\n")
            print(f"[TESTE] Iniciando log em: {self.filepath}")

    def log_section(self, title, content):
        with open(self.filepath, 'a', encoding='utf-8') as f:
            f.write(f"## {title}\n\n")
            if isinstance(content, (dict, list)):
                f.write("```json\n")
                f.write(json.dumps(content, indent=2, ensure_ascii=False))
                f.write("\n```\n\n")
            else:
                f.write(f"{content}\n\n")

    def log_llm_interaction(self, step_name, prompt_messages, response_data):
        with open(self.filepath, 'a', encoding='utf-8') as f:
            f.write(f"### 🤖 Interação LLM: {step_name}\n")
            
            # Log do Prompt COMPLETO
            f.write("**Prompt Enviado:**\n")
            for msg in prompt_messages:
                role = msg['role'].upper()
                content = msg['content']
                f.write(f"- **{role}:**\n")
                f.write("```text\n")
                f.write(f"{content}\n")
                f.write("```\n")
            
            # Log da Resposta
            f.write("**Resposta Recebida:**\n")
            if 'error' in response_data:
                f.write(f"❌ **ERRO:** {response_data['error']}\n")
            else:
                content = response_data.get('content')
                usage = response_data.get('usage', {})
                latency = response_data.get('latency', 0)
                in_tokens = usage.get('prompt_tokens', 0)
                out_tokens = usage.get('completion_tokens', 0)
                
                # Formato solicitado: ✅ **Sucesso** (6.43s | Tokens: In 248 / Out 639)
                f.write(f"✅ **Sucesso** ({latency:.2f}s | Tokens: In {in_tokens} / Out {out_tokens})\n")
                
                f.write("```json\n")
                f.write(json.dumps(content, indent=2, ensure_ascii=False))
                f.write("\n```\n")
            
            f.write("---\n")

    def log_result(self, result_data):
        with open(self.filepath, 'a', encoding='utf-8') as f:
            f.write("## 🏁 Resultado Final do Módulo\n")
            f.write("```json\n")
            f.write(json.dumps(result_data, indent=2, ensure_ascii=False))
            f.write("\n```\n")