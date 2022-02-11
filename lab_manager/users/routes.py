from flask import render_template, Blueprint, redirect, flash, url_for
from lab_manager.users.forms import Registration, Login
from lab_manager import db
from lab_manager.models import User
from flask_login import current_user, login_user, logout_user, login_required

users = Blueprint('users', __name__)


@users.route("/register", methods = ['GET', 'POST'])
def register():
    """ Register Route

        Parameters  :   None
        Methods     :   GET, POST
        Redirect to :   Login page when successfull
    """
    if current_user.is_authenticated:
        flash("User already logged in!", 'info')
        return redirect(url_for('users.profile'))

    form = Registration()

    if form.validate_on_submit():

        #Verify if email or grr is already in use
        # email_exists = User.query.filter_by(email=form.email.data).first()
        # grr_exists = User.query.filter_by(grr=form.grr.data).first()

        user = User(
            name=form.name.data, 
            email=form.email.data, 
            grr=form.grr.data, 
            course=form.course.data,
            project=form.project.data
            )
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash(f'User {form.email.data} registered successfully! Go to you profile page and update your personal information.', 'success')

        return redirect(url_for('users.login'))

    return render_template('users/register.jinja2', title='Register', form=form, user=current_user)


@users.route("/login", methods = ['GET', 'POST'])
def login():
    """ User Login Route

        Parameters  :   None
        Methods     :   GET, POST
        Redirect to :   User Dashboard when successfull, Home if already Logged In
    """
    if current_user.is_authenticated:
        flash("User already logged in!", 'info')
        return redirect(url_for('users.profile'))

    form = Login()

    if form.validate_on_submit():
        
        user = User.query.filter_by(email=form.email.data).first()

        if user is None or user.check_password(form.password.data):
            flash("Invalid username or password!", 'danger')
            return redirect(url_for('users.login'))
        else:
            login_user(user)
            flash(f'User {form.email.data} logged in successfully!', 'success')
            return redirect(url_for('users.profile'))

    return render_template('users/login.jinja2', title='Login', form=form, user=current_user)


@users.route("/logout")
def logout():
    logout_user()
    flash('User logged out successfully!', 'success')
    return redirect(url_for('main.home'))


@users.route("/profile")
@login_required
def profile():
    """ User Profile Route

        Parameters  :   None
        Methods     :   None
        Redirect to :   User Profile
    """
    return render_template('users/profile.jinja2', title=current_user.name + ' Profile', user=current_user)