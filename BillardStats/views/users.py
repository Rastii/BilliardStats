import flask

from flask_restful import reqparse

import BillardStats.views
import BillardStats.controllers
import BillardStats.controllers.users as users_controller

users_view = flask.Blueprint('users', __name__)

@users_view.route('/', methods=['GET'])
@BillardStats.views.json_response
def get_users():
    users = users_controller.get_users()
    return users, 200, None

@users_view.route('/', methods=['POST'])
@BillardStats.views.json_response
def add_user():
    args = flask.request.form

    username = args.get('username', None)
    if not username:
        raise BillardStats.views.InvalidOrMissingParameter(
            'A username is required')

    try:
        user = users_controller.add_user(username)
    except BillardStats.controllers.DuplicateUser as e:
        raise BillardStats.views.DuplicateEntity(e.message)

    return user, 200, None

@users_view.route('/<int:user_id>/', methods=['GET'])
@BillardStats.views.json_response
def get_user(user_id):
    user = users_controller.get_user(user_id=user_id)
    return user, 200, None

@users_view.route('/<int:user_id>/wins', methods=['GET'])
@BillardStats.views.json_response
def get_user_wins(user_id):
    user_wins = users_controller.get_user_wins(user_id)
    return user_wins, 200, None

@users_view.route('/<int:user_id>/losses', methods=['GET'])
@BillardStats.views.json_response
def get_user_losses(user_id):
    try:
        user_losses = users_controller.get_user_losses(user_id)
    except BillardStats.controllers.UnknownUser as e:
        raise BillardStats.views.InvalidOrMissingParameter(e.message)

    return user_losses, 200, None

