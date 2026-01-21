from dicegame.commands.auth_non_interactive import(
    login_cmd,
    signup_cmd,
)
from dicegame.commands.delete_player import delete_player_cmd
#from dicegame.commands.auth import logout_cmd
from dicegame.services.leaderboard import(
    players_service,
    leaderboard_service
)
from dicegame.cli.interactive import interactive_loop
from dicegame.session.session import Session
from dicegame.utils.common_utils import inline_space
from dicegame.commands.dice_roll import(
    simple_dice_roll_cmd,
    play_dice_roll_cmd,
    guess_dice_roll_cmd
)
from dicegame.utils.errors import AppError
from dicegame.utils.rich_pkg.console import console
import sys


def dispatch(args):
    try:
        session = Session()

        if args.interactive:
            interactive_loop(session)
            return

        if args.version:
            print("dicegame-cli 0.3.1")

        if args.command == 'login':
            # login cmd
            login_cmd(args)
            return

        if args.command == 'player':
            if args.action == 'list':
                players_service()
                return

            if args.action == 'delete':
                #try:
                delete_player_cmd()
                #except AppError as e:
                #console.print(f"[error] {e} [/error]")
                 #   return 1

        if args.command == 'leaderboard':
            leaderboard_service()
            return

     #   if args.command == 'logout':
      #      logout_cmd(args)
       #     return

        if args.command == 'signup':
            signup_cmd(args)
            return

        if args.command == 'roll':
            simple_dice_roll_cmd()
            return

        if args.command == 'play':
            play_dice_roll_cmd()
            return

        if args.command == 'guess':
            guess_dice_roll_cmd(args.user_guess)
            return

    except AppError as e:
        console.print(f"[error] {e} [/error]")
        sys.exit(1)
