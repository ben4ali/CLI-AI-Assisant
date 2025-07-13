import sys
from assistant.utils.display import show_loading, print_result
from assistant.services.llm_service import get_bash_command

def run_cli():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"your natural language instruction\"")
        return

    query = " ".join(sys.argv[1:])
    show_loading("Processing your request")
    
		
    command = get_bash_command(query)
    if command == "[ERROR]":
        return
    
    print_result(command)
