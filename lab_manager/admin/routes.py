from flask import render_template, Blueprint, redirect, flash, url_for, abort
from flask_login import current_user
from lab_manager.users.forms import Registration, Login
from functools import wraps

admin = Blueprint('admin', __name__)


@admin.errorhandler(403)
def forbidden_403(exception):
    return 'Admin access only', 403


def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("It did something")
        if current_user.is_anonymous:
            flash("Please log in to use this site.", "info")
            return redirect(url_for('admin.login'))
        if not current_user.admin:
            abort(403)
        return func(*args, **kwargs)
    return wrapper


@admin.route("/admin/register", methods = ['GET', 'POST'])
def register():

    form = Registration()
    if form.validate_on_submit():
        flash(f'Admin {form.username} registered successfully! Go to you profile page and update your personal information.', category='success')
        return redirect('/success')

    return render_template('admin/register.jinja2', title='Admin Register', form=form)


@admin.route("/admin/login", methods = ['GET', 'POST'])
def login():

    form = Login()
    if form.validate_on_submit():
        flash(f'Admin {form.username} logged in successfully!', category='success')
        return redirect('/success')

    return render_template('admin/login.jinja2', title='Admin Login', form=form)


@admin.route("/admin")
@admin_only
def admin_dash():
    return render_template('admin/dashboard.jinja2', title = "Admin Dashboard")

