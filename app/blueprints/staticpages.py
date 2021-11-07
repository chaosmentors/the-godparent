"""Defines the routes for static page editing.
   Created On: Sun 07 Nov 2021 03:31:00 PM CET
   Last Modified: Sun 07 Nov 2021 03:55:03 PM CET
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from app import db
from app.forms.edit_static import EditStaticForm
from apps.models.page import Static

bp = Blueprint('staticpage',__name__)


@bp.route('/static/edit', methods=['GET', 'POST'])
@login_required
def edit_static(page_type):
    """Edit an existing page type"""
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    if not current_user.is_godmother:
        flash('Only godparents can use this function.')
        redirect(url_for('index'))
    form = EditStaticForm()
    if form.validate_on_submit():
        static = Static.query.filter(Static.type == page_type).first()
        if not static:
            static.content = form.content.data
            static.description = form.description.data
            static.type = page_type
            db.session.add(static)
        else:
            static.content = form.content.data
            static.description = form.description.data
        db.session.commit()        
        return redirect(url_for(staticpages.list))
    elif request.method == 'GET':
        static = Static.query.filter(Static.type == page_type).first_or_404()
        form.content = static.content
        form.description = static.description
        return render_template('edit_static', user=current_user,
                               form=form, page_type=page_type)
