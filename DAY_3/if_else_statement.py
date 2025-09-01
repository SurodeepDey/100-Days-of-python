import os
os.system('cls')

print(f'Welcome to the RollerCoaster ride!')

height = int(input('What is your height in cm? '))

# if-else statement
# if height > 120:
#     print(f'You can ride the rollercoaster!')
# else:
#     print(f'Sorry, you have to grow taller before you can ride.')

# adjusting condition to include height for 120 cm also

# if height >= 120:
#     print(f'You can ride the rollercoaster!')
# else:
#     print(f'Sorry, you have to grow taller before you can ride.')

# = vs ==
# = means assignment
# == means comparison or equality check

if height == 120:
    print(f'You can ride the rollercoaster!')
else:
    print(f'Sorry, you have to grow taller before you can ride.')