import click
import re
import sqlite3
from flask import current_app, g


def get_version(db):
    """! Returns the current version of the database
    @param db: An active database connection
    """
    with current_app.open_resource('database/schema/get_version.sql') as f:
        version = db.execute(f.read().decode('utf8')).fetchone()

        if version is None:
            return '0000-00-00.0'
        return version['last_version']


def print_script_info(script):
    """! Walks through the text of a script, and prints out the line that begins
         with -- INFO:
    """
    lines = script.split("\n")
    for line in lines:
        if line.startswith('-- INFO:'):
            click.echo(re.sub(r'^' + re.escape('-- INFO: '), '', line))


def run_sql(db, name):
    """! Runs an sql script on the given database connection.
    @param db: An active database connection
    @param name: Name of the script to run.
    """
    with current_app.open_resource(name) as f:
        script = f.read().decode('utf8')
        print_script_info(script)
        db.executescript(script)


def set_version(db, version_string):
    """! Sets the current version of the database.
    @param db: An active database connection
    @param version_string: The version to set. Must be in format yyyy-mm-dd.n
    """
    with current_app.open_resource('database/schema/set_version.sql') as f:
        db.execute(f.read().decode('utf8').format(last_version=version_string))
