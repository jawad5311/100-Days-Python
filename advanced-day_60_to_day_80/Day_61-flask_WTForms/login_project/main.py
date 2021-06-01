import flask
import wtforms
from flask import Flask, render_template
from wtforms import Form, BooleanField, StringField, validators, PasswordField


class LoginForm(Form):
    email = StringField(
        'Email Address',
        [
         validators.Length(min=6, max=35)]
    )
    password = PasswordField(
        'Password',
        [validators.Length(min=8, max=25),
         validators.DataRequired()]
    )
    accept_rules = BooleanField(
        'I accept the site rules',
        [validators.InputRequired()]
    )
    submit_btn = wtforms.SubmitField('Login')

    # check = email.gettext()


app = Flask(__name__)
app.secret_key = 'this_is_secret'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if flask.request.method == 'POST':
        print("form validated")
        if login_form.email.data == "admin@admin.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)