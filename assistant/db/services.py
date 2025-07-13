from assistant.db.dao import get_shell_preference, set_shell_preference, init_db

def configure_shell(shell_name: str):
    init_db()
    set_shell_preference(shell_name)

def fetch_shell() -> str:
    init_db()
    pref = get_shell_preference()
    return pref.shell_name if pref else "bash"
