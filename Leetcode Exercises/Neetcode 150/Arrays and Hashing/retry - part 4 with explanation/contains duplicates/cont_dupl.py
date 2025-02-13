"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""
from typing import List

class Solution:
    def contains_duplicates(self, nums: List[int]) -> bool:
        # part 1 using brute force
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

print(Solution().contains_duplicates(nums=[1,2,3,4,1]))