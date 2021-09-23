"""The blueprint for the index route. 
This will get the user to the public start page, or their personal overview.
"""

from app.sidebar import generate_page_list
from flask import Blueprint, flash, g, redirect, render_template, url_for
from flask_login import current_user, login_required
from werkzeug.exceptions import abort

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    """Route to the startpage"""
    return render_template('index.html')


@bp.route('/godparent/dashboard')
@login_required
def dashboard():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    if not current_user.is_godmother:
        flash('Only godparents can open the dashboard.')
        return redirect(url_for('index'))
    pages = generate_page_list()
    return render_template('dashboard.html',
                           pages=pages,
                           page_name='Dashboard')
