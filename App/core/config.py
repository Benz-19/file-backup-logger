import json
import os

class ConfigManager:
    def __init__(self, config_path="config/user_config.json"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        if not os.path.exists(self.config_path):
            return self._default_config()
        try:
            with open(self.config_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return self._default_config()

    def _default_config(self):
        return {
            "default_source": "",
            "default_destination": "backups",
            "backup_interval_minutes": 0,
            "use_zip": True,
            "last_version_tag": "v1.0.0"
        }

    def save(self):
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=4)

    def get(self, key, fallback=None):
        return self.config.get(key, fallback)

    def set(self, key, value):
        self.config[key] = value
        self.save()
