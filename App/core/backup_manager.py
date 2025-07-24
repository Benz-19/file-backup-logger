import os
import shutil
import zipfile
from datetime import datetime
from .logger import BackupLogger
from .config import ConfigManager

class BackupManager:
    def __init__(self):
        self.logger = BackupLogger()
        self.config = ConfigManager()

    def create_backup_name(self, source_folder, version_tag="v1.0.0", zip_mode=False):
        folder_name = os.path.basename(source_folder.rstrip('/\\'))
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        suffix = f"{folder_name}_{timestamp}_{version_tag}"
        if zip_mode:
            return suffix + ".zip"
        return suffix

    def backup_folder(self, source_folder, dest_folder, version_tag="v1.0.0", zip_mode=False):
        if not os.path.exists(source_folder):
            self.logger.log(f"ERROR: Source folder '{source_folder}' does not exist.")
            return False

        os.makedirs(dest_folder, exist_ok=True)
        backup_name = self.create_backup_name(source_folder, version_tag, zip_mode)
        backup_path = os.path.join(dest_folder, backup_name)

        try:
            start_time = datetime.now()
            if zip_mode:
                self._zip_folder(source_folder, backup_path)
            else:
                shutil.copytree(source_folder, backup_path)
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()

            file_count = self._count_files(source_folder)
            self.logger.log(f"SUCCESS: Backed up '{source_folder}' to '{backup_path}' "
                            f"({file_count} files, {duration:.2f} seconds)")
            return True
        except Exception as e:
            self.logger.log(f"ERROR: {e}")
            return False

    def _zip_folder(self, source_folder, output_path):
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(source_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_folder)
                    zipf.write(file_path, arcname)

    def _count_files(self, folder):
        return sum(len(files) for _, _, files in os.walk(folder))
