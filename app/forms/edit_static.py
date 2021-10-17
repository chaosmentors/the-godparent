""" Defines a form that allows a user to edit the text for the static webpages.
    Static pages contain information such as the welcome screen, the imprint
    and the privacy policy.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField


class EditStaticForm(FlaskForm):
    content = TextAreaField('Content', validators=None)
    description = StringField('Title', validators=None)
    submit = SubmitField('Save')
