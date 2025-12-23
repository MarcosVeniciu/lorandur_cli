import os
import json
import requests
import sys

# Garante que scripts na raiz ou subpastas encontrem o arquivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRETS_FILE = os.path.join(BASE_DIR, "secrets.json")

class LLMClient:
    def __init__(self):
        self.api_key = None
        self.site_url = ""
        self.site_name = ""
        self.model_name = "google/gemini-2.0-flash-lite-001" # Modelo escolhido
        
        self._load_secrets()

        if not self.api_key:
            print("[LLM] AVISO CRÍTICO: 'OPENROUTER_API_KEY' não encontrada em secrets.json!")
        else:
            print(f"[LLM] Cliente OpenRouter inicializado (Modelo: {self.model_name})")

    def _load_secrets(self):
        try:
            if os.path.exists(SECRETS_FILE):
                with open(SECRETS_FILE, "r") as f:
                    data = json.load(f)
                    self.api_key = data.get("OPENROUTER_API_KEY")
                    self.site_url = data.get("SITE_URL", "http://localhost")
                    self.site_name = data.get("SITE_NAME", "Lorandur CLI")
            else:
                print(f"[LLM] Arquivo secrets.json não encontrado em: {SECRETS_FILE}")
        except Exception as e:
            print(f"[LLM] Erro ao ler secrets.json: {e}")

    def send_prompt(self, messages, temperature=0.7):
        """
        Envia o prompt para o OpenRouter via requisição HTTP POST.
        Suporta string única ou lista de mensagens.
        """
        if not self.api_key:
            print("[LLM] Erro: API Key não configurada.")
            return "<erro>Sem API Key</erro>"

        # 1. Preparar Mensagens no formato OpenAI/OpenRouter
        formatted_messages = []
        
        if isinstance(messages, str):
            # Se for string crua, envelopa como user message
            formatted_messages.append({"role": "user", "content": messages})
        elif isinstance(messages, list):
            # Se já for lista de dicts (chat history), usa direto
            # Se for lista de strings ou formato antigo, converte
            for msg in messages:
                if isinstance(msg, dict):
                    formatted_messages.append(msg)
                else:
                    formatted_messages.append({"role": "user", "content": str(msg)})

        # 2. Configurar Headers e Payload
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": self.site_url, # Necessário para rankings do OpenRouter
            "X-Title": self.site_name,
        }

        payload = {
            "model": self.model_name,
            "messages": formatted_messages,
            "temperature": temperature,
            # "max_tokens": 1024, # Opcional, Gemini tem contexto grande
            # "top_p": 1,
            # "repetition_penalty": 1,
        }

        # 3. Enviar Requisição
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                data=json.dumps(payload),
                timeout=30 # Timeout para evitar travamento eterno
            )

            # 4. Tratar Resposta
            if response.status_code == 200:
                data = response.json()
                # O OpenRouter retorna no formato OpenAI padrão
                try:
                    content = data['choices'][0]['message']['content']
                    return content
                except (KeyError, IndexError):
                    print(f"[LLM] Resposta inesperada: {data}")
                    return "<erro>Formato de resposta inválido</erro>"
            else:
                print(f"[LLM] Erro API ({response.status_code}): {response.text}")
                return f"<erro>API Error {response.status_code}</erro>"

        except requests.exceptions.RequestException as e:
            print(f"[LLM] Erro de Conexão: {e}")
            return "<erro>Falha na Conexão</erro>"
        except Exception as e:
            print(f"[LLM] Erro Genérico: {e}")
            return "<erro>Erro Interno</erro>"

# Instância global
llm_client = LLMClient()