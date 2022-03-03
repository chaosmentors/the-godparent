""" Defines a form that allows a user to edit the text for the static webpages.
    Static pages contain information such as the welcome screen, the imprint
    and the privacy policy.
"""

from flask_table import Table, Col, LinkCol, OptCol, create_table
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from app.models.languages import Language
from app.models.pages import PageTypeDescriptions

class EditStaticForm(FlaskForm):
    """ Edit the content of a specific page/language """
    content = TextAreaField('Content', validators=None)
    description = StringField('Title', validators=None)
    submit = SubmitField('Save')


class StaticPageItem:
    """ An entry to the static page table """
    def __init__(self, page_type, language_id):
        self.page_type = page_type
        self.language = language_id
        self.edit = 'Edit'


def create_static_table():
    """ Generates a table that contains the list of static pages and links
        to the editors per language
    """
    languages = Language.query.order_by(Language.iso_code).all()
    choices = {}
    for language in languages:
        choices[language.iso_code] = language.name

    TableCls = create_table('TableCls')\
        .add_column('page_type', Col('Page Type'))\
        .add_column('language', OptCol('Language', choices))\
        .add_column('edit', Col('Edit'))

    items = []
    for page_type in PageTypeDescriptions:
        items.append(StaticPageItem(page_type,languages[0].iso_code))

    return TableCls(items)
