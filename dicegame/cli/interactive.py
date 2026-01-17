from dicegame.session.session import Session
from dicegame.commands.auth_interactive import(
    login_cmd_interactive,
    logout_cmd_interactive,
    signup_cmd_interactive
)
from dicegame.commands.view_interactive import(
    view_users_cmd_interactive,
    view_scores_cmd_interactive
)
from dicegame.commands.dice_roll_interactive import(
    display_dice_roll_cmd_interactive
)
from dicegame.commands.dice_roll_interactive import guess_dice_roll_cmd_interactive
from dicegame.utils.dice_roll_utils import get_user_guess

from dicegame.commands.delete_user  import delete_user_cmd


def handle_command_interactive(command,session):
    if command == 'login':
        if session.logged_in:
            print(f"You're already logged in as {session.username}")
            return

        login_cmd_interactive(session)

    elif command == 'logout':
        logout_cmd_interactive(session)

    elif command == 'view users':
        if not session.logged_in:
            print('Not logged in')
            return

        view_users_cmd_interactive(session)

    elif command == 'view scores':
        if not session.logged_in:
            print("Not logged in")
            return

        view_scores_cmd_interactive(session)

    elif command == 'signup':
        if session.logged_in:
            print(f"Log out of the existing account first!")
            return

        signup_cmd_interactive()

    elif command == 'delete user':
        if not session.logged_in:
            print("Not logged in")
            return
        delete_user_cmd()

    elif command == 'display':
        if not session.logged_in:
            print("Not logged in")
            return

        display_dice_roll_cmd_interactive(session)

    elif command == 'guess':
        if not session.logged_in:
            print('Not logged in')
            return

        guess = get_user_guess()
        guess_dice_roll_cmd_interactive(guess,session)

    else:
        print("Unknown command")


def interactive_loop(session):
    print("Entering interactive mode.Enter 'exit' to quit")

    while True:
        try:
            prompt = "> "
            command = input(prompt).strip()

            # Validate cmd input
            if not command:
                continue

            if command == 'exit':
                print("Exiting out of interactive mode")
                break

            handle_command_interactive(command,session)

        except KeyboardInterrupt:
           print("Enter 'exit' to quit interactive mode")

#0792674857 (junior ndunyu stage)
