# Description: Defines a class, that will return the sql code inside the
#              resource, that has the same name as the property.
# Created On: Wed 17 Feb 2021 08:37:40 PM CET
# Last Modified: Thu 22 Apr 2021 08:17:28 PM CEST

import sys
from flask import current_app


# Defines an SQL reader that will read sql commands from a resource.
# This makes sure python and SQL code stay separated.
class Reader():
    def __init__(self, namespace='database/sql'):
        """! Creates a new Reader
        @param namespace The namespace to use. Default is 'sql'        
        """
        self._namespace = namespace

    def __get_caller_name(self):
        """! Retruns the name of the calling function
        @return Name of the caller.
        """
        return sys._getframe(1).f_code.co_name

    def __get_resource(self, name):
        """! Returns a resource
        @param name Name of the sql resource to find.
        @return The sql string, when the resource was found.
        """
        with current_app.open_resource(f"{self._namespace}/{name}.sql") as f:
            return f.read().decode('utf8')
