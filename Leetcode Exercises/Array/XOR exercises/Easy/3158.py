"""
You are given an array nums, where each number in the array appears either once or twice.

Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.
"""
#we got a time and space complexity of O(N)

from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        hashmap = {}

        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        result = 0

        for num, count in hashmap.items():
            if count >= 2:
                result = result ^ num
        
        return result
    
example = Solution()
print(example.duplicateNumbersXOR(nums=[1,2,2,1]))