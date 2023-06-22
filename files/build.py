from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.jinja')


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    with app.app_context():
        rendered_content = render_template('index.jinja')
        # Save the rendered_content to the appropriate location
        # Or perform other necessary actions with the generated content
