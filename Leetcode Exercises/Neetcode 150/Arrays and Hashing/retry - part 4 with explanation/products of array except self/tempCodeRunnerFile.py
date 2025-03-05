"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?
"""

class Solution:
    def products_of_array_except_self(self, nums: list[int]) -> list[int]:

        # part 1 using brute force
        n = len(nums)
        result = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]
            
            result[i] = prod
        
        return result
print(Solution().products_of_array_except_self(nums = [1,2,4,6]))


