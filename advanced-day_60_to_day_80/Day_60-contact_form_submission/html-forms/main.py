
import smtplib
import os
import dotenv

import flask


dotenv.load_dotenv()  # Loads Environment Variables

# Get email and password from Environment Variables
email_from = os.environ.get('USER_EMAIL')
password = os.environ.get('USER_PASS')
email_to = os.environ.get('TO_EMAIL')

app = flask.Flask(__name__)  # Creates flask app


@app.route('/')  # Route to the home page
def home():
    return flask.render_template('index.html')


@app.route('/contact', methods=['POST', 'GET'])  # Contact Page
def form_submitted():
    """ Form submission check and send mail """
    if flask.request.method == 'POST':
        data = flask.request.form
        send_email(data["name"], data["email"], data["number"], data["message"])
        return "<h1>Successfully sent your message</h1>"
    return flask.render_template("contact.html")


@app.route('/login', methods=['POST'])  # User Login Page
def receive_form_data():
    username = flask.request.form['username']
    password = flask.request.form['password']
    return f"{username}  {password}"


def send_email(name, email, phone, message):
    """ Send email to myself """
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.live.com") as connection:
        connection.starttls()
        connection.login(email_from, password)
        connection.sendmail(email_from, email_to, email_message)


if __name__ == '__main__':
    app.run(debug=True)

