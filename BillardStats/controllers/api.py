import flask

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