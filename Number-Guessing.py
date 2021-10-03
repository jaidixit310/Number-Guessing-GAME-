import random as rnd


def win(start, end , number):
    y = int(number / 10)
    if tries == 1 and user != number:
        print("You guessed wrong! Try Again")
        print(f"Hint 2: Its between {y * 10} and {y * 10 + 10}.")
    elif tries == 2 and user != number:
        print("You guessed wrong! Try Again")
        print("Its factors are:-")
        for i in range(start, end):
            if number % i == 0:
                if not number / i == 1:
                    print(i)
        print("Last factor is not given")
    elif tries == 3 and user != number:
        print("Sorry! You lost")
        print(f"The number was {x}")
    elif user == number:
        print("Yeeeeeeeeeeeeeeee! You won")
        return True
    return False


'''def retry():
    finished = True
    tryagain = input("Want to play again? (y/n): ")
    tries = 0
    if tryagain.lower() == "y":
        print("Restarting")
    elif tryagain.lower() == "n":
        print("Byeeeee!")
        again = False
    else:
        print("Wrong Input, so Byeeee!")
        again = False'''

tries = 0
again = True

while again:
    a = int(input("Give the starting point: "))
    b = int(input("Give the ending point: "))
    finished = False
    x = rnd.randint(a, b)
    print(f"Hello I am the Comms, I have chosen a random number, can you guess it? Its between {a} and {b}")
    while not finished:
        tries += 1
        if tries == 1:
            if x % 2 == 0:
                print("Hint 1: Its an even number")
            else:
                print("Hint 1: Its an odd number")
        user = int(input("Number: "))
        if win(a, b, x):
            finished = True
            tryagain = input("Want to play again? (y/n): ")
            tries = 0
            if tryagain.lower() == "y":
                print("Restarting")
            elif tryagain.lower() == "n":
                print("Byeeeee!")
                again = False
            else:
                print("Wrong Input, so Byeeee!")
                again = False
        elif tries == 3 and user != x:
            finished = True
            tryagain = input("Want to play again? (y/n): ")
            tries = 0
            if tryagain.lower() == "y":
                print("Restarting")
            elif tryagain.lower() == "n":
                print("Byeeeee!")
                again = False
            else:
                print("Wrong Input, so Byeeee!")
                again = False