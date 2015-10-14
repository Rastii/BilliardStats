import flask
import BillardStats.controllers.api as api_controller

from flask_restful import reqparse
from BillardStats.views import jsonify

api_view = flask.Blueprint('api', __name__)

@api_view.route('/games', methods=['GET'])
@jsonify
def get_games():
    games = api_controller.get_games()
    return (games, 200, None)

@api_view.route('/users', methods=['GET'])
@jsonify
def get_users():
    users = api_controller.get_users()
    return users, 200, None

@api_view.route('/users/<int:user_id>/wins', methods=['GET'])
@jsonify
def get_user_wins(user_id):
    user_wins = api_controller.get_user_wins(user_id)
    return user_wins, 200, None