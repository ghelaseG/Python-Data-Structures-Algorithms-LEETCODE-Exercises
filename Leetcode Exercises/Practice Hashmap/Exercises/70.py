"""
Write a Python program to map the values of a given list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value.
Sample Output:
{1: 1, 2: 4, 3: 9, 4: 16}
"""

#define a function that takes 2 parameters, 'integer' and 'function'

def test(itr, fn):
    #use the zip function to pair each element from itr with the result of applying fn to that element
    #convert the zipped pairs into a dictionary where the elements from itr are keys, and the result of fn are values
    return dict(zip(itr, map(fn, itr)))

#we use lambda to square its input
result = test([1,2,3,4], lambda x: x * x)

print(result)