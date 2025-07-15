import sys
from assistant.db.services import set_config, get_config, configure_shell, fetch_shell
from assistant.utils.messages import print_error, print_success
from assistant.prompts import get_supported_languages, get_language_name, get_ui_message

VALID_SHELLS = ["bash", "powershell", "zsh"]
VALID_MODELS = ["gpt-4", "gpt-3.5-turbo", "gpt-4o-mini"]
VALID_BOOLEAN = ["true", "false"]
VALID_KEYS = {
    "default_shell": VALID_SHELLS,
    "default_model": VALID_MODELS,
    "allow_execution": VALID_BOOLEAN,
    "history_enabled": VALID_BOOLEAN,
    "default_language": get_supported_languages()
}

def run_config():
    args = sys.argv
    if len(args) < 3:
        print_error(get_ui_message("config_usage"))
        return

    action = args[2].lower()

    if action == "list":
        print_success(get_ui_message("current_configs"))
        for key in VALID_KEYS.keys():
            val = get_config(key)
            if key == "default_language":
                language_name = get_language_name(val) if val else "Unknown"
                print(f"- {key}: {val} ({language_name})")
            else:
                print(f"- {key}: {val}")
        return

    if action not in ["get", "set"]:
        print_error(get_ui_message("invalid_action"))
        return

    if len(args) < 4:
        print_error(get_ui_message("specify_key"))
        return

    key = args[3].lower()
    if key not in VALID_KEYS:
        error_msg = get_ui_message("invalid_config_key", keys=', '.join(VALID_KEYS.keys()))
        print_error(error_msg)
        return

    if action == "get":
        val = get_config(key)
        if val is None:
            error_msg = get_ui_message("no_value_set", key=key)
            print_error(error_msg)
        else:
            print_success(f"{key} = {val}")
        return

    if len(args) < 5:
        print_error(get_ui_message("specify_value"))
        return

    value = args[4].lower()
    if value not in VALID_KEYS[key]:
        error_msg = get_ui_message("invalid_value", key=key, values=', '.join(VALID_KEYS[key]))
        if key == "default_language":
            from assistant.prompts import get_all_languages_info
            lang_info = get_all_languages_info()
            error_msg += "\nAvailable languages:"
            for code, name in lang_info.items():
                error_msg += f"\n  - {code}: {name}"
        print_error(error_msg)
        return

    set_config(key, value)

    if key == "default_shell":
        configure_shell(value)

    success_msg = get_ui_message("config_set", key=key, value=value)
    print_success(success_msg)
