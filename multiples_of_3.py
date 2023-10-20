""" 
If we list all the positive integers below 10 that are multiples of 3, we get 3, 6, and 9. The sum of these
multiples is 3 + 6 + 9 = 18.
Implement a function called multiples_of_3. This function accepts a single parameter called
upper_bound. Assume upper_bound is a positive integer greater than 1. This function must return the
sum of all the positive multiples of 3 below upper_bound.
"""


def multiples_of_3(upper_bound):
    sum = 0
    for number in range(0, upper_bound, 3):
        sum += number
    
    return sum


def main():
    print(multiples_of_3(10))
    print(multiples_of_3(12))

if __name__ == "__main__":
    main()
    
    
