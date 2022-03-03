from flask import render_template, Blueprint, redirect, flash, url_for, request
from lab_manager import db
from lab_manager.models import Post
from flask_login import current_user, login_user, logout_user, login_required

posts = Blueprint('posts', __name__)

@posts.route("/post/create", methods = ['GET', 'POST'])
@login_required
def create_post():
    """ Create Route

        Parameters  :   None
        Methods     :   GET, POST
        Redirect to :   Main page
    """
    if request.method == 'POST':

        text = request.form.get('post-text')

        if not text:
            flash("Your post should not be empty!", 'warning')
        else:
            post = Post(text = text, author = current_user.id)
            db.session.add(post)
            db.session.commit()

            flash("Post created!", 'success')

            return redirect(url_for('users.profile'))

    return redirect(url_for('users.profile'))

