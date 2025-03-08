"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?
"""

class Solution:
    def products_of_array_except_self(self, nums: list[int]) -> list[int]:

        # part 1 using brute force
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

        # # part 2 using division
        # product = 1
        # zero_cnt = 0

        # for num in nums:
        #     if num:
        #         product *= num
        #     else:
        #         zero_cnt += 1
        # if zero_cnt > 1:
        #     return [0] * len(nums)
        
        # result = [0] * len(nums)
        # for i, c in enumerate(nums):
        #     if zero_cnt:
        #         result[i] = 0 if c else product
        #     else:
        #         result[i] = product // c
        # return result
        
        # # part 3 using prefix & sufix
        # n = len(nums)
        # result = [0] * n
        # pref = [0] * n
        # suff = [0] * n

        # pref[0] = suff[n - 1] = 1
        # for i in range(1, n):
        #     pref[i] = nums[i - 1] * pref[i - 1]
        # for i in range(n - 2, -1, -1):
        #     suff[i] = nums[i + 1] * suff[i + 1]
        # for i in range(n):
        #     result[i] = pref[i] * suff[i]
        # return result

        # part 4 using prefix and suffix (optimal)
        result = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
    
print(Solution().products_of_array_except_self(nums = [1,2,4,6]))


