"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] =nums[i-1] + nums[i]
        return nums
    
example = Solution()
print(example.runningSum(nums=[1,2,3,4]))

#time complexity: O(N), space: O(1)