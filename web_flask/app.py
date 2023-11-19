#!/usr/bin/python3
"""Main app file where Flask app is defined and configure"""
from flask import Flask, render_template, redirect, url_for
from routes.user import user
from routes.job import job
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from models.user import User
from models import storage


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)



@login_manager.user_loader
def load_user(user_id):
    """Loads user based on id"""
    return storage.get(User, user_id)

@login_manager.unauthorized_handler
def unauthorized():
    """Handles edirection for protected routes"""
    return redirect(url_for('user.login'))


app.register_blueprint(user, url_prefix='/')
app.register_blueprint(job, url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True)