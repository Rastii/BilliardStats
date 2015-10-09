from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    wins = db.relationship('Game', foreign_keys='Game.winner_user_id')
    losses = db.relationship('Game', foreign_keys='Game.loser_user_id')

    def __init__(self, name):
        self.name = name

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    winner_user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    loser_user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    winner_user = db.relationship('User', foreign_keys='Game.winner_user_id')
    losing_user = db.relationship('User', foreign_keys='Game.loser_user_id')

    def __init__(self, winning_user, losing_user):
        self.winner_user = winning_user
        self.losing_user = losing_user
