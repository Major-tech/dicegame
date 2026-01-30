from dicegame.db.queries import(
    fetch_user,
    add_score_guess,
    add_score_play,
    reset_score,
    fetch_current_score
)
from dicegame.db.connection import get_connection
from dicegame.utils.logging import get_logger
from dicegame.utils.rich_pkg.console import console
from dicegame.utils.rich_pkg.progress import progress_bar
from dicegame.utils.security import verify_password
from dicegame.utils.errors import(
    UserNotFoundError,
    AppError,
    ResetScoreError
)
from dicegame.utils.common_utils import confirm_reset
from dicegame.session.session_disk import Session
from dicegame.utils.dice_roll_utils import(
    SimpleDiceRollResult,
    ResetScoreResult,
    PlayModeResult,
    GuessModeResult
)


# logger
logger = get_logger(__name__)


def simple_dice_roll_service(dice_roll_output: int,session: Session) -> SimpleDiceRollResult:
    """Returns the simple dice roll output"""

    # progress bar
    progress_bar()

    return SimpleDiceRollResult(guess= dice_roll_output)


def play_dice_roll_service(dice_roll_output: int,session: Session) -> PlayModeResult:
    """Returns the play mode dice roll output"""

    winning_numbers = (4, 5, 6)

    print(f"\nWinning numbers: {winning_numbers}")

    progress_bar() # dice roll progress

     # Dice roll result
    print(f"\nDice roll result: {dice_roll_output}")

    # variables
    player_has_won = dice_roll_output in winning_numbers

    # If player is logged out
    if not session:
        # Win
        if player_has_won:
            return PlayModeResult(success= True,logged_in= False)
        # Lose
        else:
            return PlayModeResult(success= False,logged_in= False)

    # If player is logged in
    if session and session.logged_in:
        # Win
        if player_has_won:
            # (ADDING POINTS IF USER WINS)
            with get_connection() as conn:
                try:
                    add_score_play(conn,session.username)
                    logger.info("score added successfully")

                    return PlayModeResult(success= True,logged_in= True)
                except Exception as e:
                    raise

        # Lose
        else:
            return PlayModeResult(success= False,logged_in= True)


def guess_dice_roll_service(computer_guess: int,player_guess: int,session: Session) -> GuessModeResult:
    """Returns the guess mode dice roll output"""

    progress_bar() # dice roll progress

    # Dice roll results
    console.print(f"\n[info]User guess: {player_guess}[/info]")
    console.print(f"[info]Dice roll result: {computer_guess}[/info]")

    # Evaluate to True if computer guess == player guess
    player_has_won = False

    if computer_guess == player_guess: # player wins
        player_has_won = True

    # If player is logged out
    if not session:
        # Win
        if player_has_won:
            return GuessModeResult(success= True,lucky_number= computer_guess,logged_in= False)
        # Lose
        else:
            return GuessModeResult(success= False,lucky_number= computer_guess,logged_in= False)


    # If player is logged in
    if session and session.logged_in:
        # Win
        if player_has_won:
            with get_connection() as conn:
                try:
                    add_score_guess(conn,session.username)
                    logger.info("score added successfully")

                    return GuessModeResult(success= True,lucky_number= computer_guess,logged_in= True)

                except Exception as e:
                    raise

        # Lose
        else:
            return GuessModeResult(success= False,lucky_number= computer_guess,logged_in= True)


def reset_score_service(password: str,session: Session) -> ResetScoreResult:
    with get_connection() as conn:
        try:

            # Get user password from db
            player = fetch_user(conn,session.username)

            # Verify password
            password_is_correct = verify_password(player['password'],password)

            if password_is_correct: # password is correct

                # Fetch current_score
                current_score = fetch_current_score(conn,player['id'])

                # Stop if current_score is currently = 0
                if current_score['score'] <= 0:
                    raise ResetScoreError("Your score is zero.Nothing to reset.")

                if confirm_reset(): # confirm reset score command

                    # Reset if score > 0
                    reset_score(conn,player['id'])
                    logger.info('successful player score reset')

                    # Score reset
                    return ResetScoreResult(success= True,previous_score= current_score['score'])

            else: # incorrect password
                logger.warning("Invalid login credentials")
                raise UserNotFoundError()

        except Exception as e:
            raise

    return ResetScoreResult(success= False,previous_score= 0)
