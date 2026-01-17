from dicegame.services.dice_roll import(
    display_dice_roll_service,
    guess_dice_roll_service
)
from dicegame.utils.dice_roll_utils import get_random_number


def display_dice_roll_cmd():
    dice_roll_result = get_random_number()
    display_dice_roll_service(dice_roll_result)


def guess_dice_roll_cmd(guess: int):
    dice_roll_result = get_random_number()
    guess_dice_roll_service(dice_roll_result,guess)
