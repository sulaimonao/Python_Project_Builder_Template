# scaffold.py            # Directory creation utilities

import os

def scaffold_project_structure(base_path, structure, config):
    """
    Dynamically create directories and files based on the configuration.
    """
    for directory in structure.get("root_directories", []):
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
    
    for config_file in structure.get("config_files", []):
        file_path = os.path.join(base_path, config_file)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                # Insert placeholders or configurations dynamically
                content = f"# {config.get_value('project.name', 'Project')}\n"
                file.write(content)
