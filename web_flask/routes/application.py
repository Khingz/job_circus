from flask import Blueprint, render_template, redirect, url_for, flash
from ..forms.application import ApplicationForm
from models.user import User
from models.job import Job
from models.application import Application
from flask_login import login_required, current_user
from models import storage
from flask_mail import Message

applications = Blueprint('applications', __name__)

@applications.route('/apply/<string:job_id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def apply(job_id):
    """Handles job apllication"""
    from web_flask import mail
    if not current_user.email_verify:
        return redirect(url_for('user.confirm_page'))
    form = ApplicationForm()
    if form.validate_on_submit():
        # Create a new application
        data = {
            "user_id": current_user.id,
            "job_id": job_id,
            "cover_letter": form.cover_letter.data
        }
        for item in current_user.applications:
            if item.job_id == job_id:
                flash('You already applied for this job')
                return render_template('apply.html', job_id=job_id, form=form)
        new_application = Application(**data)
        # Save the application to the database
        new_application.save()
        flash('Application submitted successfully!')
        job = storage.get(Job, job_id)
        employer = storage.get(User, job.user_id)
        msg = Message('New Job Application Notification',
                        sender='noreply',
                        recipients=[employer.email])
        msg. body = f'Hi,\n\nYou have a new job application for the position of {job.title}.\n\nApplicant: {current_user.username}\n\nPlease log in to your job portal to review the application.'
        mail.send(msg)
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
    
@applications.route('/application/<string:app_id>', methods=['POST'], strict_slashes=False)
def delete_app(app_id):
    """Delete App route - delete a application"""
    if not current_user.email_verify:
        return redirect(url_for('user.confirm_page'))
    app = storage.get(Application, app_id)
    if app:
       storage.delete(app)
       storage.save()
       flash('Application deleted successfully!')
       return redirect(url_for('job.home'))
    else:
        return render_template('404.html')