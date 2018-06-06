"""Main user section, including dashboard."""

from flask import Blueprint, render_template
from flask_user import login_required

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('main/dashboard.html')
