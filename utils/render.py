#render.py              # Template rendering utilities

from jinja2 import Environment, FileSystemLoader
import os

def render_template(template_dir, template_name, context, output_path):
    """
    Render Jinja2 templates with dynamic context values.
    """
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    rendered_content = template.render(context)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as file:
        file.write(rendered_content)
