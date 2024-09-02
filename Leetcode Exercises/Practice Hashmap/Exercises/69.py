"""
 Write a Python program to group the elements of a given list based on the given function.
Sample Output:
Original list & function:
[7, 23, 3.2, 3.3, 8.4] Function name: floor:
Group the elements of the said list based on the given function:
{7: [7], 23: [23], 3: [3.2, 3.3], 8: [8.4]}
Original list & function:
['Red', 'Green', 'Black', 'White', 'Pink'] Function name: len:
Group the elements of the said list based on the given function:
{3: ['Red'], 5: ['Green', 'Black', 'White'], 4: ['Pink']}
"""

from collections import defaultdict
from math import floor

def group_elements(lst, fn):
    #create a defaultdict object 'd' with a default value of an empty list
    d = defaultdict(list)

    #iterate through the elements in the input list
    for el in lst:
        #apply the function to the current element to determine the group key
        key = fn(el)

        #append the current element to the list associated with the calculated key
        d[key].append(el)
    
    return dict(d)

nums = [7, 23, 3.2, 3.3, 8.4]

print("Group the elements of the said list based on the given function:")
print(group_elements(nums, floor))

colours = ['Red', 'Green', 'Black', 'White', 'Pink']

print("Group the elements of the said list based on the given function:")
print(group_elements(colours, len))
