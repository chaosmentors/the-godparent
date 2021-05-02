"""Configuration parameter for the app."""
import json


class Config:
    """Stores configuration data from a json object"""
    def __init__(self, dict):
        vars(self).update(dict)


def load_config(fname) -> Config:
    """Loads the configuration from a json file
    fname -- Name of the configuration file.
    Returns a configuration object.
    """

    with open(fname, 'r') as config_file:
        data = config_file.read()

    return json.loads(data, object_hook=Config)
