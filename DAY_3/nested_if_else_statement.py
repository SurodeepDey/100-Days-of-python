import os
os.system('cls')


# nested if-else statement
print(f'Welcome to the RollerCoaster ride!')
height = int(input('What is your height in cm? '))
bill = 0

if height >= 120:
    age = int(input('What is your current age (in Years)? '))
    if age < 12:
        bill = 5
        print(f'young one, please pay $5.')
    elif age>= 12 and age<= 18:
        bill = 7
        print(f'Teenager, please pay $7.')
    else:
        bill = 12
        print(f'Adult, please pay $12.')
    want_Photo = input('Do you want a photo to be takenn? Y or N. ')
    if want_Photo == 'Y':
        bill+= 3
        print(f' please add $3 to your bill.')
    else:
        print(f'No photo will be taken.')
    print(f'Total bill is : ${bill}. Enjoy the ride!')



else:
    print(f'Sorry, you have to grow taller before you can ride.')