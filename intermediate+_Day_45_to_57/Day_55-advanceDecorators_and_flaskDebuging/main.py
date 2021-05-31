
import flask

app = flask.Flask(__name__)


def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper


def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper


def make_underline(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper


@app.route('/')
@make_bold
@make_emphasis
@make_underline
def hello_world():
    return 'Hello, World'


@app.route('/user/<name>')
def greet(name):
    return f"Hello {name}"




if __name__ == '__main__':
    app.run(debug=True)