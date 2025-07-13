from assistant.utils.messages import print_error, print_success, print_info, print_warning

def show_loading(message="🔍 Processing your request"):
    import sys
    import time
    for i in range(3):
        sys.stdout.write(f"\r{message}{'.' * (i + 1)}{' ' * (2 - i)}")
        sys.stdout.flush()
        time.sleep(0.4)
    print()

def print_result(command: str):
    print_success("\nSuggested Command:\n")
    print(f"\033[92m{command}\033[0m")
