from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create a Flask Instance
app = Flask(__name__)

# Add Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# # SECRET KEY! 
# app.config['SECRET_KEY'] = 'secret key'

# # Initialize the Database
# db = SQLAlchemy(app)

# # Create a Model
# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#     email = db.Column(db.String(200), nullable=False, unique=True)
#     date_added = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return "<Name %r>" % self.name

# JINGA FILTERS: https://tedboy.github.io/jinja2/templ14.html
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags

# HOW TO USE:
# In rendered html templates {{first_name|capitalize}}

# {{ }} - double curly brackets used to print something
# {% for _____ %} {% endfor %} - curly with percent used for logic, make sure you end logic 
# thelist=[hi,lmao,lol] to index list in JINGA use {{thelist.0}} = hi

# Create a route decorator
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name = name)

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(debug=True)