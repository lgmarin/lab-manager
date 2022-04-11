import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bf4bd5bd26c6dbefa05f29c1a8f87060'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
        os.getenv('DB_USER', 'root'),
        os.getenv('DB_PASSWORD', 'biscoito'),
        os.getenv('DB_HOST', 'localhost'),
        os.getenv('DB_NAME', 'lab_manager')
    )

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
    #     'postgres://', 'postgresql://') or \
    #     'sqlite:///' + os.path.join(basedir, 'database.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTS_PER_PAGE = 4
    ELASTICSEARCH_URL= os.environ.get('ELASTICSEARCH_URL') or 'http://localhost:9200'