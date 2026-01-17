from dicegame.db.connection import get_connection


def init_db():
    table_query = """CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    score INTEGER DEFAULT 0
    )"""

    # USE WITH TO COMMIT & CLOSE THE CONNECTION
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(table_query)
