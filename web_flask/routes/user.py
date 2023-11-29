#!/usr/bin/env python3
"""User routes"""
from flask import Blueprint, render_template, redirect, url_for, flash
from forms.login import LoginForm
from forms.register import RegisterForm
from flask_bcrypt import Bcrypt
from models.user import User
from models.job import Job
from models import storage

from flask_login import login_user, current_user, login_required, logout_user


bcrypt = Bcrypt()
user = Blueprint('user', __name__)


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
            "github_url": form.github_url.data
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
        # Rediect to Loggin Page
        return redirect(url_for('user.login'))
    flash("Fill in all fields", "success")
    return render_template('register.html', form=form)


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