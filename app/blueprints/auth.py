"""Defines the routes for login an registration
   Created On: Tue 11 May 2021 09:51:00 PM CEST
   Last Modified: Mon 24 May 2021 12:13:53 AM CEST
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from app import db
from app.forms.login import LoginForm
from app.forms.registration import RegistrationForm
from app.models.users import User

bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Route to the login page"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid user name or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    """Log out an active user."""
    logout_user()
    return redirect(url_for('index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, nickname=form.nickname.data)
        user.set_password(form.password.data)
        role = request.args.get('role')
        if role and role == 'mentor':
            user.role = 1
        else:
            user.role = 0

        has_user = User.query.first()
        if has_user is None:
            user.is_godmother = True
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered. Please check your e-mail' +
              'account for the confirmation e-mail.')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)
