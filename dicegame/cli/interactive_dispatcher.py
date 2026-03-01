from dicegame.session.session_disk import Session
from dicegame.commands.auth import(
    login_cmd,
    signup_cmd,
    logout_cmd,
    reset_password_cmd
)
from dicegame.commands.leaderboard import(
    leaderboard_cmd,
    player_list_cmd
)
from dicegame.commands.dice_roll import(
    simple_dice_roll_cmd,
    play_dice_roll_cmd,
    guess_dice_roll_cmd,
    reset_score_cmd
)
from dicegame.utils.auth import(
    collect_auth_credentials,
    collect_new_password,
    collect_password
)
from dicegame.utils.logging import get_logger
from dicegame.utils.errors import(
    AppError,
    AuthError,
    NotLoggedInError,
    AlreadyLoggedInError,
    UnknownCommandError
)
from types import SimpleNamespace
from dicegame.utils.dice_roll_utils import(
    get_user_guess,
    get_random_number,
    play_mode_dice_roll_result
)
from dicegame.commands.player_delete import player_delete_cmd
from dicegame.utils.rich_pkg.console import console
from rich.panel import Panel
from dicegame.utils.auth import who_am_i
from dicegame.services.auth import load_session
from dicegame.commands.report_bug import report_bug_cmd
from dicegame.commands.logs import view_logs_cmd
from dicegame.commands.logs import clear_logs_cmd
from dicegame.utils.errors import not_logged_in
from dicegame.version import get_version
import sys


# logger
logger = get_logger(__name__)


def interactive_dispatch(session: Session):
    """Runs the interactive mode"""
    console.print(Panel("DICER (Dice Rolling Game)\nLOG IN TO PLAY",style='bold violet'))
    console.print("[info]Entering interactive mode.Enter 'exit' to quit[/info]")
    console.print("[error]NOTE: Awarded points will not be saved if not logged in[/error]\n")

    while True:
        try:
            prompt = "> "
            command = input(prompt).strip()

            # Validate cmd input
            if not command:  # blank input field
                continue

            if command == 'exit':
                console.print("[info]Exiting out of interactive mode[/info]")
                break

            if command == 'log list':
                #Ensure player is logged in
                not_logged_in(session)

                view_logs_cmd(session)
                continue

            if command == 'log clear':

                not_logged_in(session)

                clear_logs = clear_logs_cmd(session)

                if clear_logs:
                    console.print("[success]All logs cleared successfully[/success]")
                else:
                    console.print("[warning]Request aborted[/warning]")
                continue

            if command == 'report-bug':

                not_logged_in(session)

                archive_path = report_bug_cmd(session)

                if archive_path:
                    console.print("\n[success]✅ Bug report created:[/success]")
                    print(archive_path)
                    console.print("\n[info]You can now attach this file to an issue or email it to support.[/info]")
                else:
                    console.print("[info]Bug report aborted[/info]")
                continue

            if command == 'version':
                console.print(f"dicegame v{get_version()}")
                continue

            if command == 'whoami':
                user = who_am_i(session)
                if user: # display user
                    console.print(user,style= 'bold blue')
                else:  # user is logged out
                    console.print("[error]Not logged in[/error]")
                continue
            if command == 'login':
                # Check login status before initiating logging command
                if session and session.logged_in:
                    raise AlreadyLoggedInError(f'{session.username}')

                args = SimpleNamespace() # Empty args object(Imitate cli args)
                # Pre-dispatch Normalization
                username,password = collect_auth_credentials(args)
                # Dispatch Normalized data to login cmd
                session = login_cmd(username,password,session)
                console.print("[success]Login successful![/success]")
                #interactive_loop(session) # load session

            elif command == 'logout':
                session = logout_cmd(session)
                console.print("[success]User logged out successfully[/success]")

            elif command == 'player list':
                player_list_cmd(session)

            elif command == 'leaderboard':
                leaderboard_cmd(session)

            elif command == 'signup':
                # Check login status before initiating logging command
                if session and session.logged_in:
                    raise AlreadyLoggedInError(f'{session.username}')

                args = SimpleNamespace() # Empty args object(Imitate cli args)
                # Pre-dispatch Normalization
                username,password = collect_auth_credentials(args)
                # Dispatch Normalized data to signup cmd
                session = signup_cmd(username,password,session)
                console.print("[success]Signup successful![/success]")

            elif command == 'player delete':
                # Ensure player is logged in
                not_logged_in(session)

                console.print("DELETE ACCOUNT\n",style= 'bold magenta') # header                                                    

                # Prompt for account password
                args = SimpleNamespace()
                password = collect_password(args)
                # Get delete player cmd response
                delete_account =  player_delete_cmd(password,session)

                # Successful account deletion
                if delete_account.success:
                    logout_cmd(session) # logout deleted account
                    console.print(f"[success]{session.username}'s account was deleted successfully![/success]")                                     
                else:
                    # User cancelled request
                    console.print("[warning]Delete account request aborted[/warning]")

            elif command == 'roll':
                dice_roll_result = get_random_number() # get random number in range (1-6)
                result = simple_dice_roll_cmd(dice_roll_result,session)
                console.print(f"\n[success]You rolled a {result.guess}[/success]")

            elif command == 'play':

                # Get dice roll result
                dice_roll_result = play_mode_dice_roll_result(session)

                # Get PlayModeResult instance
                win = play_dice_roll_cmd(dice_roll_result,session)

                # Dice roll result
                console.print(f"\n[info]Dice roll result: {win.lucky_number}[/info]")

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

            elif command == 'guess':
                # Get user guess
                args = SimpleNamespace() # Empty args object
                guess = get_user_guess(args)
                # Get GuessModeResult instance
                win = guess_dice_roll_cmd(guess,session)

                # Dice roll results
                console.print(f"\n[info]User guess: {win.user_guess}[/info]")
                console.print(f"[info]Dice roll result: {win.lucky_number}[/info]")

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

            elif command == 'reset score':

                # Ensure player is logged in
                not_logged_in(session)

                console.print("RESET PLAYER SCORE\n",style= 'bold magenta') # header

                # Prompt for account password
                args = SimpleNamespace()
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

            elif command == 'reset password':

                # Ensure player is logged in
                not_logged_in(session)

                # Get new password
                args = SimpleNamespace() # Emptybargs object
                new_password = collect_new_password(args)

                # Get reset password cmd response
                reset_password =  reset_password_cmd(new_password,session)

                # Successful password reset
                if reset_password.success:
                    console.print(f"[success]{session.username}'s password was reset successfully![/success]")
                else:
                    # User cancelled request
                    console.print("[warning]Password reset aborted[/warning]")

            else:
                logger.exception("Interactive mode: Unknown command given")
                raise UnknownCommandError("Unknown command")

        except KeyboardInterrupt:
           console.print("[warning]Enter 'exit' to quit interactive mode[/warning]")

        except AppError as e:
            logger.exception("Interactive mode: AppError")
            console.print(f"[error] {e} [/error]")

        except Exception as e:
            logger.exception("Interactive mode: Unhandled error")
            console.print("[error] An unexpected error occurred [/error]")
