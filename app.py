from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'flask'


@app.route('/<name>')
def index_n(name):
    return 'hello {}'.format(name)


if __name__ == '__main__':
    app.run()