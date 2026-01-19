


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
