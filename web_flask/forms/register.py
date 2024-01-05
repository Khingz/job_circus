#!/usr/bin/python3
"""Register form extended from flask wtf"""
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, RadioField)
from wtforms.validators import InputRequired, Length, EqualTo, Email

class RegisterForm(FlaskForm):
    """Class extended from flask wtf for form login"""
    first_name = StringField('Firstname', validators=[InputRequired(), Length(min=1, max=15)])
    last_name = StringField('Lastname', validators=[InputRequired(), Length(min=1, max=15)])
    username = StringField('Username', validators=[InputRequired(), Length(min=1, max=15)], render_kw={'autocomplete': 'username'})
    email = StringField('Email', validators=[InputRequired(), Email()])
    portfolio_url = StringField('Portfolio Url', render_kw={'autocomplete': 'username'})
    github_url = StringField('Github Url', render_kw={'autocomplete': 'username'})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=100)])
    confirm_password = PasswordField('Confirm Password', validators=[
        InputRequired(), Length(min=4, max=100), EqualTo('password', message='Passwords must match')
    ])
    role = RadioField('Role', choices=['Employer', 'Job-Seeker'], validators=[InputRequired()])
    submit = SubmitField('Register')


class UpdateForm(FlaskForm):
    """Class extended from flask wtf for form login"""
    first_name = StringField('Firstname', validators=[Length(min=1, max=15)])
    last_name = StringField('Lastname', validators=[Length(min=1, max=15)])
    portfolio_url = StringField('Portfolio Url', render_kw={'autocomplete': 'username'})
    github_url = StringField('Github Url', render_kw={'autocomplete': 'username'})
    new_password = PasswordField('New password')
    confirm_new_password = PasswordField('Confirm new password', validators=[
       EqualTo('new_password', message='Passwords must match')
    ])
    update = SubmitField('Update')
