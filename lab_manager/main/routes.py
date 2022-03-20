from datetime import datetime
from flask import g, render_template, Blueprint, redirect, url_for
from flask_login import current_user, login_required
from lab_manager.main.forms import SearchForm
from lab_manager import db

main = Blueprint('main', __name__)

@main.route("/")
@login_required
def home():
    return redirect(url_for("users.profile"))


@main.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
        g.search_form = SearchForm()
 