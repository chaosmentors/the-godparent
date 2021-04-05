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
    sql = embeddedsql.Reader()
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = db.get_db().execute(
            sql.getUserById.format(user_id)).fetchone()
        tags = db.get_db().execute(sql.getTagByPerson.format(g.user.id))
        return render_template('index.html', Tags=tags)

    return render_template('index.html')
