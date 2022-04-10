"""
This file (test_models.py) contains the unit tests for the models.py file.
"""
from lab_manager.models import User


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password_hashed, authenticated, and active fields are defined correctly
    """
    user = User(
        name="Test Mr Anderson", 
        email="chosen@one.com", 
        grr=256428, 
        course="Mechanical Engineering"
    )
    user.set_password("Trinity123")

    assert user.email == 'chosen@one.com'
    assert user.check_password("Trinity123")


def test_setting_password(new_user):
    """
    GIVEN an existing User
    WHEN the password for the user is set
    THEN check the password is stored correctly and not as plaintext
    """
    new_user.set_password('MyNewPassword')
    assert new_user.check_password('MyNewPassword')
    assert not new_user.check_password('MyNewPassword2')
    assert not new_user.check_password('TESTSTSST')
