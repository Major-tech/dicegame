from dicegame.services.delete_player_service import(
    confirm_player_service,
    delete_player_service
)
from dicegame.utils.rich_pkg.console import console


def delete_player_cmd():
    attempts = 3

    while attempts != 0:
        player_to_delete = input("Enter player name:  ")
        attempts -= 1
        if attempts == 0:
            console.print("[error]Too many invalid attempts[/error]")
            return

        if not player_to_delete:
            console.print("[warning]Please type a valid username [/warning]")
            continue


        player_id = confirm_player_service(player_to_delete)

        if not player_id:
            console.print(f"[error]User {player_to_delete} not found[/error]")
            continue

        break

    delete_player_service(player_id)
