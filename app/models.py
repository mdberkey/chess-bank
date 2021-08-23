from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    """
    User Model
    """
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    games = db.relationship('Game', backref='player')


class Game(db.Model):
    """
    Game model related to a defined user
    """
    id = db.Column(db.Integer, unique=True, primary_key=True)
    link = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80))
    outcome = db.Column(db.Integer)
    notes = db.Column(db.String(80))
    player_id = db.Column(db.Integer, db.ForeignKey('user.id'))
