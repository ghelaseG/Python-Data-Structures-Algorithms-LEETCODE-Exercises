"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""
from typing import List

class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        # part 1 using brute force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # part 2 using sorting
        # nums.sort()
        # for i in range(1 , len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False

        # part 3 using hash set
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # part 4 using hash set length
        return len(set(nums)) < len(nums)
nums = [1, 2, 3, 3]
print(Solution().contains_duplicate(nums))