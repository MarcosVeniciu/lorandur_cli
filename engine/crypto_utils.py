import os
import json
from cryptography.fernet import Fernet
from typing import Dict, Any

class CryptoUtils:
    # Em produção real, isso seria ofuscado ou lido de var de ambiente.
    # Para o CLI local, uma chave estática garante que o banco funcione entre reinicios.
    # ATENÇÃO: Se mudar essa chave, o banco antigo se torna ilegível.
    _STATIC_KEY = b'G4qR-8Yt5z9XwL2v3B7n1M6c0J9k4F8d2S5a1H3j5K7=' 

    def __init__(self):
        # Garante que a chave tenha o tamanho correto para o Fernet (base64 urlsafe)
        # Se a chave estática for inválida, gera uma nova (apenas para dev)
        try:
            self.cipher = Fernet(self._STATIC_KEY)
        except ValueError:
            print("[CryptoUtils] Chave estática inválida. Gerando temporária.")
            key = Fernet.generate_key()
            self.cipher = Fernet(key)

    def encrypt_json(self, data: Dict[str, Any]) -> str:
        """Converte dict para JSON string e criptografa."""
        json_str = json.dumps(data, ensure_ascii=False)
        encrypted_bytes = self.cipher.encrypt(json_str.encode('utf-8'))
        return encrypted_bytes.decode('utf-8')

    def decrypt_json(self, encrypted_str: str) -> Dict[str, Any]:
        """Descriptografa string e converte de volta para dict."""
        try:
            encrypted_bytes = encrypted_str.encode('utf-8')
            decrypted_bytes = self.cipher.decrypt(encrypted_bytes)
            return json.loads(decrypted_bytes.decode('utf-8'))
        except Exception as e:
            print(f"[CryptoUtils] Erro ao descriptografar: {e}")
            return {}