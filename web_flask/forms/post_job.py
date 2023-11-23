#!/usr/bin/python3
"""Post form extended from flask wtf"""
from flask_wtf import FlaskForm
from wtforms import (StringField, DateField, SubmitField)
from wtforms.validators import InputRequired, Length

class PostJobForm(FlaskForm):
    """Pst job form class"""
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=4, max=30)])
    description =StringField('Description', validators=[InputRequired(),
                                             Length(min=10, max=5000)])
    location = StringField('loation', validators=[InputRequired(),
                                             Length(min=4, max=100)])
    salary = StringField('Salary', validators=[InputRequired(),
                                             Length(min=1, max=15)])
    requirements = StringField('Requirements', validators=[InputRequired(),
                                             Length(min=4, max=1000)])
    deadline = DateField('Deadline', format='%Y-%m-%d')
    submit = SubmitField('Post')