import sys

def run_cli():
    from App.core.backup_manager import BackupManager

    manager = BackupManager()

    source = input("Enter the source folder path to backup: ").strip()
    destination = input("Enter the destination folder path: ").strip() or "backups"
    version_tag = input("Enter version tag (e.g., v1.2.3): ").strip() or "v1.0.0"
    zip_choice = input("Zip the backup? (yes/no): ").strip().lower() == "yes"

    success = manager.backup_folder(source, destination, version_tag, zip_choice)
    if success:
        print("Backup completed successfully.")
    else:
        print("Backup failed. Check logs for details.")

def run_gui():
    from tkinter import Tk
    from App.gui.main_window import BackupApp

    root = Tk()
    app = BackupApp(root)
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        run_cli()
    else:
        run_gui()
