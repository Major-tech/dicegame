from dicegame.services.player_delete_service import player_delete_service
from dicegame.utils.dice_roll_utils import RemovePlayerResult
from dicegame.session.session_disk import Session


def player_delete_cmd(password: str,session: Session) -> RemovePlayerResult:
    """Collect user data and route it to service layer for account deletion"""

    return player_delete_service(password,session)


