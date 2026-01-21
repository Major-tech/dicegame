class AppError(Exception):
    """Base class for all domain errors"""
    pass


class UserAlreadyExistsError(AppError):
    def __init__(self,username):
        self.username = username


    def __str__(self):
        return f"The Username '{self.username}' already exists!"


class UserNotFoundError(AppError):
    def __str__(self):
        return f"Wrong username or password"


class AccountDeletionNotAllowedError(AppError):
    """Raised when a user tries to delete an account while logged in."""
    default_message = "For security reasons you cannot delete account while logged in"

    def __init__(self, message=None):
        if message is None:
            message = self.default_message
        super().__init__(message)
