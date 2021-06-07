"""Defines the routes for profile information
   Created On: Mon 24 May 2021 12:55:44 PM CEST
   Last Modified: Mon 07 Jun 2021 10:14:17 PM CEST
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from app import db
from app.forms.edit_profile import EditProfileForm, EditButtonForm
from app.models.users import User

bp = Blueprint('profile', __name__)


@bp.route('/profile/<nickname>', methods=['GET', 'POST'])
@login_required
def user(nickname):
    """Displays the profile page of a user"""
    form = EditButtonForm()
    if form.validate_on_submit():
        return redirect(url_for('profile.edit_profile'))
    elif request.method == 'GET':
        user = User.query.filter_by(nickname=nickname).first_or_404()
        return render_template('profile.html', user=user, form=form)


@bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.nickname = form.nickname.data
        current_user.pronoun = form.pronoun.data
        current_user.description = form.description.data
        if form.password.data is not None:
            current_user.set_password(form.password.data)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('profile.user',
                                nickname=current_user.nickname))
    elif request.method == 'GET':
        form.nickname.data = current_user.nickname
        form.description.data = current_user.description
        form.pronoun.data = current_user.pronoun
        return render_template('edit_profile.html',
                               title='Edit Profile',
                               form=form)
