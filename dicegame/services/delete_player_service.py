from dicegame.db.queries import fetch_user,delete_player
from dicegame.db.connection import get_connection
from dicegame.utils.logging import get_logger
from dicegame.utils.rich_pkg.console import console
from dicegame.utils.security import verify_password
from dicegame.utils.errors import UserNotFoundError


# logger
logger = get_logger(__name__)


def delete_player_service(player_name: str,password: str):

    with get_connection() as conn:
        try:
            player = fetch_user(conn,player_name)

            if player is None:
                logger.warning('Invalid login credentials')
                raise UserNotFoundError
                return

            # verify password
            password_match = verify_password(player['password'],password)

            if password_match:
                delete_player(conn,player['id'])
                logger.info('Player deleted successfully')
                console.print("[success]Player deleted successfully![/success]")


            if not password_match:
                logger.warning("Invalid login credentials")
                raise UserNotFoundError

        except Exception as e:
            raise
