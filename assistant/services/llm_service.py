from openai import OpenAI
from dotenv import load_dotenv
from assistant.db.services import fetch_shell, get_config
from assistant.utils.messages import print_error
from assistant.utils.filesystem import get_directory_context

import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_bash_command(prompt: str, current_path: str = None) -> str:
    shell = fetch_shell()
    model = get_config("default_model") or "gpt-4"

    system_content = (
        f"You are a shell expert. Convert the user's request into a valid {shell} command. "
        "Only return the command. No explanation."
    )

    if current_path:
        system_content += f"\nThe user is currently in: {current_path}."

        files, dirs = get_directory_context(current_path)
        if files:
            system_content += f"\nFiles in current directory: {', '.join(files)}"
        if dirs:
            system_content += f"\nFolders in current directory: {', '.join(dirs)}"

        system_content += "\nIf relevant, prefer relative paths in your output."

    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        return completion.choices[0].message.content.strip()

    except Exception as e:
        print_error(f"An error occurred while processing the AI request:\n{str(e)}")
        return "[ERROR]"
