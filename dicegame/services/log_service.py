from dicegame.logging.config import LOG_DIR
from dicegame.session.session_disk import Session
from dicegame.utils.rich_pkg.console import console
from dicegame.utils.common_utils import confirm_reset


def view_logs_service(session: Session):
    """Prints out all the available app logs stored locally"""

    console.print("LOGS\n",style='bold magenta')

    for i, log in enumerate(LOG_DIR.iterdir(),start=1):
        print(i, log)


def clear_logs_service(session: Session):
    """Deletes all the available app logs stored locally"""

    if confirm_reset():

        for file in LOG_DIR.glob("*.log"):
            file.unlink()
        return True

    return False
