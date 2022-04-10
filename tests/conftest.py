import pytest

from lab_manager import create_app, db
from lab_manager.models import User


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ELASTICSEARCH_URL = None    


@pytest.fixture(scope='module')
def new_user():
    user = User(
    name="Test Mr Anderson", 
    email="chosen@one.com", 
    grr=256428, 
    course="Mechanical Engineering"
    )
    user.set_password("Trinity123")

    return user


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(TestConfig)

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    user1 = User(
        name="Test Mr Anderson", 
        email="chosen@one.com", 
        grr=256428, 
        course="Mechanical Engineering"
    )
    user1.set_password("Trinity123")

    user2 = User(
        name="Test Trinity", 
        email="trinity@matrix.com", 
        grr=564882, 
        course="Mechanical Engineering"
    )
    user2.set_password("NeoGostoso123")

    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()


@pytest.fixture(scope='function')
def login_default_user(test_client):
    test_client.post('/login',
                     data=dict(email='chosen@one.com', password='Trinity123'),
                     follow_redirects=True)

    yield  # this is where the testing happens!

    test_client.get('/logout', follow_redirects=True)
