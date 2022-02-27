""" Defines a form that allows a user to edit the text for the static webpages.
    Static pages contain information such as the welcome screen, the imprint
    and the privacy policy.
"""

from flask_table import Table, Col, LinkCol, create_table
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from app.models.languages import Language

class EditStaticForm(FlaskForm):
    """ Edit the content of a specific page/language """
    content = TextAreaField('Content', validators=None)
    description = StringField('Title', validators=None)
    submit = SubmitField('Save')

def create_static_table():
    """ Generates a table that contains the list of static pages and links
        to the editors per language
    """
    languages = Language.query.order_by(Language.iso_code)
    table = create_table('TableCls').add_column('page_type',Col('Page Type'))
    for lang in languages:
        table.add_column(lang.iso_code, LinkCol(lang.iso_code, 'staticpages.edit',
                                                url_kwargs=dict(page_type='page_type',iso_code='iso_code')))
    return table
