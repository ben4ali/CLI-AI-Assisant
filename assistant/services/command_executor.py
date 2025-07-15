import subprocess
from assistant.utils.messages import print_info, print_error, print_success
from assistant.prompts import get_ui_message

def execute_command(command: str, shell: str = "bash"):
    try:
        executing_msg = get_ui_message("executing", command=command)
        print_info(f"{executing_msg}\n")
        result = subprocess.run(command, shell=True, text=True, capture_output=True)

        if result.returncode == 0:
            success_msg = get_ui_message("execution_success")
            print_success(success_msg)
            print(result.stdout)
        else:
            failed_msg = get_ui_message("execution_failed")
            print_error(failed_msg)
            print(result.stderr)

    except Exception as e:
        error_msg = get_ui_message("execution_error")
        print_error(f"{error_msg}\n{str(e)}")
