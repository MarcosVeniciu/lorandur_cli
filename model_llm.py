import os
import json
import time
import requests
from typing import Dict, Any, List, Optional, Union

class ModelLLM:
    """
    Cliente para a API OpenRouter.
    """

    def __init__(self):
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = self._load_headers()
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
            raise ValueError("API Key do OpenRouter não encontrada.")

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
        
        response_format = {
            "type": "json_schema",
            "json_schema": {
                "name": "structured_output",
                "strict": True,
                "schema": response_schema
            }
        }

        # Repassa flags de debug/teste se necessário
        raw_response = self.generate(
            system_instruction=system_instruction,
            prompt=user_message,
            response_format=response_format,
            model_preset=model_preset
        )

        if raw_response.get("error"):
            return {"error": raw_response["error"]}

        content = raw_response.get("content", "")
        if not content:
            return {"error": "EMPTY_CONTENT"}

        cleaned_content = self._clean_markdown(content)
        
        try:
            parsed_json = json.loads(cleaned_content)
            # Injeta metadados de uso no JSON retornado para fins de log/custo
            if isinstance(parsed_json, dict) and "usage" in raw_response:
                parsed_json["_meta_usage"] = raw_response["usage"]
            return parsed_json
        except json.JSONDecodeError as e:
            print(f"[ModelLLM ERROR] Falha no Parse JSON: {e}")
            return {"error": "JSON_PARSE_FAILED", "raw_content": content}

    def _clean_markdown(self, text: str) -> str:
        text = text.strip()
        if text.startswith("```json"):
            text = text[7:]
        elif text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        return text.strip()

    def generate(
        self, 
        prompt: str, 
        system_instruction: str = None, 
        messages: List[Dict[str, str]] = None,
        model_preset: str = None,
        response_format: Dict = None
    ) -> Dict[str, Any]:
        
        conversation = []
        if messages:
            conversation = messages
            if system_instruction and not any(m['role'] == 'system' for m in conversation):
                conversation.insert(0, {"role": "system", "content": system_instruction})
        else:
            if system_instruction:
                conversation.append({"role": "system", "content": system_instruction})
            conversation.append({"role": "user", "content": prompt})

        target_model = model_preset if model_preset else self.default_model

        payload = {
            "model": target_model, 
            "messages": conversation,
            "plugins": [{"id": "response-healing"}],
            # Flag para garantir retorno de usage (padrão OpenRouter, mas reforçado)
            "include_non_standard_pricing": True 
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
                
                if response.status_code >= 400:
                    print(f"[ModelLLM ERROR] API HTTP {response.status_code}: {response.text}")
                    return {"content": "", "error": f"HTTP {response.status_code}: {response.text}"}

                data = response.json()
                
                if "choices" in data and len(data["choices"]) > 0:
                    content = data["choices"][0]["message"]["content"]
                    usage = data.get("usage", {})
                    # Tenta capturar custo se a API mandar em extensões não padrão
                    # Caso contrário, o BaseTest calculará via usage
                    return {"content": content, "usage": usage}
                else:
                    return {"content": "", "error": "Empty response from API"}

            except requests.exceptions.RequestException as e:
                time.sleep(2 ** attempt)
        
        return {"content": "", "error": "Connection failed after retries"}