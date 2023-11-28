#!/usr/bin/env python3
"""Main app file where Flask app is defined and configure"""
from flask import Flask, render_template, redirect, url_for
from routes.user import user
from routes.job import job
from routes.application import applications
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from models.user import User
from models import storage

import sys
print(sys.path)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)



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
    """Handles edirection for protected routes"""
    return redirect(url_for('user.login'))

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session and start a new session for each request"""
    storage.close()


app.register_blueprint(user, url_prefix='/')
app.register_blueprint(job, url_prefix='/')
app.register_blueprint(applications, url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True)