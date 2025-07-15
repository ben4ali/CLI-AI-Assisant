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
        "relative_paths": "If relevant, prefer relative paths in your output.",
        # UI Messages
        "processing": "Processing your request",
        "suggested_command": "Suggested Command:",
        "execute_prompt": "Do you want to execute this command? (y/N): ",
        "command_not_executed": "Command was not executed.",
        "command_cancelled": "Command execution cancelled by user.",
        "executing": "Executing: {command}",
        "execution_success": "Command executed successfully.",
        "execution_failed": "Command execution failed:",
        "execution_error": "Error while executing the command:",
        "usage_message": "Usage: python main.py \"your natural language instruction\"",
        "config_usage": "Usage: python main.py -config <get|set|list> [key] [value]",
        "invalid_action": "Invalid action. Use get, set or list.",
        "specify_key": "Please specify the key.",
        "invalid_config_key": "Invalid config key. Valid keys: {keys}",
        "no_value_set": "No value set for '{key}'",
        "specify_value": "Please specify a value to set.",
        "invalid_value": "Invalid value for {key}. Valid values: {values}",
        "config_set": "Configuration '{key}' set to '{value}'",
        "current_configs": "Current configurations:"
    },
    "fr": {
        "system_prompt": "Vous êtes un expert en ligne de commande. Convertissez la demande de l'utilisateur en une commande {shell} valide. Retournez seulement la commande. Aucune explication.",
        "current_directory": "L'utilisateur se trouve actuellement dans : {current_path}.",
        "files_context": "Fichiers dans le répertoire actuel : {files}",
        "folders_context": "Dossiers dans le répertoire actuel : {folders}",
        "relative_paths": "Si pertinent, privilégiez les chemins relatifs dans votre réponse.",
        # UI Messages
        "processing": "Traitement de votre demande",
        "suggested_command": "Commande suggérée :",
        "execute_prompt": "Voulez-vous exécuter cette commande ? (o/N) : ",
        "command_not_executed": "La commande n'a pas été exécutée.",
        "command_cancelled": "Exécution de la commande annulée par l'utilisateur.",
        "executing": "Exécution : {command}",
        "execution_success": "Commande exécutée avec succès.",
        "execution_failed": "Échec de l'exécution de la commande :",
        "execution_error": "Erreur lors de l'exécution de la commande :",
        "usage_message": "Utilisation : python main.py \"votre instruction en langage naturel\"",
        "config_usage": "Utilisation : python main.py -config <get|set|list> [clé] [valeur]",
        "invalid_action": "Action invalide. Utilisez get, set ou list.",
        "specify_key": "Veuillez spécifier la clé.",
        "invalid_config_key": "Clé de configuration invalide. Clés valides : {keys}",
        "no_value_set": "Aucune valeur définie pour '{key}'",
        "specify_value": "Veuillez spécifier une valeur à définir.",
        "invalid_value": "Valeur invalide pour {key}. Valeurs valides : {values}",
        "config_set": "Configuration '{key}' définie à '{value}'",
        "current_configs": "Configurations actuelles :"
    },
    "es": {
        "system_prompt": "Eres un experto en línea de comandos. Convierte la solicitud del usuario en un comando {shell} válido. Solo devuelve el comando. Sin explicaciones.",
        "current_directory": "El usuario se encuentra actualmente en: {current_path}.",
        "files_context": "Archivos en el directorio actual: {files}",
        "folders_context": "Carpetas en el directorio actual: {folders}",
        "relative_paths": "Si es relevante, prefiere rutas relativas en tu respuesta.",
        # UI Messages
        "processing": "Procesando tu solicitud",
        "suggested_command": "Comando sugerido:",
        "execute_prompt": "¿Quieres ejecutar este comando? (s/N): ",
        "command_not_executed": "El comando no fue ejecutado.",
        "command_cancelled": "Ejecución del comando cancelada por el usuario.",
        "executing": "Ejecutando: {command}",
        "execution_success": "Comando ejecutado con éxito.",
        "execution_failed": "Falló la ejecución del comando:",
        "execution_error": "Error al ejecutar el comando:",
        "usage_message": "Uso: python main.py \"tu instrucción en lenguaje natural\"",
        "config_usage": "Uso: python main.py -config <get|set|list> [clave] [valor]",
        "invalid_action": "Acción inválida. Usa get, set o list.",
        "specify_key": "Por favor especifica la clave.",
        "invalid_config_key": "Clave de configuración inválida. Claves válidas: {keys}",
        "no_value_set": "No hay valor establecido para '{key}'",
        "specify_value": "Por favor especifica un valor a establecer.",
        "invalid_value": "Valor inválido para {key}. Valores válidos: {values}",
        "config_set": "Configuración '{key}' establecida a '{value}'",
        "current_configs": "Configuraciones actuales:"
    },
    "de": {
        "system_prompt": "Sie sind ein Shell-Experte. Wandeln Sie die Anfrage des Benutzers in einen gültigen {shell}-Befehl um. Geben Sie nur den Befehl zurück. Keine Erklärung.",
        "current_directory": "Der Benutzer befindet sich derzeit in: {current_path}.",
        "files_context": "Dateien im aktuellen Verzeichnis: {files}",
        "folders_context": "Ordner im aktuellen Verzeichnis: {folders}",
        "relative_paths": "Falls relevant, bevorzugen Sie relative Pfade in Ihrer Ausgabe.",
        # UI Messages
        "processing": "Ihre Anfrage wird bearbeitet",
        "suggested_command": "Vorgeschlagener Befehl:",
        "execute_prompt": "Möchten Sie diesen Befehl ausführen? (j/N): ",
        "command_not_executed": "Befehl wurde nicht ausgeführt.",
        "command_cancelled": "Befehlsausführung vom Benutzer abgebrochen.",
        "executing": "Ausführung: {command}",
        "execution_success": "Befehl erfolgreich ausgeführt.",
        "execution_failed": "Befehlsausführung fehlgeschlagen:",
        "execution_error": "Fehler bei der Befehlsausführung:",
        "usage_message": "Verwendung: python main.py \"Ihre Anweisung in natürlicher Sprache\"",
        "config_usage": "Verwendung: python main.py -config <get|set|list> [Schlüssel] [Wert]",
        "invalid_action": "Ungültige Aktion. Verwenden Sie get, set oder list.",
        "specify_key": "Bitte geben Sie den Schlüssel an.",
        "invalid_config_key": "Ungültiger Konfigurationsschlüssel. Gültige Schlüssel: {keys}",
        "no_value_set": "Kein Wert für '{key}' gesetzt",
        "specify_value": "Bitte geben Sie einen Wert zum Setzen an.",
        "invalid_value": "Ungültiger Wert für {key}. Gültige Werte: {values}",
        "config_set": "Konfiguration '{key}' auf '{value}' gesetzt",
        "current_configs": "Aktuelle Konfigurationen:"
    },
    "it": {
        "system_prompt": "Sei un esperto di shell. Converti la richiesta dell'utente in un comando {shell} valido. Restituisci solo il comando. Nessuna spiegazione.",
        "current_directory": "L'utente si trova attualmente in: {current_path}.",
        "files_context": "File nella directory corrente: {files}",
        "folders_context": "Cartelle nella directory corrente: {folders}",
        "relative_paths": "Se pertinente, preferisci percorsi relativi nella tua risposta.",
        # UI Messages
        "processing": "Elaborazione della tua richiesta",
        "suggested_command": "Comando suggerito:",
        "execute_prompt": "Vuoi eseguire questo comando? (s/N): ",
        "command_not_executed": "Il comando non è stato eseguito.",
        "command_cancelled": "Esecuzione del comando annullata dall'utente.",
        "executing": "Esecuzione: {command}",
        "execution_success": "Comando eseguito con successo.",
        "execution_failed": "Esecuzione del comando fallita:",
        "execution_error": "Errore durante l'esecuzione del comando:",
        "usage_message": "Uso: python main.py \"la tua istruzione in linguaggio naturale\"",
        "config_usage": "Uso: python main.py -config <get|set|list> [chiave] [valore]",
        "invalid_action": "Azione non valida. Usa get, set o list.",
        "specify_key": "Specifica la chiave.",
        "invalid_config_key": "Chiave di configurazione non valida. Chiavi valide: {keys}",
        "no_value_set": "Nessun valore impostato per '{key}'",
        "specify_value": "Specifica un valore da impostare.",
        "invalid_value": "Valore non valido per {key}. Valori validi: {values}",
        "config_set": "Configurazione '{key}' impostata a '{value}'",
        "current_configs": "Configurazioni attuali:"
    },
    "pt": {
        "system_prompt": "Você é um especialista em shell. Converta a solicitação do usuário em um comando {shell} válido. Retorne apenas o comando. Sem explicações.",
        "current_directory": "O usuário está atualmente em: {current_path}.",
        "files_context": "Arquivos no diretório atual: {files}",
        "folders_context": "Pastas no diretório atual: {folders}",
        "relative_paths": "Se relevante, prefira caminhos relativos em sua resposta.",
        # UI Messages
        "processing": "Processando sua solicitação",
        "suggested_command": "Comando sugerido:",
        "execute_prompt": "Você quer executar este comando? (s/N): ",
        "command_not_executed": "O comando não foi executado.",
        "command_cancelled": "Execução do comando cancelada pelo usuário.",
        "executing": "Executando: {command}",
        "execution_success": "Comando executado com sucesso.",
        "execution_failed": "Falha na execução do comando:",
        "execution_error": "Erro ao executar o comando:",
        "usage_message": "Uso: python main.py \"sua instrução em linguagem natural\"",
        "config_usage": "Uso: python main.py -config <get|set|list> [chave] [valor]",
        "invalid_action": "Ação inválida. Use get, set ou list.",
        "specify_key": "Por favor especifique a chave.",
        "invalid_config_key": "Chave de configuração inválida. Chaves válidas: {keys}",
        "no_value_set": "Nenhum valor definido para '{key}'",
        "specify_value": "Por favor especifique um valor para definir.",
        "invalid_value": "Valor inválido para {key}. Valores válidos: {values}",
        "config_set": "Configuração '{key}' definida para '{value}'",
        "current_configs": "Configurações atuais:"
    },
    "ru": {
        "system_prompt": "Вы эксперт по командной строке. Преобразуйте запрос пользователя в действительную команду {shell}. Верните только команду. Без объяснений.",
        "current_directory": "Пользователь находится в: {current_path}.",
        "files_context": "Файлы в текущей директории: {files}",
        "folders_context": "Папки в текущей директории: {folders}",
        "relative_paths": "Если уместно, предпочитайте относительные пути в ответе.",
        # UI Messages
        "processing": "Обработка вашего запроса",
        "suggested_command": "Предлагаемая команда:",
        "execute_prompt": "Хотите выполнить эту команду? (д/Н): ",
        "command_not_executed": "Команда не была выполнена.",
        "command_cancelled": "Выполнение команды отменено пользователем.",
        "executing": "Выполнение: {command}",
        "execution_success": "Команда выполнена успешно.",
        "execution_failed": "Ошибка выполнения команды:",
        "execution_error": "Ошибка при выполнении команды:",
        "usage_message": "Использование: python main.py \"ваша инструкция на естественном языке\"",
        "config_usage": "Использование: python main.py -config <get|set|list> [ключ] [значение]",
        "invalid_action": "Неверное действие. Используйте get, set или list.",
        "specify_key": "Пожалуйста, укажите ключ.",
        "invalid_config_key": "Неверный ключ конфигурации. Допустимые ключи: {keys}",
        "no_value_set": "Значение для '{key}' не установлено",
        "specify_value": "Пожалуйста, укажите значение для установки.",
        "invalid_value": "Неверное значение для {key}. Допустимые значения: {values}",
        "config_set": "Конфигурация '{key}' установлена в '{value}'",
        "current_configs": "Текущие конфигурации:"
    },
    "zh": {
        "system_prompt": "您是一个shell专家。将用户的请求转换为有效的{shell}命令。只返回命令，不要解释。",
        "current_directory": "用户当前位于：{current_path}。",
        "files_context": "当前目录中的文件：{files}",
        "folders_context": "当前目录中的文件夹：{folders}",
        "relative_paths": "如果相关，请在输出中优先使用相对路径。",
        # UI Messages
        "processing": "正在处理您的请求",
        "suggested_command": "建议的命令：",
        "execute_prompt": "您要执行此命令吗？(y/N)：",
        "command_not_executed": "命令未执行。",
        "command_cancelled": "用户取消了命令执行。",
        "executing": "正在执行：{command}",
        "execution_success": "命令执行成功。",
        "execution_failed": "命令执行失败：",
        "execution_error": "执行命令时出错：",
        "usage_message": "用法：python main.py \"您的自然语言指令\"",
        "config_usage": "用法：python main.py -config <get|set|list> [键] [值]",
        "invalid_action": "无效操作。请使用 get、set 或 list。",
        "specify_key": "请指定键。",
        "invalid_config_key": "无效的配置键。有效键：{keys}",
        "no_value_set": "'{key}' 未设置值",
        "specify_value": "请指定要设置的值。",
        "invalid_value": "{key} 的值无效。有效值：{values}",
        "config_set": "配置 '{key}' 已设置为 '{value}'",
        "current_configs": "当前配置："
    },
    "ja": {
        "system_prompt": "あなたはシェルの専門家です。ユーザーのリクエストを有効な{shell}コマンドに変換してください。コマンドのみを返してください。説明は不要です。",
        "current_directory": "ユーザーは現在次の場所にいます：{current_path}。",
        "files_context": "現在のディレクトリのファイル：{files}",
        "folders_context": "現在のディレクトリのフォルダ：{folders}",
        "relative_paths": "関連する場合は、出力で相対パスを優先してください。",
        # UI Messages
        "processing": "リクエストを処理中",
        "suggested_command": "提案されたコマンド：",
        "execute_prompt": "このコマンドを実行しますか？(y/N)：",
        "command_not_executed": "コマンドは実行されませんでした。",
        "command_cancelled": "ユーザーがコマンド実行をキャンセルしました。",
        "executing": "実行中：{command}",
        "execution_success": "コマンドが正常に実行されました。",
        "execution_failed": "コマンドの実行に失敗しました：",
        "execution_error": "コマンド実行時にエラーが発生しました：",
        "usage_message": "使用法：python main.py \"自然言語での指示\"",
        "config_usage": "使用法：python main.py -config <get|set|list> [キー] [値]",
        "invalid_action": "無効なアクション。get、set、または list を使用してください。",
        "specify_key": "キーを指定してください。",
        "invalid_config_key": "無効な設定キー。有効なキー：{keys}",
        "no_value_set": "'{key}' に値が設定されていません",
        "specify_value": "設定する値を指定してください。",
        "invalid_value": "{key} の値が無効です。有効な値：{values}",
        "config_set": "設定 '{key}' を '{value}' に設定しました",
        "current_configs": "現在の設定："
    },
    "ar": {
        "system_prompt": "أنت خبير في سطر الأوامر. قم بتحويل طلب المستخدم إلى أمر {shell} صالح. أرجع الأمر فقط. بدون شرح.",
        "current_directory": "المستخدم حالياً في: {current_path}.",
        "files_context": "الملفات في المجلد الحالي: {files}",
        "folders_context": "المجلدات في المجلد الحالي: {folders}",
        "relative_paths": "إذا كان ذا صلة، فضل المسارات النسبية في إجابتك.",
        # UI Messages
        "processing": "معالجة طلبك",
        "suggested_command": "الأمر المقترح:",
        "execute_prompt": "هل تريد تنفيذ هذا الأمر؟ (ن/ل): ",
        "command_not_executed": "لم يتم تنفيذ الأمر.",
        "command_cancelled": "تم إلغاء تنفيذ الأمر من قبل المستخدم.",
        "executing": "تنفيذ: {command}",
        "execution_success": "تم تنفيذ الأمر بنجاح.",
        "execution_failed": "فشل في تنفيذ الأمر:",
        "execution_error": "خطأ أثناء تنفيذ الأمر:",
        "usage_message": "الاستخدام: python main.py \"تعليماتك باللغة الطبيعية\"",
        "config_usage": "الاستخدام: python main.py -config <get|set|list> [مفتاح] [قيمة]",
        "invalid_action": "إجراء غير صالح. استخدم get أو set أو list.",
        "specify_key": "يرجى تحديد المفتاح.",
        "invalid_config_key": "مفتاح تكوين غير صالح. المفاتيح الصالحة: {keys}",
        "no_value_set": "لا توجد قيمة محددة لـ '{key}'",
        "specify_value": "يرجى تحديد قيمة للتعيين.",
        "invalid_value": "قيمة غير صالحة لـ {key}. القيم الصالحة: {values}",
        "config_set": "تم تعيين التكوين '{key}' إلى '{value}'",
        "current_configs": "التكوينات الحالية:"
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

def get_ui_message(message_key: str, language: str = None, **kwargs) -> str:
    """
    Get a UI message in the specified language.
    
    Args:
        message_key: The key of the message to retrieve
        language: Language code (if None, will get from config)
        **kwargs: Format arguments for the message
        
    Returns:
        The message text in the specified language
    """
    if language is None:
        from assistant.db.services import get_config
        language = get_config("default_language") or "en"
    
    message = get_language_prompt(language, message_key)
    if kwargs:
        try:
            return message.format(**kwargs)
        except KeyError:
            # If formatting fails, return the message as-is
            return message
    return message
