from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
# THIS HAS BEEN EDITED
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mandy@localhost/sc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jwmkkkpinyezpa:82620c65d6883e2025f58162fe0cbd2c6b8f2e1ac9c56627a4cf807a0df18b6a@ec2-54-75-184-144.eu-west-1.compute.amazonaws.com:5432/d8up2dhh9dgqg8'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'hi'

db = SQLAlchemy(app)

db.create_all()

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80), unique=True, nullable=False)
    color = db.Column(db.String(120), nullable=False)

    def __init__(self, pname, color):
        self.pname = pname
        self.color = color


@app.route('/')
def home():
    return '<a href="/addperson"><button> Click here </button></a>'


@app.route("/addperson")
def addperson():
    return render_template("index.html")


@app.route("/personadd", methods=['POST'])
def personadd():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = People(pname, color)
    db.session.add(entry)
    db.session.commit()

    return render_template("index.html")


if __name__ == '__main__':
    # with app.app_context():
    # db.create_all()
    app.run(debug=True)