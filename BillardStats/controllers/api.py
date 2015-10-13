import flask

from BillardStats import models
from BillardStats.controllers import jsonify

api_view = flask.Blueprint('api', __name__)

"""
Here we do the routes...
example:

@api_view.route('/foo')
def foo():
    return 'BAR'

The following would return 'BAR' when visiting /api/foo
"""

@api_view.route('/foo')
def foo():
    return 'BAR'

@api_view.route('/games', methods=['GET'])
@jsonify
def get_games():
    is_raw = flask.request.args.get('raw', False)
    games = models.Game.query
    return [g.to_dict(raw=is_raw) for g in games], 200, None
