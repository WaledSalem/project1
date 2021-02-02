from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def hello_internet():
    return "Hello Internet!"


@app.route('/home')
def home():
    return 'This is the home page'


@app.route('/about')
def about():
    return 'This is the about page'


if __name__ == '__main__':
    app.run(debug=True)
