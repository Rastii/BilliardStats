

class Error(Exception):
    def __init__(self, msg=None):
        Exception.__init__(self, msg or self.__class__.__name__)

class ControllerError(Error):
    """
    """

class DuplicateUser(ControllerError):
    """
    This exception is raised when the DB already contains an user,
    example: "User1" already exists when attempting to create a new user
    with the name of "User1"
    """

class UnknownUser(ControllerError):
    """
    An unknown user was specified.  Typically if an invalid id or username
    is passed
    """
