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
    cards_data = [
    {'title': 'Client Meeting', 'date': 'Jan 15', 'description': 'Scheduled a meeting with clients to discuss the upcoming project milestones, address any concerns, and ensure everyone is aligned on the project goals.'},
    {'title': 'Project Deadline', 'date': 'Feb 03', 'description': 'Project deadline approaching! The team is working hard to finalize the last set of features and conduct thorough testing to deliver a high-quality product on time.'},
    {'title': 'Team Building Event', 'date': 'Mar 22', 'description': 'Organizing a team-building event at a local venue. This event aims to strengthen team bonds, improve communication, and foster a positive and collaborative work environment.'},
    {'title': 'Product Launch', 'date': 'Apr 10', 'description': 'Exciting times ahead! We are gearing up for the official product launch. The marketing team is finalizing promotional materials, and the development team is conducting last-minute checks to ensure a smooth launch.'},
    {'title': 'Training Session', 'date': 'May 05', 'description': 'Conducting a comprehensive training session for team members. The session will cover new tools and technologies, best practices, and skill development to enhance overall team efficiency and effectiveness.'},
    {'title': 'Training Session', 'date': 'May 05', 'description': 'Conducting a comprehensive training session for team members. The session will cover new tools and technologies, best practices, and skill development to enhance overall team efficiency and effectiveness.'},
    # Add more events as needed
]
    return render_template('home.html', cards=cards_data)


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
        # extract data from form
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