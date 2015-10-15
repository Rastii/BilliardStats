import flask

from flask_restful import reqparse
from BillardStats.views import jsonify
import BillardStats.controllers.users as users_controller

users_view = flask.Blueprint('users', __name__)

@users_view.route('/', methods=['GET'])
@jsonify
def get_users():
    users = users_controller.get_users()
    return users, 200, None

@users_view.route('/<int:user_id>/wins', methods=['GET'])
@jsonify
def get_user_wins(user_id):
    user_wins = users_controller.get_user_wins(user_id)
    return user_wins, 200, None