"""
Write a function item_in_common(list1, list2) that takes two lists as input and returns True if there is at least one common item between the two lists, False otherwise.

Use a dictionary to solve the problem that creates an O(n) time complexity.
"""

def item_in_common(list1, list2):

    my_dict = {} #we first create a dict to store our list1 items

    for i in list1:
        my_dict[i] = True #here we add each value as a key in the dict

    for j in list2: #iterate through the second list
        if j in my_dict:
            #if j matches any of the value from list1, then return true
            return True
        
    return False #if none of this happened, return False