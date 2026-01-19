from random import randint
from dicegame.utils.rich_pkg.console import console


#--------------------NON-INTERACTIVE-----------------
def get_random_number ():
    return randint(1,6)


#--------------------INTERACTIVE--------------------
def get_user_guess():
    while True:
        try:
            guess = int(input("Guess: "))

            if guess not in range(1,7):
                console.print("[warning]Guess must be between 1 and 6[/warning]")
                continue

        except ValueError:
            print("[warning]{Please enter a number[/warning]")
        else:
            break
    return guess


def not_logged_in():
    console.print("[error]Not logged in[/error]")
