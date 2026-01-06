import os
import json
import time
import requests
from typing import Dict, Any, List, Optional, Union

class ModelLLM:
    """
    Cliente para a API OpenRouter.
    Configurado para usar Presets (@preset/nome) como definição de modelo e parâmetros.
    """

    def __init__(self):
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = self._load_headers()
        
        # DEFINIÇÃO PADRÃO: Usa o preset do OpenRouter para o CLI
        # Isso carrega modelo, temperatura e system prompts base definidos na interface do OpenRouter
        self.default_model = "@preset/lorandur-cli"

    def _load_headers(self) -> Dict[str, str]:
        try:
            base_path = os.path.dirname(os.path.abspath(__file__))
            secrets_path = os.path.join(base_path, "secrets.json")
            
            with open(secrets_path, "r") as f:
                secrets = json.load(f)
                api_key = secrets.get("OPENROUTER_API_KEY")
        except FileNotFoundError:
            api_key = os.getenv("OPENROUTER_API_KEY")

        if not api_key:
            raise ValueError("API Key do OpenRouter não encontrada em secrets.json ou variáveis de ambiente.")

        return {
            "Authorization": f"Bearer {api_key}",
            "HTTP-Referer": "https://github.com/marcosveniciu/lorandur_cli",
            "X-Title": "Lorandur CLI RPG Engine",
            "Content-Type": "application/json"
        }

    def generate_structured(
        self, 
        system_instruction: str, 
        user_message: str, 
        response_schema: Dict[str, Any], 
        model_preset: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Gera uma resposta estruturada (JSON) forçando o schema via response_format.
        """
        response_format = {
            "type": "json_schema",
            "json_schema": {
                "name": "structured_output",
                "strict": True,
                "schema": response_schema
            }
        }

        # Chama o método genérico
        raw_response = self.generate(
            system_instruction=system_instruction,
            prompt=user_message,
            response_format=response_format,
            model_preset=model_preset
        )

        content = raw_response.get("content", "{}")
        
        try:
            parsed_json = json.loads(content)
            return parsed_json
        except json.JSONDecodeError as e:
            print(f"[ModelLLM] Erro de Parse JSON: {e}")
            print(f"[ModelLLM] Conteúdo recebido: {content[:200]}...")
            return {"error": "JSON_PARSE_FAILED", "raw_content": content}

    def generate(
        self, 
        prompt: str, 
        system_instruction: str = None, 
        messages: List[Dict[str, str]] = None,
        model_preset: str = None,
        temperature: float = 0.7,
        max_tokens: int = 4000,
        response_format: Dict = None
    ) -> Dict[str, Any]:
        
        # 1. Construção do Histórico de Mensagens (Roles)
        conversation = []
        
        if messages:
            conversation = messages
            # Se houver instrução de sistema explícita, adiciona se não existir
            if system_instruction and not any(m['role'] == 'system' for m in conversation):
                conversation.insert(0, {"role": "system", "content": system_instruction})
        else:
            if system_instruction:
                conversation.append({"role": "system", "content": system_instruction})
            conversation.append({"role": "user", "content": prompt})

        # 2. Definição do Modelo / Preset
        # Se um preset específico for passado pelo módulo, usa ele.
        # Senão, usa o default definido no __init__ (@preset/lorandur-cli)
        target_model = model_preset if model_preset else self.default_model

        # 3. Construção do Payload
        payload = {
            "model": target_model, 
            "messages": conversation,
            # Parâmetros explícitos podem sobrescrever o preset dependendo da API,
            # mas mantemos para garantir consistência local se o preset não definir.
            "temperature": temperature,
            "max_tokens": max_tokens,
            "plugins": [
                {"id": "response-healing"}
            ]
        }

        if response_format:
            payload["response_format"] = response_format

        return self._make_request_with_retry(payload)

    def _make_request_with_retry(self, payload: Dict, retries: int = 3) -> Dict[str, Any]:
        for attempt in range(retries):
            try:
                response = requests.post(
                    self.api_url, 
                    headers=self.headers, 
                    data=json.dumps(payload),
                    timeout=60
                )
                
                if response.status_code in [429, 500, 502, 503, 504]:
                    response.raise_for_status()
                
                if response.status_code >= 400:
                    print(f"[ModelLLM] Erro de API ({response.status_code}): {response.text}")
                    return {"content": "", "error": response.text}

                data = response.json()
                
                if "choices" in data and len(data["choices"]) > 0:
                    content = data["choices"][0]["message"]["content"]
                    finish_reason = data["choices"][0].get("finish_reason")
                    usage = data.get("usage", {})
                    
                    return {
                        "content": content,
                        "usage": usage,
                        "finish_reason": finish_reason
                    }
                else:
                    return {"content": "", "error": "Empty response from API"}

            except requests.exceptions.RequestException as e:
                wait_time = 2 ** attempt
                print(f"[ModelLLM] Falha na conexão (Tentativa {attempt+1}/{retries}). Aguardando {wait_time}s...")
                time.sleep(wait_time)
        
        print("[ModelLLM] Todas as tentativas falharam.")
        return {"content": "", "error": "Connection failed after retries"}