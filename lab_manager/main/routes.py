from flask import render_template, Blueprint
from flask_login import current_user, login_required

main = Blueprint('main', __name__)

@main.route("/")
@login_required
def home():
    return render_template('users/profile.jinja2', title = "Home", user=current_user)