from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    time = datetime.date.today().year
    return render_template('index.html', year=time)


if __name__ == "__main__":
    app.run(debug=True)


