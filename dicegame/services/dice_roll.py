from dicegame.db.queries_interactive import add_score
from dicegame.db.connection import get_connection
from dicegame.utils.logging import get_logger


# logger
logger = get_logger(__name__)


def display_dice_roll_service(dice_roll_output: int):
    print(f"\nDice roll result: {dice_roll_output}")


def guess_dice_roll_service(computer_guess,player_guess,session=None):
    print(f"\nUser guess: {player_guess}")
    print(f"Dice roll result: {computer_guess}")

    # correct guess
    match = False

    if computer_guess == player_guess:
        match = True

    if match:
        print("WIN⭐")
    else:
        print("LOSE😞")
        return

    if session:
        with get_connection() as conn:
            try:
                add_score(conn,session.username)

                logger.info("score added successfully")
                print(f"\n1 point added for user {session.username}\n")
            except Exception as e:
                raise
