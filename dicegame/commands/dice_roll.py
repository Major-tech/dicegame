from dicegame.services.dice_roll import(
    simple_dice_roll_service,
    play_dice_roll_service,
    guess_dice_roll_service,
    reset_score_service
)
from dicegame.utils.dice_roll_utils import(
    get_random_number,
    guest_mode,
    SimpleDiceRollResult,
    ResetScoreResult,
    PlayModeResult,
    GuessModeResult
)
from dicegame.utils.rich_pkg.console import console
from dicegame.session.session_disk import Session
from dicegame.utils.rich_pkg.progress import progress_bar


def simple_dice_roll_cmd(dice_roll_output: int,session: Session) -> SimpleDiceRollResult:
    """Routes a random number to the service function"""

    progress_bar() # dice roll progress

    return simple_dice_roll_service(dice_roll_output,session)


def play_dice_roll_cmd(dice_roll_output,session: Session) -> PlayModeResult:
    """Returns a random integer in range(1-6)"""

    print(f"\nWinning numbers: 4, 5 or 6")

    progress_bar() # dice roll progress

    return play_dice_roll_service(dice_roll_output,session)


def guess_dice_roll_cmd(guess: int,session: Session) -> GuessModeResult:
    """Routes user guess and computer guess to the guess service"""

    # Alert users that scores will not be saved
    if not session:
        guest_mode()

    progress_bar() # dice roll progres

    dice_roll_result = get_random_number()

    return guess_dice_roll_service(dice_roll_result,guess,session)


def reset_score_cmd(password: str,session: Session) -> ResetScoreResult:
    """Routes the new password to the service function"""

    return reset_score_service(password,session)
