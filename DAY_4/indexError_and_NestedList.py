"""
indexError and Nested List:

suppose we have a list and 0 is starting index and 9 is ending index,
now if we want to access the 10th index, the python interpretor will throws an error which is known as indexError.
because the index 10 is out of range.

Nested list:

suppose, fruits = ['apple', 'banana', 'cherry']
vegetables = ['carrot', 'potato', 'cabbage']

dirty_dozen = [fruits, vegetables]
print(dirty_dozen) # [['apple', 'banana', 'cherry'], ['carrot', 'potato', 'cabbage']]

it generates a list inside of which contains two lists.

"""


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])