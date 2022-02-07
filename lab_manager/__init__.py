from flask import Flask
# from flask_login import LoginManager
from lab_manager.config import Config

# login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
# login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # login_manager.init_app(app)

    #Load Blueprints
    from lab_manager.main.routes import main
    from lab_manager.users.routes import users
    #Register Blueprints
    app.register_blueprint(main)
    app.register_blueprint(users)

    return app