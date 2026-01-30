from dicegame.logging.config import setup_logger
from dicegame.utils.logging import get_logger
from dicegame.db.schema import init_db
from dicegame.cli.parser import build_parser
from dicegame.cli.dispatcher import dispatch
from dicegame.utils.rich_pkg.console import console
from dicegame.services.auth import load_session
from dicegame.cli.interactive_dispatcher import interactive_dispatch
import logging
import sys


def main():
    # Create an arguments parser
    parser = build_parser()
    args = parser.parse_args()

     # Module logger
    logger = get_logger(__name__)

    # Initialize root logger
    if args.debug:
        setup_logger(level = logging.DEBUG)
        logger.info("Debug mode enabled")
    else:
        setup_logger()

    logger.debug("App Started")

    init_db() # Initialize database

    session = load_session() # load session

    # Welcome message for logged in users
    if session and session.logged_in:
        console.print(f"Welcome Back {session.username}🙂\n",style='bold cyan')

    # Use appropriate dispatcher
    if args.interactive:
        interactive_dispatch(session)
    else:
        dispatch(args,session)


if __name__ == '__main__':
    sys.exit(main())
