from dicegame.utils.rich_pkg.console import console
from dicegame.utils.errors import(
    TooManyInvalidAttemptsError,
    NotLoggedInError,
    AuthError
)
from dataclasses import dataclass
from dicegame.session.session_disk import Session
from dicegame.db.connection import get_connection
from dicegame.db.queries import fetch_user
import getpass


# CLASSES

# Reset password
@dataclass
class ResetPasswordResult:
    success: bool


# FUNCTIONS
def validate_username(username: str) -> bool:

    """Checks if username is registered"""
    with get_connection() as conn:
        try:
            user = fetch_user(conn,username)

            if user is None:
                raise AuthError("Player name doesn't exist")

            return True
        except Exception as e:
            raise


def collect_auth_credentials(args):
    """Collect username and password details"""

    attempts = 4

    while attempts != 0:

        # getattr defaults to None and prevents AttributeError from being raised
        username = getattr(args, "username", None)
        if not username:
            username = input("Username*: ").strip()

        password = getattr(args, "password", None)
        if not password:
            password = getpass.getpass("Password*: ").strip()

        attempts -= 1
        if attempts == 0:
            raise TooManyInvalidAttemptsError()

        if len(password) < 3: # short password
            console.print("[warning]Password is too short[/warning]")
            continue

        if not username or not password: # Blank field(s)
            console.print("[warning]All fields are required![/warning]")
            continue

        break

    return username,password


def collect_password(args) -> str:
    """Collect a user's password"""

    attempts = 4

    while attempts != 0:

        password = getattr(args, "password", None)
        if not password:
            password = getpass.getpass("Enter your password*: ").strip()

        attempts -= 1
        if attempts == 0:
            raise TooManyInvalidAttemptsError()

        if len(password) < 3: # short password
            console.print("[warning]Password is too short[/warning]")
            continue

        if not password: # Blank field
            console.print("[warning]Password is required![/warning]")
            continue

        break

    return password


def collect_new_password(args) -> str:
    """Returns a string which is used to update a user's current password """

    # Header
    console.print("[info]RESET PASSWORD[/info]\n",style='bold magenta')

    for i in range(4): # 4 attempts specified

        # Get new password
        password = getattr(args,'password',None)

        if not password: # argument hasn't been given
            password = getpass.getpass("New Password: ").strip()

        if not password: # blank field
            console.print("[warning]Password is required![/warning]")
            continue
        if len(password) < 3: # short password
            console.print("[warning]Password is too short![/warning]")
            continue

        # confirm password
        for i in range(3): # 3 retries specified
            confirm_password = getpass.getpass("Confirm New Password: ")

            # Both passwords match
            if password == confirm_password:

                # RETURN NEW PASSWORD
                return password

            if not confirm_password: # blank field
                console.print("[warning]Password confirmation required![/warning]")
                continue

            # Passwords don't match
            if password != confirm_password:
                console.print("[warning]Passwords do not match[/warning]")
                continue
    raise TooManyInvalidAttemptsError()


def who_am_i(session: Session) -> str:
    """Displays the currently logged in user"""

    # show logged-in user
    if session and session.logged_in:
        return f"{session.username}"

    raise NotLoggedInError("Not logged in") # No active user session present


