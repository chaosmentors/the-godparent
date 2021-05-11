"""Defines a login form for logging in and registering new users.
   Created On: Tue 11 May 2021 09:32:30 PM CEST
   Last Modified: Tue 11 May 2021 09:57:47 PM CEST
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """Implements the login form"""
    email = StringField('E-Mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')
