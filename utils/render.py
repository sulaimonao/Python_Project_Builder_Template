#render.py              # Template rendering utilities

from jinja2 import Environment, FileSystemLoader
import os

def render_template(template_dir, template_name, context, output_file):
    """
    Render a Jinja2 template with the given context.
    """
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    rendered_content = template.render(context)
    
    with open(output_file, 'w') as file:
        file.write(rendered_content)
