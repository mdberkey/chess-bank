from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from init_app import app, db, login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    games = db.relationship('Game', backref='player')


    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Game(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    link = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80))
    outcome = db.Column(db.Integer)
    notes = db.Column(db.String(80))
    player_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Game: {self.link}>'
