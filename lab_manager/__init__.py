from flask import Flask
from os import path
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from lab_manager.config import Config


db = SQLAlchemy()
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
    # login_manager.init_app(app)

    #Load Main Blueprints
    from lab_manager.main.routes import main
    app.register_blueprint(main)

    #Load Users Blueprints
    from lab_manager.users.routes import users
    app.register_blueprint(users)

    #Load Admin Blueprints
    from lab_manager.admin.routes import admin
    app.register_blueprint(admin)

    #Load DB Models
    from .models import User, Project

    initialize_database(app)

    #Load Login Manager
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        """Login manager user reload callback
        """
        return User.query.get(int(id))    
    
    return app

def initialize_database(app):
    """ Initialize DB - Create if none found
    """
    if not path.exists("lab_manager/" + Config.DB_NAME):
        db.create_all(app=app)
        print("Database Created!")