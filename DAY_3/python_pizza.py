import os
os.system('cls')

print(f'Welcome to python pizza deliveries!')

pizza_size = input('What size of pizza do you want (S, M, L)? ')
add_pepperoni = input('Do you want to add Pepperoni? Y or N. ')
cheese = input("Do you want extra cheese? Y or N. ")
bill = 0

# approach 1:
# if pizza_size == 'S':
#     bill = 15
#     if add_pepperoni == 'Y':
#         bill+= 2
#     if cheese == 'Y':
#         bill+= 1
# elif pizza_size == 'M':
#     bill = 20
#     if add_pepperoni == 'Y':
#         bill+= 3
#     if cheese == 'Y':
#         bill+= 1
# elif pizza_size == 'L':
#     bill = 25
#     if add_pepperoni == 'Y':
#         bill+= 3
#     if cheese == 'Y':
#         bill+= 1
# else:
#     print(f'Invalid size of pizza selected.')

# print(f'The final bill you need to pay is : ${bill}. Enjoy !!')


# approach 2: using nested if-else statement
if pizza_size == 'S':
    bill+= 15
elif pizza_size == 'M':
    bill+= 20
elif pizza_size == 'L':
    bill+= 25
else:
    print(f'Invalid size of pizza selected.')

if add_pepperoni == 'Y':
    if pizza_size == 'S':
        bill+=2
    else:
        bill+3

if cheese == 'Y':
    bill+=1

print(f'The final bill is : ${bill}. Enjoy !!')


