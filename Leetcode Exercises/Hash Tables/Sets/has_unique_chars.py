"""
Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the string are unique, and False otherwise.

For example, has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should return False.
"""

def has_unique_chars(my_string):
    if len(set(my_string)) != len(my_string):
        return False
    else:
        return True

print(has_unique_chars('abcdefg'))
print(has_unique_chars('hello'))
print(has_unique_chars(''))
print(has_unique_chars('0123456789'))
print(has_unique_chars('abacadaeaf'))