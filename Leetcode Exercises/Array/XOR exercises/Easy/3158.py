"""
You are given an array nums, where each number in the array appears either once or twice.

Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.
"""

from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            for j in range(len(i+1, nums)):
                if nums[i] == nums[j]:
                    result = nums[i] ^ nums[j]
        
        return result