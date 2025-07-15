LANGUAGE_NAMES = {
    "en": "English",
    "fr": "Français (French)",
    "es": "Español (Spanish)",
    "de": "Deutsch (German)",
    "it": "Italiano (Italian)",
    "pt": "Português (Portuguese)",
    "ru": "Русский (Russian)",
    "zh": "中文 (Chinese)",
    "ja": "日本語 (Japanese)",
    "ar": "العربية (Arabic)"
}

LANGUAGE_PROMPTS = {
    "en": {
        "system_prompt": "You are a shell expert. Convert the user's request into a valid {shell} command. Only return the command. No explanation.",
        "current_directory": "The user is currently in: {current_path}.",
        "files_context": "Files in current directory: {files}",
        "folders_context": "Folders in current directory: {folders}",
        "relative_paths": "If relevant, prefer relative paths in your output."
    },
    "fr": {
        "system_prompt": "Vous êtes un expert en ligne de commande. Convertissez la demande de l'utilisateur en une commande {shell} valide. Retournez seulement la commande. Aucune explication.",
        "current_directory": "L'utilisateur se trouve actuellement dans : {current_path}.",
        "files_context": "Fichiers dans le répertoire actuel : {files}",
        "folders_context": "Dossiers dans le répertoire actuel : {folders}",
        "relative_paths": "Si pertinent, privilégiez les chemins relatifs dans votre réponse."
    },
    "es": {
        "system_prompt": "Eres un experto en línea de comandos. Convierte la solicitud del usuario en un comando {shell} válido. Solo devuelve el comando. Sin explicaciones.",
        "current_directory": "El usuario se encuentra actualmente en: {current_path}.",
        "files_context": "Archivos en el directorio actual: {files}",
        "folders_context": "Carpetas en el directorio actual: {folders}",
        "relative_paths": "Si es relevante, prefiere rutas relativas en tu respuesta."
    },
    "de": {
        "system_prompt": "Sie sind ein Shell-Experte. Wandeln Sie die Anfrage des Benutzers in einen gültigen {shell}-Befehl um. Geben Sie nur den Befehl zurück. Keine Erklärung.",
        "current_directory": "Der Benutzer befindet sich derzeit in: {current_path}.",
        "files_context": "Dateien im aktuellen Verzeichnis: {files}",
        "folders_context": "Ordner im aktuellen Verzeichnis: {folders}",
        "relative_paths": "Falls relevant, bevorzugen Sie relative Pfade in Ihrer Ausgabe."
    },
    "it": {
        "system_prompt": "Sei un esperto di shell. Converti la richiesta dell'utente in un comando {shell} valido. Restituisci solo il comando. Nessuna spiegazione.",
        "current_directory": "L'utente si trova attualmente in: {current_path}.",
        "files_context": "File nella directory corrente: {files}",
        "folders_context": "Cartelle nella directory corrente: {folders}",
        "relative_paths": "Se pertinente, preferisci percorsi relativi nella tua risposta."
    },
    "pt": {
        "system_prompt": "Você é um especialista em shell. Converta a solicitação do usuário em um comando {shell} válido. Retorne apenas o comando. Sem explicações.",
        "current_directory": "O usuário está atualmente em: {current_path}.",
        "files_context": "Arquivos no diretório atual: {files}",
        "folders_context": "Pastas no diretório atual: {folders}",
        "relative_paths": "Se relevante, prefira caminhos relativos em sua resposta."
    },
    "ru": {
        "system_prompt": "Вы эксперт по командной строке. Преобразуйте запрос пользователя в действительную команду {shell}. Верните только команду. Без объяснений.",
        "current_directory": "Пользователь находится в: {current_path}.",
        "files_context": "Файлы в текущей директории: {files}",
        "folders_context": "Папки в текущей директории: {folders}",
        "relative_paths": "Если уместно, предпочитайте относительные пути в ответе."
    },
    "zh": {
        "system_prompt": "您是一个shell专家。将用户的请求转换为有效的{shell}命令。只返回命令，不要解释。",
        "current_directory": "用户当前位于：{current_path}。",
        "files_context": "当前目录中的文件：{files}",
        "folders_context": "当前目录中的文件夹：{folders}",
        "relative_paths": "如果相关，请在输出中优先使用相对路径。"
    },
    "ja": {
        "system_prompt": "あなたはシェルの専門家です。ユーザーのリクエストを有効な{shell}コマンドに変換してください。コマンドのみを返してください。説明は不要です。",
        "current_directory": "ユーザーは現在次の場所にいます：{current_path}。",
        "files_context": "現在のディレクトリのファイル：{files}",
        "folders_context": "現在のディレクトリのフォルダ：{folders}",
        "relative_paths": "関連する場合は、出力で相対パスを優先してください。"
    },
    "ar": {
        "system_prompt": "أنت خبير في سطر الأوامر. قم بتحويل طلب المستخدم إلى أمر {shell} صالح. أرجع الأمر فقط. بدون شرح.",
        "current_directory": "المستخدم حالياً في: {current_path}.",
        "files_context": "الملفات في المجلد الحالي: {files}",
        "folders_context": "المجلدات في المجلد الحالي: {folders}",
        "relative_paths": "إذا كان ذا صلة، فضل المسارات النسبية في إجابتك."
    }
}

def get_language_prompt(language: str, prompt_key: str) -> str:
    """
    Get a specific prompt for a given language.
    
    Args:
        language: Language code (e.g., 'en', 'fr', 'es')
        prompt_key: The key of the prompt to retrieve
        
    Returns:
        The prompt text in the specified language, or English if language not found
    """
    if language not in LANGUAGE_PROMPTS:
        language = "en"
    
    return LANGUAGE_PROMPTS[language].get(prompt_key, LANGUAGE_PROMPTS["en"][prompt_key])

def get_supported_languages() -> list[str]:
    """
    Get a list of all supported language codes.
    
    Returns:
        List of supported language codes
    """
    return list(LANGUAGE_PROMPTS.keys())

def get_language_name(language_code: str) -> str:
    """
    Get the human-readable name for a language code.
    
    Args:
        language_code: The language code (e.g., 'en', 'fr', 'es')
        
    Returns:
        The human-readable name of the language
    """
    return LANGUAGE_NAMES.get(language_code, language_code)

def get_all_languages_info() -> dict[str, str]:
    """
    Get a dictionary mapping language codes to their human-readable names.
    
    Returns:
        Dictionary with language codes as keys and names as values
    """
    return LANGUAGE_NAMES.copy()
