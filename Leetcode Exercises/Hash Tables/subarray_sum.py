"""
Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

Your function should take two arguments:

nums: a list of integers representing the input array

target: an integer representing the target sum


Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. If there is no such subarray, your function should return an empty list.
"""

def subarray_sum(nums, target):
    res = 0
    curSum = 0
    prefSum = {0:1}

    for i in nums:
        curSum += i
        diff = curSum - target

        res += prefSum.get(diff, 0)
        prefSum[curSum] = 1 + prefSum.get(curSum, 0)
    
    return res

