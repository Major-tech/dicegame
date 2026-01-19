from dicegame.session.session import Session
from dicegame.utils.security import hash_password
from dicegame.services.auth import(
    login_service,
    signup_service
)
import getpass
from dicegame.utils.errors import AppError
from dicegame.utils.logging import get_logger
from dicegame.utils.rich_pkg.console import console


# logger
logger = get_logger(__name__)


def login_cmd_interactive(session):
    while True:
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        if not username or not password:
            console.print("[warning]All fields are required![/warning]")
            continue

        break

    try:
        # LOGIN_SERVICE
        login_service(username,password)
    except AppError as e:
        logger.warning(str(e))
        console.print(f"[error]{e}[/error]")
    else:
        # start session
        session.login(username)
        console.print(f"[success]Logged in as[/success] {session.username}")


def logout_cmd_interactive(session):
    if not session.logged_in:
        console.print("[error]Not logged in[error]")
        return

    user = session.username
    session.logout()
    console.print(f"[success]User {user} logged out successfully[success]")


def signup_cmd_interactive():
    while True:
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        if not username or not password:
            console.print("[warning]All fields are required![warning]")
            continue

        if len(password) < 3:
            console.print("[warning]{Password is too short[warning]")
            continue

        break

    # hash password
    hashed_password = hash_password(password)

    # SERVICE LAYER
    signup_service(username,hashed_password)

