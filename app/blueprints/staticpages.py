"""Defines the routes for static page editing.
   Created On: Sun 07 Nov 2021 03:31:00 PM CET
   Last Modified: Thu 10 Feb 2022 08:59:03 PM CET
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from app import db
from app.forms.edit_static import EditStaticForm
from app.models.pages import PageTypeDescriptions, Static

bp = Blueprint('staticpage',__name__)


@bp.route('/godparent/static/edit/<page_type>/<lang_id>', methods=['GET', 'POST'])
@login_required
def edit_static(page_type, lang_id):
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
        static = Static.query.filter((Static.type == page_type) and
                                     (Static.language_id == lang_id))
        if not isinstance(static, Static):
            static = Static()
            static.language_id = lang_id
            static.type = page_type
            static.content = ''
            static.description = 'test'
        form.content.data = static.content
        form.description.data = static.description
        return render_template('edit_staticpage.html', user=current_user,
                               form=form,
                               page_type=PageTypeDescriptions[int(page_type)],
                               page_name='Static Pages')
