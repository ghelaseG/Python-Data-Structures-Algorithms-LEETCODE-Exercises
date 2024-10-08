"""
Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
Note: There will be one solution for each input and do not use the same element twice.
Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 3, 4

Difficulty: Medium. Company: Google, Facebook
"""
class Solution5:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i

print("index1 = %d, index2 = %d" % Solution5().twoSum((10,20,10,40,50,60,70),50))