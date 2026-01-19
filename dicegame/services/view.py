from dicegame.db.connection import get_connection
from dicegame.db.queries import fetch_users,fetch_scores
from dicegame.utils.rich_pkg.console import console


def view_users_service():
    with get_connection() as conn:
        try:
            users = fetch_users(conn)

            if not users:
                console.print("[error]No registered users[error]")
                return

            print("\nUSERS (DICER)\n")

            for i,user in enumerate(users,start=1):
                print(i, user['username'])

        except Exception as e:
            raise


def view_scores_service():
    with get_connection() as conn:
        try:
            scores = fetch_scores(conn)

            if not scores:
                console.print("[error]No high scores recorded[error]")
                return

            print("\nHIGH SCORES(DICER)\n")

            for i,score in enumerate(scores,start=1):
                print(f"({i}) {score['username']}  [SCORE= {score['score']}]")

        except Exception as e:
            raise
