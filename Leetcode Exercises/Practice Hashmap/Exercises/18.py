"""
Write a Python program to check if a dictionary is empty or not.
"""

#create an empty dict

my_dict = {'gg': 31}

#check if the dict is empty by evaluating its boolean value
#the bool function check and return False for an empty dict

if not bool(my_dict):
    print('Dictionary is empty')
else:
    print('we got something:', my_dict.keys())