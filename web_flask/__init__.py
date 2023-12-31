#!/usr/bin/env python3
"""Main app file where Flask app is defined and configure"""
from flask import Flask, render_template, redirect, url_for
from .routes.user import user
from .routes.job import job
from .routes.application import applications
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from models.user import User
from models import storage
from dotenv import load_dotenv
import os
from flask_mail import Mail 


# Load environment variables from .env file
load_dotenv()

# Get env variables
FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_PORT = os.getenv('MAIL_PORT')
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# App Config
app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'noreply'
mail = Mail(app)


# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Login manager for flas login
@login_manager.user_loader
def load_user(user_id):
    """Loads user based on id"""
    return storage.get(User, user_id)

# Redirection for unathorized page for non logged in user
@login_manager.unauthorized_handler
def unauthorized():
    """Handles redirection for protected routes"""
    return redirect(url_for('user.login'))

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session and start a new session for each request"""
    storage.close()


app.register_blueprint(user, url_prefix='/')
app.register_blueprint(job, url_prefix='/')
app.register_blueprint(applications, url_prefix='/')