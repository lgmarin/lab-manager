from flask import render_template, Blueprint, redirect, flash, url_for, abort
from flask_login import current_user, login_user, logout_user
from lab_manager.users.forms import Registration, Login
from lab_manager.models import User, Project
from functools import wraps

admin = Blueprint('admin', __name__)


# Error handler to be used together with the admin_only custom decorator
@admin.errorhandler(403)
def forbidden_403(exception):
    return 'Admin access only', 403


def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_anonymous:
            flash("You should be logged in to see this page!", "warning")
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

    return render_template('admin/register.jinja2', title='Admin Register', form=form, user=current_user)


@admin.route("/admin/login", methods = ['GET', 'POST'])
def login():
    """ Admin Login Route

        Parameters  :   None
        Methods     :   GET, POST
        Redirect to :   User Dashboard when successfull, Home if already Logged In
    """    

    if current_user.is_authenticated:
        flash("User is already logged in!", 'info')
        return redirect(url_for("admin.dashboard"))
    
    form = Login()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if not user.admin:
            flash("You are not an administrator, please go to the users login!", 'warning')
            return redirect(url_for("users.login"))
        elif user is None or not user.check_password(form.password.data):
            flash("Invalid username or password!", 'danger')
            return redirect(url_for("admin.login"))
        else:
            login_user(user)
            flash(f'Admin {form.email} logged in successfully!', category='success')
            return redirect(url_for("admin.dashboard"))

    return render_template('admin/login.jinja2', title='Admin Login', form=form, user=current_user)


@admin.route("/admin")
@admin_only
def dashboard():
    return render_template('admin/dashboard.jinja2', title = "Admin Dashboard", user=current_user)


@admin.route("/admin/users")
@admin_only
def users():
    users = User.query

    return render_template('admin/users.jinja2', title = "Users", users=users, user=current_user)


@admin.route("/admin/projects")
@admin_only
def projets():
    projects = Project.query

    return render_template('admin/projects.jinja2', title = "Projects", projects=projects, user=current_user)


@admin.route("/logout")
@admin_only
def logout():
    logout_user()
    flash('User logged out successfully!', 'success')
    return redirect(url_for('main.home'))
