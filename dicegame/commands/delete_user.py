from dicegame.services.delete_user_service import(
    confirm_username_service,
    delete_user_service
)
from dicegame.utils.rich_pkg.console import console


def delete_user_cmd():
    attempts = 3

    while attempts != 0:
        user_to_delete = input("Enter username:  ")
        if attempts == 0:
            console.print("[error]Too many invalid attempts[/error]")
            return
        attempts -= 1

        if not user_to_delete:
            console.print("[warning]Please type a valid username [/warning]")
            continue


        user_id = confirm_username_service(user_to_delete)

        if not user_id:
            console.print(f"[error]User {user_to_delete} not found[/error]")
            continue

        break

    delete_user_service(user_id)
