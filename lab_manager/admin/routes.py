from flask import render_template, Blueprint, redirect, flash, url_for, abort, request
from flask_login import current_user, login_user, logout_user
from lab_manager.users.forms import Registration, Login
from lab_manager import db
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


""" Admin Login / Logout Routes
"""

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


@admin.route("/logout")
@admin_only
def logout():
    logout_user()
    flash('User logged out successfully!', 'success')
    return redirect(url_for('main.home'))


@admin.route("/admin")
@admin_only
def dashboard():
    return render_template('admin/dashboard.jinja2', title = "Admin Dashboard", user=current_user)


""" Admin Users Management Routes Routes
"""

@admin.route("/admin/users")
@admin_only
def users():
    """ Admin Manage Users Route

        Parameters  :   None
        Methods     :   None
        Redirect to :   Users management page
    """     

    users = User.query

    return render_template('admin/users.jinja2', title = "Users", users=users, user=current_user)


""" Admin Projects Management Routes Routes
"""

@admin.route("/admin/projects")
@admin_only
def projects():
    """ Admin Manage Projects Route

        Parameters  :   None
        Methods     :   None
        Redirect to :   Projects management page
    """     

    projects = Project.query

    return render_template('admin/projects.jinja2', title = "Projects", projects=projects, user=current_user)

@admin.route("/admin/projects/add", methods = ['GET', 'POST'])
@admin_only
def add_project():
    """ Admin Manage Projects Route - Add New Project

        Parameters  :   None
        Methods     :   GET, POST
        Redirect to :   Projects management page
    """
    if request.method == 'POST':

        name = request.form.get('project-name')

        #Verify if the project already exists
        project_exists = Project.query.filter_by(name=name).first()
        
        if not name:
            flash("The project name should not be empty!", 'warning')
        elif project_exists:
            flash("The project name already exists!", 'warning')
        else:
            project = Project(name=name, active=True, created_by=current_user.id)
            db.session.add(project)
            db.session.commit()

            flash("New project created successfully!", 'success')

            return redirect(url_for('admin.projects'))

    return redirect(url_for('admin.projects'))


@admin.route("/admin/projects/edit", methods = ['GET', 'POST'])
@admin_only
def edit_project():
    """ Admin Manage Projects Route - Edit Project

        Parameters  :   None
        Methods     :   GET, POST
        Redirect to :   Projects management page
    """
    project = Project.query.filter_by(id=(request.form.get('id'))).first()

    if not project:
        flash("The project does not exist!", 'warning')
    elif request.method == 'POST':
        project.name = request.form.get('project-name')

        db.session.add(project)
        db.session.commit()

        flash("Project updated successfully!", 'success')

        return redirect(url_for('admin.projects'))

    return redirect(url_for('admin.projects'))

