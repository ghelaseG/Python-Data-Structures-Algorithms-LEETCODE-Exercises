"""
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
"""

from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        #here we initialise the variable with a size that accommodates indexing
        freq = [0] * (len(nums) + 1)
        result = []

        for i in nums:
            #if the integer frequency is >= than the len of the result,
            ##we add an empty subarray to result
            if freq[i] >= len(result):
                result.append([])
            #then here we add the integer to the sublist and increment by 1 the frequency of the integer
            result[freq[i]].append(i)
            freq[i] += 1

        return result
    
example = Solution()
print(example.findMatrix(nums=[1,3,4,1,2,3,1]))

