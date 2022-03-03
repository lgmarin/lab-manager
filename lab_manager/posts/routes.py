from flask import render_template, Blueprint, redirect, flash, url_for, request
from lab_manager import db
from lab_manager.models import Post
from flask_login import current_user, login_user, logout_user, login_required


posts = Blueprint('posts', __name__)


@posts.route("/post/create", methods = ['GET', 'POST'])
@login_required
def create_post():
    """ Create Post Route

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


@posts.route("/post/remove/<id>")
@login_required
def remove_post(id: int):
    """ Remove Post Route

        Parameters  :   None
        Methods     :   
        Redirect to :   Main page
    """
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash("Post does not exist!", 'danger')
    elif post.author != current_user.id:
        flash("You don`t have permission to delete this post!", 'danger')
    else:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted!", 'warning')

    return redirect(url_for('users.profile'))