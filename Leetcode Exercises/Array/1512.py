"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #first we make sure we add 1 for each pair in this variable count
        count = 0
        #then we iterate to get the index, so we can use nums[index] etc
        for i in range(len(nums)):
            for j in range(len(nums)):
                #then we make sure that we use i < j, otherwise will count the first pairs, so it will show double or even more
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count
    
exp = Solution()
print(exp.numIdenticalPairs(nums=[1,2,3,1,1,3]))
#in this exp, there are 4 pairs: (0,3), (0,4), (3,4), (2,5) 0-indexed.