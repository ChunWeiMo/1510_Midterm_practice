"""
Define a function called reverse_sorted that accepts a list called my_list and returns a copy that
has been sorted in reverse order.
"""


def reverse_sorted(my_list):
    reverse = []
    while (len(my_list) > 0):
        element = my_list.pop()
        reverse.append(element)
    return reverse

def main():
    my_list = [1.1, 2.2, 3.3, 4.4, 5.5]
    reverse = reverse_sorted(my_list)
    print(reverse)


if __name__ == "__main__":
    main()
