import sqlite3
import click

from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    """! Receive a connection to the database

    @return The database connection
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    """! Closes the database when disposing
    @param e Event details 
    """
    db = g.pop('db', None)

    if db is not None: 
        db.close()
