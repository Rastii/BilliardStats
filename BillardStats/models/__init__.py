from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def convert_time(time):
    if not time:
        return None
    return time.strftime('%m-%d-%Y %H:%M:%S')

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    wins = db.relationship('Game', foreign_keys='Game.winner_user_id')
    losses = db.relationship('Game', foreign_keys='Game.loser_user_id')

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    winner_user_id = db.Column(db.Integer,
                               db.ForeignKey('user.id'),
                               nullable=False)
    loser_user_id = db.Column(db.Integer,
                              db.ForeignKey('user.id'),
                              nullable=False)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime, default=datetime.datetime.utcnow())


    winner_user = db.relationship('User', foreign_keys='Game.winner_user_id')
    losing_user = db.relationship('User', foreign_keys='Game.loser_user_id')

    def __init__(self, winning_user=None, losing_user=None,
                 winning_user_id=None, loser_user_id=None,
                 start_time=None, end_time=None):

        if self.winner_user:
            self.winner_user = winning_user
        else:
            self.winner_user_id = winning_user_id

        if self.losing_user:
            self.losing_user = losing_user
        else:
            self.loser_user_id = loser_user_id

        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self, tc=convert_time):
        return {
            'id': self.id,
            'start_time': tc(self.start_time),
            'end_time': tc(self.end_time),
            'winning_user': self.winner_user.to_dict(),
            'losing_user': self.losing_user.to_dict()
        }
