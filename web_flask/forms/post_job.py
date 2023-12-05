#!/usr/bin/python3
"""Post form extended from flask wtf"""
from flask_wtf import FlaskForm
from wtforms import (StringField, DateField, SubmitField, TextAreaField, RadioField)
from wtforms.validators import InputRequired, Length

class PostJobForm(FlaskForm):
    """Pst job form class"""
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=1, max=30)])
    description = TextAreaField('Description', validators=[InputRequired(),
                                             Length(min=10, max=2000)],
                                             render_kw={'style': 'height: 5rem; resize: none;'})
    location = StringField('loation', validators=[InputRequired(),
                                             Length(min=1, max=100)])
    salary = StringField('Salary', validators=[InputRequired(),
                                             Length(min=1, max=15)])
    requirements = StringField('Requirements', validators=[InputRequired(),
                                             Length(min=1, max=1000)])
    type = RadioField('type', choices=['Partime', 'Fulltime'],
                       validators=[InputRequired()])
    deadline = DateField('Deadline', format='%Y-%m-%d')
    submit = SubmitField('Post')