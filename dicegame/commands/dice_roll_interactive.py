from dicegame.utils.dice_roll_utils import get_random_number
from dicegame.services.dice_roll import display_dice_roll_service
from dicegame.services.dice_roll import guess_dice_roll_service


def display_dice_roll_cmd_interactive(session):
    dice_roll_result = get_random_number()

    display_dice_roll_service(dice_roll_result)


def guess_dice_roll_cmd_interactive(user_guess,session):
    dice_roll_result = get_random_number()
#    win = guess_dice_roll_service(dice_roll_result,user_guess)
    guess_dice_roll_service(dice_roll_result,user_guess,session)


