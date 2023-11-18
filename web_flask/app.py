#!/usr/bin/python3
"""Main app file where Flask app is defined and configure"""
from flask import Flask, render_template
from routes.user import user
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
bcrypt = Bcrypt(app)


app.register_blueprint(user, url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True)