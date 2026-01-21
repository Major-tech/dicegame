from dicegame.db.queries_interactive import(
    add_score_guess,
    add_score_play
)
from dicegame.db.connection import get_connection
from dicegame.utils.logging import get_logger
#from dicegame.utils.dice_roll_ut
from dicegame.utils.rich_pkg.console import console
from dicegame.utils.rich_pkg.progress import progress_bar


# logger
logger = get_logger(__name__)


def add_points_play_interactive(session):
    if session:
        with get_connection() as conn:
            try:
                add_score_play(conn,session.username)

                logger.info("score added successfully")
                console.print(f"\n[success]5 points added for user[/success] {session.username}\n")
            except Exception as e:                                                                                        raise


def add_points_guess_interactive(session):
    if session:
        with get_connection() as conn:
            try:
                add_score_guess(conn,session.username)

                logger.info("score added successfully")
                console.print(f"\n[success]10 points added for user[/success] {session.username}\n")
            except Exception as e:
                raise


def simple_dice_roll_service(dice_roll_output: int):
    # progress bar
    progress_bar()

    console.print(f"\nYou rolled a {dice_roll_output}",style='yellow')


def play_dice_roll_service(dice_roll_output,session=None):
    winning_numbers = (4, 5, 6)

    print(f"\nWinning numbers: {winning_numbers}")

    progress_bar()

    print(f"\nDice roll result: {dice_roll_output}")

    if dice_roll_output not in winning_numbers:
        print('\nLOSE😢')
        return

    print("\nWIN🥂")

    # INTERACTIVE (ADDING POINTS IF USER WINS)
    add_points_play_interactive(session)


def guess_dice_roll_service(computer_guess,player_guess,session=None):
    progress_bar()

    console.print(f"\n[info]User guess: {player_guess}[/info]")
    console.print(f"[info]Dice roll result: {computer_guess}[/info]")

    # correct guess
    match = False

    if computer_guess == player_guess:
        match = True

    if match:
        console.print("[success]\nWIN⭐[/success]")
    else:
        console.print("[error]\nLOSE😞[/error]")
        return

    # INTERACTIVE(ADDING POINTS IF USER WINS)
    add_points_guess_interactive(session)

