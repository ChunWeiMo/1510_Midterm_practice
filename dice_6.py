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
