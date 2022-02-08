""" Models for the SQLAlchemy Structure
    
    Laboratory Manager
    Developper: Luiz Marin
"""
from . import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    """ User Model - Non Admin Access
    
        Columns:

            id              :   Integer
            username        :   String
            email           :   String
            name            :   String
            grr             :   Integer
            password        :   String
            date_created    :   DateTime
            approved        :   Boolean (Default = False)
            biometry        :   Boolean (Default = False)
            
            project         :   Relationship - Project
            approved_by     :   Relationship - Admin
            approved_in     :   DateTime

    """

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True)
    username = db.Column(db.String(100), unique = True)
    name = db.Column(db.String(150), unique = True)
    grr = db.Column(db.Integer, unique = True)
    password = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    approved = db.Column(db.Boolean, default=False, nullable=False)
    biometry = db.Column(db.Boolean, default=False, nullable=False)

    project = db.Column(db.Integer, db.ForeignKey('project.id'), nullable = False)
    approved_by = db.Column(db.Integer, db.ForeignKey('admin.id'))

class Project(db.Model):
    """ Project Model
    
        Columns:

            id              :   Integer
            name            :   String
            date_created    :   DateTime
            active          :   Boolean (Default = True)

    """
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique = True)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    active = db.Column(db.Boolean, default=True, nullable=False)
    admin = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable = False)


class Admin(db.Model, UserMixin):
    """ User Model - Non Admin Access
    
        Columns:

            id              :   Integer
            username        :   String
            email           :   String
            name            :   String
            password        :   String
            biometry        :   Boolean (Default = False)
            active          :   Boolean (Default = True)
            date_created    :   DateTime

        Relationships:

            users           :   User Model

    """

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True)
    username = db.Column(db.String(100), unique = True)
    name = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    biometry = db.Column(db.Boolean, default=False, nullable=False)