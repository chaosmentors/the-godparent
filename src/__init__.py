# Imports
import os

from flask import Flask
from .database import db
from .blueprints import auth

# Functions
def create_app(test_config=None):
    """! Creates a new instance of the godparent app.

    @param test_config The configuration data for testing the app.

    @return The application instance
    """

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='debug',
            DATABASE=os.path.join(app.instance_path, 'godparent.db')
    )

    if test_config is None:
        # load the instance config, if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config, if passed in
        app.config.from_pyfile(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello, change this later
    @app.route('/hello')
    def hello():
        return 'Hello, World'

    db.init_app(app)
    app.register_blueprint(auth.bp)

    return app
