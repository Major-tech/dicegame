from dicegame.services.leaderboard import(
    player_list_service,
    leaderboard_service
)
from dicegame.session.session_disk import Session


def player_list_cmd(session: Session):
    """Returns a list of registered players"""

    return player_list_service(session)


def leaderboard_cmd(session: Session):
    """Returns a list of registered players and their scores"""

    return leaderboard_service(session)
