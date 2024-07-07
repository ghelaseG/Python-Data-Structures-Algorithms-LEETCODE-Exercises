"""
Write a Python script to check whether a given key already exists in a dictionary.
"""

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def check_key(i):
    if i in d:
        print('Key is here')
    else:
        print('Not today :)')

check_key(20)