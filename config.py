import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bf4bd5bd26c6dbefa05f29c1a8f87060'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
        os.getenv('DB_USER', 'lab_manager'),
        os.getenv('DB_PASSWORD', ''),
        os.getenv('DB_HOST', 'mysql'),
        os.getenv('DB_NAME', 'lab_manager')
    )

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
    #     'postgres://', 'postgresql://') or \
    #     'sqlite:///' + os.path.join(basedir, 'database.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTS_PER_PAGE = 4
    ELASTICSEARCH_URL= os.environ.get('ELASTICSEARCH_URL') or 'http://localhost:9200'