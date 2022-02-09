""" Models for the SQLAlchemy Structure
    
    Laboratory Manager
    Developper: Luiz Marin
"""
from . import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    """ User Model
    
        Columns:

            id              :   Integer
            email           :   String
            username        :   String
            name            :   String
            password        :   String

            grr             :   Integer
            course          :   String

            date_created    :   DateTime
            approved        :   Boolean (Default = False)
            biometry        :   Boolean (Default = False)
            
            project         :   Relationship - Project
            approved_by     :   Relationship - Admin
            approved_in     :   DateTime

            admin           :   Boolean (Default = False)
    """
    #Basic ID for users
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), unique = True)
    username = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(100))

    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    biometry = db.Column(db.Boolean, default = False, nullable = False)
    project = db.Column(db.Integer, db.ForeignKey('project.id'), nullable = False)

    #Profile Data
    grr = db.Column(db.Integer, unique = True)
    course = db.Column(db.String(50))

    #Relationships
    approved_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_approved = db.Column(db.DateTime, default = datetime.utcnow)
    approved = db.Column(db.Boolean, default = False, nullable = False)
    admin = db.Column(db.Boolean, default = False, nullable = False)


class Project(db.Model):
    """ Project Model
    
        Columns:

            id              :   Integer
            name            :   String
            date_created    :   DateTime
            active          :   Boolean (Default = True)
            created_by      :   String (Relationship - User Model)
    """
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique = True)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    active = db.Column(db.Boolean, default=True, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))