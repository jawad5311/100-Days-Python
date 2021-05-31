
import flask
import random

app = flask.Flask(__name__)


@app.route('/')  # Route to the Home Page
def game_start():
    return "Guess a number between 0 and 9<br>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


# Creates a random number between 0 and 9
random_num = random.randint(0, 9)
print(random_num)


@app.route('/<int:guess>')  # Creates a URL on user input
def user_guess(guess):
    if guess > random_num:
        return f"<h1>{guess} is not the correct answer!<br>" \
               f"<h1>Too High. Go down ⬇️</h1><br>" \
               f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif guess < random_num:
        return f"<h1>{guess} is not the correct answer!<br>" \
               f"Too Low. Go up ⬆️</h1><br>" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return f"<h1>You guessed the number <em>{random_num}</em> right!</h1><br><br>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == '__main__':
    app.run(debug=True)
