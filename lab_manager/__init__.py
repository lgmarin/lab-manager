from flask import Flask
from lab_manager.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    #Load Blueprints
    from lab_manager.main.routes import main
    app.register_blueprint(main)

    return app