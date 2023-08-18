"""
The Godparent
A simple planning tool for the chaos mentor
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return '<h1>Hello, World</h1>'


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
