# -*- coding: utf-8 -*-
""" A web application for maintaining chaos mentors

This web application allows registration as well as maintenance for
participants of the chaos mentors program.
"""

import os

from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth.login'

# The following imports need to access the above global variables,
# and are thus postponed to here. This is, I kid you not, the official
# solution flask uses to allow blueprints and SQLAlchemy at the
# same time
from app.blueprints import index, auth, profile
from app.models import users
from app.models import posts

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

app.register_blueprint(index.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(profile.bp)
app.add_url_rule('/', endpoint='index')
