"""Public section, including homepage."""

from flask import Blueprint, render_template

public = Blueprint('public', __name__, template_folder='templates')


@public.route('/')
def home():
    return render_template('public/home.html')
