"""
You are given a list of n integers and a non-negative integer k.

Your task is to write a function called rotate that takes the list of integers and an integer k as input and rotates the list to the right by k steps.

The function should modify the input list in-place, and you should not return anything.

Constraints:

Each element of the input list is an integer.

The integer k is non-negative.



Function signature: def rotate(nums, k):

Example:

Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Function call: rotate(nums, k)
Output: nums = [5, 6, 7, 1, 2, 3, 4]


Explanation: The list has been rotated to the right by 3 steps:



[7, 1, 2, 3, 4, 5, 6]

[6, 7, 1, 2, 3, 4, 5]

[5, 6, 7, 1, 2, 3, 4]
"""

def rotate(nums, k):

    k = k % len(nums) #if k is the same as the length, then we dont have to rotate
    left, right = 0, len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left + 1, right - 1

    left, right = 0, k -1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left + 1, right - 1

    left, right = k, len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left + 1, right - 1

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)

#we using space complexity O(1), and time complexity O(n)