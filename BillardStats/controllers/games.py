import BillardStats.models as models
import BillardStats.controllers

def get_games():
    games = models.Game.query
    return [g.to_dict() for g in games]

def get_game(game_id):
    game = models.Game.query.filter(models.Game.id == game_id).first()

    if not game:
        return {}

    return game.to_dict()

def add_game(winning_user_id, loser_using_id, start_time=None, end_time=None):
    #TODO: User id validation
    #TODO: start_time / end_time validation
    game = models.Game(winning_user_id=winning_user_id,
                       loser_user_id=loser_using_id,
                       start_time=start_time,
                       end_time=end_time)

    models.db.session.add(game)
    models.db.session.commit()

    return game.to_dict()
