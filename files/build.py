from flask import Flask, render_template
import os
print(f"os.listdir = {os.listdir()}")
print(f"cwd = {os.getcwd()}")

app = Flask(__name__)

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    with app.app_context():
        rendered_content = render_template('index.jinja')

        # Save the rendered content to an HTML file
        output_file = os.path.join(os.getcwd(), 'index.html')
        with open(output_file, 'w', encoding="utf-8") as file:
            file.write(rendered_content)
