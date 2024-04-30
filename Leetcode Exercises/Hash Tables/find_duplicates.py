"""
Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).
"""

def find_duplicates(nums):
    array = []

    if array == None:
        return False
    
    for i in nums:
        for j in nums:
            if i == j:
                array += i
    