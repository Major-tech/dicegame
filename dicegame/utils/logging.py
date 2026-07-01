import logging


def get_logger(name) -> logging.Logger:
    """Returns the module name to be used when logging errors raised in the current module"""

    return logging.getLogger(name)


