# scaffold.py            # Directory creation utilities

import os

def create_directories(base_path, structure):
    """
    Recursively create directories based on a given structure.
    """
    for folder, subfolders in structure.items():
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        if isinstance(subfolders, dict):
            create_directories(path, subfolders)
