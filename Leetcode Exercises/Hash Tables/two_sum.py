"""
Problem:
Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.

The main challenge here is to implement this function in one pass through the array. This means you should not iterate over the array more than once. Therefore, your solution should have a time complexity of O(n), where n is the number of elements in nums.



Input:

A list of integers nums .

A target integer target.



Output:

A list of two integers representing the indices of the two numbers in the input array nums that add up to the target. If no two numbers in the input array add up to the target, return an empty list [].
"""

def two_sum(nums, target):
    prev = {} #here we store our value(key) and index(value)

    for ind, val in enumerate(nums):
        diff = target - val
        if diff in prev:
            return [prev[diff], ind] #here we return the index of the diff, and the current index
        prev[val] = ind #otherwise,if the diff not in the dict, we add them
    return [] #if none of this are happening, then we return an empty list

print(two_sum([5,1,7,2,9,3], 10))
print(two_sum([4,2,11,7,6,3], 9))
print(two_sum([10,15,5,2,8,1,7], 12))
print(two_sum([1,3,5,7,9], 10))
print(two_sum([1,2,3,4,5], 10))
print(two_sum([1,2,3,4,5], 7))
print(two_sum([1,2,3,4,5], 3))
print(two_sum([], 0))