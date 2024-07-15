"""
Write a Python program to map two lists into a dictionary.
"""

keys = ['red', 'green', 'blue']

values = ['#FF0000', '#008000', '#0000FF']

#we use zip function to create a tuple with the 2 lists and pair each color name
new_dict = zip(keys, values)
convert_to_dict = dict(new_dict)
print(convert_to_dict)
#if you want to print the tuple, before we convert it to dict, use this:
"""
test_print = list(zip(keys, values))
zipped_list = test_print[:]
zipped_list_2 = list(test_print)

print(zipped_list_2)
"""