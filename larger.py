"""
Define a function called larger that accepts two parameters in this order: a list called measurements
and a float called tolerance. Assume the list contains floats and has non-zero length. The function
should return a new list that consists of all the numbers in the list called measurements that are greater
than tolerance.
"""


def larger(measurements, tolerance):
    after_tolerance = []
    for number in measurements:
        if number >= tolerance:
            after_tolerance.append(number)
    measurements = after_tolerance
    return measurements


def main():
    measurements = [1.1, 2.2, 3.3, 4.4, 5.5]
    after_tolerance = larger(measurements, 4.0)
    print(after_tolerance)


if __name__ == "__main__":
    main()
