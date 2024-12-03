#config_parser.py       # Config parsing logic 

import yaml
import os

class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)

    def get_value(self, key_path, default=None):
        """
        Retrieve nested keys from the YAML file using dot notation.
        """
        keys = key_path.split('.')
        value = self.config
        for key in keys:
            if key in value:
                value = value[key]
            else:
                return default
        return value
