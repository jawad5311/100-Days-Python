import wtforms
from flask import Flask, render_template
from wtforms import Form, BooleanField, StringField, validators, PasswordField


class LoginForm(Form):
    email = StringField(
        'Email Address',
        [validators.Length(min=6, max=35),
         validators.DataRequired(),
         validators.Email()]
    )
    password = PasswordField(
        'password',
        [validators.Length(min=4, max=25),
         validators.DataRequired()]
    )
    accept_rules = BooleanField(
        'I accept the site rules',
        [validators.InputRequired()]
    )
    submit_btn = wtforms.SubmitField('Login')


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template("login.html", form=LoginForm())


if __name__ == '__main__':
    app.run(debug=True)