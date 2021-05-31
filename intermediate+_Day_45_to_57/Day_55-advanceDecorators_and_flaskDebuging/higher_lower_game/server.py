
import flask
import random

app = flask.Flask(__name__)


def make_heading_1(func):
    def wrapper():
        return f"<h1>{func()}</h1>" \
               f"<img src='ahttps://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

    return wrapper


@app.route('/')
@make_heading_1
def game_start():
    return "Guess a number between 0 and 9"







if __name__ == '__main__':
    app.run(debug=True)
