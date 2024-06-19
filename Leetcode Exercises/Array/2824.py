"""
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
 
"""

from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i, j in enumerate(nums):
            if i + j < target:
                count += 1
        return count