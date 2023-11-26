#!/usr/bin/python3
"""Register form extended from flask wtf"""
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, RadioField)
from wtforms.validators import InputRequired, Length, EqualTo

class RegisterForm(FlaskForm):
    """Class extended from flask wtf for form login"""
    firstname = StringField('Firstname', validators=[InputRequired(),
                                             Length(min=4, max=15)])
    lastname = StringField('Lastname', validators=[InputRequired(),
                                             Length(min=4, max=15)])
    username = StringField('Username', validators=[InputRequired(),
                                             Length(min=4, max=15)])
    email = StringField('Email', validators=[InputRequired(),
                                             Length(min=4, max=100)])
    password = PasswordField('Password', validators=[InputRequired(),
                                             Length(min=4, max=100)])
    confirm_password = PasswordField('Password',
                                     validators=[InputRequired(), Length(min=4, max=100),
                                                 EqualTo('password')])
    role = RadioField('role',
                       choices=['Employer', 'Job-Seeker'],
                       validators=[InputRequired()])
    submit = SubmitField('Register')