"""
Write a Python unit test that checks if a function handles floating-point calculations accurately.
"""

import unittest


class CheckFloatingPointCalc(unittest.TestCase):

    def test_addition(self):
        #perform the addition operation
        result = 0.3 + 0.5
        #assert that the resutlt is approximately equal to 0.8 
        self.assertAlmostEqual(result, 0.8, places=6)

    def test_division(self):
        result = 0.9 / 0.3
        self.assertAlmostEqual(result, 2.333333, places=6)

    def test_multiplication(self):
        result = 0.3 * 0.5
        self.assertAlmostEqual(result, 0.15, places=6)

if __name__ == '__main__':
    unittest.main()