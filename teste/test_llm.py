import os
import sys

# Garante que scripts na raiz encontrem os módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model_llm import LLMClient

def teste_conexao():
    print("=== DIAGNÓSTICO DE CONEXÃO LLM (OPENROUTER) ===")
    
    # 1. Verifica arquivo secrets.json
    if os.path.exists("secrets.json"):
        print("[OK] Arquivo 'secrets.json' encontrado.")
    else:
        print("[FALHA] Arquivo 'secrets.json' NÃO encontrado na raiz!")
        return

    # 2. Inicializa Cliente
    print("Inicializando cliente...")
    client = LLMClient()
    
    # VERIFICAÇÃO ATUALIZADA: Checa se tem API Key em vez de checar se tem modelo carregado
    if not client.api_key:
        print("[FALHA] API Key não carregada (Verifique secrets.json).")
        return

    print(f"[OK] Cliente pronto. Usando modelo: {client.model_name}")

    # 3. Teste de Envio
    print("Enviando prompt de teste (Aguarde...)...")
    try:
        resposta = client.send_prompt("Responda apenas com a palavra: FUNCIONOU.")
        print(f"\nRESPOSTA DA IA: '{resposta}'")
        
        if "FUNCIONOU" in resposta.upper():
            print("\n[SUCESSO] A conexão está perfeita!")
        else:
            print("\n[AVISO] A IA respondeu, mas algo inesperado (Verifique se não é erro de cota/bloqueio):")
            print(resposta)
            
    except Exception as e:
        print(f"\n[ERRO CRÍTICO] Falha ao enviar: {e}")

if __name__ == "__main__":
    teste_conexao()