"""
Write a Python program that creates key-value list pairings within a dictionary.
Original dictionary:
{1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
A key-value list pairings of the said dictionary:
[{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]
"""

students = {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}

from itertools import product
 
def transform(dictt):
    #use list comprehension to create a list of dictionaries by pairing keys from dictt
    ##with all possible combinations of values from the input dictionary
    result = [dict(zip(dictt,sub)) for sub in product(*dictt.values())]
    return result

print(transform(students))