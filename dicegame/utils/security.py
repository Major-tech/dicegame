from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import secrets


# Global ph config
ph = PasswordHasher(
    time_cost= 3,
    memory_cost= 65536,
    parallelism= 4,
    hash_len= 32,
    salt_len= 16
)


def hash_password(password) -> str:
    """Hashes a password using argon2 and returns it"""
    return ph.hash(password)


def verify_password(hashed_password: str, raw_password: str) -> bool:
    """Compares the entered password with the password hash stored in the database and returns True if they match"""

    try:
        ph.verify(hashed_password, raw_password)
        return True
    except VerifyMismatchError:
        return False


def generate_session_token() -> str:
    """Returns a randomly generated token"""

    return secrets.token_urlsafe(32)
