"""
Write a Python unit test program that checks if two lists are equal.
"""

import unittest

def lists_are_equal(lst1, lst2):
    return lst1 == lst2

class TestListEquality(unittest.TestCase):
    def test_equal_lists(self):
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [1, 2, 3, 4, 5]

        print("\nEqual list test :\n", nums1, "\n", nums2)
        self.assertTrue(lists_are_equal(nums1, nums2), "The list are equal")

    def test_unequal_lists(self):
        nums1 = [1, 2, 3, 4, 9]
        nums2 = [2, 4, 5, 6, 1]

        print("\n Unequal lists:\n", nums1, "\n", nums2)
        self.assertFalse(lists_are_equal(nums1, nums2), "The lists are not equal")

if __name__ == '__main__':
    unittest.main()