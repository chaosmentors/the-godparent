# -*- coding: utf-8 -*-
""" A web application for maintaining chaos mentors

This web application allows registration as well as maintenance for
participants of the chaos mentors program.
"""

import os

from flask import Flask
from .database import db


# functions
def create_app(test_config=None) -> Flask:
    """Returns a Flask application

    Arguments:
    test_config -- The configuration data for testing the app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='debug',
                            DATABASE=os.path.join(app.instance_path,
                                                  'godparent.db'))
    if test_config is None:
        # load the instance config if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config, if passed in
        app.config.from_pyfile(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # for starters, just say hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    db.init_app(app)

    return app
