# Project: the-godmother
# Created On: Wed 17 Feb 2021 07:58:06 PM CET
# Last Modified: Wed 17 Feb 2021 10:15:23 PM CET

import functools

from flask import (
        Blueprint, flash, g, redirect, render_template, request, session,
        url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from ..database import ( db, embeddedsql )

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    render_template('auth/login.html')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    sql = embeddedsql.Reader()
    if request.method == 'POST':
        email = request.form('email')
        password = request.form('password')
        db = db.get_db()
        error = none

        if not email:
            error = 'A valid e-mail address is required.'
        elif not password:
            error = 'A password is required'
        elif db.execute(sql.getUserId.format(email)
        ).fetchone() is not None:
            error = 'The email address {} is already registered.'.format(email)

        if error is None:
            db.execute(sql.createAccount.format(email,
                generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)
    return render_template('auth/register.html')
