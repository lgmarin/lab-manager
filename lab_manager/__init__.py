import os
from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch

import logging
from logging.handlers import RotatingFileHandler

from config import Config

db = SQLAlchemy()
migrate = Migrate()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    """ Create Flask APP
        Appname = app
    """ 
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None
        
    #Load Main Blueprints
    from lab_manager.main.routes import main
    app.register_blueprint(main)

    #Load Users Blueprints
    from lab_manager.users.routes import users
    app.register_blueprint(users)

    #Load Admin Blueprints
    from lab_manager.admin.routes import admin
    app.register_blueprint(admin)

    #Load Posts Blueprints
    from lab_manager.posts.routes import posts
    app.register_blueprint(posts)

    #Load DB Models
    from .models import User, Project, Post

    #Load Login Manager
    login_manager.init_app(app)

    #Error Handling Registration
    from lab_manager.errors.errors_handler import errors
    app.register_blueprint(errors)

    #Loggin Errors
    if not os.path.exists('logs'):
        os.mkdir('logs')
    
    file_handler = RotatingFileHandler('logs/labmanager.log', maxBytes=10240, backupCount=5)
    
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('LabManager started!')
        

    @login_manager.user_loader
    def load_user(id):
        """Login manager user reload callback
        """
        return User.query.get(int(id))    
    
    return app