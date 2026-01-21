from dicegame.logging.config import setup_logger
from dicegame.utils.logging import get_logger
from dicegame.db.schema import init_db
from dicegame.cli.parser import build_parser
from dicegame.cli.dispatcher import dispatch
from dicegame.utils.rich_pkg.console import console,err_console
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
    except Exception as e:
        logger.exception("Unhandled main error")
        err_console.print("[error]We experienced some trouble while processing your request[/error]")
        return 1


def run() -> int:
    try:
        return main()
    except Exception:
        logger.exception("Unhandled run(main) error")
        err_console.print("[error]An internal error occurred[/error]")
        return 1


if __name__ == '__main__':
    sys.exit(run())
