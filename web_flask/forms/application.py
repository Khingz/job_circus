#!/usr/bin/python3
"""Application form extended from flask wtf"""
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, SubmitField)
from wtforms.validators import InputRequired, Length

class ApplicationForm(FlaskForm):
    """Class extended from flask wtf for form login"""
    cover_letter = TextAreaField('Cover Letter', validators=[InputRequired(), 
                                                           Length(min=1, max=5000)],
                                                           render_kw={'style': 'height: 10rem; resize: none;'})
    submit = SubmitField('Submit')