"""
Define a function called list_maker that accepts two parameters in this order: an integer called
lower_bound, and an integer called upper_bound. The list_maker function must ensure
lower_bound is strictly less than upper_bound. If it is, list_maker will return a list composed of the
sequence of integers from lower_bound to upper_bound inclusive. Otherwise, list_maker will return
an empty list.
"""


def list_maker(lower_bound, upper_bound):
    if lower_bound < upper_bound:
        between=range(lower_bound, upper_bound+1)
    else:
        between=list()
    return between


def main():
    print(list_maker(2,4))


if __name__ == "__main__":
    main()

