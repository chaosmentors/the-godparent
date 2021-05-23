"""Configuration parameter for the app."""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Stores the configuration data """

    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        'abe826f5-70a8-4dc0-9dfe-ab8d10c37c85'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, '../instance/godparent.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
