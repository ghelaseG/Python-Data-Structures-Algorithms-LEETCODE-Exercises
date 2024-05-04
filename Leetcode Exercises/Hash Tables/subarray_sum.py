"""
Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

Your function should take two arguments:

nums: a list of integers representing the input array

target: an integer representing the target sum


Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. If there is no such subarray, your function should return an empty list.
"""

def subarray_sum(nums, target):
    #let's create a dict to store the sums as keys with their index
    sum_index = {0: -1}
    # 0: will be the default sum when we search for subarrays
    #-1: shows that there's no subarray yet
    ## this setup helps handle special cases, for example when the first element itself is equal to the target

    current_sum = 0 #here we keep track of the running sum, as we iterate through the array

    for i, num in enumerate(nums):
        current_sum += num #here we update the current sum by adding the current 'num'

        #we then check if a subarray exists with the sum that we need
        ##we basically check if sum - target is a key in the sum_index
        if current_sum - target in sum_index:
            #if it is, then we have found the subarray, and
            ##we return the indices as a list
            ###we add 1 to move past the element before the subarray starts
            ####i is the end index
            return [sum_index[current_sum - target]+1, i]
        
        #if we haven't yet found it, we add the current sum and its index to our dict
        sum_index[current_sum] = i

        #and if there's no subarray, we return an empty list
        return []
    

nums = [1, 2, 3, 4, 5]
target = 9
print( subarray_sum(nums, target))

nums = [-1, 2, 3, -4, 5]
target = 0
print(subarray_sum(nums, target))

nums = [2,3,4,5,6]
target = 3
print( subarray_sum(nums, target))

nums = []
target = 0
print(subarray_sum(nums, target))

