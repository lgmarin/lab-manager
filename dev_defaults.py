""" FOR DEV AND DEBUGGING ONLY
    THIS WILL BE REMOVED LATTER
""" 
from lab_manager import db
from lab_manager.models import User

admin = User(name="Administrador Adm", email="admin@adminmail.com", admin=True)
admin.set_password("12345678")

db.session.add(admin)
db.session.commit()