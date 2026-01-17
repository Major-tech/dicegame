from dicegame.session.session import Session
from dicegame.utils.security import hash_password
from dicegame.services.auth import(
    login_service,
    signup_service
)
import getpass
from dicegame.utils.errors import AppError
from dicegame.utils.logging import get_logger


# logger
logger = get_logger(__name__)


def login_cmd_interactive(session):
    while True:
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        if not username or not password:
            print("All fields are required!")
            continue

        break

    try:
        # LOGIN_SERVICE
        login_service(username,password)
    except AppError as e:
        logger.warning(str(e))
        print(e)
    else:
        # start session
        session.login(username)
        print(f"Logged in as {session.username}")


def logout_cmd_interactive(session):
    if not session.logged_in:
        print("Not logged in")
        return

    user = session.username
    session.logout()
    print(f"User {user} logged out successfully")


def signup_cmd_interactive():
    while True:
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        if not username or not password:
            print("All fields are required!")
            continue

        if len(password) < 3:
            print("Password is too short")
            continue

        break

    # hash password
    hashed_password = hash_password(password)

    # SERVICE LAYER
    signup_service(username,hashed_password)

