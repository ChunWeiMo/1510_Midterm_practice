""" 
Implement a function called prepender that accepts two parameters, a list of strings and another
string. The function should modify the list by prepending (adding) the given string to the beginning of each
string in the given list. The function should modify the list given without returning anything.
"""


def prepender(list_str: list, str1):
    index = 0
    while index < len(list_str):
        list_str.insert(index, str1)
        index += 2


def main():
    list_str = ['a', 'b', 'c', 'd', 'f', 'g']
    prepender(list_str, 'h')
    print(list_str)


if __name__ == "__main__":
    main()
