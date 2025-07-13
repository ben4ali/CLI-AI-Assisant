import sqlite3
from assistant.db.models import ShellPreference

DB_PATH = "assistant.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shell_preferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            shell_name TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

def set_shell_preference(shell_name: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM shell_preferences;")
    cursor.execute("INSERT INTO shell_preferences (shell_name) VALUES (?)", (shell_name,))
    conn.commit()
    conn.close()

def get_shell_preference() -> ShellPreference | None:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, shell_name FROM shell_preferences LIMIT 1;")
    row = cursor.fetchone()
    conn.close()
    return ShellPreference(*row) if row else None
