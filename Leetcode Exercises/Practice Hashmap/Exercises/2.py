"""
Write a Python script to add a key to a dictionary.
Example:
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""

dict = {0: 10, 1: 20}

print(dict)

dict.get({2:30})
#or we can use dict.update({2:30})

print(dict)
