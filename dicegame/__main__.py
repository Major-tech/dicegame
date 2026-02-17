from dicegame.logging.config import setup_logger
from dicegame.utils.logging import get_logger
from dicegame.db.schema import init_db
from dicegame.cli.parser import build_parser
from dicegame.cli.dispatcher import dispatch
from dicegame.utils.rich_pkg.console import console
from dicegame.services.auth import load_session
from dicegame.cli.interactive_dispatcher import interactive_dispatch
from dicegame.logging.config import redact
from dicegame.version import get_version
import logging
import sys


def main():
    # -------------------------
    # 1. Build parser & parse args
    # -------------------------
    parser = build_parser()  # or define parser here
    args = parser.parse_args()

    # -------------------------
    # 2. Early-exit global flags
    # -------------------------
    if args.version:
        version = get_version()
        console.print(f"dicegame v{version}")
        return 0

    # -------------------------
    # 3. Logging setup
    # -------------------------
    if args.debug:
        setup_logger(logging.DEBUG)
        logger = get_logger(__name__)
        logger.info("Debug mode enabled")
    else:
        setup_logger()
        logger = get_logger(__name__)

    logger.debug("App started")

    # -------------------------
    # 4. Heavy initialization
    # -------------------------
    init_db()
    session = load_session()

     # Welcome message for logged in users
    if session and session.logged_in:
        # Redact username for logs if needed
        safe_username = redact({'username': session.username})
        logger.info(f"User '{safe_username}' session loaded")
        console.print(f"Welcome back {session.username} 🙂")

    # -------------------------
    # 5. Interactive Dispatch
    # -------------------------
    if args.interactive:
        # interactive mode takes priority over missing command
        interactive_dispatch(session)
        return 0

    if args.command is None:
        # no command given and not interactive → show help
        parser.print_help()
        return 0

    # -------------------------
    # 6. Normal subcommand dispatch
    # -------------------------
    # Any sensitive info passed in commands should also be redacted here
    dispatch(args, session)

    return 0


# PROGRAM START
if __name__ == '__main__':
    sys.exit(main())
