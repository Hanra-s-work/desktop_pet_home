from flask import Flask, render_template
import os
import sys

app = Flask(__name__)


def create_paths_if_not_exist(path: str = f"{os.getcwd()}/output") -> None:
    """ Create the output path if it does not exist """
    if os.path.exists(path) == False:
        os.makedirs(path, exist_ok=True)


if __name__ == '__main__':
    output_folder = "output"
    if len(sys.argv) > 1:
        output_folder = sys.argv[1]
    print(f"cwd = {os.getcwd()}")
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    with app.app_context():
        rendered_content = render_template('index.jinja')
        src_path = os.path.join(os.getcwd(), output_folder)
        create_paths_if_not_exist(src_path)
        # Save the rendered content to an HTML file
        output_file = os.path.join(src_path, 'index.html')
        print(f"output_file = {output_file}")
        sys.stdout.flush()
        with open(output_file, 'w', encoding="utf-8") as file:
            file.write(rendered_content)
    print(f"os.listdir = {os.listdir()}")
