from dicegame.db.connection import get_connection
from dicegame.db.queries import(
    add_user,
    fetch_user,
    create_session,
    get_session_details,
    delete_session,
    reset_password
)
from dicegame.utils.security import(
    verify_password,
    hash_password
)
from dicegame.utils.logging import get_logger
from dicegame.utils.errors import(
    AppError,
    UserAlreadyExistsError,
    UserNotFoundError,
    ResetPasswordError
)
import sqlite3
from dicegame.utils.rich_pkg.console import console
from dicegame.utils.security import generate_session_token
from dicegame.session.session_disk import(
    Session,
    save_session_token,
    load_session_token,
    clear_session_token
)
from dicegame.utils.auth import ResetPasswordResult
from dicegame.utils.common_utils import confirm_reset
from dicegame.logging.config import redact,_redact_value


# logger
logger = get_logger(__name__)


# Check for any running session
def load_session() -> Session:
    """Returns a running session object"""
    token = load_session_token() # get token(str)
    if token is None:
        return None

    # Retrieve session user data
    with get_connection() as conn:
        try:
            session_details = get_session_details(conn,token)
        except Exception as e:
            raise

    # Session object
    if session_details:
        return Session(user_id=session_details['id'],username=session_details['username'],logged_in=True)


def login_service(username: str,password: str) -> Session:
    """Authenticates user login credentials"""

    with get_connection() as conn:
        try:
            user = fetch_user(conn,username)

            # Redact sensitive info
            safe_username = redact({'username': username})

            if user is None:
                logger.warning('Invalid login credentials')
                raise UserNotFoundError()

            # Verify password
            password_match = verify_password(user['password'],password)

            if password_match:
                # Create session
                token = generate_session_token()
                create_session(conn,user['id'],token)

                logger.info(f"User {safe_username} logged in successfully.")

            if not password_match:
                logger.warning(f"Failed login attempt for user, {safe_username}")
                raise UserNotFoundError()

        except Exception as e:
            raise

    # Save session_token
    save_session_token(token)

    # Return a session object
    return Session(user_id= user['id'],username= user['username'],logged_in= True)


def signup_service(username: str,password: str,session: Session):
    """Adds a new user account"""

    # hash password
    hashed_password = hash_password(password)

    # Redact sensitive info
    safe_username = redact({'username': username})

    with get_connection() as conn:
        try:
            user = fetch_user(conn,username)
            if user:
                logger.warning(f"User {safe_username} already exists")
                raise UserAlreadyExistsError(username)

            add_user(conn,username,hashed_password)
            logger.info(f"Successful signup for user, {safe_username}")

        except Exception as e:
            raise

    # Automatic login for new users
    return login_service(username,password)


def logout_service(token: str,session: Session) -> Session:
    """Ends the current user session and deletes the saved session token from disk"""
    with get_connection() as conn:
        try:
            delete_session(conn,token) # delete token from db
            clear_session_token() # delete token from disk

            # Redact sensitive info
            logger.info(f"User {redact({'username': session.username})} logged out successfully")
            # End session
            return Session(logged_in=False)

        except Exception as e:
            raise


def reset_password_service(password: str,session: Session):
    """Resets a registered user's password"""
    with get_connection() as conn:
        try:
            if confirm_reset(): # confirm reset password command

                # hash_password
                hashed_password = hash_password(password)
                # Reset
                reset_password(conn,session.username,hashed_password)
                logger.info("Successful password reset")

                # Return success
                return ResetPasswordResult(success= True)

        except Exception as e:
            raise

    return ResetPasswordResult(success= False)

