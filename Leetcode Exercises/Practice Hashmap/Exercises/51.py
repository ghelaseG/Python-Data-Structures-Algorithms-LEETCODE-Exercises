"""
A Python Dictionary contains List as a value. Write a Python program to update the list values in the said dictionary.
Original Dictionary:
{'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
Update the list values of the said dictionary:
{'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}
"""

dictionary = { 
    'Math': [88, 89, 90], 
    'Physics': [92, 94, 89],
    'Chemistry': [90, 87, 93]
}

def test(dictionary):

    dictionary['Math'] = [x + 1 for x in dictionary['Math']]
    dictionary['Physics'] = [x - 2 for x in dictionary['Physics']]
    
    return dictionary

print(test(dictionary))