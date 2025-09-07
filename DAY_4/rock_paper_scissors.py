import random
import os
import sys
os.system('cls')

try:
    choice = int(input('What do you want to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: '))
except ValueError:
    print('Invalid Input. Please enter a number (0, 1, or 2).')
    sys.exit(1)

if choice not in [0, 1, 2]:
    print('Invalid choice. Please choose 0, 1 or 2.')
    sys.exit(1)

choices = ["Rock", "Papers", "Scissors"]
i_choose = choices[choice]
print(f'Your choice: {i_choose}')

computer_choice = random.randint(0, 2)
you_choose = choices[computer_choice]
print(f'Computer choice: {you_choose}')

if choice == computer_choice:
    print(f'Your choice is {i_choose}, computer chooses {you_choose}. It\'s a Draw.')
elif (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 0):
    print(f'Your choice is {i_choose}, Computer chooses {you_choose}. {you_choose} wins.')
else:
    print(f'Your choice is {i_choose}, Computer chooses {you_choose}. {i_choose} wins.')