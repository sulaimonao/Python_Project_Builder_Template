#config_parser.py       # Config parsing logic 

import yaml
import os

def load_config(config_file):
    """
    Load the YAML configuration file.
    """
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file {config_file} not found.")
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

