import getpass
from dicegame.utils.security import hash_password
from dicegame.services.auth import(
    login_service,
    signup_service
)
from dicegame.utils.rich_pkg.console import console


def login_cmd(args):
    while True:
        args.username = input("Username: ")
        args.password = getpass.getpass("Password: ")

        if not args.username or not args.password:
            console.print("[warning]All fields are required![/warning]")
            continue

        break

    # LOGIN SERVICE
    login_service(args.username,args.password)


def signup_cmd(args):
    while True:
        args.username = input("Username: ")
        args.password = getpass.getpass("Password: ")

        if not args.username or not args.password:
            console.print("[warning]All fields are required![/warning]")
            continue

        if len(args.password) < 3:
            console.print("[warning]Password is too short[/warning]")
            continue

        break

    # hash password
    hashed_password = hash_password(args.password)

    # SERVICE LAYER
    signup_service(args.username,hashed_password)
