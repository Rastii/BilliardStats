import BilliardStats.models as models
import BilliardStats.controllers
import sqlalchemy

def get_games():
    games = models.Game.query.order_by(sqlalchemy.desc(models.Game.end_time))
    return [g.to_dict() for g in games]

def get_game(game_id):
    game = models.Game.query.filter(models.Game.id == game_id).first()

    if not game:
        return {}

    return game.to_dict()

def add_game(winning_user_id, loser_user_id, start_time=None, end_time=None):
    """
    Add a game to the DB.
    Note: It is expected that the view already parsed and validated
          start_time / end_time
    """

    #First make sure that both user_ids are valid
    users = models.User.query.filter(models.User.id.in_(
        [winning_user_id, loser_user_id]
    )).all()

    if len(users) != 2:
        raise BilliardStats.controllers.UnknownUser(
            'An invalid user_id was specified')

    game = models.Game(winning_user_id=winning_user_id,
                       loser_user_id=loser_user_id,
                       start_time=start_time,
                       end_time=end_time)

    models.db.session.add(game)
    models.db.session.commit()

    return game.to_dict()
