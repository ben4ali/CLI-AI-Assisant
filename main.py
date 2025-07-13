from assistant.cli import run_cli
from assistant.config import run_config
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "-config":
        run_config()
    else:
        run_cli()
