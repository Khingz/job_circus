#!/usr/bin/env python3
"""User routes"""
from flask import Blueprint, render_template, redirect, url_for, flash
from ..forms.login import LoginForm
from ..forms.register import RegisterForm
from flask_bcrypt import Bcrypt
from models.user import User
from models.job import Job
from models import storage
from flask_login import login_user, current_user, login_required, logout_user
from itsdangerous import URLSafeTimedSerializer
import os
from dotenv import load_dotenv
from flask_mail import Message

load_dotenv()


# Get env variables
ITD_SECRET_KEY = os.getenv('ITD_SECRET_KEY')

bcrypt = Bcrypt()
user = Blueprint('user', __name__)
serializer = URLSafeTimedSerializer(ITD_SECRET_KEY)

@user.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    """Login route"""
    if current_user.is_authenticated:
        return redirect(url_for('job.home'))
    form = LoginForm()
    if form.validate_on_submit():
        # Handle form submission logic here
        email = form.email.data
        password = form.password.data
        user = storage.get_email(User, email.lower())
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('job.home'))
        flash('Invalid username or password', 'error')
    return render_template('login.html', form=form)


@user.route('/register', methods=['GET', 'POST'], endpoint='register')
def register():
    """Register route"""
    if current_user.is_authenticated:
        return redirect(url_for('job.home'))
    form = RegisterForm()
    if form.validate_on_submit():
        """Handle form submission logic here"""
        # extract data from form
        data = {
            "username": form.username.data,
            "first_name": form.firstname.data,
            "last_name": form.lastname.data,
            "password": bcrypt.generate_password_hash(form.password.data).decode('utf-8'),
            "email": form.email.data.lower(),
            "role": form.role.data,
            "portfolio_url": form.portfolio_url.data,
            "github_url": form.github_url.data,
            "email_verify": False
        }
        # Check if the email is already registered
        existing_email = storage.get_email(User, data['email'])
        if existing_email:
            flash('Email address is already registered. Please use a different email.', 'danger')
            return redirect(url_for('user.register'))
        # Check if the username already exist
        existing_username = storage.get_username(User, data['username'])
        if existing_username:
            flash('Username is already registered. Please use a different username.', 'danger')
            return redirect(url_for('user.register'))
        # Create new User
        new_user = User(**data)
        # Save User in database
        new_user.save()
        flash("User Created Successfully", "success")
        # Login user
        login_user(new_user)
        # Redirect to confirm email
        return redirect(url_for('user.confirm_email'))
    return render_template('register.html', form=form,)


@user.route('/confirm_email', methods=['GET', 'POST'], endpoint='confirm_email')
def confirm_email():
    """Sends link to verify email"""
    from web_flask import mail
    if current_user.email_verify:
        return redirect(url_for('job.home'))
    user_id = current_user.id 
    user_email = current_user.email
    token = serializer.dumps(user_id)
    verification_link = url_for('user.verify_email', token=token, _external=True)
    msg = Message('Verify Your Email',
                  sender='noreply',
                  recipients=[user_email])
    msg.body = f'To Complete your sign up please click the following link to verify your email: {verification_link}'
    mail.send(msg)
    return render_template('confirm-email.html')

@user.route('/verify_email/<token>', methods=['GET', 'POST'], endpoint='verify_email')
def verify_email(token):
    """Handles email verification"""
    try:
        user_id = serializer.loads(token, max_age=900)
        user = user = storage.get(User, user_id)
        user.email_verify = True
        user.save()
        flash('Email verification successful')
        return redirect(url_for('job.home'))
    except Exception as e:
        # Handle token verification failure
        flash('Email verification failed. Please try again')
        return redirect(url_for('user.confirm_email'))


@user.route("/logout")
@login_required
def logout():
    """Log out functionality"""
    logout_user()
    return redirect(url_for('user.login'))

@user.route("/user/<string:user_id>")
@login_required
def single_user(user_id):
    """Return a single user"""
    user = storage.get(User, user_id)
    if user:
       if user.role == "Employer":
        for job in user.jobs:
            job.username = user.username
        return render_template('profile.html', user=user, jobs=user.jobs)
       else:
            for app in user.applications:
                job = storage.get(Job, app.job_id)
                user = storage.get(User, app.user_id)
                app.title = job.title
                app.firstname = user.first_name
                app.lastname = user.last_name
            return render_template('profile.html', user=user, applications=user.applications)
    else:
        return render_template('404.html')
    
@user.route('/user/<string:user_id>', methods=['POST'], strict_slashes=False)
@login_required
def delete_user(user_id):
    """Delete User route - delete a user account"""
    user = storage.get(User, user_id)
    if user:
       storage.delete(user)
       storage.save()
       return redirect(url_for('user.register'))
    else:
        return render_template('404.html')
    

# @user.route('/user/update/<string:user_id>', methods=['GET', 'POST'])
# @login_required
# def update_user(user_id):
#     """Update route"""
#     user = storage.get(User, user_id)
#     if not user:
#         flash("User not found", "error")
#         return redirect(url_for('job.home'))
#     form = UpdateForm(obj=user)
#     if form.validate_on_submit():
#         """Handle form submission logic here"""
#         # extract data from form
#         data = {
#             "first_name": form.firstname.data,
#             "last_name": form.lastname.data,
#             "password": bcrypt.generate_password_hash(form.password.data).decode('utf-8'),
#             "portfolio_url": form.portfolio_url.data,
#             "github_url": form.github_url.data
#         }
#         # Create new User
#         user.update(**data)
#         flash("User Updated Successfully", "success")
#         # Rediect to Loggin Page
#         return redirect(url_for('job.home'))
#     return render_template('update_user.html', form=form, user=current_user)