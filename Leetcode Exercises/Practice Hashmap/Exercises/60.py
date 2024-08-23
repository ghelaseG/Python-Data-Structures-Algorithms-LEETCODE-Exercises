"""
Write a Python program to find the shortest list of values for the keys in a given dictionary.
Original Dictionary: {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]} Shortest list of values with the keys of the said dictionary: ['VI', 'VIII', 'X']
"""

dictt = {
    'V': [10, 12],
    'VI': [10],
    'VII': [10, 20, 30, 40],
    'VIII': [20],
    'IX': [10, 30, 50, 70],
    'X': [80]
}

def check(dictt):
    #define a minimum value for the length of sublists
    min_value = 1

    #create a list of 'k' keys for which the length of the associated list 'v' is equal to 'min_value'
    result = [k for k , v in dictt.items() if len(v) == min_value]

    #return the list of keys
    return result

print(check(dictt))