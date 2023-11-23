#!/usr/bin/env python3
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from forms.post_job import PostJobForm
from models.job import Job
from models.user import User
from models import storage
import sys


job = Blueprint('job', __name__)


@job.route('/', methods=['GET', 'POST'], strict_slashes=False)
def home():
    """home route"""
    jobs_data = []
    jobs = storage.all(Job).values()
    for index, job in enumerate(jobs):
        # Limit the loop to the first 9 iterations
        if index >= 9:
            break
        user = storage.get(User, job.user_id)
        if user:
            job_data = {
                'id': job.id,
                'title': job.title,
                'description': job.description,
                'location': job.location,
                'salary': job.salary,
                'requirements': job.requirements,
                'deadline': job.deadline,
                'created_at': job.created_at.strftime("%B %d"),
                'username': user.username,
                'user_id': job.user_id
            }
        jobs_data.append(job_data)
    return render_template('home.html', cards=jobs_data)


@job.route('/jobs', methods=['GET'], strict_slashes=False)
def all_jobs():
    """List all jobs"""
    jobs_data = []
    jobs = storage.all(Job).values()
    for job in jobs:
        user = storage.get(User, job.user_id)
        if user:
            job_data = {
                'id': job.id,
                'title': job.title,
                'description': job.description,
                'location': job.location,
                'salary': job.salary,
                'requirements': job.requirements,
                'deadline': job.deadline,
                'created_at': job.created_at.strftime("%B %d"),
                'username': user.username,
                'user_id': job.user_id
            }
        jobs_data.append(job_data)
    return render_template('jobs.html', cards=jobs_data)


@job.route('/job/create', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def post_job():
    """Post job route"""
    form = PostJobForm()
    if form.validate_on_submit():
        """Handle form submission logic here"""
        # extract data from form and add user_id
        data = {
            "title": form.title.data,
            "description": form.description.data,
            "location": form.location.data,
            "salary": form.salary.data,
            "requirements": form.requirements.data,
            "deadline": form.deadline.data,
            "user_id": current_user.id
        }
        # Create new User
        new_job = Job(**data)
        # Save User in database
        new_job.save()
        flash("Job Created Successfully", "success")
        # Rediect to Loggin Page
        return redirect(url_for('job.home'))
    flash("Fill in all fields", "success")
    return render_template('postform.html', form=form)


@job.route('/job/<string:job_id>', methods=['GET'], strict_slashes=False)
def single_job(job_id):
    """Single Job route - displays a single job"""
    job = storage.get(Job, job_id)
    if job:
        return render_template('singlejob.html', job=job)
    else:
        return render_template('404.html')


@job.route('/job/<string:job_id>', methods=['POST'], strict_slashes=False)
def delete_job(job_id):
    """Delete Job route - delete a single job"""
    job = storage.get(Job, job_id)
    if job:
       storage.delete(job)
       storage.save()
       return redirect(url_for('job.home'))
    else:
        return render_template('404.html')