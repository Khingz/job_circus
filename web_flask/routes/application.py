from flask import Blueprint, render_template, redirect, url_for, flash
from forms.application import ApplicationForm
from models.user import User
from models.job import Job
from models.application import Application
from flask_login import login_required, current_user
from models import storage
import sys

applications = Blueprint('applications', __name__)

@applications.route('/apply/<string:job_id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def apply(job_id):
    """Handles job apllication"""
    form = ApplicationForm()
    if form.validate_on_submit():
        # Create a new application
        data = {
            "user_id": current_user.id,
            "job_id": job_id,
            "cover_letter": form.cover_letter.data
        }
        new_application = Application(**data)
        # Save the application to the database
        new_application.save()

        flash('Application submitted successfully!', 'success')
        return redirect(url_for('job.home'))
    return render_template('apply.html', job_id=job_id, form=form)