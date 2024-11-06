"""
Write a Python unit test program to check if a database connection is successful.
"""

import unittest
import sqlite3

class TestDataBase(unittest.TestCase):
    def test_database_connection(self):
        #create a database connection in memory
        conn = sqlite3.connect(':memory:')
        #create a cursor to interact with the database
        cursor = conn.cursor()
        #execute a simple query to select the value 1
        cursor.execute("SELECT 1")
        #fetch the result of the query
        result = cursor.fetchone()
        #close the cursor and the database connection
        cursor.close()
        conn.close()
        #assert that the fetched result is as expected, which should be a tuple containing 1
        self.assertEqual(result, (1,))
    
#check if the script is run as the main program
if __name__ == '__main__':
    unittest.main()