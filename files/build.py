import os
from flask import Flask
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)


def create_if_not_exists(folder_path: str) -> None:
    """Creates a folder at the given path only when it does not exist"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)


def configure_template_environment(template_folder):
    template_loader = FileSystemLoader(template_folder)
    template_env = Environment(loader=template_loader)
    template_env.trim_blocks = True  # Add this line to remove unnecessary whitespace
    app.jinja_env = template_env


def render_template(template_file):
    try:
        template = app.jinja_env.get_template(template_file)
        rendered_content = template.render()
        return rendered_content
    except Exception as e:
        print(f"Failed to render template '{template_file}': {e}")
        return None


def render_templates(input_folder, output_folder):
    configure_template_environment(input_folder)

    for root, dirs, files in os.walk(input_folder):
        # Render pages in the current directory
        for file in files:
            if file == 'index.jinja':
                template_file = os.path.relpath(
                    os.path.join(root, file), input_folder)
                print(f"Rendering template: {template_file}")
                rendered_content = render_template(template_file)
                if rendered_content:
                    output_path = os.path.join(
                        output_folder, template_file.replace('.jinja', '.html'))
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    with open(output_path, 'w') as f:
                        f.write(rendered_content)
                    print(
                        f"Template '{template_file}' rendered and saved to '{output_path}'")

        # Move HTML files to output folder while preserving directory structure
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            output_dir = os.path.join(
                output_folder, os.path.relpath(dir_path, input_folder))
            create_if_not_exists(output_dir)
            for file in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file)
                if file.endswith('.html'):
                    output_file = os.path.join(output_dir, file)
                    os.rename(file_path, output_file)
                    print(f"Moved file '{file_path}' to '{output_file}'")


if __name__ == '__main__':
    input_folder = 'files/templates'
    output_folder = 'output'
    render_templates(input_folder, output_folder)
