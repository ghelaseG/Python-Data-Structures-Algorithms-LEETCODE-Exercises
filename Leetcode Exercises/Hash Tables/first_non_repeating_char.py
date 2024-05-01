"""
You have been given a string of lowercase letters.

Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return None.

For example, if the input string is "leetcode", the function should return "l" because "l" is the first character that appears only once in the string. Similarly, if the input string is "hello", the function should return "h" because "h" is the first non-repeating character in the string.
"""

def first_non_repeating_char(letters):
    check_letters = {}

    for letter in letters:
        check_letters[letter] = check_letters.get(letter, 0) + 1

    for letter, count in check_letters.items():
        if count = 1:
            print(letter)
        else:
            return None
