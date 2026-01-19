from dicegame.db.queries_interactive import add_score
from dicegame.db.connection import get_connection
from dicegame.utils.logging import get_logger
from dicegame.utils.rich_pkg.console import console
from dicegame.utils.rich_pkg.progress import progress_bar


# logger
logger = get_logger(__name__)


def display_dice_roll_service(dice_roll_output: int):
    # progress bar
    progress_bar()

    console.print(f"\nYou rolled a {dice_roll_output}",style='yellow')


def guess_dice_roll_service(computer_guess,player_guess,session=None):
    progress_bar()

    console.print(f"\n[info]User guess: {player_guess}[info]")
    console.print(f"[info]Dice roll result: {computer_guess}[info]")

    # correct guess
    match = False

    if computer_guess == player_guess:
        match = True

    if match:
        console.print("[success]\nWIN⭐[success]")
    else:
        console.print("[error]\nLOSE😞[error]")
        return

    if session:
        with get_connection() as conn:
            try:
                add_score(conn,session.username)

                logger.info("score added successfully")
                console.print(f"\n[success]1 point added for user[success] {session.username}\n")
            except Exception as e:
                raise
