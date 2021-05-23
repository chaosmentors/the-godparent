"""Defines a registration form for new users to register
   Created On: Sun 23 May 2021 11:21:10 PM CEST
   Last Modified: Sun 23 May 2021 11:22:03 PM CEST
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models.users import User


class RegistrationForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    nickname = StringField('Your Nickname', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField(
        'Repeat Password', validators=[DataRequired(),
                                       EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This e-mail address is already in use.')
