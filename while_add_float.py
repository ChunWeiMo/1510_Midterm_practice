""" 
(5) Write a code snippet that uses a while loop to ask the user for a float and adds the float to a list called
input. Make sure the user knows they must type quit when they are finished. After the user types
quit, use a simple for loop or a list comprehension to create a list called clean_input that contains the
absolute value of each element in input.
(Recall that we can use the global abs() function to find the absolute value of a numeric literal in Python.)
"""


def add_abs():
    input_list = []
    while (True):
        number = input("Enter a float: ")
        if number == "quit":
            break
        input_list.append(float(number))

    clean_input=[]
    for number in input_list:
        clean_input.append(abs(number))
    
    return clean_input

def main():
    print(add_abs())


if __name__ == "__main__":
    main()

