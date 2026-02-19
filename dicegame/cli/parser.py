
import argparse


def build_parser() -> argparse.ArgumentParser:
    """
    dicegame CLI Parser

    Professional behavior:
    - Running `dicegame` with no args shows help/usage.
    - Commands are grouped cleanly.
    - Subcommands are required where appropriate.
    """

    parser = argparse.ArgumentParser(
        prog="dicegame",
        description=(
            "dicegame — a CLI dice rolling game.\n\n"
            "Play dice challenges, manage user accounts, view leaderboards,\n"
            "and interact with the game directly from your terminal."
        ),
        usage="dicegame <command> [options]",
        epilog=(
            "Quick Examples:\n"
            "  dicegame signup --username dennis --password secret\n"
            "  dicegame login --username dennis --password secret\n\n"

            "  ⚠️ Note: The `--password` flag is ignored for security reasons.\n"
            "  Command-line passwords can leak via shell history or process lists.\n"
            "  So dicegame always prompts securely instead. For best practice, omit `--password` entirely.\n"
            "  It appears only as a reference for automation tools that may inject credentials via secure prompts or environment-based workflows.\n\n"

            "  dicegame play\n"
            "  dicegame guess 4\n"
            "  dicegame leaderboard\n"
            "  dicegame log list\n\n"
            "Command Help:\n"
            "  dicegame <command> -h\n"
            "  dicegame player -h\n"
            "  dicegame reset score -h\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # ============================================================
    # GLOBAL FLAGS
    # ============================================================
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug output (useful for troubleshooting).",
    )

    parser.add_argument(
        "-V",
        "--version",
        action="store_true",
        help="Show the installed DiceGame CLI version and exit.",
    )

    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Start DiceGame in interactive shell mode.",
    )

    # ============================================================
    # TOP-LEVEL COMMANDS
    # ============================================================
    subparsers = parser.add_subparsers(
        dest="command",
        title="Commands",
        metavar="<command>",
        required=False,
    )

    # ============================================================
    # LOG COMMAND (2-level)
    # ============================================================
    log = subparsers.add_parser(
        "log",
        help="Inspect and manage application logs.",
        description=(
            "The log command provides tools for viewing or clearing\n"
            "DiceGame's stored application logs.\n\n"
            "Logs are useful for debugging and auditing gameplay events."
        ),
        epilog=(
            "Examples:\n"
            "  dicegame log list\n"
            "  dicegame log clear\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    log_sub = log.add_subparsers(
        dest="log_cmd",
        title="Log Commands",
        metavar="<log_cmd>",
        required=True,
    )

    log_sub.add_parser(
        "list",
        help="Display all stored application logs.",
        description=(
            "Prints the complete log history recorded by DiceGame.\n"
            "Useful when investigating errors or reviewing activity."
        ),
        epilog="Example:\n  dicegame log list\n",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    log_sub.add_parser(
        "clear",
        help="Delete all stored application logs.",
        description=(
            "Removes all log entries from the local log file.\n"
            "Use with caution — this action cannot be undone."
        ),
        epilog="Example:\n  dicegame log clear\n",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # ============================================================
    # REPORT BUG
    # ============================================================
    subparsers.add_parser(
        "report-bug",
        help="Submit a bug report to the developer.",
        description=(
            "Use this command to report unexpected behavior, crashes,\n"
            "or gameplay issues directly to the DiceGame developer."
        ),
        epilog="Example:\n  dicegame report-bug\n",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # ============================================================
    # WHOAMI
    # ============================================================
    subparsers.add_parser(
        "whoami",
        help="Show the currently logged-in user.",
        description=(
            "Displays information about the active session.\n\n"
            "- If logged in: prints your username.\n"
            "- If not logged in: informs you no session is active."
        ),
        epilog=(
            "Examples:\n"
            "  dicegame whoami\n\n"
            "Notes:\n"
            "  - This command does not modify your session.\n"
            "  - Works in both CLI and interactive mode.\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # ============================================================
    # SIGNUP
    # ============================================================
    signup = subparsers.add_parser(
        "signup",
        help="Create a new DiceGame account.",
        description=(
            "Registers a new user account.\n\n"
            "You must provide a username and password."
            """ ⚠️ Note: The `--password` flag is ignored for security reasons.
            Command-line passwords can leak via shell history or process lists, so dicegame always                    prompts securely instead. For best practice, omit `--password` entirely.                                  it appears only as a reference for automation tools that may inject credentials via
            secure prompts or environment-based workflows.\n"""
        ),
        epilog="Example:\n  dicegame signup --username dennis --password secret\n",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    signup.add_argument(
        "--username",
        required=False,
        help="Desired username for the new account.",
    )
    signup.add_argument(
        "--password",
        required=False,
        help="Password for the new account.",
    )

    # ============================================================
    # LOGIN
    # ============================================================
    login = subparsers.add_parser(
        "login",
        help="Log into an existing DiceGame account.",
        description=(
            "Authenticates a user and starts an active session.\n\n"
            "You must be logged in to play scoring game modes."
        ),
        epilog="Example:\n  dicegame login --username dennis --password secret\n",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    login.add_argument("--username", type=str, required=False, help="Your account username.")
    login.add_argument("--password", type=str, required=False, help=argparse.SUPPRESS) # hide help

    # ============================================================
    # LEADERBOARD
    # ============================================================
    subparsers.add_parser(
        "leaderboard",
        help="View the top players and their scores.",
        description=(
            "Displays the DiceGame leaderboard ranked by score.\n"
            "Use this to compare your progress with other players."
        ),
        epilog="Example:\n  dicegame leaderboard\n",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # ============================================================
    # LOGOUT
    # ============================================================
    subparsers.add_parser(
        "logout",
        help="Log out of the current session.",
        description=(
            "Ends the active user session.\n\n"
            "After logout, scoring commands will require logging in again."
        ),
        epilog="Example:\n  dicegame logout\n",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # ============================================================
    # PLAYER COMMAND (2-level)
    # ============================================================
    player = subparsers.add_parser(
        "player",
        help="Manage player accounts.",
        description=(
            "Player management commands.\n\n"
            "Use these tools to list all registered users or delete accounts."
        ),
        epilog=(
            "Examples:\n"
            "  dicegame player list\n"
            "  dicegame player delete\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    player_sub = player.add_subparsers(
        dest="action",
        title="Player Actions",
        metavar="<action>",
        required=True,
    )

    player_sub.add_parser(
        "list",
        help="List all registered players.",
        description="Displays all user accounts currently stored in DiceGame.",
        epilog="Example:\n  dicegame player list\n",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    player_sub.add_parser(
        "delete",
        help="Delete a player account.",
        description=(
            "Deletes a player account from the system.\n"
            "This action may be permanent depending on implementation."
        ),
        epilog="Example:\n  dicegame player delete\n",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # ============================================================
    # ROLL
    # ============================================================
    subparsers.add_parser(
        "roll",
        help="Roll a dice once (no points awarded).",
        description=(
            "Performs a simple dice roll and prints the result.\n\n"
            "This command does not affect scoring."
        ),
        epilog="Example:\n  dicegame roll\n",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # ============================================================
    # PLAY
    # ============================================================
    subparsers.add_parser(
        "play",
        help="Start a scoring dice game round in 'play' mode.",
        description=(
            "Begins a dice guessing game in 'play' mode.\n\n"
            "Winning dice roll numbers are between 4, 5 and 6.\n"
        ),
        epilog="Example:\n  dicegame play\n",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # ============================================================
    # GUESS
    # ============================================================
    guess = subparsers.add_parser(
        "guess",
        help="Submit your dice guess (1–6).",
        description=(
            "Submit a number between 1 and 6 as your dice guess.\n\n"
            "If the guess matches the winning roll, points are awarded."
        ),
        epilog="Example:\n  dicegame guess 4\n",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    guess.add_argument(
        "user_guess",
        type=int,
        choices=[1, 2, 3, 4, 5, 6],
        help="Your guess (must be an integer from 1 to 6).",
    )

    # ============================================================
    # RESET COMMAND (2-level)
    # ============================================================
    reset = subparsers.add_parser(
        "reset",
        help="Reset password or score.",
        description=(
            "Reset account-related values such as score or password.\n\n"
            "Subcommands determine what is being reset."
        ),
        epilog=(
            "Examples:\n"
            "  dicegame reset score --password secret\n"
            "  dicegame reset password --password secret\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    reset_sub = reset.add_subparsers(
        dest="reset_cmd",
        title="Reset Commands",
        metavar="<reset_cmd>",
        required=True,
    )

    score = reset_sub.add_parser(
        "score",
        help="Reset your score back to 0.",
        description="Sets the current player's score to zero.",
        epilog="Example:\n  dicegame reset score --password secret\n",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    password = reset_sub.add_parser(
        "password",
        help="Reset your account password.",
        description="Allows a player to reset their account password securely.",
        epilog="Example:\n  dicegame reset password --password oldpass\n",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    return parser

