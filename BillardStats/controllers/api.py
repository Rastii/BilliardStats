import BillardStats.models as models
import BillardStats.controllers

# USER ROUTES
def get_users():
    users = models.User.query
    return [u.to_dict() for u in users]

def get_user(user_id=None, username=None):
    if user_id:
        user = models.User.query.filter(models.User.id == user_id).first()
    else:
        user = models.User.query.filter(models.User.name == username).first()

    if not user:
        return {}

    return user.to_dict()

def get_user_wins(user_id):
    wins = models.Game.query\
        .filter(models.Game.winner_user_id == user_id)\
        .order_by(models.Game.end_time.desc())
    return [w.to_dict() for w in wins]

def get_user_losses(user_id):
    losses = models.Game.query\
        .filter(models.Game.loser_user_id == user_id)\
        .order_by(models.Game.end_time.desc())
    return [w.to_dict() for w in losses]

def add_user(username):
    #Check if User exists
    if get_user(username=username):
        raise BillardStats.controllers.DuplicateEntity(
            'Username "%s" already exists' % username)

    #Doesn't exist, let's create the user.
    user = models.User(username)
    models.db.session.add(user)
    models.db.session.commit()

    #We want to return the user info so the requester has the new ID
    return user.to_dict()


# GAME ROUTES
def get_games():
    games = models.Game.query
    return [g.to_dict() for g in games]

def get_game(game_id):
    game = models.Game.query.filter(models.Game.id == game_id).first()

    if not game:
        return {}

    return game.to_dict()

