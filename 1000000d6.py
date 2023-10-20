"""
Write a program that simulates rolling 1000000d6 and tallies the results. That is, roll a 6-sided die one
million times and keep track of how many times each side is rolled, then report the results.
(Consider what we need to do. We need to simulate rolling a die a million times. That suggests we need
generate a random number, and we need to use a loop. While we have not yet rolled the die a million
times, we roll it again, and record the value, keeping track of whether we’ve reach a million yet.
We probably want to record the value using a dictionary. The dictionary’s keys should be integers: 1, 2, 3,
4, 5, 6, and its values will be the number of times each number is rolled
Before any die has been rolled, the values in the dictionary will be zero of course. Suppose the first thing
we roll is a 1. The value for the key 1 will increment from 0 to 1. Suppose we roll a 1 again (imagine the
odds!). The value for the key 1 must now increment from 1 to 2.
There are at least three ways we can loop through the dictionary and print its contents. After the die has
been rolled one million times, pick one, and print the results.)
"""

import random



def dice_6():
    tallies = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    roll = 0

    while roll < 1000000:
        result = random.randrange(1, 7)
        # print("result =",result)
        if result == 1:
            tallies[1] += 1
        elif result == 2:
            tallies[2] += 1
        elif result == 3:
            tallies[3] += 1
        elif result == 4:
            tallies[4] += 1
        elif result == 5:
            tallies[5] += 1
        else:
            tallies[6] += 1
        roll += 1

    for side in tallies:
        print("Side", side, "appears", tallies[side], "times")


def main():
    dice_6()


if __name__ == "__main__":
    main()
