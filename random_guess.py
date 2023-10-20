""" 
(5) Write a program that generates a random number in the range of 1 through 100, and asks the user to
guess what the number is. While the user’s guess is higher than the random number or lower than the
random number, the program should display “Too high, try again” or “Too low, try again” as appropriate.
When the user correctly guesses the number, print out the number of guesses the user made.
(Recall that the random module contains a function called randint(a, b) which accepts two integers
and returns a random integer N such that a <= N <= b.)
"""

import random


def random_guess():
    random_number = random.randint(1, 100)
    while (True):
        guess = int(input("Guess a number: "))
        if guess > random_number:
            print("Too high, try again")
        elif guess < random_number:
            print("Too low, try again")
        else:
            print("Correct")
            print("The number is", random_number)
            break


def main():
    random_guess()


if __name__ == "__main__":
    main()
