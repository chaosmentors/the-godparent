# Description: Defines a class, that will return the sql code inside the
#              resource, that has the same name as the property.
# Created On: Wed 17 Feb 2021 08:37:40 PM CET
# Last Modified: Sun 11 Apr 2021 06:28:36 PM CEST

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

    @property
    def createAccount(self):
        """! Retruns the SQL that creates a new account
        """
        return self.__get_resource(self.__get_caller_name())

    @property
    def getTagByPerson(self):
        """! Return the SQL that returns a list of tags for a specific user
        """
        return self.__get_resource(self.__get_caller_name())

    @property
    def getUserByEmail(self):
        """! Retruns the sql code for getting the user record by its email
        address.
        """
        return self.__get_resource(self.__get_caller_name())

    @property
    def getUserById(self):
        """! Returns the sql code for getting the user record by its id.
        """
        return self.__get_resource(self.__get_caller_name())

    @property
    def getUserId(self):
        """! Retruns the sql code for getting the user id by email.
        """
        return self.__get_resource(self.__get_caller_name())

    @property
    def schema(self):
        """! Retruns the schema.sql code
        """
        return self.__get_resource(self.__get_caller_name())
