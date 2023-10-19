"""
Define a function called count_evens.

The count_evens function accepts a non-empty list of integers called readings.

The count_evens function must return a tuple that contains two integers.
The first value in the tuple must be the number of even integers in the list called readings.
The second value must be the sum of the even integers in the list called readings.

You may not modify the list passed as an argument in any way, even temporarily, if you do you
will earn zero marks for this question.

You must provide a full docstring for this function including all pre- and post-conditions.
You must create two useful and different doctests for this function.
No main function is required.
"""


def count_evens(list1):
    """
    Count evens in the input list, and sum those evens.

    :param list1: a non-empty list
    :precondition: all element in list1 should be integer
    :postcondition: Count evens in the input list, and sum those evens.

    :return a tuple of even counts and the sum
    """
    evens_count = 0
    sum_evens = 0
    for number in list1:
        if number % 2 == 1:
            evens_count += 1
            sum_evens += number
    return (evens_count, sum_evens)


def main():
    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tuple1 = count_evens(list1)
    print(tuple1)
    
    list1 = [1,3,3,3,5]
    tuple1 = count_evens(list1)
    print(tuple1)
    
    list1 = [2,2,2,2,2]
    tuple1 = count_evens(list1)
    print(tuple1)


if __name__ == "__main__":
    main()
