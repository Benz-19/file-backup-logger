# File Backup Logger

A Python program to back up files and folders with versioning, logging, compression (ZIP), and a user-friendly GUI. Built using OOP principles, it supports config persistence and logs all operations locally.

## Features

- Back up folders as plain copies or zipped archives
- Add timestamps and version tags to backups
- Built-in GUI with folder pickers and options
- Logging of all actions with status, duration, and file counts
- Save preferences in a JSON config file
- Clean OOP-based structure for easy maintenance and scaling
- CLI mode support for terminal-based usage

## Screenshots
- Interface 1
  - ![App_1](https://raw.githubusercontent.com/Benz-19/file-backup-logger/main/screenshots/Screenshot_1.png)

- Interface 2
  - ![App_2](https://raw.githubusercontent.com/Benz-19/file-backup-logger/main/screenshots/Screenshot_2.png)


## Getting Started

Clone or download this repository:

```bash
git clone https://github.com/benz-19/file-backup-logger.git
cd file-backup-logger
```
**file-backup-logger** is a Python-based application designed to back up files and directories with version control, ZIP compression support, logging, a graphical user interface (GUI), and persistent user preferences. The program is written using Object-Oriented Programming principles.

## Features

* Backup folders as plain copies or zipped archives
* Add timestamps and custom version tags to backup names
* Simple GUI built with tkinter for easy interaction
* Detailed log file with backup status, duration, and file count
* Saves preferences (paths, ZIP option, version) in a JSON config file
* CLI mode for terminal users
* OOP-based structure for clean, scalable development

## Getting Started

### Clone or Download

```bash
git clone https://github.com/benz-19/file-backup-logger.git
cd file-backup-logger
```

### Run the App

**With CLI:**

```bash
python main.py --cli
```

## Requirements

No external libraries are required. The project uses only Python standard libraries:

* `os`
* `shutil`
* `zipfile`
* `datetime`
* `json`
* `tkinter`

Works on any system running Python 3.x with Tkinter installed.

## Project Structure

```
backup_app/
├── App/
│   ├── core/
│   │   ├── backup_manager.py       # Handles core backup logic
│   │   ├── config.py              # Manages config persistence
│   │   ├── logger.py
│   │   └── utils.py
│   └── gui/
│       └── main_window.py         # Tkinter-based GUI interface
├── config/
│   └── user_config.json           # Stores last used paths and settings
├── logs/
│   └── backup.log                 # Backup logs
├── backups/
├── main.py                        # Default entry point
├── requirements.txt
└── README.md
```

## Example Log Entry

```
[2025-07-24 14:42:35] SUCCESS: Backed up 'C:/Users/Host_System/Folder/file-backup-logger/test' to 'backups\test_2025-07-24_14-42-35_v1.0.0.zip' (1 files, 0.01 seconds)
```

## Future Improvements

* Scheduled automatic backups
* System tray minimization
* File type filtering and exclusion rules

## License

This project is licensed under the MIT License. Feel free to use and modify.

---

\*\*Made by Kingsley

````
    git clone https://github.com/benz-19/file-backup-logger.git cd backup-tool
````
