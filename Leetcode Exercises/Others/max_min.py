"""
Write a Python function that takes a list of integers as input and returns a tuple containing the maximum and minimum values in the list.

The function should have the following signature:

def find_max_min(myList):


Where myList is the list of integers to search for the maximum and minimum values.

The function should traverse the list and keep track of the current maximum and minimum values. It should then return these values as a tuple, with the maximum value as the first element and the minimum value as the second element.

For example, if the input list is [5, 3, 8, 1, 6, 9], the function should return (9, 1) since 9 is the maximum value and 1 is the minimum value.
"""
#the way this program works, is very simple
##we first initialize the variable max and min with the first element of the list, in our case is 5
###after this we iterate through the list with the for loop and compare every element with those variable
####for example, after we check 5, we then go to 3, and 3 < minimum(5), so then minimum becomes 3, while maximum is still 5, and so on
def find_max_min(myList):
    maximum = minimum = myList[0]
    for num in myList:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num
    return maximum, minimum

print(find_max_min([5,3,8,1,6,9])) 