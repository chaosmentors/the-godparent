import functools

from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)
from werkzeug.security import (check_password_hash, generate_password_hash)

from ..database import (db, embeddedsql)

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    """!
    Generates the start page. The content differs, whether or
    not a user is logged in.
    """
    return render_template('index.html')
