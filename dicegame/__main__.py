from dicegame.logging.config import setup_logger
from dicegame.utils.logging import get_logger
from dicegame.db.schema import init_db
from dicegame.cli.parser import build_parser
from dicegame.cli.dispatcher import dispatch
from dicegame.utils.errors import AppError
import sys


def main():
    setup_logger()

    logger = get_logger(__name__)
    logger.debug("App started")

    init_db()

    parser = build_parser()
    args = parser.parse_args()

    try:
        dispatch(args)
        return 0
    except AppError as e:
        logger.warning(str(e))
        print(e)
        return 1
    except Exception as e:
        logger.exception("Unhandled main error")
        print("We experienced some trouble while processing your request.",file=sys.stderr)
        return 1


def run() -> int:
    try:
        return main()
    except Exception:
        logger.exception("Unhandled run(main) error")
        print("An internal error occurred",file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(run())
