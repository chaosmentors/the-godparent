""" Defines the page entries, that will be shown on the side bar 
    Created On: Thu 23 Sep 2021 08:19:34 PM CEST
    Last Modified On: Thu 23 Sep 2021 08:19:34 PM CEST
"""

from flask import url_for


def generate_page_list():
    """Generates a list of pages that link to the admin sidebar."""
    pages = [{
        'name': 'Dashboard',
        'url': url_for('index.dashboard')
    }, {
        'name': 'Languages',
        'url': url_for('language.list')
    },{
        'name': 'Static Pages',
        'url': 'static'
    }]

    return pages
