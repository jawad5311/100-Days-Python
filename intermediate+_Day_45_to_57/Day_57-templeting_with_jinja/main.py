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

    return render_template(
        'index.html',
        username=name,
        gender=user_gender,
        age=user_age
    )


@app.route('/blog')
def blog():
    url = 'https://api.npoint.io/ecc8ddefc7a8ef28a6c1'
    response = requests.get(url).json()
    return render_template('blog.html', posts=response)



if __name__ == "__main__":
    app.run(debug=True)


