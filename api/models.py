from datetime import datetime
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.String)
    view = db.Column(db.Integer, default=0)
    created_date = db.Column(db.String, default=datetime.now())

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# run this codes to create database
# from api.models import User, ...
# from api import db, create_app
# db.create_all(app=create_app())