from dicegame.db.connection import get_connection
from dicegame.db.queries import(
    add_user,
    fetch_user
)
from dicegame.utils.security import verify_password
from dicegame.utils.logging import get_logger
from dicegame.utils.errors import(
    UserAlreadyExistsError,
    UserNotFoundError
)
import sqlite3
from dicegame.utils.rich_pkg.console import console


# logger
logger = get_logger(__name__)


def login_service(username: str,password: str):
    with get_connection() as conn:
        try:
            user = fetch_user(conn,username)

            if user is None:
                logger.warning('Invalid login credentials')
                raise UserNotFoundError
                return

            # verify password
            password_match = verify_password(user['password'],password)

            if password_match:
                logger.info("Successful user login")
                console.print("[success]Login successful![/success]")


            if not password_match:
                logger.warning("Invalid login credentials")
                raise UserNotFoundError

        except Exception as e:
            raise


def signup_service(username: str,password_hash: str):
    with get_connection() as conn:
        try:
            add_user(conn,username,password_hash)
            logger.info("Successful user signup")
            console.print("[success]Sign up was successful![/success]")

        except sqlite3.IntegrityError as e:
            logger.warning("username already exists")
            raise UserAlreadyExistsError(username) from e

        except Exception as e:
            raise

