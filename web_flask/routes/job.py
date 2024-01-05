#!/usr/bin/env python3
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..forms.post_job import PostJobForm
from models.job import Job
from models.user import User
from models import storage


job = Blueprint('job', __name__)


@job.route('/', methods=['GET'], strict_slashes=False)
def home():
    """home route"""
    jobs_data = []
    jobs = storage.all(Job).values()
    for index, job in enumerate(jobs):
        # Limit the loop to the first 9 iterations
        if index >= 7:
            break
        user = storage.get(User, job.user_id)
        if user:
            job_data = {
                'id': job.id,
                'title': job.title,
                'description': job.description,
                'created_at': job.created_at,
                'username': user.username,
                'user_id': job.user_id
            }
        jobs_data.append(job_data)
    return render_template('home.html', cards=jobs_data)


@job.route('/jobs', methods=['GET', 'POST'], strict_slashes=False)
def all_jobs():
    """List all jobs"""
    jobs_data = []
    keyword = request.args.get('search', '')
    if not keyword:
        jobs = storage.all(Job).values()
    else:
        jobs = storage.search(Job, keyword).values()
    for job in jobs:
        user = storage.get(User, job.user_id)
        # extract data from form and add user_id
        if user:
            job_data = {
                'id': job.id,
                'title': job.title,
                'description': job.description,
                'location': job.location,
                'salary': job.salary,
                'requirements': job.requirements,
                'deadline': job.deadline,
                'created_at': job.created_at,
                'username': user.username,
                'user_id': job.user_id
            }
        jobs_data.append(job_data)
    return render_template('jobs.html', cards=jobs_data, search=keyword)


@job.route('/job/create', methods=['POST', 'GET'])
@login_required
def post_job():
    """Post job route"""
    if not current_user.email_verify:
        flash('Please verify your email to continue!')
        return redirect(url_for('user.confirm_page'))
    form = PostJobForm()
    if form.validate_on_submit():
        """Handle form submission logic here"""
        data = {
            "title": form.title.data,
            "description": form.description.data,
            "location": form.location.data,
            "salary": form.salary.data,
            "requirements": form.requirements.data,
            "deadline": form.deadline.data,
            "type": form.type.data,
            "user_id": current_user.id
        }
        # Create new User
        new_job = Job(**data)
        # Save User in database
        new_job.save()
        flash("Job posted successfully")
        # Rediect to Login Page
        return redirect(url_for('job.home'))
    flash("Fill in all fields")
    return render_template('postform.html', form=form)


@job.route('/job/<string:job_id>', methods=['GET'], strict_slashes=False)
def single_job(job_id):
    """Single Job route - displays a single job"""
    job = storage.get(Job, job_id)
    if job:
        user = storage.get(User, job.user_id)
        return render_template('singlejob.html', job=job, user=user)
    else:
        return render_template('404.html')


@job.route('/job/<string:job_id>', methods=['POST'], strict_slashes=False)
def delete_job(job_id):
    """Delete Job route - delete a single job"""
    if not current_user.email_verify:
        flash('Please verify your email to continue!')
        return redirect(url_for('user.confirm_page'))
    job = storage.get(Job, job_id)
    if job:
       storage.delete(job)
       storage.save()
       flash('Job deleted successfully!')
       return redirect(url_for('job.home'))
    else:
        return render_template('404.html')