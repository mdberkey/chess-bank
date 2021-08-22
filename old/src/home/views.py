from flask import Flask, render_template, request, redirect
from flask_login import current_user, login_required

from flask import Blueprint
home = Blueprint('home', __name__)


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title='Welcome')


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title='Dashboard')
