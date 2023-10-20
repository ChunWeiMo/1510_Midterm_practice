""" 
(5) Suppose there are three seating categories in a venue. Class A seats cost $40. Class B seats cost $25.
Class C seats cost $10. I know it sounds cheap, but let’s pretend everything is affordable again. Write a
program that asks the user how many seats for each class were sold, and then displays the total amount of
income generated from ticket sales. Indirection is unnecessary.
(Before you start coding, break this problem down into a sequence of steps. For each step, think about
which control structure(s) you can use. Remember, there is no need for indirection. Keep it simple.)
"""

price_A = 40
price_B = 25
price_C = 10

seat_A = int(input("How many seat A were sold: "))
seat_B = int(input("How many seat B were sold: "))
seat_C = int(input("How many seat C were sold: "))

total_income = price_A * seat_A + price_B * seat_B + price_C * seat_C
print(total_income)