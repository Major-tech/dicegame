from dicegame.services.delete_player_service import(
    delete_player_service
)
from dicegame.utils.errors import AccountDeletionNotAllowedError,AppError
from dicegame.utils.rich_pkg.console import console
import getpass


def delete_player_cmd(session=None):
    if session:
        if session.logged_in:
            raise AccountDeletionNotAllowedError

    attempts = 3

    while attempts != 0:
        player_to_delete = input("Enter player name: ")
        password = getpass.getpass("Password: ")

        attempts -= 1
        if attempts == 0:
            console.print("[error]Too many invalid attempts[/error]")
            return

        if not player_to_delete or not password:
            console.print("[warning]All fields are required[/warning]")
            continue

        break

    delete_player_service(player_to_delete,password)

