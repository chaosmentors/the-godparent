"""The blueprint for the index route. 
This will get the user to the public start page, or their personal overview.
"""

from flask import (Blueprint, flash, g, redirect, render_template, url_for)
from werkzeug.exceptions import abort

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    """Route to the startpage"""
    return render_template('index.html')
