import os

def get_directory_context(path: str, max_files=20, max_dirs=5):
    try:
        all_items = os.listdir(path)
    except Exception:
        return [], []

    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))][:max_files]
    dirs = [item for item in all_items if os.path.isdir(os.path.join(path, item))][:max_dirs]

    return files, dirs
