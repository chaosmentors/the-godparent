"""Performs updates on the database

This module provides the DatabaseUpdater class, that can be used to provide
updates to the database.
"""
import os
import re
import click
from flask import current_app


class DatabaseUpdater:  # pylint: disable=too-few-public-methods
    """Runs an automatic update on the database, when the init command is
       run.
    """
    def __init__(self, db, base_path):
        """Creates a new updater.

        db -- An sqlite3.Connection.
        base_path -- contiains the path where schema update scripts are stored.
        """
        self._db = db
        self._path = base_path

    def __get_update_scripts(self, last_version):
        """Returns a list of file names, that need to be executed.

        This will give a list of all SQL files, that begin with a number that
        matches the pattern <yyyy-ddd-nn*.sql>. Where yyyy is the year, ddd the
        day of the year and nn the version number for that day, starting with
        1.

        last_version -- Version string of the last version that was
                        successfully executed.
        """
        file_list = [
            fn for fn in os.listdir(self._path)
            if re.match(r'\d{4}-\d{3}-\d{2}-.*.sql', fn)
        ]
        return sorted(fn for fn in file_list if fn[0:11] > last_version)

    def __get_version(self):
        """Returns the current version of the database"""
        with current_app.open_resource('database/schema/get_version.sql') as f:
            version = self._db.execute(f.read().decode('utf8')).fetchone()

            if version is None:
                return '0000-00-00.0'
            return version['last_version']

    @staticmethod
    def __print_script_info(script):
        """Walks through the text of a script, and prints out the line that
            begins with -- INFO:
        """
        lines = script.split("\n")
        for line in lines:
            if line.startswith('-- INFO:'):
                click.echo(re.sub(r'^' + re.escape('-- INFO: '), '', line))

    def __run_sql(self, name):
        """Runs an sql script on the given database connection.

        name -- Name of the script to run.
        """
        with current_app.open_resource("{}/{}.sql".format(self._path,
                                                          name)) as f:
            script = f.read().decode('utf8')
            self.__print_script_info(script)
            self._db.executescript(script)

    def __set_version(self, version_string):
        """Sets the current version of the database.

        version_string -- The version to set.
               Must be in format yyyy-mm-dd.n
        """
        with current_app.open_resource("{}/set_version.sql".format(
                self._path)) as f:
            self._db.execute(
                f.read().decode('utf8').format(last_version=version_string))

    def update(self):
        """Checks for new update scripts, and then runs an update on
           the database.
        """
        # First, run the basic initialisation
        self.__run_sql('init')

        # Now get all updateable elements and run them.
        file_list = self.__get_update_scripts(self.__get_version())
        for fn in file_list:
            self.__run_sql(fn[:-4])

        if file_list:
            self.__set_version(file_list[-1][0:11])
        else:
            print('-- No updates found')
