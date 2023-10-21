"""
There is a simple algorithm that employs exhaustive enumeration to determine the integer cube
root, if it exists, of a positive integer. Starting with a value of 0, cube the value and test if it equal to
the positive integer. If it is less than the positive integer, we must increment value and try again. If the
cube of value is greater than the positive integer, we know there is no integer cube root and we can
end. If it is equal, we have found the cube root.

Implement a function called cube_root. This function accepts a positive integer. This function is not
required to work if the argument is not a positive integer (assume zero is positive). Employ the
algorithm I just described to determine the cube root of the argument. If it exists, print it. If it doesn’t
exist, print a message in the recommended format. You may use the next page if you run out of room.

Here is what the doctest for your function would look like (this is a hint to help you develop your code):
>>> cube_root(0)
0
>>> cube_root(8)
2
>>> cube_root(9)
No cube root for 9!
>>> cube_root(27)
3
"""


def cube_root(int1):
    value = 0
    for i in range()    
