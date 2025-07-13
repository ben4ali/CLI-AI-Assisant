from openai import OpenAI
import os
from dotenv import load_dotenv
from assistant.db.services import fetch_shell
from assistant.utils.messages import print_error

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_bash_command(prompt: str) -> str:
    shell = fetch_shell()

    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"You are a shell expert. Convert the user's request into a valid {shell} command. "
                        "Only return the command. No explanation."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        return completion.choices[0].message.content.strip()

    except Exception as e:
        print_error(f"An error occurred while processing the AI request:\n{str(e)}")
        return "[ERROR]"
