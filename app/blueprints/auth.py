"""Defines the routes for login an registration
   Created On: Tue 11 May 2021 09:51:00 PM CEST
   Last Modified: Tue 11 May 2021 10:03:58 PM CEST
"""

from flask import (Blueprint, redirect, render_template)
from app.forms.login import LoginForm

bp = Blueprint('login', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Route to the login page"""
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/index')

    return render_template('login.html', title='Sign In', form=form)
