"""
Write a Python function called find_longest_string that takes a list of strings as an input and returns the longest string in the list. The function should iterate through each string in the list, check its length, and keep track of the longest string seen so far. Once it has looped through all the strings, the function should return the longest string found.
"""

def find_longest_string(myList):
    for i in myList:
        if len(myList[0]) > len(myList[i]):
            return myList[0]
        else:
            return myList[i]
        
string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)