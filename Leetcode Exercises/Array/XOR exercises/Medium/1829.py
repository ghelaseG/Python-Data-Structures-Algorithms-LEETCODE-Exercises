"""
You are given a sorted array nums of n non-negative integers and an integer maximumBit. You want to perform the following query n times:

Find a non-negative integer k < 2maximumBit such that nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
Remove the last element from the current array nums.
Return an array answer, where answer[i] is the answer to the ith query.
"""

from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix = []

        mask = (1 << maximumBit) - 1
        for x in nums:
            prefix.append(mask ^ x)
            mask ^= x
        prefix.reverse()
        return prefix
    
example = Solution()
print(example.getMaximumXor(nums = [0,1,1,3], maximumBit = 2))