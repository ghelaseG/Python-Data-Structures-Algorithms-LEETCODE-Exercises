"""
Write a Python unit test program to check if a string is a palindrome.
"""

import unittest

def is_palindrome(string):
    return string == string[::-1]

