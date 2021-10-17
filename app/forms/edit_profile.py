""" Defines a form, that allows a user to edit their profile.
    Created On: Mon 24 May 2021 02:34:06 PM CEST
    Last Modified: Tue 22 Jun 2021 06:59:19 PM CEST
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class EditProfileForm(FlaskForm):
    description = TextAreaField('About Me', validators=None)
    nickname = StringField('Nickname', validators=[DataRequired()])
    pronoun = StringField('Pronoun', validators=None)
    password = PasswordField('New Password', validators=None)
    repeat_password = PasswordField('Repeat New Password',
                                    validators=[EqualTo('password')])
    submit = SubmitField('Save')
    tags = StringField('Tags', validators=None)


class EditButtonForm(FlaskForm):
    """ Presents an edit button, that can be clicked to 
        open the profile editor
    """
    submit = SubmitField('Edit')
