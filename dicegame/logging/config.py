from typing import Any
import logging
import logging.handlers
from dicegame.utils.paths import get_app_data_dir


# LOG DIR
LOG_DIR = get_app_data_dir() / 'logs'
LOG_DIR.mkdir(parents=True,exist_ok=True)

# APP LOG
APP_LOG_FILE = LOG_DIR / 'app.log'

# ERROR LOG
ERROR_LOG_FILE = LOG_DIR/ 'error.log'

# USER PRIVACY RESPECTING LOGGING CONFIG
SENSITIVE_KEYS = {  # This info will not be sent to developer for debugging
    "username",
    "password",
    "pass",
    "token",
    "secret",
    "key",
    "api_key",
    "auth",
}


def _redact_value(key: str, value: Any) -> Any:
    """Redacts sensitive values from user logs"""

    if key.lower() in SENSITIVE_KEYS:
        return "***REDACTED***"
    return value


def redact(data: dict | None) -> dict | None:
    """Returns a secure app log stripped of sensitive user data"""

    if not data:
        return data
    return {k: _redact_value(k, v) for k, v in data.items()}


def setup_logger(level: int = logging.INFO) -> None:
    """Central logging configuration"""

    # ROOT LOGGER
    root_logger = logging.getLogger()

    # Prevent duplicate handlers in tests/reloads
    if root_logger.handlers:
        return root_logger

    # Set root logger log level
    root_logger.setLevel(level)

    # Configure formatter
    formatter = logging.Formatter(
        fmt = "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S"
    )

    # APP ROTATING LOG FILE HANDLER
    app_log_handler = logging.handlers.RotatingFileHandler(
        APP_LOG_FILE,
        maxBytes=1+3_000_000,
        backupCount=3,
        encoding = 'utf-8'
    )

    # Configure log level and formatter
#    app_log_handler.setLevel(logging.DEBUG)
    app_log_handler.setFormatter(formatter)

    # APP ROTATING LOG FILE HANDLER
    error_log_handler = logging.handlers.RotatingFileHandler(
        ERROR_LOG_FILE,
        maxBytes=3_000_000,
        backupCount=3,
        encoding='utf-8'
    )

    # Configure log level and formatter
    error_log_handler.setLevel(logging.ERROR)
    error_log_handler.setFormatter(formatter)

    # CONSOLE HANDLER
    console_handler = logging.StreamHandler()

    # Configure log level and formatter
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)

    # Add handlers
    root_logger.handlers.clear()
    root_logger.addHandler(app_log_handler)
    root_logger.addHandler(error_log_handler)
#    root_logger.addHandler(console_handler)

 #   root_logger.propagate = False
#    return root_logger


