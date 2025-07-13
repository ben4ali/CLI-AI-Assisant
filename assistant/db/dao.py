import sqlite3

DB_PATH = "assistant.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT NOT NULL,
            command TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    conn.close()

def set_setting(key: str, value: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO settings(key, value) VALUES (?, ?)
        ON CONFLICT(key) DO UPDATE SET value=excluded.value;
    """, (key, value))
    conn.commit()
    conn.close()

def get_setting(key: str) -> str | None:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM settings WHERE key = ?", (key,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def insert_history(query: str, command: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO history (query, command) VALUES (?, ?)
    """, (query, command))

    cursor.execute("""
        DELETE FROM history
        WHERE id NOT IN (
            SELECT id FROM history ORDER BY timestamp DESC LIMIT 30
        );
    """)

    conn.commit()
    conn.close()

def get_history(limit=30) -> list[tuple]:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT query, command, timestamp
        FROM history
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))
    result = cursor.fetchall()
    conn.close()
    return result