class Config:
    SECRET_KEY = "SUPERSECRETCODE"
    DB_NAME = "database.db"
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'