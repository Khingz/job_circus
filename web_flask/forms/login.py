#!/usr/bin/python3
"""Login form extended from flask wtf"""
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField)
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    """Class extended from flask wtf for form login"""
    email = StringField('Username', validators=[InputRequired(),
                                             Length(min=1, max=100)])
    password = PasswordField('Password', validators=[InputRequired(),
                                             Length(min=1, max=100)])
    submit = SubmitField('Login')