"""Defines the routes for adding and editing the supported languages.
   Created On: Sat 24 Jul 2021 09:01:05 PM CEST
   Last Modified: Thu 23 Sep 2021 08:37:19 PM CEST
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from app import db
from app.forms.language import EditLanguageForm, ListLanguages
from app.models.languages import Language
from app.sidebar import generate_page_list

bp = Blueprint('language', __name__)


@bp.route('/godparent/language/add', methods=['GET', 'POST'])
@login_required
def add():
    """Adds a new language to the list of supported languages."""
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    if not current_user.is_godmother:
        flash('Only godparents can add languages.')
        return redirect(url_for('index'))
    form = EditLanguageForm()
    if form.validate_on_submit():
        lang = Language.query.filter(
            Language.iso_code == form.iso_code.data).first()
        if lang:
            flash('There already exists a language for ' + lang.iso_code)
            return render_template('edit_language.html',
                                   user=current_user,
                                   form=form,
                                   new=True)
        lang = Language()
        lang.iso_code = form.iso_code.data
        lang.name = form.name.data
        db.session.add(lang)
        db.session.commit()
        return redirect(url_for('language.list'))
    elif request.method == 'GET':
        return render_template('edit_language.html',
                               user=current_user,
                               form=form,
                               new=True)


@bp.route('/godparent/language/delete/<iso_code>', methods=['GET'])
@login_required
def delete(iso_code):
    """Delete an existing code."""
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    if not current_user.is_godmother:
        flash('Only godparents can delete languages.')
        return redirect(url_for('index'))
    lang = Language.query.filter(Language.iso_code == iso_code).first()
    if lang:
        db.session.delete(lang)
        db.session.commit()
    return redirect(url_for('language.list'))


@bp.route('/godparent/language/edit/<iso_code>', methods=['GET', 'POST'])
@login_required
def edit(iso_code):
    """Edit an existing language code."""
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    if not current_user.is_godmother:
        flash('Only godparents can use this function.')
        redirect(url_for('index'))
    form = EditLanguageForm()
    form.iso_code.data = iso_code
    if form.validate_on_submit():
        lang = Language.query.filter(Language.iso_code == iso_code).first()
        if not lang:
            lang.iso_code = form.iso_code.data
            lang.name = form.name.data
            db.session.add(lang)
        else:
            lang.name = form.name.data
        db.session.commit()
        return redirect(url_for('language.list'))
    elif request.method == 'GET':
        lang = Language.query.filter(
            Language.iso_code == iso_code).first_or_404()
        form.iso_code.data = lang.iso_code
        form.name.data = lang.name
        return render_template('edit_language.html',
                               user=current_user,
                               form=form,
                               new=False)


@bp.route('/godparent/languages', methods=['GET'])
@login_required
def list():
    """List all supported languages."""
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    if not current_user.is_godmother:
        flash('Only godparents can use this function.')
        return redirect(url_for('index'))
    results = Language.query.order_by(Language.iso_code)

    if not results:
        redirect(url_for('language.add'))
    else:
        table = ListLanguages(results)
        pages = generate_page_list()
        return render_template('languages.html',
                               table=table,
                               pages=pages,
                               page_name='Languages')
