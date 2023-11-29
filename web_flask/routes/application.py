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


@applications.route('/applications/<string:job_id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def get_applications(job_id):
    """Handles get for all job apllication"""
    apps_data = []
    apps = storage.all(Application).values()
    for app in apps:
        if app.job_id == job_id:
            job = storage.get(Job, app.job_id)
            user = storage.get(User, app.user_id)
            app.title = job.title
            app.firstname = user.first_name
            app.lastname = user.last_name
            apps_data.append(app)
    return render_template('application-list.html', applications=apps_data)

@applications.route('/application/<string:app_id>', methods=['GET'], strict_slashes=False)
@login_required
def single_app(app_id):
    """Single App route - displays a single app"""
    app = storage.get(Application, app_id)
    if app:
        user = storage.get(User, app.user_id)
        job = storage.get(Job, app.job_id)
        return render_template('singleapp.html', job=job, user=user, app=app)
    else:
        return render_template('404.html')