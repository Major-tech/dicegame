from dicegame.db.connection import get_connection
from dicegame.db.queries import fetch_users,fetch_scores
from dicegame.utils.rich_pkg.console import console
from rich.table import Table


def players_service():
    with get_connection() as conn:
        try:
            players = fetch_users(conn)

            if not players:
                console.print("[error]No registered players[/error]")
                return

            # PLAYERS TABLE
            table = Table(
                title='Players',
                header_style='bold cyan',
                border_style ='dim',
                row_styles=['none','dim'],
                highlight=True
            )

            table.add_column('Serial No.')
            table.add_column('Player',style='cyan')

            for i,player in enumerate(players,start=1):
                player = str(player['username'])

                table.add_row(str(i), player)

            console.print(table,style='blue')

        except Exception as e:
            raise


def leaderboard_service():
    with get_connection() as conn:
        try:
            scores = fetch_scores(conn)

            if not scores:
                console.print("[error]No high scores recorded[/error]")
                return

            # LEADERBOARD TABLE
            table = Table(
                title="Dicer Leaderboard",
                header_style='bold cyan',
                border_style ='dim',
                row_styles=['none','dim'],
                highlight=True
            )

            table.add_column('Serial No.')
            table.add_column('Players',style='cyan')
            table.add_column('Points',style='magenta')

            for i,score in enumerate(scores,start=1):
                 player = score['username']
                 score = str(score['score'])

                 table.add_row(str(i),player,score)

            console.print(table,style='yellow')

        except Exception as e:
            raise
