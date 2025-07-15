# Terminal Assistant

**Terminal Assistant** is a smart CLI tool that converts natural language instructions into terminal c| Key | Default | Description |
|-----|---------|-------------|
| default_shell | bash | Preferred shell to generate commands for |
| default_model | gpt-4 | AI model used to process instructions |
| allow_execution | false | If true, executes generated commands |
| history_enabled | false | If true, saves the last 30 commands |
| default_language | en | Language for AI prompts and UI messages (en, fr, es, de, it, pt, ru, zh, ja, ar) | using AI (OpenAI GPT). It supports dynamic shell preferences (bash, PowerShell, etc.), remembers your configuration, logs history, and optionally executes commands directly in your terminal.

---

## Features

- Translate natural language into real shell commands
- Supports multiple shells (bash, PowerShell, etc.)
- **Multilingual interface** - supports 10 languages (English, French, Spanish, German, Italian, Portuguese, Russian, Chinese, Japanese, Arabic) for both AI prompts and UI messages
- Persistent settings using SQLite
- Command history (last 30 entries)
- Optional command execution
- Configurable AI model (GPT-4 or GPT-3.5)
- Easy to extend and modular Python architecture

---

## Technologies Used

- Python 3.10+
- [OpenAI Python SDK](https://pypi.org/project/openai/)
- SQLite3 (with DAO/service layers)
- Dotenv for environment variables

---

## Installation

1. **Clone the project**

   ```bash
   git clone https://github.com/ben4ali/CLI-AI-Assitant
   cd CLI-AI-Assitant
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux/macOS
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your environment**

   Create a `.env` file by copying the sample:

   ```bash
   cp .env.sample .env
   ```

   And update the `.env` file with your OpenAI API key:

   ```env
   OPENAI_API_KEY=your-key-here
   ```

---

## Usage

### Natural Language Command

```bash
python main.py "list all files modified in the last 10 minutes"
```

Output:
```bash
find . -type f -mmin -10
```

If `allow_execution` is enabled, the command is executed automatically.

### Configuration

Use the `-config` flag to manage settings:

#### Set a config value

```bash
python main.py -config set default_shell bash
python main.py -config set default_model gpt-4
python main.py -config set allow_execution true
python main.py -config set default_language fr  # Set to French
```

#### Set Language for Multilingual Support

The assistant supports 10 languages with both AI prompts and UI messages translated:

```bash
# Set to French
python main.py -config set default_language fr

# Set to Spanish  
python main.py -config set default_language es

# Set to German
python main.py -config set default_language de

# Other supported languages: en (English), it (Italian), pt (Portuguese), 
# ru (Russian), zh (Chinese), ja (Japanese), ar (Arabic)
```

When you change the language, all interface messages (like "Processing your request", "Suggested Command", "Do you want to execute this command?") will appear in the selected language, and the AI will also generate responses in that language.

#### Get a specific config value

```bash
python main.py -config get default_model
```

#### List all config

```bash
python main.py -config list
```

### Command History

To view the latest 30 commands generated:

```bash
python main.py -history
```

Example output:

```text
1. [2025-07-13 14:45:11] show current directory -> pwd
2. [2025-07-13 14:44:50] list txt files -> ls *.txt
```

---

## Default Configuration Values

| Key | Default | Description |
|-----|---------|-------------|
| default_shell | bash | Preferred shell to generate commands for |
| default_model | gpt-4 | AI model used to process instructions |
| allow_execution | false | If true, executes generated commands |
| history_enabled | false | If true, saves the last 30 commands |
| default_language | en | Language used for generating commands and responses |

---

## Example Prompts

```bash
python main.py "create a folder named 'project' and move all .py files into it"
python main.py "show me running processes and sort by memory"
python main.py "list all folders in this directory"
```

## License

MIT — use it freely, no restrictions.

---

## Author

Made by Ali Benkarrouch  
[GitHub](https://github.com/ben4ali)