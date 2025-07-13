import subprocess
from assistant.utils.messages import print_info, print_error, print_success

def execute_command(command: str, shell: str = "bash"):
    try:
        print_info(f"Executing: {command}\n")
        result = subprocess.run(command, shell=True, text=True, capture_output=True)

        if result.returncode == 0:
            print_success("Command executed successfully.")
            print(result.stdout)
        else:
            print_error("Command execution failed:")
            print(result.stderr)

    except Exception as e:
        print_error(f"Error while executing the command:\n{str(e)}")
