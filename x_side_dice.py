"""
Write a program that simulates rolling a die and tallies and then reports the result. Start by asking
the user for the number of sides, and then how many times they want to roll the die. You must tally and
then report the results, i.e., keep track of how many times each side is rolled, then print the results.
"""


import random


def x_side_dice():
    side = int(input("the number of sides: "))
    roll_times = int(input("how many times they want to roll the die: "))
    dice = {}
    for i in range(1, side+1):
        dice[i]=0
    
    for i in range(roll_times):
        result = random.randint(1,side)
        dice[result] += 1
    
    for side in dice:
        print("side {} appear {} times".format(side, dice[side]))


def main():
    x_side_dice()

if __name__ == "__main__":
    main()
    