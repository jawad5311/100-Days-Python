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

    def get_gender(user_name):
        url = f"https://api.genderize.io?name={user_name}"
        response = requests.get(url)
        gender = response.json()['gender']
        return gender

    def get_age(user_name):
        url = f"https://api.agify.io?name={user_name}"
        response = requests.get(url)
        age = str(response.json()['age'])
        return age

    # user_gender = get_gender(name)
    user_age = get_age(name)
    return user_age





if __name__ == "__main__":
    app.run(debug=True)


