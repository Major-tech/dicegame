import sqlite3
from dicegame.utils.paths import DB_PATH


def get_connection():
    """Connects to the database"""

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


