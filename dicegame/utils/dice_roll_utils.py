from random import randint


#--------------------NON-INTERACTIVE-----------------
def get_random_number ():
    return randint(1,6)


#--------------------INTERACTIVE--------------------
def get_user_guess():
    while True:
        try:
            guess = int(input("Guess: "))

            if guess not in range(1,7):
                print("Guess must be between 1 and 6")
                continue

        except ValueError:
            print("Please enter a number")
        else:
            break
    return guess
