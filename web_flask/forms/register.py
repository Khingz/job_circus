#!/usr/bin/python3
"""Register form extended from flask wtf"""
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, RadioField)
from wtforms.validators import InputRequired, Length, EqualTo, Email

class RegisterForm(FlaskForm):
    """Class extended from flask wtf for form login"""
    firstname = StringField('Firstname', validators=[InputRequired(),
                                             Length(min=1, max=15)])
    lastname = StringField('Lastname', validators=[InputRequired(),
                                             Length(min=1, max=15)])
    username = StringField('Username', validators=[InputRequired(),
                                             Length(min=1, max=15)], render_kw={'autocomplete': 'username'})
    email = StringField('Email', validators=[InputRequired(),
                                             Length(min=8, max=100)], render_kw={'autocomplete': 'username'})
    portfolio_url = StringField('Portfolio Url', render_kw={'autocomplete': 'username'})
    github_url = StringField('Github Url', render_kw={'autocomplete': 'username'})
    password = PasswordField('Password', validators=[InputRequired(),
                                             Length(min=4, max=100)])
    confirm_password = PasswordField('Password',
                                     validators=[InputRequired(), Length(min=4, max=100),
                                                 EqualTo('password')])
    role = RadioField('role',
                       choices=['Employer', 'Job-Seeker'],
                       validators=[InputRequired()])
    submit = SubmitField('Register')