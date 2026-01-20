from dicegame.db.queries import fetch_user,delete_player
from dicegame.db.connection import get_connection
from dicegame.utils.logging import get_logger
from dicegame.utils.rich_pkg.console import console


# logger
logger = get_logger(__name__)


def confirm_player_service(player_name):
    with get_connection() as conn:
        try:
            player = fetch_user(conn,player_name)

            if player:
                player_id = player['id']
                return player_id
            return False

        except Exception as e:
            raise


def delete_player_service(player_id):
    with get_connection() as conn:
        try:
            delete_player(conn,player_id)
            logger.info("Player deleted successfully")
            console.print("[success]Player deleted successfully[/success]")

        except Exception as e:
            raise
