import getpass
from dicegame.utils.security import hash_password
from dicegame.services.auth import(
    login_service,
    signup_service
)


def login_cmd(args):
    while True:
        args.username = input("Username: ")
        args.password = getpass.getpass("Password: ")

        if not args.username or not args.password:
            print("All fields are required!")
            continue

        break

    # LOGIN SERVICE
    login_service(args.username,args.password)


def signup_cmd(args):
    while True:
#        if not args.username:
        args.username = input("Username: ")
        #if not args.password:
        args.password = getpass.getpass("Password: ")

        if not args.username or not args.password:
            print("All fields are required!")
            continue

        if len(args.password) < 3:
            print("Password is too short")
            continue

        break

    # hash password
    hashed_password = hash_password(args.password)

    # SERVICE LAYER
    signup_service(args.username,hashed_password)
