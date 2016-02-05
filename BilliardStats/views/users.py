import flask

from flask_restful import reqparse

import BilliardStats.views
import BilliardStats.controllers
import BilliardStats.controllers.users as users_controller

users_view = flask.Blueprint('users', __name__)

@users_view.route('/', methods=['GET'])
@BilliardStats.views.json_response
def get_users():
    users = users_controller.get_users()
    return users, 200, None

@users_view.route('/', methods=['POST'])
@BilliardStats.views.json_response
def add_user():
    args = flask.request.form

    username = args.get('username', None)
    if not username:
        raise BilliardStats.views.InvalidOrMissingParameter(
            'A username is required')

    try:
        user = users_controller.add_user(username)
    except BilliardStats.controllers.DuplicateUser as e:
        raise BilliardStats.views.DuplicateEntity(e.message)

    return user, 200, None

@users_view.route('/<int:user_id>/', methods=['GET'])
@BilliardStats.views.json_response
def get_user(user_id):
    user = users_controller.get_user(user_id=user_id)
    return user, 200, None

@users_view.route('/<int:user_id>/wins', methods=['GET'])
@BilliardStats.views.json_response
def get_user_wins(user_id):
    user_wins = users_controller.get_user_wins(user_id)
    return user_wins, 200, None

@users_view.route('/<int:user_id>/losses', methods=['GET'])
@BilliardStats.views.json_response
def get_user_losses(user_id):
    try:
        user_losses = users_controller.get_user_losses(user_id)
    except BilliardStats.controllers.UnknownUser as e:
        raise BilliardStats.views.InvalidOrMissingParameter(e.message)

    return user_losses, 200, None

