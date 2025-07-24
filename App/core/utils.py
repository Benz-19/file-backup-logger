import os

def is_valid_folder(path: str) -> bool:
    return os.path.isdir(path)
