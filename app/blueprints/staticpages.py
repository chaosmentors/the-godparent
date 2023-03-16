"""Defines the routes for static page editing.
   Created On: Sun 07 Nov 2021 03:31:00 PM CET
   Last Modified: Thu 16 Mar 2023 09:29:40 pm CET
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from app import db
from app.models.languages import Language
from app.forms.static import EditStaticForm, ShowStaticForm
from app.models.pages import PageTypeDescriptions, Static
from app.sidebar import generate_page_list

bp = Blueprint('staticpage',__name__)


@bp.route('/godparent/static/edit/<page_type>/<lang_id>', methods=['GET', 'POST'])
@login_required
def edit(page_type, lang_id):
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
        return redirect(url_for('staticpage.list'))
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

@bp.route('/godparent/static', methods=['GET', 'POST'])
@login_required
def list():
    """ Show the existing static page types """
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    if not current_user.is_godmother:
        flash('Only godparents can use this function.')
        redirect(url_for('index'))

    form = ShowStaticForm()
    languages = Language.query.order_by(Language.iso_code).all()
    form.language.choices = [(i.iso_code, i.name) for i in languages]
    if form.validate_on_submit():
        # TODO: redirect to the edit page.
        current_id = request.form["id"]
        static = Static.query.filter(Static.id == current_id).first() 
        if not static:
            static = Static()
            static.language = request.form["language"]
            static.type = PageTypeDescriptions[0]
            static.content = ''
            static.description = ''
        form.content.data = static.content
        form.description.data = static.description
        return render_template('edit_staticpage.html', user=current_user,
                               form=form,
                               page_type=PageTypeDescriptions[int(static.type)],
                               page_name='Static Pages')
    elif request.method == 'GET':
        # TODO: Find a way to find out which edit button was clicked.
        pages = generate_page_list()
        static_pages = Static.query.all()
        if not static_pages:
            for index, page_type in enumerate(PageTypeDescriptions):
                static = Static()
                static.type = index
        return render_template('staticpages.html',
                            form=form,
                            static_pages = static_pages,
                            pages=pages,
                            page_name='Static Pages')
