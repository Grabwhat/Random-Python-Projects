import random
def highlow():
    num = random.randint(1, 300)
    win = False
    print("\nI've picked a number from 1 and 300, can you guess it?\n")

    while win == False:
        guess = input("Guess: ")

        if 300 >= int(guess) > num:
            print("\nLower!\n")
        elif 1 <= int(guess) < num:
            print("\nHigher!\n")
        elif int(guess) == num:
            print("\nYou Won!\n")
        else:
            print("\nInvalid input, guess again.\n")

highlow()