#!/usr/bin/python3
"""Application form extended from flask wtf"""
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField)
from wtforms.validators import InputRequired, Length

class ApplicationForm(FlaskForm):
    """Class extended from flask wtf for form login"""
    firstname = StringField('Username', validators=[InputRequired(),
                                             Length(min=4, max=15)])
    lastname = StringField('Username', validators=[InputRequired(),
                                             Length(min=4, max=15)])
    email = StringField('Email', validators=[InputRequired(),
                                             Length(min=4, max=100)])
    cover_letter = StringField('Cover Letter', validators=[InputRequired(), 
                                                           Length(min=50, max=268)])
    submit = SubmitField('Submit')