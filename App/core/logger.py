import os
from datetime import datetime

class BackupLogger:
    def __init__(self, log_dir="logs", log_file="backup.log"):
        self.log_path = os.path.join(log_dir, log_file)
        os.makedirs(log_dir, exist_ok=True)

    def log(self, message: str):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log_entry = f"{timestamp} {message}"
        print(log_entry)  # Optional: Print to console
        with open(self.log_path, "a") as f:
            f.write(log_entry + "\n")
