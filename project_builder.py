project_builder.py         # Main entry point for the builder

import os
from utils.config_parser import load_config
from utils.scaffold import create_directories
from utils.render import render_template

def main():
    # Load configuration
    config = load_config('configs/default_config.yaml')

    # Define the output directory
    output_dir = config['output_directory']
    os.makedirs(output_dir, exist_ok=True)

    # Create project structure
    structure = {
        "src": {
            "main": {"java": {}, "res": {"layout": {}, "values": {}}},
            "test": {}
        },
        "build": {},
        "gradle": {}
    }
    create_directories(output_dir, structure)

    # Render templates
    template_dir = os.path.join("templates", config['platform'])
    render_template(
        template_dir=template_dir,
        template_name="MainActivity.kt.jinja2",
        context={"project_name": config['project_name']},
        output_file=os.path.join(output_dir, "src/main/java/MainActivity.kt")
    )

if __name__ == "__main__":
    main()

