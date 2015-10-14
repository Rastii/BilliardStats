import flask
import json
import functools


def jsonify(method):
    @functools.wraps(method)
    def inner(*args, **kwargs):
        #TODO: Catch view exceptions here and wrap in appropriate exception class
        data, status, msg = method(*args, **kwargs)
        formatted_data = {
            'data': data,
            'status': status,
        }
        if msg:
            formatted_data['msg'] = msg

        return flask.Response(json.dumps(formatted_data),
                              mimetype='application/json')

    return inner
