import os
import json
import glob
from typing import List, Dict, Any
from database.db_manager import DBManager

class SyncManager:
    """
    Responsável por sincronizar os arquivos JSON locais (modules_source/)
    com o banco de dados criptografado (modules.db).
    """

    def __init__(self, source_dir: str = None):
        # CORREÇÃO CRÍTICA: Define o caminho relativo à localização deste arquivo script
        # lorandur_cli/engine/sync_manager.py -> (sobe 1) engine -> (sobe 2) lorandur_cli root
        if source_dir:
            self.source_dir = source_dir
        else:
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.source_dir = os.path.join(base_path, "modules_source")
            
        self.db = DBManager()

    def sync_all(self) -> Dict[str, List[str]]:
        """
        Varre o diretório de fontes e atualiza o DB se a versão do arquivo
        for superior à versão do banco.
        """
        report = {"updated": [], "skipped": [], "errors": []}
        
        # Garante que a pasta existe (agora no lugar certo)
        if not os.path.exists(self.source_dir):
            try:
                os.makedirs(self.source_dir)
                print(f"[SyncManager] Pasta criada (vazia): {self.source_dir}")
                # Se criou agora, não tem arquivos, retorna
                return report
            except OSError as e:
                report["errors"].append(f"Erro ao criar pasta {self.source_dir}: {e}")
                return report

        json_files = glob.glob(os.path.join(self.source_dir, "*.json"))
        
        if not json_files:
            print(f"[SyncManager] ⚠️ Nenhum JSON encontrado em: {self.source_dir}")

        for file_path in json_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_data = json.load(f)
                
                module_id = file_data.get('module_id')
                file_version = file_data.get('version')

                if not module_id or not file_version:
                    report["errors"].append(f"{os.path.basename(file_path)}: ID ou Versão faltando")
                    continue

                if self._should_update(module_id, file_version):
                    self.db.upsert_module(file_data)
                    report["updated"].append(f"{module_id} (v{file_version})")
                else:
                    report["skipped"].append(module_id)

            except json.JSONDecodeError:
                report["errors"].append(f"{os.path.basename(file_path)}: JSON Inválido")
            except Exception as e:
                report["errors"].append(f"{os.path.basename(file_path)}: {str(e)}")

        self._print_report(report)
        return report

    def _should_update(self, module_id: str, file_version: str) -> bool:
        db_version = self.db.get_module_version(module_id)
        if not db_version:
            return True
        return self._compare_versions(file_version, db_version)

    def _compare_versions(self, v1: str, v2: str) -> bool:
        try:
            parts1 = [int(x) for x in v1.split('.')]
            parts2 = [int(x) for x in v2.split('.')]
            return parts1 > parts2
        except ValueError:
            return v1 != v2

    def _print_report(self, report: Dict):
        if report["updated"]:
            print(f"[SyncManager] 🔄 Atualizados: {', '.join(report['updated'])}")
        if report["errors"]:
            print(f"[SyncManager] ❌ Erros: {report['errors']}")