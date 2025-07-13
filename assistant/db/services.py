from assistant.db.dao import init_db, set_setting, get_setting

DEFAULT_CONFIG = {
    "default_shell": "bash",
    "default_model": "gpt-4",
    "allow_execution": "false",
    "history_enabled": "false",
    "default_language": "en"
}

def configure_shell(shell_name: str):
    init_db()
    set_setting("default_shell", shell_name)

def fetch_shell() -> str:
    init_db()
    shell = get_setting("default_shell")
    if shell:
        return shell
    set_setting("default_shell", DEFAULT_CONFIG["default_shell"])
    return DEFAULT_CONFIG["default_shell"]

def set_config(key: str, value: str):
    init_db()
    set_setting(key, value)

def get_config(key: str) -> str | None:
    init_db()
    val = get_setting(key)
    if val is None and key in DEFAULT_CONFIG:
        set_setting(key, DEFAULT_CONFIG[key])
        return DEFAULT_CONFIG[key]
    return val
