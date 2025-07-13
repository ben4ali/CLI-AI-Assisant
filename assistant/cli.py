import os
import sys
from assistant.utils.display import show_loading, print_result
from assistant.services.llm_service import get_bash_command
from assistant.db.services import get_config, fetch_shell, save_history_if_enabled
from assistant.services.command_executor import execute_command
from assistant.utils.messages import print_info

def run_cli():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"your natural language instruction\"")
        return

    query = " ".join(sys.argv[1:])
    current_path = os.getcwd()
    shell = fetch_shell()

    show_loading("Processing your request")

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
            user_input = input(f"\033[93m\nDo you want to execute this command? (y/N): \033[0m").strip().lower()
            if user_input == "y":
                execute_command(command, shell)
            else:
                print_info("Command was not executed.")
        except KeyboardInterrupt:
            print_info("\nCommand execution cancelled by user.")
