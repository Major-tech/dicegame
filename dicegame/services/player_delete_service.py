from dicegame.db.queries import fetch_user,delete_player,fetch_player
from dicegame.db.connection import get_connection
from dicegame.utils.logging import get_logger
from dicegame.utils.security import verify_password
from dicegame.utils.errors import UserNotFoundError
from dicegame.session.session_disk import Session
from dicegame.utils.dice_roll_utils import RemovePlayerResult
from dicegame.utils.common_utils import confirm_reset


# logger
logger = get_logger(__name__)


def player_delete_service(password: str,session: Session) -> RemovePlayerResult:
    """Deletes an existing user account"""
    with get_connection() as conn:
        try:
            # Fetch user's saved password hash
            player = fetch_player(conn,session.user_id)
            if player is None: # user not found
                raise UserNotFoundError()

            # verify password
            password_is_correct = verify_password(player['password'],password)

            if password_is_correct: # correct password
                if confirm_reset():
                    delete_player(conn,player['id'])
                    logger.info('Player deleted successfully')

                    return RemovePlayerResult(success= True,username= player['username'])

            else: # wrong password
                logger.warning("Invalid login credentials")
                raise UserNotFoundError()

        except Exception as e:
            raise
    return RemovePlayerResult(success= False)
