import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from App.core.backup_manager import BackupManager
from App.core.config import ConfigManager

class BackupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Backup Tool")
        self.root.geometry("500x350")
        self.manager = BackupManager()
        self.config = ConfigManager()

        self.source_path = tk.StringVar(value=self.config.get("default_source"))
        self.dest_path = tk.StringVar(value=self.config.get("default_destination"))
        self.version_tag = tk.StringVar(value=self.config.get("last_version_tag"))
        self.use_zip = tk.BooleanVar(value=self.config.get("use_zip"))

        self.build_ui()

    def build_ui(self):
        padding = {'padx': 10, 'pady': 10}

        tk.Label(self.root, text="Source Folder").grid(row=0, column=0, sticky="w", **padding)
        tk.Entry(self.root, textvariable=self.source_path, width=50).grid(row=0, column=1, **padding)
        tk.Button(self.root, text="Browse", command=self.select_source).grid(row=0, column=2, **padding)

        tk.Label(self.root, text="Destination Folder").grid(row=1, column=0, sticky="w", **padding)
        tk.Entry(self.root, textvariable=self.dest_path, width=50).grid(row=1, column=1, **padding)
        tk.Button(self.root, text="Browse", command=self.select_dest).grid(row=1, column=2, **padding)

        tk.Label(self.root, text="Version Tag").grid(row=2, column=0, sticky="w", **padding)
        tk.Entry(self.root, textvariable=self.version_tag).grid(row=2, column=1, **padding)

        tk.Checkbutton(self.root, text="ZIP Backup", variable=self.use_zip).grid(row=3, column=1, sticky="w", **padding)

        tk.Button(self.root, text="Start Backup", command=self.start_backup, bg="#4caf50", fg="white", width=20)\
            .grid(row=4, column=1, pady=30)

    def select_source(self):
        path = filedialog.askdirectory()
        if path:
            self.source_path.set(path)

    def select_dest(self):
        path = filedialog.askdirectory()
        if path:
            self.dest_path.set(path)

    def start_backup(self):
        src = self.source_path.get().strip()
        dst = self.dest_path.get().strip()
        tag = self.version_tag.get().strip() or "v1.0.0"
        zip_mode = self.use_zip.get()

        success = self.manager.backup_folder(src, dst, tag, zip_mode)

        self.config.set("default_source", src)
        self.config.set("default_destination", dst)
        self.config.set("last_version_tag", tag)
        self.config.set("use_zip", zip_mode)

        if success:
            messagebox.showinfo("Backup Successful", "Backup completed successfully!")
        else:
            messagebox.showerror("Backup Failed", "Check the logs for details.")

