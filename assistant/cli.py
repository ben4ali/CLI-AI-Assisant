import os
import sys
from assistant.utils.display import show_loading, print_result
from assistant.services.llm_service import get_bash_command
from assistant.db.services import get_config, fetch_shell, save_history_if_enabled
from assistant.services.command_executor import execute_command
from assistant.utils.messages import print_info
from assistant.prompts import get_ui_message

def run_cli():
    if len(sys.argv) < 2:
        print(get_ui_message("usage_message"))
        return

    query = " ".join(sys.argv[1:])
    current_path = os.getcwd()
    shell = fetch_shell()

    show_loading()

    # print(f"\nContext detected: {query}")
    # print(f"Current path: {current_path}")

    command = get_bash_command(query, current_path)
    print_result(command)

    save_history_if_enabled(query, command)

    allow_execution = get_config("allow_execution") == "true"

    if allow_execution:
        execute_command(command, shell)
    else:
        try:
            execute_prompt = get_ui_message("execute_prompt")
            user_input = input(f"\033[93m\n{execute_prompt}\033[0m").strip().lower()
            
            # Accept different positive responses based on language
            positive_responses = ["y", "yes", "o", "oui", "s", "si", "sì", "j", "ja", "д", "да", "ن", "نعم"]
            
            if user_input in positive_responses:
                execute_command(command, shell)
            else:
                print_info(get_ui_message("command_not_executed"))
        except KeyboardInterrupt:
            print_info(get_ui_message("command_cancelled"))
