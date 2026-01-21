from dicegame.utils.dice_roll_utils import get_random_number
from dicegame.services.dice_roll import(
    simple_dice_roll_service,
    play_dice_roll_service,
    guess_dice_roll_service
)


def simple_dice_roll_cmd_interactive(session):
    dice_roll_result = get_random_number()

    simple_dice_roll_service(dice_roll_result)


def play_dice_roll_cmd_interactive(session):

    for i in range(1, 4):
        roll = input("\nEnter 'r' to roll the dice: ").lower()

        if roll != "r":
            print("Please enter 'r'")
            continue
        break

    if roll != "r":
        print("\nToo many invalid attempts")
        return

    dice_roll_result = get_random_number()

    play_dice_roll_service(dice_roll_result,session)


def guess_dice_roll_cmd_interactive(user_guess,session):
    dice_roll_result = get_random_number()

    guess_dice_roll_service(dice_roll_result,user_guess,session)


