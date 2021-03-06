import sqlite3
import click

from flask import current_app, g
from flask.cli import with_appcontext
from . import embeddedsql


def close_db(e=None):
    """! Closes the database when disposing
    @param e Event details
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()


def get_db():
    """! Receive a connection to the database

    @return The database connection
    """
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'],
                               detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row

    return g.db


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def init_db():
    """! Initializes the database on first run
    """
    db = get_db()

    db.executescript(embeddedsql.Reader().schema)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """ Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database')
