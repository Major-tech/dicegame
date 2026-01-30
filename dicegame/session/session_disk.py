from dicegame.utils.paths import SESSION_FILE
from dataclasses import dataclass


# Session class

@dataclass
class Session:
    user_id: int | None = None
    username: str | None = None
    logged_in: bool = False


def save_session_token(token: str):
    SESSION_FILE.write_text(token)


def load_session_token():
    if SESSION_FILE.exists():
        return SESSION_FILE.read_text().strip()
    return None


def clear_session_token():
    if SESSION_FILE.exists():
        SESSION_FILE.unlink()


