""" Defines a form that allows a user to edit the text for the static webpages.
    Static pages contain information such as the welcome screen, the imprint
    and the privacy policy.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired
from app.models.languages import Language
from app.models.pages import PageTypeDescriptions

class EditStaticForm(FlaskForm):
    """ Edit the content of a specific page/language """
    content = TextAreaField('Content', validators=None)
    description = StringField('Title', validators=None)
    submit = SubmitField('Save')


class ShowStaticForm(FlaskForm):
    """ Show a list of static for editing """
    id = HiddenField()
    page_type = StringField('Page Type')
    language = SelectField('Language', validators=[DataRequired()])
    submit = SubmitField('Edit')
