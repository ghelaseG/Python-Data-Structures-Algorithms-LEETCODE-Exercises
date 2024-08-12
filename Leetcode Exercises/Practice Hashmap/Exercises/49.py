"""
Write a Python program to convert string values of a given dictionary into integer/float datatypes.
Original list:
[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
String values of a given dictionary, into integer types:
[{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
Original list:
[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
String values of a given dictionary, into float types:
[{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]
"""

nums_int = [
    {'x': '10', 'y': '20', 'z': '30'},
    {'p': '40', 'q': '50', 'r': '60'}
]

def convert_to_int(lst):
    #we use a list comprehension to iterate through each dictionary 
    #for each dictionary, convert the string values to integers and create a new dictionary
    result = [dict([a, int(x)] for a, x in b.items()) for b in lst]
    return result

nums_float = [
    {'x': '10.12', 'y': '20.23', 'z': '30'},
    {'p': '40.00', 'q': '50.19', 'r': '60.99'}
]

def convert_to_float(lst):
    result = [dict ([a, float(x)] for a, x in b.items()) for b in lst]
    return result

print(convert_to_int(nums_int))

print('Float')

print(convert_to_float(nums_float))