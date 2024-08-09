"""
Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
Original list:
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
"""

colours = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

def grouping_dictionary(colours):
    result = {}

    for key, value in colours:
        #use 'setdefault' to append the value to the list associated with the key
        result.setdefault(key, []).append(value)
    return result

print(grouping_dictionary(colours))