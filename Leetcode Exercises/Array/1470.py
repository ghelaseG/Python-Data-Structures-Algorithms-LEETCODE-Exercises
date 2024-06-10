"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #let's create a new list
        new_list = []
        #we can create a new list of indexes that has only half of the "nums"
        half_list = len(nums) // 2
        #let's iterate through the half of the given list
        for i in range(len(nums) // 2):
            #now we can append one after another (this will be x1)
            new_list.append(nums[i])
            #and now y1 etc
            new_list.append(nums[i + half_list])
        return new_list
    
exp = Solution()
print(exp.shuffle(nums=[2,5,1,3,4,7], n=3))