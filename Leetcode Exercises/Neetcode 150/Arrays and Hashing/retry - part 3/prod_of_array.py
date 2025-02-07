"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?
"""
from typing import List

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        
        #part 1 using brute force

        # n = len(nums)
        # result = [0] * n

        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
            
        #     result[i] = prod
        # return result

        # part 2 using prefix & suffix

        n = len(nums)
        result = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1

        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            result[i] = pref[i] * suff[i]
        return result
    
print(Solution().product_except_self(nums = [1,2,4,6]))