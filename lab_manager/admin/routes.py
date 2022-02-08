from flask import render_template, Blueprint, redirect, flash
from lab_manager.users.forms import Registration, Login

admin = Blueprint('admin', __name__)

@admin.route("/register", methods = ['GET', 'POST'])
def register():

    form = Registration()
    if form.validate_on_submit():
        flash(f'User {form.username} registered successfully! Go to you profile page and update your personal information.', category='success')
        return redirect('/success')

    return render_template('register_adm.jinja2', title='Register', form=form)

@admin.route("/login", methods = ['GET', 'POST'])
def login():

    form = Login()
    if form.validate_on_submit():
        flash(f'User {form.username} logged in successfully!', category='success')
        return redirect('/success')

    return render_template('login_adm.jinja2', title='Login', form=form)