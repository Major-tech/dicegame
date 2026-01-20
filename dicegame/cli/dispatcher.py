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
    display_dice_roll_cmd,
    guess_dice_roll_cmd
)


def dispatch(args):
    session = Session()

    if args.interactive:
        interactive_loop(session)
        return

    if args.version:
        print("dicegame-cli v0.3.1")

    if args.command == 'login':
        # login cmd
        login_cmd(args)
        return

    if args.command == 'player':
        if args.action == 'list':
            players_service()
            return

        if args.action == 'delete':
            delete_player_cmd()
            return

    if args.command == 'leaderboard':
        leaderboard_service()
        return

 #   if args.command == 'logout':
  #      logout_cmd(args)
   #     return

    if args.command == 'signup':
        signup_cmd(args)
        return

    if args.command == 'display':
        display_dice_roll_cmd()
        return

    if args.command == 'guess':
        guess_dice_roll_cmd(args.user_guess)
        return

    print("\nHELP:",end=' ')
    print("Enter dicegame -h or dicegame --help")
    print(inline_space(5),"Read README.md to see accepted commands")
