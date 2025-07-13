import os
import sys
from assistant.utils.display import show_loading, print_result
from assistant.services.llm_service import get_bash_command

def run_cli():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"your natural language instruction\"")
        return

    query = " ".join(sys.argv[1:])
    current_path = os.getcwd()

    show_loading("Processing your request")

    # print(f"\nContext detected: {query}")
    # print(f"Current path: {current_path}")

    command = get_bash_command(query, current_path)
    print_result(command)
