# Project: the-godmother
# Created On: Wed 17 Feb 2021 07:58:06 PM CET
# Last Modified: Wed 03 Mar 2021 08:46:29 PM CET

import functools

from flask import (
        Blueprint, flash, g, redirect, render_template, request, session,
        url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from ..database import ( db, embeddedsql )

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.before_app_request
def load_logged_in_user():
    """! Called everytime a resource is requested.
    """
    sql = embeddedsql.Reader()
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(sql.getUserById().format(user_id).fetchone()

@bp.route('/login', methods=('GET', 'POST'))
def login():
    """! Shows the login page, and receives the credentials.
    METHODS: GET, POST
    When called with GET, this method shows the login screen.
    When called with POST, this method sends the login data to the database.
    """
    sql = embeddedsql.Reader()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(sql.getUseriByEmail().format(email)).fetchone()

        if user is None:
            error = 'Incorrect e-mail address or password.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect e-mail address or password.'
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

    render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@bp.route('/register', methods=('GET', 'POST'))
def register():
    """! Registers a new user.
    METHODS: GET, POST
    GET shows register page. 
    When called with POST, the 
    login is created.
    
    @return The /register page, when called by GET
    """
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


