from flask import render_template, Blueprint, redirect, flash, url_for, request
from lab_manager import db
from lab_manager.models import Post, Comment
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


@posts.route("/posts/edit/<id>", methods=['GET', 'POST'])
@login_required
def edit_post(id: int):
    """ Edit Post Route

        Parameters  :   None
        Methods     :   GET, POST
        Redirect to :   Main page
    """
    post = Post.query.filter_by(id=id).first()
    text = request.form.get("post-text")

    if request.method == 'POST':
        if not post:
            flash("Post does not exist!", 'danger')
        elif post.author != current_user.id:
            flash("You don't have permission to edit this post!", 'danger')
        elif text is None:
            flash("Your post should not be empty!", 'danger')
        else:
            post.text = text
            db.session.add(post)
            db.session.commit()

        return redirect(url_for('users.profile'))

    return redirect(url_for('users.profile'))


@posts.route("/comment/<post_id>", methods=['GET', 'POST'])
@login_required
def create_comment(post_id):
    """ Create Comment Route

        Parameters  :   post id
        
        Methods     :   GET, POST

        Redirect to :   Main page when successfull
    """
    if request.method == 'POST':
        text = request.form.get('text')
        if not text:
            flash("Your comment should not be empty!", category='error')
        else:
            comment = Comment(text=text, author=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
            flash("Comment created!", 'success')
            return redirect(url_for('users.profile'))

    return render_template('create-comment.html.j2', user = current_user)


@posts.route("/comment/delete/<comment_id>")
@login_required
def delete_comment(comment_id):
    """ Delete Comment Route

        Parameters  :   comment id
        
        Methods     :   None

        Redirect to :   Main page when successfull
    """
    comment = Comment.query.filter_by(id=id).first()

    if not comment:
        flash("Comment does not exist!", category='error')
    elif current_user.id != comment.author and current_user.id != comment.post.author:
        flash("You don\'t have permission to delete this post!", category='error')
    else:
        db.session.delete(comment)
        db.session.commit()
        flash("Comment deleted!")

    return redirect(url_for('users.profile'))