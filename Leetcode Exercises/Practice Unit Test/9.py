"""
Write a Python unit test program to check if a database query returns the expected results.
"""

import unittest
import sqlite3

class TestDataBaseQuery(unittest.TestCase):
    #define a method that is executed before each test
    def setUp(self):
        #create a database connection in memory and insert test data
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        #create an 'employees' table and insert test records
        self.cursor.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL)")
        self.cursor.execute("INSERT INTO employees (name, salary) VALUES ('Georgian Geo', 1800.0)")
        self.cursor.execute("INSERT INTO employees (name, salary) VALUES ('Geo Georgian', 2100.0)")
        self.conn.commit()

    #define a method that is executed after each test
    def tearDown(self):
        #close the database cursor and the database connection
        self.cursor.close()
        self.conn.close()

    #define a test method to test a database query
    def test_database_query(self):
        #execute an SQL query to select employee names and salaries, ordered by name
        self.cursor.execute('SELECT name, salary FROM employees ORDER BY name')
        results = self.cursor.fetchall()

        #define the expected results as a list of tuples
        expected_results = [('Geo Georgian', 2100.0), ('Georgian Geo', 1800.0)]

        #assert that the results match the expected results
        self.assertEqual(results, expected_results)

#check if the script is run as the main program
if __name__ == '__main__':
    unittest.main()