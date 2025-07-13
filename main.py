from assistant.cli import run_cli
from assistant.config import run_config
from assistant.db.services import get_history
from assistant.utils.messages import print_success

import sys

if __name__ == "__main__":
    args = sys.argv

    if len(args) >= 2:
        if args[1] in ("-config", "--config"):
            run_config()
        elif args[1] in ("-history", "--history"):
            print_success("Recent command history:")
            history = get_history()
            for i, (query, command, timestamp) in enumerate(history, start=1):
                print(f"{i}. [{timestamp}] {query} -> {command}")
        else:
            run_cli()
    else:
        print("Usage:")
        print("- Run a command:         python main.py \"your question\"")
        print("- Configure settings:    python main.py -config [get|set|list] ...")
        print("- Show history:          python main.py -history")
