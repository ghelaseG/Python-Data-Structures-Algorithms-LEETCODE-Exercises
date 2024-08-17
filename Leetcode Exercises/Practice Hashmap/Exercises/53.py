"""
Write a Python program to find the length of a dictionary of values.
"""

color_dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

def check_length(dict):

    result = {}
    for value in dict.values():
        #calculate the length of each value
        result[value] = len(value)
    return result

print(check_length(color_dict))

color_dict = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

print(check_length(color_dict))