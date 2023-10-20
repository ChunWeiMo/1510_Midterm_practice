""" 
Implement a function called cutoff. This function accepts two parameters: a list of integers, and
another integer. The function should return a count of the number of integers in the list that are a multiple
of the given number. Invoke this function from the main method with a set of arguments that will return
the value 3.
"""


def cutoff(list_int, base):
    count = 0
    for number in list_int:
        if number % base == 0:
            count += 1
    return count


def main():
    print(cutoff([3, 6, 9], 3))


if __name__ == "__main__":
    main()
