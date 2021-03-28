# Imports
import os

from flask import (Flask, g, request)
from flask_babel import Babel
from .database import db
from .blueprints import (auth, main)


# Functions
def create_app(test_config=None):
    """! Creates a new instance of the godparent app.

    @param test_config The configuration data for testing the app.

    @return The application instance
    """

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='debug',
                            DATABASE=os.path.join(app.instance_path,
                                                  'godparent.db'))
    babel = Babel(app)

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

    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    app.add_url_rule('/', endpoint='index')

    return app

    @babel.localeselector
    def get_locale():
        """! Chooses the locale to set for a user
        @return The selected locale
        """
        # if a user is logged in, use the locale from the user settings.
        user = getattr(g, 'user', None)
        if user is not None:
            return user.locale
        # otherwise try to guess the language from the user accept
        # header the browser transmits.
        return request.accept_languages.best_match(['de', 'en'])

    @babel.timezoneselector
    def get_timezone():
        """! Chooses the time zone based on the user's settings.
        @return The selected timezone.
        """
        user = getattr(g, 'user', None)
        if (user is not None):
            return user.timezone

        return None
