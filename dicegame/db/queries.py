# TABLE: USERS ------------------

def fetch_user(conn: sqlite3.Connection, username: str) -> sqlite3.Row | None:
    """Returns a single user's details,fetches by the username"""

    fetch_query = "SELECT id,username,password FROM users WHERE username = ?"

    cur = conn.cursor()
    cur.execute(fetch_query,(username,))
    return cur.fetchone()


def fetch_player(conn: sqlite3.Connection,user_id: int) -> sqlite3.Row | None:
    """Returns a single user's details,fetches by user id"""

    fetch_query = "SELECT id,username,password FROM users WHERE id = ?"

    cur = conn.cursor()
    cur.execute(fetch_query,(user_id,))
    return cur.fetchone()


def delete_player(conn: sqlite3.Connection, player_id: int) -> None:
    """Deletes a player account"""

    delete_query = "DELETE FROM users WHERE id = ?"

    cur = conn.cursor()
    cur.execute(delete_query,(player_id,))


def fetch_users(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    """Fetches all usernames from the db"""

    fetch_query = "SELECT username FROM users"

    cur = conn.cursor()
    cur.execute(fetch_query)
    return cur.fetchall()


def fetch_scores(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    """Fetches all users and their corresponding scores"""

    fetch_query = "SELECT username,score FROM users ORDER BY score DESC"

    cur = conn.cursor()
    cur.execute(fetch_query)
    return cur.fetchall()


def add_user(conn: sqlite3.Connection, username: str, hashed_password: str) -> None:
    """Adds a new user"""

    add_query = "INSERT INTO users (username,password) VALUES (?,?)"

    cur = conn.cursor()
    cur.execute(add_query,(username,hashed_password))


def add_score_play(conn: sqlite3.Connection, username: str) -> None:
    """Add points earned in the play game mode"""

    update_query = "UPDATE users SET score = score + 5 WHERE username = ?"
    cur = conn.cursor()
    cur.execute(update_query,(username,))


def add_score_guess(conn: sqlite3.Connection, username: str) -> None:
    """Add points earned in the guess game mode"""

    update_query = "UPDATE users SET score = score + 10 WHERE username = ?"
    cur = conn.cursor()
    cur.execute(update_query,(username,))


def fetch_current_score(conn: sqlite3.Connection, user_id: int) -> sqlite3.Row | None:
    """Fetches a single user's current score"""

    fetch_query = "SELECT score FROM users WHERE id = ?"
    cur = conn.cursor()
    cur.execute(fetch_query,(user_id,))

    return cur.fetchone()


def reset_score(conn: sqlite3.Connection, user_id: int) -> None:
    """Resets a user's current score to 0"""

    reset_query = "UPDATE users SET score = 0 WHERE id = ?"
    cur = conn.cursor()
    cur.execute(reset_query,(user_id,))


def reset_password(conn: sqlite3.Connection, username: str,password_hash: str) -> None:
    """Resets a user's password"""

    reset_query = "UPDATE users SET password = ? WHERE username = ?"
    cur = conn.cursor()
    cur.execute(reset_query,(password_hash,username))



# TABLE: SESSIONS-----------

def create_session(conn: sqlite3.Connection, user_id: int, token: str) -> None:
    """Stores a session token in the db"""

    add_query = "INSERT INTO sessions (user_id,token) VALUES (?,?)"

    cur = conn.cursor()
    cur.execute(add_query,(user_id,token))


def get_session_details(conn: sqlite3.Connection, token: str) -> sqlite3.Row | None:
    """Returns a row from the users table whose primary key is linked to the sessions table"""

    cur = conn.cursor()

    cur.execute(
        """
        SELECT users.*
        FROM sessions
        JOIN users ON users.id = sessions.user_id
        WHERE sessions.token = ?
        """,
        (token,)
    )
    return cur.fetchone()


def delete_session(conn: sqlite3.Connection, token: str) -> None:
    """Removes a session token from the db"""

    delete_query = "DELETE FROM sessions WHERE token = ?"
    cur = conn.cursor()
    cur.execute(delete_query,(token,))

