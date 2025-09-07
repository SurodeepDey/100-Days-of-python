import os
import random
os.system('cls')

# random integer between 1 and 10 (greater or equal to 1 and less than or equal to 10)

# random_integer = random.randint(1, 10)
# print(random_integer)

# random floating point number ( greater or equal to 0.0 and less than 1.0)
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# another floating point random number generator

# random_float = random.uniform(1, 10)
# print(random_float)


# head or tail

head = 0
tail = 1

heads_or_tails = random.randint(head, tail)
if heads_or_tails == 0:
    print(f'Heads')
else:
    print(f'Tails')