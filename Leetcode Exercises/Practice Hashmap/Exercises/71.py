"""
Write a Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list.
Sample Output:
Russell
2
"""

from functools import reduce
from operator import getitem

def test(d, selectors):
    #use reduce to succesively apply getitem with each element in selectors on the dictionary 'd'
    #this effectively drills down into the dictionary using the sequence of selectors
    return reduce(getitem, selectors, d)

#create a nested dictionary 'users'
users = {
    'Carla': {
        'name': {
            'first': 'Carla ',
            'last': 'Russell'
        },
        'postIds': [1, 2, 3, 4, 5]
    }
}

# call the test function with two sets of selectors to access specific values within the 'users' dictionary
# the first call accesses Carla's last name, and the second call accesses one of Carla's post IDs
print(test(users, ['Carla', 'name', 'last']))
print(test(users, ['Carla', 'postIds', 1]))