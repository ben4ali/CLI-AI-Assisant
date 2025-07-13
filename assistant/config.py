import sys
from assistant.db.services import configure_shell
from assistant.utils.messages import print_error, print_success

def run_config():
    if len(sys.argv) < 3:
        print_error("Usage: python main.py -config <bash|powershell|zsh>")
        return

    shell_name = sys.argv[2].lower()
    if shell_name not in ["bash", "powershell", "zsh"]:
        print_error("Unsupported shell. Choose one of: bash, powershell, zsh")
        return

    configure_shell(shell_name)
    print_success(f"Default shell set to: {shell_name}")
