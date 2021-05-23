"""Create global objects and sets the application up."""

from flask import g

class Setup:
    @property
    def db(self):
        """Creates or retrieves the db object."""
        if g.
