"""
You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:

|x - y| <= min(x, y)
You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.

Return the maximum XOR value out of all possible strong pairs in the array nums.

Note that you can pick the same integer twice to form a pair.
"""

from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maxXOR = 0

        for i in nums:
            for j in nums:
                if abs(i - j) <= min(i, j):
                    maxXOR = max(maxXOR, i ^ j)
        
        return maxXOR

example = Solution()
print(example.maximumStrongPairXor(nums=[5,6,25,30]))