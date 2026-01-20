from dicegame.services.leaderboard import(
    players_service,
    leaderboard_service
)


def player_list_cmd_interactive(session):
    players_service()


def leaderboard_cmd_interactive(session):
    leaderboard_service()



