""" Defines a form, that allows a user to edit their profile.
    Created On: Mon 24 May 2021 02:34:06 PM CEST
    Last Modified: Tue 25 May 2021 06:57:53 PM CEST
"""

from flask_wtf import FlaskForm
from wtforms import (BooleanField, StringField, PasswordField, TextAreaField,
                     SubmitField)
from wtforms.validators import DataRequired, EqualTo


class EditProfileForm(FlaskForm):
    description = TextAreaField('About Me', validators=None)
    nickname = StringField('Nickname', validators=[DataRequired()])
    password = PasswordField('New Password', validators=None)
    repeat_password = PasswordField('Repeat New Password',
                                    validators=[EqualTo('password')])
    is_godmother = BooleanField('Godmother', validators=None)
    submit = SubmitField('Speichern')
