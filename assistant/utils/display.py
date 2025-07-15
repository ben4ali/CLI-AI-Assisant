from assistant.utils.messages import print_error, print_success, print_info, print_warning
from assistant.prompts import get_ui_message

def show_loading(message_key="processing"):
    import sys
    import time
    message = get_ui_message(message_key)
    for i in range(3):
        sys.stdout.write(f"\r{message}{'.' * (i + 1)}{' ' * (2 - i)}")
        sys.stdout.flush()
        time.sleep(0.4)
    print()

def print_result(command: str):
    suggestion_text = get_ui_message("suggested_command")
    print_success(f"\n{suggestion_text}\n")
    print(f"\033[92m{command}\033[0m")
