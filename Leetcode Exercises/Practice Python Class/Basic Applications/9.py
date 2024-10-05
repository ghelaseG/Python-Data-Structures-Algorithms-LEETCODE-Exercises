"""
Write a Python class that has two methods: get_String and print_String , get_String accept a string from the user and print_String prints the string in upper case.
"""

class Solution9:
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = Solution9()
str1.get_String()
str1.print_String()