from dicegame.commands.auth import(
    login_cmd,
    signup_cmd,
    logout_cmd,
    reset_password_cmd
)
from dicegame.commands.player_delete import player_delete_cmd
from dicegame.commands.leaderboard import(
    player_list_cmd,
    leaderboard_cmd
)
from dicegame.session.session_disk import Session
from dicegame.utils.common_utils import inline_space
from dicegame.commands.dice_roll import(
    simple_dice_roll_cmd,
    play_dice_roll_cmd,
    guess_dice_roll_cmd,
    reset_score_cmd
)
from dicegame.utils.errors import(
    AppError,
    AuthError,
    AlreadyLoggedInError
)
from dicegame.utils.rich_pkg.console import console,err_console
from dicegame.services.auth import load_session
from dicegame.utils.logging import get_logger
from dicegame.utils.auth import(
    collect_auth_credentials,
    collect_password,
    collect_new_password,
    who_am_i
)
import sys
from dicegame.utils.dice_roll_utils import(
    get_random_number,
    play_mode_dice_roll_result
)
from dicegame.commands.report_bug import report_bug_cmd
from dicegame.commands.logs import view_logs_cmd
from dicegame.commands.logs import clear_logs_cmd


# logger
logger = get_logger(__name__)

def dispatch(args,session):
    """Route user cli commands to appropriate command functions"""

    try:
        if args.command == 'log':
            if args.log_cmd == 'list':
                view_logs_cmd(session)
                return

            if args.log_cmd == 'clear':
                clear_logs = clear_logs_cmd(session)

                if clear_logs:
                    console.print("[success]All logs cleared successfully[/success]")
                else:
                    console.print("[warning]Request aborted[/warning]")
                return

        if args.command == 'report-bug':
            report_bug_cmd(session)
            return

        if args.version:
            print("dicegame-cli 0.6.0")
            return

        if args.command == 'whoami':
            user = who_am_i(session)
            console.print(user)
            return

        if args.command == 'login':
            # Check for any active sessions
            if session and session.logged_in:
                raise AlreadyLoggedInError(f'{session.username}')

            username,password = collect_auth_credentials(args) # get user logins
            session = login_cmd(username,password,session) # start user session after successful login
            console.print("[success]Login successful![/success]")
            session = load_session() # load session
            return

        if args.command == 'player':
            if args.action == 'list':
                player_list_cmd(session)
                return

            if args.action == 'delete':
                # Ensure player is logged in
                if not session or not session.logged_in:
                    raise AuthError("Log in required to perform this action")

                console.print("DELETE ACCOUNT\n",style= 'bold magenta') # header

                # Prompt for account password
                password = collect_password(args)
                # Get player delete cmd response
                deleted_account =  player_delete_cmd(password,session)

                # Successful account deletion
                if deleted_account.success:
                    logout_cmd(session) # logout deleted account
                    console.print(f"[success]{deleted_account.username}'s account was deleted successfully![/success]")
                else:
                    # User cancelled request
                    console.print("[warning]Delete account request aborted[/warning]")
                return

        if args.command == 'leaderboard':
            leaderboard_cmd(session)
            return

        if args.command == 'logout':
            logout_cmd(session)
            console.print("[success]User logged out successfully[/success]")
            return

        if args.command == 'signup':
            # Check for any active sessions
            if session and session.logged_in:
                raise AlreadyLoggedInError(f'{session.username}')

            username,password = collect_auth_credentials(args)
            session = signup_cmd(username,password,session)
            console.print("[success]Sign up was successful![/success]")
            return

        if args.command == 'roll':
            dice_roll_result = get_random_number() # get random number in range (1-6)
            result = simple_dice_roll_cmd(dice_roll_result,session)
            console.print(f"\n[success]You rolled a {result.guess}[/success]")

        if args.command == 'play':
            # Get dice roll result
            dice_roll_result = play_mode_dice_roll_result(session)

            # Get PlayModeResult instance
            win = play_dice_roll_cmd(dice_roll_result,session)
            # If player wins whether they are logged in or not
            if win.success:
                console.print("[success]\nWIN🥂[/success]")
                # if a logged in player wins
                if win.logged_in:
                    console.print(f"\n[success]5 points added for {session.username}[/success]\n")
            # If player loses whether they are logged in or not
            if not win.success:
                console.print('\nLOSE😢',style='yellow')
                # if a logged in player loses
                if win.logged_in:
                    console.print("No points added",style='yellow')
            return

        if args.command == 'guess':

            # Get GuessModeResult instance
            win = guess_dice_roll_cmd(args.user_guess,session)

            # If player wins whether they are logged in or not
            if win.success:
                console.print("[success]\nWIN🥂[/success]")
                # if a logged in player wins
                if win.logged_in:
                    console.print(f"\n[success]10 points added for {session.username}[/success]")
            # If player loses whether they are logged in or not
            if not win.success:
                console.print('\nLOSE😢',style='yellow')
                # if a logged in player loses
                if win.logged_in:
                    console.print("No points added",style='yellow')
            return


        if args.command == 'reset':
            if args.reset_cmd == 'score':

                 # Ensure player is logged in
                if not session or not session.logged_in:
                    raise AuthError("Log in required to perform this action")

                console.print("RESET PLAYER SCORE\n",style= 'bold magenta') # header

                # Prompt for account password
                password = collect_password(args)
                # Get reset score cmd response
                reset_score =  reset_score_cmd(password,session)

		# Successful score reset
                if reset_score.success:
                    console.print(f"[success]{session.username}'s score was reset successfully![/success]")
                    console.print(f"Previous score: {reset_score.previous_score} points")
                else:
     		    # User cancelled request
                    console.print("[warning]Score reset aborted[/warning]")
                return

            if args.reset_cmd == 'password':

                # Ensure player is logged in
                if not session or not session.logged_in:
                    raise AuthError("Log in required to perform this action")

                # Get new password
                new_password = collect_new_password(args)

                # Get reset password cmd response
                reset_password =  reset_password_cmd(new_password,session)

                # Successful password reset
                if reset_password.success:
                    console.print(f"[success]{session.username}'s password was reset successfully![/success]")
                else:
                    # User cancelled request
                    console.print("[warning]Password reset aborted[/warning]")
                return

    except AppError as e:
        logger.error(e)
        console.print(f"[error] {e} [/error]")
        return

    except Exception as e:
        logger.exception("Unhandled main error")
        err_console.print("An internal error occurred",style='bold red')
        raise
     #   sys.exit(1) # use this in production, not raise

    except KeyboardInterrupt:
        console.print("[error]\n\nExiting...[/error]")


