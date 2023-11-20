from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user


job = Blueprint('job', __name__)


@job.route('/', methods=['GET', 'POST'])
def home():
    """home route"""
    return render_template('home.html')


@job.route('/protected', methods=['GET', 'POST'])
@login_required
def protected():
    """protected"""
    return render_template('protected.html')