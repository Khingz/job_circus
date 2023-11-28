#!/usr/bin/python3
"""Application form extended from flask wtf"""
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField)
from wtforms.validators import InputRequired, Length

class ApplicationForm(FlaskForm):
    """Class extended from flask wtf for form login"""
    cover_letter = StringField('Cover Letter', validators=[InputRequired(), 
                                                           Length(min=50, max=268)],
                                                           render_kw={'style': 'height: 10rem; resize: none;'})
    submit = SubmitField('Submit')