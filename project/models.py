

from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.Text(), unique=False, nullable=False)
    imageb64 = db.Column(db.Text(), unique=False, nullable=False)

    def __init__(self, name, description, imageb64):
        self.name = name
        self.description = description
        self.imageb64 = imageb64
