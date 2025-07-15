from openai import OpenAI
from dotenv import load_dotenv
from assistant.db.services import fetch_shell, get_config
from assistant.utils.messages import print_error
from assistant.utils.filesystem import get_directory_context
from assistant.prompts import get_language_prompt

import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_bash_command(prompt: str, current_path: str = None) -> str:
    shell = fetch_shell()
    model = get_config("default_model") or "gpt-4"
    language = get_config("default_language") or "en"

    system_content = get_language_prompt(language, "system_prompt").format(shell=shell)

    if current_path:
        system_content += "\n" + get_language_prompt(language, "current_directory").format(current_path=current_path)

        files, dirs = get_directory_context(current_path)
        if files:
            system_content += "\n" + get_language_prompt(language, "files_context").format(files=', '.join(files))
        if dirs:
            system_content += "\n" + get_language_prompt(language, "folders_context").format(folders=', '.join(dirs))

        system_content += "\n" + get_language_prompt(language, "relative_paths")

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
