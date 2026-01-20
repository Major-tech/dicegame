from dicegame.session.session import Session
from dicegame.commands.auth_interactive import(
    login_cmd_interactive,
    logout_cmd_interactive,
    signup_cmd_interactive
)
from dicegame.commands.leaderboard_interactive import(
    player_list_cmd_interactive,
    leaderboard_cmd_interactive
)
from dicegame.commands.dice_roll_interactive import(
    display_dice_roll_cmd_interactive
)
from dicegame.commands.dice_roll_interactive import guess_dice_roll_cmd_interactive
from dicegame.utils.dice_roll_utils import get_user_guess

from dicegame.commands.delete_player  import delete_player_cmd
from dicegame.utils.dice_roll_utils import not_logged_in
from dicegame.utils.rich_pkg.console import console
from rich.panel import Panel


def handle_command_interactive(command,session):
    if command == 'login':
        if session.logged_in:
            console.print(f"[error]You're already logged in as {session.username}[/error]")
            return

        login_cmd_interactive(session)

    elif command == 'logout':
        logout_cmd_interactive(session)

    elif command == 'player list':
        if not session.logged_in:
            not_logged_in()
            return

        player_list_cmd_interactive(session)

    elif command == 'leaderboard':
        if not session.logged_in:
            not_logged_in()
            return

        leaderboard_cmd_interactive(session)

    elif command == 'signup':
        if session.logged_in:
            console.print(f"[error]Log out of the existing account first![/error]")
            return

        signup_cmd_interactive()

    elif command == 'player delete':
        if not session.logged_in:
            not_logged_in()
            return
        delete_player_cmd()

    elif command == 'display':
        if not session.logged_in:
            not_logged_in()
            return

        display_dice_roll_cmd_interactive(session)

    elif command == 'guess':
        if not session.logged_in:
            not_logged_in()
            return

        guess = get_user_guess()
        guess_dice_roll_cmd_interactive(guess,session)

    else:
        console.print("[error]Unknown command[/error]")


def interactive_loop(session):
    console.print(Panel("DICER (Dice rolling game)\nLOG IN TO PLAY",style='bold violet'))
    console.print("[info]Entering interactive mode.Enter 'exit' to quit[/info]")

    while True:
        try:
            prompt = "> "
            command = input(prompt).strip()

            # Validate cmd input
            if not command:
                continue

            if command == 'exit':
                console.print("[info]Exiting out of interactive mode[/info]")
                break

            handle_command_interactive(command,session)

        except KeyboardInterrupt:
           console.print("[warning]Enter 'exit' to quit interactive mode[/warning]")

#0792674857 (junior ndunyu stage)
