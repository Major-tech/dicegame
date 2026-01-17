from dicegame.commands.auth_non_interactive import(
    login_cmd,
    signup_cmd,
)
from dicegame.commands.delete_user import delete_user_cmd
#from dicegame.commands.auth import logout_cmd
from dicegame.services.view import(
    view_users_service,
    view_scores_service
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

    if args.command == 'login':
        # login cmd
        login_cmd(args)
        return

    if args.command == 'view':
        space = inline_space(7)

        if args.view_cmd == 'users':
            view_users_service()
            return

        if args.view_cmd == 'scores':
            view_scores_service()
            return

 #   if args.command == 'logout':
  #      logout_cmd(args)
   #     return

    if args.command == 'signup':
        signup_cmd(args)
        return

    if args.command == 'delete':
        delete_user_cmd()
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
