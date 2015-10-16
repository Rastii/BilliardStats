import flask
import json
import functools
import werkzeug.exceptions
import BillardStats

class Error(Exception):
    code = None

    def __init__(self, msg=None):
        Exception.__init__(self, msg or self.__class__.__name__)

class ViewError(Error):
    """

    """
    code = 400
    msg = "An unhandled error has occurred"

class InvalidOrMissingParameter(ViewError):
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

class DuplicateEntity(ViewError):
    """
    The request could not be completed due to a conflict with the current state
    of the resource. This code is only allowed in situations where it is
    expected that the user might be able to resolve the conflict and resubmit
    the request. The response body SHOULD include enough information for the
    user to recognize the source of the conflict. Ideally, the response entity
    would include enough information for the user or user agent to fix the
    problem; however, that might not be possible and is not required.
    """
    code = 409


def __formatted_data(data={}, msg=None, status=None):
    return {
        'data': data,
        'msg': msg,
        'status': status
    }


def __formatted_response(formatted_data, mimetype=None):
    return flask.Response(json.dumps(formatted_data),
                          mimetype=mimetype)


def json_response(method):
    @functools.wraps(method)
    def inner(*args, **kwargs):
        try:
            data, status, msg = method(*args, **kwargs)
            formatted_data = __formatted_data(data=data,
                                              status=status,
                                              msg=msg)

        except werkzeug.exceptions.HTTPException as e:
            formatted_data = __formatted_data(status=e.code,
                                              msg=e.description)
        except ViewError as e:
            formatted_data = __formatted_data(status=e.code, msg=e.message)
        #We want to log ALL exceptions.  If we are in DEBUG mode, then have
        #werkzeug display the trace
        except Exception as e:
            BillardStats.app.logger.exception(e)
            if BillardStats.app.debug:
                raise
            formatted_data = __formatted_data(
                status=400,
                msg='An unhandled error has occured')

        return __formatted_response(formatted_data, mimetype='application/json')

    return inner

