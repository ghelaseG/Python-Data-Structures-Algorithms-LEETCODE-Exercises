"""
Write a Python unit test program to check if a given number is prime or not.
"""

import unittest

#define a function prime to check if a number is prime
def check_num_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

#define a test case class 'prime numbers' that inherits from 'unittest.TestCase'
class PrimeNumbersTest(unittest.TestCase):
    def testPrimeNumbers(self):
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        ##example with wrong numbers commented below
        #prime_numbers = [2, 3, 4, 8, 11, 13, 17, 19, 23, 30, 31]
        print("Prime numbers:", prime_numbers)
        #iterate through prime numbers and assert that they are recognised as prime
        for number in prime_numbers:
            self.assertTrue(check_num_prime(number), f"{number} is not recognised as a prime number")

    #define a test function 'non-prime numbers' 
    def test_non_prime_numbers(self):
        non_prime_numbers = [4, 6, 8, 10, 12, 14, 16, 18, 20]
        print('Non-prime numbers:', non_prime_numbers)
        for number in non_prime_numbers:
            self.assertFalse(check_num_prime(number), f"{number} is incorrectly recognised as a prime number")

if __name__ == '__main__':
    unittest.main()