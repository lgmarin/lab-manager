from flask import render_template, Blueprint, redirect, flash
from lab_manager.users.forms import Registration, Login

users = Blueprint('users', __name__)

@users.route("/register", methods = ['GET', 'POST'])
def register():

    form = Registration()
    if form.validate_on_submit():
        flash(f'User {form.username} registered successfully! Go to you profile page and update your personal information.', category='success')
        return redirect('/success')

    return render_template('register.jinja2', title='Register', form=form)

@users.route("/login", methods = ['GET', 'POST'])
def login():

    form = Login()
    if form.validate_on_submit():
        flash(f'User {form.username} logged in successfully!', category='success')
        return redirect('/success')

    return render_template('login.jinja2', title='Login', form=form)