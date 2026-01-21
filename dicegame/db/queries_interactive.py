def add_score_play(conn,username):
    update_query = "UPDATE users SET score = score + 5 WHERE username = ?"
    cur = conn.cursor()
    cur.execute(update_query,(username,))


def add_score_guess(conn,username):
    update_query = "UPDATE users SET score = score + 10 WHERE username = ?"
    cur = conn.cursor()
    cur.execute(update_query,(username,))
