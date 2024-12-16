"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
"""
from typing import List

class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        result = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            result = max(result, streak)
        print(streak)
        return result
    
solution = Solution()
nums = [2,20,4,10,3,4,5]
print(solution.longest_consecutive(nums))