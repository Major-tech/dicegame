from dicegame.db.queries import fetch_user,delete_user
from dicegame.db.connection import get_connection
from dicegame.utils.logging import get_logger


# logger
logger = get_logger(__name__)


def confirm_username_service(username):
    with get_connection() as conn:
        try:
            user = fetch_user(conn,username)

            if user:
                user_id = user['id']
                return user_id
            return False

        except Exception as e:
            raise


def delete_user_service(user_id):
    with get_connection() as conn:
        try:
            delete_user(conn,user_id)
            logger.info("User deleted successfully")
            print("User deleted successfully")

        except Exception as e:
            raise
