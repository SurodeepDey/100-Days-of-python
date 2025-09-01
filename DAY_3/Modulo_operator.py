# The Modulo operator is represented by a percentage sign 
# It is an binary operator that returns the remainder after the division between two numbers.

# even or odd checking

import os
import ast
os.system('cls')

num = ast.literal_eval(input("Enter a number to check: "))

def isEvenOrOdd(n):
    if n%2 != 1:
        print(f'{n} is an Even number.')
    else:
        print(f'{n} is an Odd number.')
    return n

isEvenOrOdd(num)



