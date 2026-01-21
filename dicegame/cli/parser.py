import argparse


def build_parser():
    parser = argparse.ArgumentParser(
       prog="Simple Dice Game",
       description="Roll the dice and participate in different types of game options"
    )

    parser.add_argument('-V','--version',action='store_true',help='current app version')

    parser.add_argument('-i','--interactive',action='store_true',help='Enter interactive mode')

    subparsers = parser.add_subparsers(dest='command',required=False)

    signup = subparsers.add_parser('signup', help="user sign up")
    signup.add_argument('--username')
    signup.add_argument('--password')


    login = subparsers.add_parser('login', help="user login")
    login.add_argument('--username')
    login.add_argument('--password')


    leaderboard = subparsers.add_parser('leaderboard',help="See leaderboard,list of users and their scores")


    #logout = subparsers.add_parser('logout',help='logout user')

    #-------------------PLAYER CMD----------------
    # 1ST LEVEL CMDs
    player = subparsers.add_parser('player',help='player command')

    # 2ND LEVEL CMDs
    player_sub = player.add_subparsers(dest='action',required=True)

    player_sub.add_parser('list',help='A list of all players')
    player_sub.add_parser('delete',help='delete a player account')


    roll = subparsers.add_parser('roll',help='simple dice roll,no points awarded')

    play = subparsers.add_parser('play',help='guess the dice roll output,winning numbers are (4,5 or 6)')

    guess = subparsers.add_parser('guess', help='guess dice roll result')
    guess.add_argument('user_guess',type=int,choices= [1,2,3,4,5,6], help= "User's guess")

    return parser
