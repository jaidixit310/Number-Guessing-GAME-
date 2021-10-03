import random as rnd
# Importing Random file for its various functions

# Defining a function to determine the winner of the game
def win(start, end , number):
    # Giving the second hint to the user
    y = int(number / 10)
    if tries == 1 and user != number:
        print("You guessed wrong! Try Again")
        print(f"Hint 2: Its between {y * 10} and {y * 10 + 10}.")# Printing the range in which the number lies
    # Giving the third hint to the user
    elif tries == 2 and user != number:
        print("You guessed wrong! Try Again")
        print("Its factors are:-") # Printing its factors in the hint
        for i in range(start, end):
            if number % i == 0:
                if not number / i == 1:
                    print(i)
        print("Last factor is not given")
    # If the user exceeds the amount of tries he has, he looses
    elif tries == 3 and user != number:
        print("Sorry! You lost")
        print(f"The number was {x}")
    # If the user found the number
    elif user == number:
        print("Yeeeeeeeeeeeeeeee! You won")
        return True
    return False

# To count the number of the tries the player has taken in guessing the nubmer
tries = 0
# To control the loop (If player doesn't want to play again then "again = False". This will stop the loop)
again = True

# Running the game's menu kind of part
while again:
    a = int(input("Give the starting point: ")) # Starting point for random number selection
    b = int(input("Give the ending point: ")) # Ending point for random number selection
    finished = False # To check whether the game is finished or not
    x = rnd.randint(a, b) # Getting a random number
    print(f"Hello I am the Comms, I have chosen a random number, can you guess it? Its between {a} and {b}")
    # Running the game
    while not finished:
        # Counting the tries
        tries += 1
        # Giving the first Hint to the user
        if tries == 1:
            if x % 2 == 0:
                print("Hint 1: Its an even number")
            else:
                print("Hint 1: Its an odd number")
        # Taking the guessed number of the user
        user = int(input("Number: "))
        # Checking whether the guessed number is right or wrong
        if win(a, b, x):
            # If the user won
            finished = True
            # Game finished
            tryagain = input("Want to play again? (y/n): ")
            # If he wants to play again the game
            # Marking the tries to 0
            tries = 0
            # Checking the user's input
            if tryagain.lower() == "y":
                print("Restarting")
            # If he doesn't wants to play then the game's main loop ends thus ending the game
            elif tryagain.lower() == "n":
                print("Byeeeee!")
                again = False
            else:
                print("Wrong Input, so Byeeee!")
                again = False
        # If the user is not able to guess the number in 3 times then the game ends.
        elif tries == 3 and user != x:
            finished = True
            # Finishing the game
            tryagain = input("Want to play again? (y/n): ")
            # In case he wants to play again
            tries = 0
            if tryagain.lower() == "y":
                print("Restarting\n")
            elif tryagain.lower() == "n":
                print("Byeeeee!")
                again = False
            else:
                print("Wrong Input, so Byeeee!")
                again = False
