from flask import render_template, Blueprint, redirect, flash, url_for
from lab_manager.users.forms import Registration, Login
from lab_manager import db
from lab_manager.models import User
from flask_login import current_user 

users = Blueprint('users', __name__)


@users.route("/register", methods = ['GET', 'POST'])
def register():
    """ Register Route

        Parameters  :   None
        Methods     :   GET, POST
        Redirect to :   User Dashboard when successfull

    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = Registration()
    if form.validate_on_submit():

        #Verify if email or grr is already in use
        email_exists = User.query.filter_by(email=form.email.data).first()
        grr_exists = User.query.filter_by(grr=form.grr.data).first()

        user = User(name=form.name.data, email=form.email.data, password=form.password.data, grr=form.grr.data, project=form.project.data)
        db.session.add(user)
        db.session.commit()

        flash(f'User {form.email} registered successfully! Go to you profile page and update your personal information.', category='success')

        return redirect(url_for('users.login'))

    return render_template('register.jinja2', title='Register', form=form)


@users.route("/login", methods = ['GET', 'POST'])
def login():

    form = Login()
    if form.validate_on_submit():
        flash(f'User {form.username} logged in successfully!', category='success')
        return redirect('/success')

    return render_template('login.jinja2', title='Login', form=form)