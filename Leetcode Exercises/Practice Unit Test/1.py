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
        
