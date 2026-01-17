import argparse


def build_parser():
    parser = argparse.ArgumentParser(
       prog="Simple Dice Game",
       description="Roll the dice and participate in different types of game options"
    )

    parser.add_argument('-i','--interactive',action='store_true',help='Enter interactive mode')

    subparsers = parser.add_subparsers(dest='command',required=False)

    signup = subparsers.add_parser('signup', help="user sign up")
    signup.add_argument('--username')
    signup.add_argument('--password')

    login = subparsers.add_parser('login', help="user login")
    login.add_argument('--username')
    login.add_argument('--password')

    view = subparsers.add_parser('view', help="display list of users of high scores")
    # view subcommands(actions)
    view_sub = view.add_subparsers(dest="view_cmd",required=True)
    users = view_sub.add_parser("users")
    scores = view_sub.add_parser('scores')

    #logout = subparsers.add_parser('logout',help='logout user')

    delete = subparsers.add_parser('delete',help='Delete user account')
    delete_sub = delete.add_subparsers(dest='del_cmd',required=True)
    user = delete_sub.add_parser('user')

    display = subparsers.add_parser('display',help='display computer dice roll result only')

    guess = subparsers.add_parser('guess', help='guess dice roll result')
    guess.add_argument('user_guess',type=int,choices= [1,2,3,4,5,6], help= "User's guess")

    return parser
