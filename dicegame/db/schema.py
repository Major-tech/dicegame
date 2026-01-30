from dicegame.db.connection import get_connection


def init_db():
    """Creates database tables"""

    table_query = """CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    score INTEGER DEFAULT 0
    )"""

    sessions_query = """CREATE TABLE IF NOT EXISTS sessions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    token TEXT UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
    )"""

    # USE WITH TO COMMIT & CLOSE THE CONNECTION
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(table_query)
        cur.execute(sessions_query)
