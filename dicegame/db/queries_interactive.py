def add_score(conn,username):
 #   select_query = "SELECT score FROM USERS where username = ?"
    update_query = "UPDATE users SET score = score + 1 WHERE username = ?"
    cur = conn.cursor() 
#    cur.execute(select_query,(username,))
    cur.execute(update_query,(username,))
