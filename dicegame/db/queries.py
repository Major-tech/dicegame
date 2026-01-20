import sqlite3


def fetch_user(conn,username):
    fetch_query = "SELECT id,username,password FROM users WHERE username = ?"

    cur = conn.cursor()
    cur.execute(fetch_query,(username,))
    return cur.fetchone()


def delete_player(conn,id_player):
    delete_query = "DELETE FROM users WHERE id = ?"

    cur = conn.cursor()
    cur.execute(delete_query,(id_player,))


def fetch_users(conn):
    fetch_query = "SELECT username FROM users"

    cur = conn.cursor()
    cur.execute(fetch_query)
    return cur.fetchall()


def fetch_scores(conn):
    fetch_query = "SELECT username,score FROM users ORDER BY score DESC"

    cur = conn.cursor()
    cur.execute(fetch_query)
    return cur.fetchall()


def add_user(conn, username: str, hashed_password):
    add_query = "INSERT INTO users (username,password) VALUES (?,?)"

    cur = conn.cursor()
    cur.execute(add_query,(username,hashed_password))
