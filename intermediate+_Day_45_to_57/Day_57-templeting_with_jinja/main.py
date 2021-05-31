from flask import Flask, render_template
import datetime
import requests


app = Flask(__name__)


@app.route('/')
def home():
    time = datetime.date.today().year
    return render_template('index.html', year=time)


@app.route('/guess/<name>')
def get_name_data(name):
    """
        Takes user name and provides age and gender.
    :param name: Username
    :return: Gender (male / female), Age
    """
    def get_gender(user_name):
        """ Get user gender using API """
        url = f"https://api.genderize.io?name={user_name}"
        response = requests.get(url)
        gender = response.json()['gender']
        return gender  # Return user gender

    def get_age(user_name):
        """ Get user age using agify API """
        url = f"https://api.agify.io?name={user_name}"
        response = requests.get(url)
        age = str(response.json()['age'])
        return age  # Return user age

    # Calling the functions to get user age and gender
    user_gender = get_gender(name)
    user_age = get_age(name)
    # Creates a template to be displayed on screen
    template_text = f"<h1>Hey {name},</h1>" \
                    f"<h2>I think you are {user_gender},</h2>\n" \
                    f"<h3>And maybe {user_age} years old.</h3>"

    return template_text


if __name__ == "__main__":
    app.run(debug=True)


