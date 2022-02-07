from flask import render_template, Blueprint
from lab_manager.users.forms import Registration, Login

users = Blueprint('users', __name__)

@users.route("/register", methods = ['GET', 'POST'])
def register():

    form = Registration()

    return render_template('register.jinja2', title='Register', form=form)

@users.route("/login", methods = ['GET', 'POST'])
def login():

    form = Login()

    return render_template('login.jinja2', title='Login', form=form)