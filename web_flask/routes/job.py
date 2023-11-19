from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user


job = Blueprint('job', __name__)


@job.route('/dashboard', methods=['GET', 'POST'], endpoint='dashboard')
@login_required
def dashboard():
    """Dashboard"""
    return render_template('dashboard.html')