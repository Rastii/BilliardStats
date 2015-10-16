import flask

import BillardStats.controllers
import BillardStats.controllers.games as games_controller
import BillardStats.views

games_view = flask.Blueprint('games', __name__)

@games_view.route('/', methods=['GET'])
@BillardStats.views.json_response
def get_games():
    games = games_controller.get_games()
    return games, 200, None

@games_view.route('/<int:game_id>/', methods=['GET'])
@BillardStats.views.json_response
def get_game(game_id):
    game = games_controller.get_game(game_id)
    return game, 200, None

@games_view.route('/', methods=['POST'])
@BillardStats.views.json_response
def add_game():
    args = flask.request.form

    if not args.get('winning_user_id') or not args.get('losing_user_id'):
        raise BillardStats.views.InvalidOrMissingParameter(
            'winning_user_id and losing_user_id is required')
    try:
        result = games_controller.add_game(args.get('winning_user_id'),
                                           args.get('losing_user_id'),
                                           start_time=args.get('start_time'))

    except BillardStats.controllers.UnknownUser as e:
        raise BillardStats.views.InvalidOrMissingParameter(e.msg)

    return result, 200, None