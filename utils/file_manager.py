import os
import json
from typing import Any, Dict, Optional

class FileManager:
    """
    Utilitário centralizado para I/O de arquivos JSON.
    Gerencia caminhos relativos à raiz do projeto lorandur_cli.
    """
    
    def __init__(self):
        # Define a raiz baseada na localização deste arquivo
        # utils/file_manager.py -> sobe 2 niveis -> raiz do projeto
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def save_json(self, filename: str, data: Dict[str, Any], subdir: str = "") -> bool:
        """
        Salva um dicionário como JSON.
        :param filename: Nome do arquivo (ex: save_123.json)
        :param data: Dicionário a ser salvo
        :param subdir: Subpasta dentro de lorandur_cli (ex: 'saves')
        """
        try:
            target_dir = os.path.join(self.base_dir, subdir)
            os.makedirs(target_dir, exist_ok=True)
            
            filepath = os.path.join(target_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"[FileManager] Erro ao salvar {filename}: {e}")
            return False

    def load_json(self, filename: str, subdir: str = "") -> Optional[Dict[str, Any]]:
        """
        Carrega um arquivo JSON.
        """
        try:
            filepath = os.path.join(self.base_dir, subdir, filename)
            
            if not os.path.exists(filepath):
                print(f"[FileManager] Arquivo não encontrado: {filepath}")
                return None
                
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
                
        except Exception as e:
            print(f"[FileManager] Erro ao carregar {filename}: {e}")
            return None