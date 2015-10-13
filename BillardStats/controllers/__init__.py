import flask
import json
import functools


def jsonify(method):
    @functools.wraps(method)
    def inner(*args, **kwargs):
        data, status, msg = method(*args, **kwargs)
        data = {
            'data': data,
            'status': status,
        }
        if msg:
            data['msg'] = msg

        return flask.Response(json.dumps(data), mimetype='application/json')

    return inner