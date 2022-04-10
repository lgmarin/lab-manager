from lab_manager import db
from flask import current_app, render_template

@current_app.errorhandler(404)
def notFoundError(error):
    return render_template('/errors/404.jinja2'), 404

@current_app.errorhandler(500)
def internalServerError(error):
    return render_template('/errors/500.jinja2'), 500
