
import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('index.html')


# @app.route('/contact')
# def contact_page():
#     return flask.render_template('contact.html')


@app.route('/contact', methods=['POST', 'GET'])
def form_submitted():
    if flask.request.method == 'POST':
        data = flask.request.form
        print(data["name"])
        print(data["email"])
        print(data["number"])
        print(data["message"])
        return "<h1>Successfully sent your message</h1>"
    return flask.render_template("contact.html")



@app.route('/login', methods=['POST'])
def receive_form_data():
    username = flask.request.form['username']
    password = flask.request.form['password']
    return f"{username}  {password}"




if __name__ == '__main__':
    app.run(debug=True)

