import sqlite3
import click
import re
from flask import current_app, g
from flask.cli import with_appcontext

from . import maintenance


def close_db(e=None):
    """! Closes an existing database connection, if it's open.
    """
    db = g.pop('db', None)

    if (db is not None):
        db.close()


def get_db():
    """! Returns an instance of the current database connection or 
         opens a new one.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'],
                               detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row

    return g.db


def init_db():
    """! Initialize the database, when the flask init command is called.
    """
    db = get_db()

    # initialize the database
    maintenance.run_sql(db, 'database/schema/init.sql')


@click.command('init-db')
@with_appcontext
def init_db_command():
    """! Update or create the database and new tables.
    """
    init_db()
    click.echo('Finished initialzing the database')


def init_app(app):
    """! Registers the database command with the app
    @param app: The application
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
