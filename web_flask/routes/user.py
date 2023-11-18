#!/usr/bin/python3
"""User routes"""
from flask import Blueprint, render_template, redirect, url_for, flash
from forms.login import LoginForm
from forms.register import RegisterForm
from flask_bcrypt import Bcrypt
from models.user import User
from models import storage


bcrypt = Bcrypt()
user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    """Login route"""
    form = LoginForm()
    if form.validate_on_submit():
        # Handle form submission logic here
        username = form.username.data
        password = form.password.data
        return f'Username: {username}, Password: {password}. Form submitted successfully.'
    return render_template('login.html', form=form)

@user.route('/register', methods=['GET', 'POST'], endpoint='register')
def register():
    """Register route"""
    form = RegisterForm()
    if form.validate_on_submit():
        """Handle form submission logic here"""
        # extract data from form
        data = {
            "username": form.username.data,
            "firstname": form.firstname.data,
            "lastname": form.lastname.data,
            "password": bcrypt.generate_password_hash(form.password.data).decode('utf-8'),
            "email": form.email.data,
            "role": form.role.data
        }
        # Check if the email is already registered
        existing_email = storage.get_email(User, data['email'])
        if existing_email:
            flash('Email address is already registered. Please use a different email.', 'danger')
            return redirect(url_for('user.register'))
        # Check if the username already exist
        existing_username = storage.get_username(User, data['username'])
        print(existing_username)
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
    return render_template('register.html', form=form)