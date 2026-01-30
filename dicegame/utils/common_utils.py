# COMMON UTILS
from dicegame.utils.rich_pkg.console import console


# FUNCTIONS

def inline_space(spaces):
    """Returns the specified number of inline spaces"""

    return ' ' * spaces


def confirm_reset() -> bool:
    """Confirm reset commands"""

    attempts = 3

    while attempts != 0:
        reset = input("This action is irreversible.Proceed? y/n: ").lower()

        attempts -= 1

        if attempts == 0:
            console.print("[error]Too many invalid attempts[/error]")
            break

        if reset == 'n': # user cancels request
            break

        if reset == 'y': # user confirms reset command
            return True

        if not reset: # blank field7
            console.print("[warning]You did not type anything![/warning]")
            continue

        if reset != 'y' or reset != 'n': # invalid input
            console.print("[warning]Invalid option[/warning]")
            continue

    return False
