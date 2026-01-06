import sqlite3
import os
from typing import Optional, Dict, Any
from engine.crypto_utils import CryptoUtils

class DBManager:
    def __init__(self, db_path: str = None):
        # CORREÇÃO CRÍTICA: Caminho absoluto relativo ao arquivo
        if db_path:
            self.db_path = db_path
        else:
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.db_path = os.path.join(base_path, "database", "modules.db")
            
        self.crypto = CryptoUtils()
        self._ensure_db_directory()
        self._init_db()

    def _ensure_db_directory(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

    def _init_db(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS modules (
                module_id TEXT PRIMARY KEY,
                version TEXT NOT NULL,
                module_type TEXT,
                encrypted_data TEXT NOT NULL,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS system_config (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        ''')
        
        conn.commit()
        conn.close()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def upsert_module(self, module_data: Dict[str, Any]):
        module_id = module_data.get('module_id')
        version = module_data.get('version')
        module_type = module_data.get('type', 'generic')

        if not module_id or not version:
            raise ValueError("Module must have 'module_id' and 'version'")

        encrypted_blob = self.crypto.encrypt_json(module_data)

        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO modules (module_id, version, module_type, encrypted_data, updated_at)
            VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(module_id) DO UPDATE SET
                version = excluded.version,
                module_type = excluded.module_type,
                encrypted_data = excluded.encrypted_data,
                updated_at = CURRENT_TIMESTAMP
        ''', (module_id, version, module_type, encrypted_blob))
        
        conn.commit()
        conn.close()
        # print(f"[DB] Módulo '{module_id}' (v{version}) sincronizado.") # Comentado para limpar log

    def get_module(self, module_id: str) -> Optional[Dict[str, Any]]:
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT encrypted_data FROM modules WHERE module_id = ?', (module_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return self.crypto.decrypt_json(row[0])
        return None

    def get_module_version(self, module_id: str) -> Optional[str]:
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT version FROM modules WHERE module_id = ?', (module_id,))
        row = cursor.fetchone()
        conn.close()

        return row[0] if row else None