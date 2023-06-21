from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.jinja')


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
