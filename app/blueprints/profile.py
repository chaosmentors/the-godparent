"""Defines the routes for profile information
   Created On: Mon 24 May 2021 12:55:44 PM CEST
   Last Modified: Tue 25 May 2021 06:58:26 PM CEST
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from app import db
from app.forms.edit_profile import EditProfileForm
from app.models.users import User

bp = Blueprint('profile', __name__)


@bp.route('/profile/<nickname>')
@login_required
def user(nickname):
    """Displays the profile page of a user"""
    user = User.query.filter_by(nickname=nickname).first_or_404()
    return render_template('profile.html', user=user)


@bp.route('/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.nickname = form.nickname.data
        current_user.description = form.description.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('profile.edit_profile'))
    elif request.method == 'GET':
        form.nickname.data = current_user.nickname
        form.description.data = current_user.description
        return render_template('edit_profile.html',
                               title='Edit Profile',
                               form=form)
