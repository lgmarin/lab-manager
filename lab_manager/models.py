""" Models for the SQLAlchemy Structure
    
    Laboratory Manager
    Developper: Luiz Marin
"""
from lab_manager.search import add_to_index, query_index, remove_from_index
from . import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash


class SearchableMixin(object):
    """
    When attached to a model, will give it the ability to automatically manage an associated full-text index
    """
    @classmethod
    def search(cls, expression, page, per_page):
        ids, total = query_index(cls.__tablename__, expression, page, per_page)
        if total == 0:
            return cls.query.filter_by(id=0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in_(ids)).order_by(
            db.case(when, value=cls.id)), total

    @classmethod
    def before_commit(cls, session):
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }

    @classmethod
    def after_commit(cls, session):
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes = None

    @classmethod
    def reindex(cls):
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)

db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)


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
            approved_by     :   String
            approved_in     :   DateTime

            admin           :   Boolean (Default = False)

            posts           :   Relationship - Posts    
            comments        :   Relationship - Comments   
    """
    #Basic ID for users
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(150))
    password = db.Column(db.String(128))

    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    biometry = db.Column(db.Boolean, default = False, nullable = False)
    project = db.Column(db.Integer, nullable = True)

    #Profile Data
    grr = db.Column(db.Integer, unique = True)
    course = db.Column(db.String(50))

    #Relationships
    approved_by = db.Column(db.Integer)
    date_approved = db.Column(db.DateTime, default = datetime.utcnow)
    approved = db.Column(db.Boolean, default = False, nullable = False)
    admin = db.Column(db.Boolean, default = False, nullable = False)

    projects = db.relationship('Project', backref="user", passive_deletes = False)
    posts = db.relationship('Post', backref="user", passive_deletes = True)
    comments = db.relationship('Comment', backref="user", passive_deletes = True)

    def set_password(self, password_form):
        #Set Password, store hashed password on DB
        self.password = generate_password_hash(password_form)

    def check_password(self, password_form):
        #Check password based on the stored hash
        return check_password_hash(self.password, password_form)

    def create_password(new_pass):
        return generate_password_hash(new_pass)


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
    reserved = db.Column(db.Boolean, default=False, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))


class Post(SearchableMixin, db.Model):
    """ Post Model

        Columns:

            id              :   Integer
            text            :   Text
            date_created    :   DateTime
            author          :   Integer            

        Relatiosnhips:

            comments        :   Comment Model
    """
    __searchable__ = ['text']

    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text, nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable = False)

    comments = db.relationship('Comment', backref="post", passive_deletes=True)

class Comment(db.Model):
    """ Comment Model

        Columns:

            id              :   Integer
            text            :   Text
            date_created    :   DateTime
            author          :   Integer            
            post_id         :   Integer

    """

    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text, nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable = False)
