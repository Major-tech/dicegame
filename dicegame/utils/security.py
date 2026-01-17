from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


ph = PasswordHasher(
    time_cost= 3,
    memory_cost= 65536,
    parallelism= 4,
    hash_len= 32,
    salt_len= 16
)


def hash_password(password):
    return ph.hash(password)


def verify_password(hashed_password: str, raw_password: str):
    try:
        ph.verify(hashed_password, raw_password)
        return True
    except VerifyMismatchError:
        return False
