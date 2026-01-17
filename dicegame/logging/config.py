import logging
import logging.handlers
from dicegame.utils.paths import LOG_PATH


def setup_logger(level: int = logging.DEBUG):
    formatter = logging.Formatter(
        fmt = "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S"
    )

    file_handler = logging.handlers.RotatingFileHandler(
        LOG_PATH,
        maxBytes=5_000_000,
        backupCount=3
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.handlers.clear()
    root_logger.addHandler(file_handler)
#    root_logger.addHandler(console_handler)


