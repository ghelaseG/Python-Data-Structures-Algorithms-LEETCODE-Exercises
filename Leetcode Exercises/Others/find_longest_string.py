"""
Write a Python function called find_longest_string that takes a list of strings as an input and returns the longest string in the list. The function should iterate through each string in the list, check its length, and keep track of the longest string seen so far. Once it has looped through all the strings, the function should return the longest string found.
"""

def find_longest_string(myList):
    longest_string = ""
    for i in myList:
        if len(i) > len(longest_string):
            longest_string = i
    return longest_string
        
string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)