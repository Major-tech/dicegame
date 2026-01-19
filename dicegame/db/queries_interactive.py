def add_score(conn,username):
    update_query = "UPDATE users SET score = score + 1 WHERE username = ?"
    cur = conn.cursor()
    cur.execute(update_query,(username,))
