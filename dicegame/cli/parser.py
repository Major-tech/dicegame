import argparse


def build_parser():
    """Create parser object"""

    parser = argparse.ArgumentParser(
       prog="dicegame <command> / <flag>",
       description="Roll the dice and participate in different types of game modes"
    )

    # FLAGS
    parser.add_argument('--debug',action='store_true',help='Enble debugging mode')


    parser.add_argument('-V','--version',action='store_true',help='current dicegame-cli version')


    parser.add_argument('-i','--interactive',action='store_true',help='Enter interactive mode')


    subparsers = parser.add_subparsers(dest='command')


    log = subparsers.add_parser('log',help='log file commands')

    log_sub = log.add_subparsers(dest='log_cmd',required=True)
    log_sub.add_parser('list',help='View all app logs')
    log_sub.add_parser('clear',help='Clear all app logs')


    subparsers.add_parser('report-bug',help='Report and send bugs to the developer')


    subparsers.add_parser('whoami',help='Display the currently logged-in user')


    signup = subparsers.add_parser('signup', help="user sign up")
    signup.add_argument('--username')
    signup.add_argument('--password')


    login = subparsers.add_parser('login', help="user login")
    login.add_argument('--username')
    login.add_argument('--password')


    subparsers.add_parser('leaderboard',help="view list of users and their scores")


    subparsers.add_parser('logout',help='logout user')


    # 1ST LEVEL COMMANDS
    player = subparsers.add_parser('player',help='player command')
    # 2ND LEVEL COMMANDS
    player_sub = player.add_subparsers(dest='action',required=True)

    player_sub.add_parser('list',help='A list of all players')
    player_sub.add_parser('delete',help='delete a player account')


    subparsers.add_parser('roll',help='simple dice roll.Displays the dice roll result,no points awarded')


    subparsers.add_parser('play',help='guess the dice roll output,Guess range is (1-6). Winning numbers are (4,5 or 6).5 points awarded for each correct guess')


    guess = subparsers.add_parser('guess', help='guess dice roll result.Guess range(1-6).10 points awarded for each correct guess')
    guess.add_argument('user_guess',type=int,choices= [1,2,3,4,5,6], help= "User's guess")


    # 1ST LEVEL COMMANDS
    reset = subparsers.add_parser('reset',help='reset password or user score')
    # 2MD LEVEL COMMANDS
    reset_sub = reset.add_subparsers(dest='reset_cmd',required=True)

    score = reset_sub.add_parser('score',help= 'reset user score to 0')
    score.add_argument('--password',type= str,help= "Player's password")

    password = reset_sub.add_parser('password',help='reset account password')
    password.add_argument('--password',type= str,help= "Player's password")

    return parser

