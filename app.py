from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    alive = db.Column(db.Boolean, default=True)
    date = db.Column(db.DateTime)
    height = db.Column(db.Float)


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
