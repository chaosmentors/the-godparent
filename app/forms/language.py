""" Defines a form, that allows a godparent to add and edit language code.
    Created On: Sat 24 Jul 2021 08:07:43 PM CEST
    Last Modified: Sun 01 Aug 2021 01:03:14 AM CEST
"""

from flask_table import Table, Col, LinkCol
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ListLanguages(Table):
    """Holds a list of all languages"""
    id = Col('Id', show=False)
    iso_code = Col('Iso-Code')
    name = Col('Name')
    edit = LinkCol('Edit',
                   'language.edit',
                   url_kwargs=dict(iso_code='iso_code'))
    delete = LinkCol('Delete',
                     'language.delete',
                     url_kwargs=dict(iso_code='iso_code'))


class EditLanguageForm(FlaskForm):
    """Edit language definitions"""
    iso_code = StringField('Iso-Code', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField(label='Save')
