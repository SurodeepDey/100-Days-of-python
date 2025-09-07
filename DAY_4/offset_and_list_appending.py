# list: 
"""
list is a type of data structure in python
list are mutable
list always starts with []
items seperated by comma
holds items of different data types
if we want to store multiples variables in ordered way, it depends on the order in which we store the data in the list.
number list: [1, 2, 3, 4, 5]
string list: ['apple', 'banana', 'cherry']
The index starts from 0 and goes to n-1 where n is the number of items in the list.
"""
import os 
os.system('cls')

state_of_america = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia',
                    'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas',
                    'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming',
                    'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']

# print(type(state_of_america))  # <class 'list'>

# changing the value of an item in the list
state_of_america[2] = 'Old Jersey'

# print(state_of_america)

# appending items to the list

state_of_america.append('Puerto Rico')
# print(state_of_america)

# extending the list by adding multiple items to the list
state_of_america.extend(['Washington DC', 'Guam', 'American Samoa'])
# print(state_of_america)

# remove an item from the list
state_of_america.remove('Old Jersey')   
# print(state_of_america)