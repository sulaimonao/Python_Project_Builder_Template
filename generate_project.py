import os
import subprocess
import json

# Function to prompt user for personal information
def get_user_info():
    """
    Prompts the user for personal information.

    Returns:
        dict: A dictionary containing user information.
    """
    print("Please provide the following information:")
    user_info = {
        "author_name": input("Author Name: "),
        "author_email": input("Author Email: "),
        "github_username": input("GitHub Username: ")
    }
    return user_info

# Function to load JSON data
def load_json(file_path):
    """
    Loads JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: The JSON data.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to replace placeholders in file contents
def replace_placeholders(content, user_info):
    """
    Replaces placeholders in the content with user information.

    Args:
        content (str): The content with placeholders.
        user_info (dict): The user information.

    Returns:
        str: The content with placeholders replaced.
    """
    for key, value in user_info.items():
        content = content.replace('{' + key + '}', value)
    return content

# Function to create directories and files
def create_project_structure(project_name, structure, contents, user_info):
    """
    Creates directories and files based on the provided structure and contents.

    Args:
        project_name (str): The name of the project.
        structure (dict): The project structure.
        contents (dict): The file contents.
        user_info (dict): The user information.
    """
    base_path = os.path.abspath(project_name)
    for folder, items in structure.items():
        # Determine the correct path for the folder
        folder_path = os.path.join(base_path, folder) if folder != '.' else base_path
        os.makedirs(folder_path, exist_ok=True)

        for item in items:
            item_path = os.path.join(folder_path, item)
            if '.' in item:  # If item has an extension, it's a file
                # Get content for the file, if any
                content_key = os.path.join(folder, item) if folder != '.' else item
                content = contents.get(content_key, "")
                content = replace_placeholders(content, user_info)
                with open(item_path, 'w') as f:
                    f.write(content)
            else:
                # It's a directory (ensure it's created even if empty)
                os.makedirs(item_path, exist_ok=True)

    print(f"Project '{project_name}' structure created at {base_path}")

# Function to initialize virtual environment
def initialize_virtualenv(project_name):
    """
    Initializes a Python virtual environment in the project directory.

    Args:
        project_name (str): The name of the project.
    """
    base_path = os.path.abspath(project_name)
    venv_path = os.path.join(base_path, 'venv')
    subprocess.run(["python3", "-m", "venv", venv_path])
    print("Virtual environment created. Activate it with `source venv/bin/activate`.")

# Function to install dependencies
def install_dependencies(project_name):
    """
    Installs dependencies listed in the requirements.txt file.

    Args:
        project_name (str): The name of the project.
    """
    base_path = os.path.abspath(project_name)
    venv_pip = os.path.join(base_path, "venv/bin/pip")
    requirements_file = os.path.join(base_path, "requirements.txt")
    if os.path.exists(requirements_file):
        subprocess.run([venv_pip, "install", "-r", requirements_file])
        print("Dependencies installed.")
    else:
        print("No requirements.txt file found. Skipping dependency installation.")

# Main function
def main():
    # Load project structure and file contents from JSON files
    project_structure_data = load_json('project_structure.json')
    file_contents = load_json('file_contents.json')

    project_name = project_structure_data['project_name']
    project_structure = project_structure_data['structure']

    # Get user information
    user_info = get_user_info()

    # Create the project structure
    create_project_structure(project_name, project_structure, file_contents, user_info)

    # Initialize virtual environment (optional)
    initialize_virtualenv(project_name)

    # Install dependencies (optional)
    install_dependencies(project_name)

    print("Project setup complete!")

if __name__ == "__main__":
    main()
