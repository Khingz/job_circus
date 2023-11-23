from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from forms.post_job import PostJobForm
from models.job import Job
from models.user import User
from models import storage


job = Blueprint('job', __name__)


@job.route('/', methods=['GET', 'POST'])
def home():
    """home route"""
    jobs_data = []
    jobs = storage.all(Job).values()
    for job in jobs:
        user = storage.get(User, job.user_id)
        if user:
            job_data = {
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


@job.route('/protected', methods=['GET', 'POST'])
@login_required
def protected():
    """protected"""
    return render_template('protected.html')

@job.route('/job/create', methods=['GET', 'POST'])
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