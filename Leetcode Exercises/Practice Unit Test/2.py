"""
Write a Python unit test program to check if a list is sorted in ascending order.
"""
import unittest

#we build a function to check if a list is sorted ascending order
def is_sorted_ascending(lst):
    #check if all elements at index i are less than or equal to elements at index i + 1
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

class TestSortedAsc(unittest.TestCase):
    def test_sorted_list(self):
        lst = [1, 2, 3, 4, 5]

        print("Sorted list:", lst)

        self.assertTrue(is_sorted_ascending(lst), "The list is not sorted in ascending order")
        