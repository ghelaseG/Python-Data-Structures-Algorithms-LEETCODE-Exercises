"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        count = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] != nums[i] and nums[j] < nums[i]:
                    count += 1
            result.append(count)
        return result

example = Solution()
print(example.smallerNumbersThanCurrent(nums=[8,1,2,2,3]))