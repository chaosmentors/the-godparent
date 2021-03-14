"""!
Project: the-godmother
Created On: Wed 17 Feb 2021 07:58:06 PM CET
Last Modified: Sun 14 Mar 2021 06:35:04 PM CET
"""
import functools

from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)
from werkzeug.security import (check_password_hash, generate_password_hash)

from ..database import (db, embeddedsql)

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
        g.user = db.get_db().execute(
            sql.getUserById.format(user_id)).fetchone()


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
        error = None
        user = db.get_db().execute(sql.getUserByEmail.format(email)).fetchone()

        if user is None:
            error = 'Incorrect e-mail address or password.'
        elif not check_password_hash(user['password_hash'], password):
            error = 'Incorrect e-mail address or password.'
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


def login_required(view):
    """! Redirects a view to the login page, when a log in is required
    @parameter view: A view that requires a valid login.

    Returns a wrapped version of the view, that will redirect users to the
    login page when needed.
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


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
        email = request.form['email']
        password = request.form['password']
        role = 1 if request.args.get('role') == 'mentor' else 0
        currentdb = db.get_db()
        error = None

        if not email:
            error = 'A valid e-mail address is required.'
        elif not password:
            error = 'A password is required'
        elif currentdb.execute(
                sql.getUserId.format(email)).fetchone() is not None:
            error = 'The email address {} is already registered.'.format(email)

        if error is None:
            currentdb.execute(
                sql.createAccount.format(email,
                                         generate_password_hash(password),
                                         role))
            currentdb.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')
