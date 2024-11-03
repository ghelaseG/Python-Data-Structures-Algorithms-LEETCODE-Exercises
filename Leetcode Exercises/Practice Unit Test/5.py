"""
Write a Python unit test program to check if a file exists in a specified directory.
"""

import os
import unittest

def file_exists(directory, filename):
    #create the fill file path by joining the directory and filename
    file_path = os.path.join(directory, filename)
    #check if the file exists there
    return os.path.exists(file_path)

class TestFileExists(unittest.TestCase):
    def test_existing_file(self):
        #define the directory and filename for an existing file
        directory = '/path/txt'
        filename = 'test1.txt'
        #assert that the file exists in the folder
        self.assertTrue(file_exists(directory, filename), "The file does not exist in the specified directory")

    def test_non_existent_file(self):
        directory = '/path/txt'
        filename = 'test2.txt'

        self.assertFalse(file_exists(directory, filename), "The file exists in the specified directory")

if __name__ == '__main__':
    unittest.main()
    