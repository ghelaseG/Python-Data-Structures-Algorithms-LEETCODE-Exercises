"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
"""
from typing import List

class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range( j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temps = [nums[i], nums[j], nums[k]]
                        result.add(tuple(temps))
        return [list(i) for i in result]
    
nums = [0,1,1]
solution = Solution()
print(solution.three_sum(nums))