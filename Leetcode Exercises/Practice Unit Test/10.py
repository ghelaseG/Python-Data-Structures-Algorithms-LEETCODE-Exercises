"""
Write a Python unit test program to check if a function correctly parses and validates input data.
"""

import unittest

def parse_and_validate_input(data):
    #check if the input data is a string and contains only numeric characters
    if isinstance(data, str) and data.isnumeric():
        #convert the string to an integer and check if it;s greater than 0
        return int(data) > 0
    return False

class TestInputParsing(unittest.TestCase):
    def test_valid_input(self):
        #define valid input data as a string containing a positive integer
        data = "100"
        #call the function with the valid input data
        result = parse_and_validate_input(data)
        #assert that the result is True => indicating valid input
        self.assertTrue(result)

        #define a test method to test invalid input data
        def test_invalid_input(self):
            #define invalid input data as a string containing non numeric characters
            data = "Hello"
            #call the function with the invalid input data
            result = parse_and_validate_input(data)
            #assert that the result is False (invalid input)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()