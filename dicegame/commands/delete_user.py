from dicegame.services.delete_user_service import(
    confirm_username_service,
    delete_user_service
)


def delete_user_cmd():
    attempts = 3

    while attempts != 0:
        user_to_delete = input("Enter username:  ")
        if attempts == 0:
            print("Too many invalid attempts")
            return
        attempts -= 1

        if not user_to_delete:
            print("Please type a valid username ")
            continue


        user_id = confirm_username_service(user_to_delete)

        if not user_id:
            print(f"User {user_to_delete} not found")
            continue

        break

    delete_user_service(user_id)
