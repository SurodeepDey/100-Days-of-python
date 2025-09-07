import os
import random
os.system('cls')

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# option 1
# pay_bill = random.choice(friends)
# print(f"{pay_bill} is going to buy the meal today!")

# option 2

starting_index = 0
ending_index = len(friends)-1
pay_bill = random.randint(starting_index, ending_index)

print(f"{friends[pay_bill]} is going to buy the meal today!") 


