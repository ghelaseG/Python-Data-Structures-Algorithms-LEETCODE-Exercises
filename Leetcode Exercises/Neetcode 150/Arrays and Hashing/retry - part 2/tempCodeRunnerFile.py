"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""
from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        #part 1
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        #part 2
        prev_map = {}

        for i, n in enumerate(nums):
            differ = target - n
            if differ in prev_map:
                return [prev_map[differ], i]
            prev_map[n] = i

nums = [3,4,5,6]
target = 7
solution = Solution()
print(solution.two_sum(nums, target)) 