class Config:
    SECRET_KEY = "bf4bd5bd26c6dbefa05f29c1a8f87060"
    DB_NAME = "database.db"
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False