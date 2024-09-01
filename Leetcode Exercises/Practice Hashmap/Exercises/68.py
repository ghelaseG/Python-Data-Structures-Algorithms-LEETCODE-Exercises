"""
Write a Python program to combine two or more dictionaries, creating a list of values for each key.
Sample Output:
Original dictionaries:
{'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
{'x': 300, 'y': 'Red', 'z': 600}
Combined dictionaries, creating a list of values for each key:
{'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}
"""

d1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
d2 = {'x': 300, 'y': 'Red', 'z': 600}

from collections import defaultdict

def combine_dict(*dictt):
    
    result = defaultdict(list)

    #iterate through the dictionaries passed as arguments
    for elements in dictt:
        #iterate through the key and values in each dictionary
        for key in elements:
            #append the value to each key to the list for that key in results 
            result[key].append(elements[key])

    #convert the defaultdict into a normal dict and return it
    return dict(result)

print(combine_dict(d1, d2))