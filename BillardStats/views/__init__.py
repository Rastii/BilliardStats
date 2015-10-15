import flask
import json
import functools
import werkzeug.exceptions

class Error(Exception):
    code = None

    def __init__(self, msg=None):
        Exception.__init__(self, msg or self.__class__.__name__)

class ViewError(Error):
    """

    """
    code = 400
    msg = "An unhandled request has occured"

class MissingRequiredParameter(ViewError):
    """
    Erorr used with missing parameter
    The 422 (Unprocessable Entity) status code means the server
    understands the content type of the request entity (hence a
    415(Unsupported Media Type) status code is inappropriate), and the
    syntax of the request entity is correct (thus a 400 (Bad Request)
    status code is inappropriate) but was unable to process the contained
    instructions.  For example, this error condition may occur if an XML
    request body contains well-formed (i.e., syntactically correct), but
    semantically erroneous, XML instructions.

    """
    code = 422



def jsonify(method):
    default_formatted_data = {
        'data': {},
        'status': 400,
        'msg': 'An unhandled request occured'
    }
    @functools.wraps(method)
    def inner(*args, **kwargs):
        formatted_data = default_formatted_data
        try:
            data, status, msg = method(*args, **kwargs)
            formatted_data = {
                'data': data,
                'status': status,
            }
            if msg:
                formatted_data['msg'] = msg

        except werkzeug.exceptions.HTTPException as e:
            formatted_data = {
                'data': {},
                'status': e.code,
                'msg': e.description
            }
        except ViewError as e:
            formatted_data = {
                'data': {},
                'status': e.code,
                'msg': e.message
            }
        finally:
            return flask.Response(json.dumps(formatted_data),
                                  mimetype='application/json')

    return inner

