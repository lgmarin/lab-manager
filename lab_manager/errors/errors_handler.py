from lab_manager import db
from flask import render_template, Blueprint
from flask_login import current_user

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def notFoundError(error):
    return render_template('errors/404.jinja2', user = current_user), 404

@errors.app_errorhandler(500)
def internalServerError(error):
    # User app_errorhandler to avoid circular import error]
    db.session.rollback()
    return render_template('errors/500.jinja2', user = current_user), 500
