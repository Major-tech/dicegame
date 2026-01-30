from dicegame.services.auth import(
    login_service,
    signup_service,
    logout_service,
    reset_password_service
)
from dicegame.utils.errors import(
    NotLoggedInError
)
from dicegame.session.session_disk import load_session_token
from dicegame.session.session_disk import Session


def login_cmd(username: str,password: str,session: Session):
    """Collects and routes user login data to the service layer"""

    return login_service(username,password)


def signup_cmd(username: str,password: str,session: Session):
    """Routes new user data to service layer for registration"""

    return signup_service(username,password,session)


def logout_cmd(session: Session):
    """End/Destroy current session saved locally on disk"""
    token = load_session_token()

    if token: # Checks if any session token is stored and forwards it to the logout service
        return logout_service(token,session)

    raise NotLoggedInError("Not logged in")


def reset_password_cmd(new_password: str,session: Session):
    """Route new password to the service layer for a password reset"""

    return reset_password_service(new_password,session)


