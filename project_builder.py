#project_builder.py         # Main entry point for the builder

import os
from utils.config_parser import ConfigLoader
from utils.scaffold import scaffold_project_structure
from utils.render import render_template
from utils.placeholder_manager import PlaceholderManager

def main():
    # Load the configuration
    config = ConfigLoader('configs/default_config.yaml')

    # Initialize Placeholder Manager
    placeholder_manager = PlaceholderManager(config)

    # Create the project structure
    structure = config.get_value("structure", {})
    base_path = config.get_value("output_directory", "./output")
    scaffold_project_structure(base_path, structure, config)

    # Render templates
    context = {
        "project_name": config.get_value("project.name"),
        "author_name": config.get_value("project.author"),
    }
    render_template(
        "templates/backend/python", 
        "app.py.jinja2", 
        context, 
        os.path.join(base_path, "src/app.py")
    )

if __name__ == "__main__":
    main()


