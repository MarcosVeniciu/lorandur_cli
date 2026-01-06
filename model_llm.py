import os
import json
import requests
import sys
import time
'''
    Quero mudar que ao inves do self.preset_name = "@preset/lorandur-cli" ser predefinido aqui,
    ele seja passado como parametro opcional na funcao send_prompt.
    Assim, diferentes presets podem ser usados em chamadas diferentes.
'''
# Garante que scripts na raiz ou subpastas encontrem o arquivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRETS_FILE = os.path.join(BASE_DIR, "secrets.json")

class LLMClient:
    def __init__(self):
        self.api_key = None
        self.site_url = ""
        self.site_name = ""
        
        # Modelo preferencial para Structured Outputs
        self.default_model = "google/gemini-2.0-flash-lite-001"
        self.preset_name = "@preset/lorandur-cli"
        
        self._load_secrets()

        if not self.api_key:
            print("[LLM] AVISO CRÍTICO: 'OPENROUTER_API_KEY' não encontrada em secrets.json!")

    def _load_secrets(self):
        try:
            if os.path.exists(SECRETS_FILE):
                with open(SECRETS_FILE, "r", encoding='utf-8') as f:
                    data = json.load(f)
                    self.api_key = data.get("OPENROUTER_API_KEY")
                    self.site_url = data.get("SITE_URL", "http://localhost")
                    self.site_name = data.get("SITE_NAME", "Lorandur CLI")
            else:
                print(f"[LLM] Arquivo secrets.json não encontrado em: {SECRETS_FILE}")
        except Exception as e:
            print(f"[LLM] Erro ao ler secrets.json: {e}")

    def send_prompt(self, 
                    messages: list, 
                    json_schema: dict = None,
                    temperature: float = 0.7) -> dict:
        """
        Envia prompt para o OpenRouter.
        Aceita lista de mensagens [{'role': 'user', 'content': '...'}].
        Se json_schema for fornecido, força Structured Output e validação.
        """
        if not self.api_key:
            return {"error": "Sem API Key"}

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": self.site_url,
            "X-Title": self.site_name,
        }

        payload = {
            "model": self.default_model, 
            "messages": messages,
            "temperature": temperature,
            "plugins": []
        }

        # Configuração de Saída Estruturada
        if json_schema:
            payload["response_format"] = {
                "type": "json_schema",
                "json_schema": {
                    "name": "lorandur_response",
                    "strict": True,
                    "schema": json_schema
                }
            }
            # O plugin response-healing ajuda a corrigir JSONs quase válidos
            payload["plugins"].append({"id": "response-healing"})

        try:
            start_time = time.time()
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                data=json.dumps(payload),
                timeout=60
            )
            latency = time.time() - start_time

            if response.status_code == 200:
                data = response.json()
                try:
                    choice = data['choices'][0]
                    raw_content = choice['message']['content']
                    finish_reason = choice.get('finish_reason', 'unknown')
                    usage = data.get('usage', {})
                    
                    # Se pediu JSON, tenta parsear imediatamente
                    parsed_content = raw_content
                    if json_schema:
                        try:
                            parsed_content = json.loads(raw_content)
                        except json.JSONDecodeError:
                            print(f"[LLM] Erro de Parse JSON. Raw: {raw_content[:50]}...")
                            return {"error": "Falha no Parse JSON", "raw": raw_content}

                    return {
                        "content": parsed_content,
                        "usage": usage,
                        "latency": latency,
                        "finish_reason": finish_reason
                    }
                    
                except (KeyError, IndexError, TypeError) as e:
                    print(f"[LLM] Erro ao extrair resposta: {e}")
                    return {"error": "Formato de resposta inválido", "details": str(data)}
            else:
                print(f"[LLM] Erro API ({response.status_code}): {response.text}")
                return {"error": f"API Error {response.status_code}", "details": response.text}

        except Exception as e:
            print(f"[LLM] Exceção de Conexão: {e}")
            return {"error": str(e)}

# Instância global
llm_client = LLMClient()