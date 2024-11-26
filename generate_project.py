#generate_project.py

import os
import json

def load_json(file_path):
    """Load a JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def replace_placeholders(content, placeholders):
    """Replace placeholders in content with actual values."""
    for key, value in placeholders.items():
        content = content.replace(f"{{{{ {key} }}}}", value)
    return content

def create_file(file_path, content):
    """Create a file with the given content."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        f.write(content)

def create_project(project_structure, file_contents, placeholders):
    """Create project files and directories based on the structure and contents."""
    for directory, files in project_structure.items():
        for file_name in files:
            file_path = os.path.join(directory.replace("{{ project_name }}", placeholders["project_name"]), file_name)
            content = file_contents.get(file_name, "")
            content = replace_placeholders(content, placeholders)
            create_file(file_path, content)

def extend_project_structure(structure, additional_dirs, additional_files):
    """Dynamically extend the project structure."""
    for dir_name in additional_dirs:
        structure[dir_name] = []

    for file_path, content in additional_files.items():
        dir_name = os.path.dirname(file_path)
        if dir_name not in structure:
            structure[dir_name] = []
        structure[dir_name].append(os.path.basename(file_path))
    
    return structure

def add_optional_modules(file_contents, placeholders, optional_features):
    """Add optional feature snippets to file contents."""
    if optional_features.get("logging"):
        file_contents[f"{placeholders['project_name']}/src/utils.py"] += """

import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)
"""
    if optional_features.get("cli"):
        file_contents[f"{placeholders['project_name']}/src/main.py"] += """

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='{{ project_name }} CLI')
    parser.add_argument('--example', type=str, help='Example argument')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    print(f"Example argument: {args.example}")
"""
    return file_contents

def main():
    print("Welcome to the Enhanced Dynamic Project Generator!")
    
    # Prompt user for project details
    project_name = input("Enter your project name: ").strip()
    author_name = input("Enter your name (author): ").strip()
    author_email = input("Enter your email: ").strip()
    
    # Load structure and content templates
    project_structure = load_json('/mnt/data/updated_project_structure.json')["structure"]
    file_contents = load_json('/mnt/data/updated_file_contents.json')
    
    # Prompt user for optional features
    print("\nOptional Features:")
    add_logging = input("Include logging support? (yes/no): ").strip().lower() == "yes"
    add_cli = input("Include CLI setup? (yes/no): ").strip().lower() == "yes"
    optional_features = {
        "logging": add_logging,
        "cli": add_cli
    }
    
    # Prompt user for additional directories and files
    print("\nWould you like to add custom directories or files?")
    additional_dirs = []
    additional_files = {}
    if input("Add custom directories? (yes/no): ").strip().lower() == "yes":
        while True:
            dir_name = input("Enter directory name (or press Enter to stop): ").strip()
            if not dir_name:
                break
            additional_dirs.append(dir_name)
    
    if input("Add custom files? (yes/no): ").strip().lower() == "yes":
        while True:
            file_path = input("Enter file path (or press Enter to stop): ").strip()
            if not file_path:
                break
            content = input(f"Enter content for {file_path} (leave blank for empty file): ")
            additional_files[file_path] = content
    
    # Prepare placeholders
    placeholders = {
        "project_name": project_name,
        "author_name": author_name,
        "author_email": author_email
    }
    
    # Extend structure and add optional modules
    project_structure = extend_project_structure(project_structure, additional_dirs, additional_files)
    file_contents = add_optional_modules(file_contents, placeholders, optional_features)
    
    # Create project files and structure
    create_project(project_structure, file_contents, placeholders)
    
    print(f"\nProject '{project_name}' has been created successfully!")
    print("Customize your new project as needed. Happy coding!")

if __name__ == "__main__":
    main()
