from flask import render_template, Blueprint, redirect, url_for
from flask_login import current_user, login_required

main = Blueprint('main', __name__)

@main.route("/")
@login_required
def home():
    return redirect(url_for("users.profile"))