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

def main():
    print("Welcome to the Dynamic Project Generator!")
    
    # Prompt user for project details
    project_name = input("Enter your project name: ").strip()
    author_name = input("Enter your name (author): ").strip()
    author_email = input("Enter your email: ").strip()
    
    # Load structure and content templates
    project_structure = load_json('/mnt/data/updated_project_structure.json')["structure"]
    file_contents = load_json('/mnt/data/updated_file_contents.json')
    
    # Prepare placeholders
    placeholders = {
        "project_name": project_name,
        "author_name": author_name,
        "author_email": author_email
    }
    
    # Create project files and structure
    create_project(project_structure, file_contents, placeholders)
    
    print(f"Project '{project_name}' has been created successfully!")
    print("Customize your new project as needed. Happy coding!")

if __name__ == "__main__":
    main()
