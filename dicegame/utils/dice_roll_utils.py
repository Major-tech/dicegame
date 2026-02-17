from random import randint
from dicegame.utils.rich_pkg.console import console
from dataclasses import dataclass
from dicegame.utils.errors import TooManyInvalidAttemptsError
from dicegame.session.session_disk import Session


#----------------INTERACTIVE & NON-INTERACTIVE----------------
# FUNCTIONS

def get_random_number() -> int:
    """Returns a random integer in the range of 1 to 6"""

    return randint(1,6)


def guest_mode() -> str:
    """Inform users that they're logged out"""

    console.print("[warning]GUEST MODE\nYou're logged out.Any points earned will not be saved[/warning]")


def play_mode_dice_roll_result(session: Session) -> int:
    """Returns a random number in range(1-6)"""

    # Alert users that scores will not be saved
    if not session:
        guest_mode()

    dice_roll_outcome = get_random_number() # get random number

    return dice_roll_outcome


# CLASSES

# Reset score
@dataclass
class ResetScoreResult:
    success: bool
    previous_score: int


# Simple dice roll
@dataclass
class SimpleDiceRollResult:
    guess: int


# Play game mode
@dataclass
class PlayModeResult:
    success: bool
    lucky_number: int
    logged_in: bool


# Guess game mode
@dataclass
class GuessModeResult:
    success: bool
    lucky_number: int
    user_guess: int
    logged_in: bool


# Delete player account
@dataclass
class RemovePlayerResult:
    success: bool
    username: str | None = None


#--------------------INTERACTIVE--------------------
# FUNCTIONS

def get_user_guess(args) -> int:
    """Returns a user's guess, an integer in range(1-6)"""

    for i in range(3):
        try:
            guess = getattr(args,'guess',None)
            if not guess:
                guess = int(input("Guess: "))

            if guess not in range(1,7): # ensure guess is in range(1-6)
                console.print("[warning]Guess must be between 1 and 6[/warning]")
                continue

            break
        except ValueError: # invalid input
            console.print("[warning]{Please enter a number[/warning]")

    if guess not in range(1,7): # invalid input
        raise TooManyInvalidAttemptsError()


    return guess



