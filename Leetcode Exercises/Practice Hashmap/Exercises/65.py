"""
Write a Python program to get the total length of all values in a given dictionary with string values.
Original dictionary:
{'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
Total length of all values of the said dictionary with string values:
20
"""

colour = {'#FF0000':'Red', '#800000':'Maroon', '#FFFF00':'Yellow', '#808000':'Olive'}

def check_sum_val(dicts):
    #use a generator expression to calculate the sum of lengths of all values in the input dictionary
    result = sum(len(values) for values in dicts.values())
    return result

print(check_sum_val(colour))