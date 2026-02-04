from dicegame.session.session_disk import Session


class AppError(Exception):
    """Base class for all domain errors"""
    pass


class AuthError(AppError):
    """Raises unspecified authentication errors"""
    pass


class ResetScoreError(AppError):
    """Raise errrors related to the reset score command"""
    pass


class ResetPasswordError(AppError):
    """Raise errrors related to the reset password command"""
    pass


class UnknownCommandError(AppError):
    """Raised if a command is unknown"""
    pass


class NotLoggedInError(AppError):
    """Raised when a user tries to logout and there's no active session present"""
    pass


class TooManyInvalidAttemptsError(AppError):
    """Raised when a user enters too many failed attempts"""
    def __str__(self):
        return "Too many invalid attempts"


class AllfieldsAreRequiredError(AppError):
    """Raised if user leaves any required field(s) blank"""
    pass


class UserAlreadyExistsError(AppError):
    """Aborts signup process if the username entered is  already registered"""
    def __init__(self,username):
        self.username = username


    def __str__(self):
        return f"The Username '{self.username}' already exists!"


class UserNotFoundError(AppError):
    """Raised if a user's credentials are incorrect"""
    def __str__(self):
        return f"Wrong username or password"


class AlreadyLoggedInError(AppError):
    """Raised when the login command is called and an active session is currently running"""
    def __init__(self,username):
        self.username = username


    def __str__(self):
        return f"You're already logged in as {self.username}\nLog out first to access login or signup"



# FUNCTIONS
def not_logged_in(session: Session):
    """Raises AuthError if a user is not logged in"""

    # Ensure player is logged in
    if not session or not session.logged_in:
        raise AuthError("Log in required to perform this action")

    return
