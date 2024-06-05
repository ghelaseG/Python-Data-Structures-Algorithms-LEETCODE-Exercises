"""
Given an array of integers nums, write a function max_subarray(nums) that finds the contiguous subarray (containing at least one number) with the largest sum and returns its sum.

Remember to also account for an array with 0 items.



Function Signature:

def max_subarray(nums):


Input:

A list of integers nums.



Output:

An integer representing the sum of the contiguous subarray with the largest sum.



Example:

max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
Output: 6
Explanation: The contiguous subarray [4, -1, 2, 1] has the largest sum, which is 6.
"""
#for better understanding, use this link: https://pythontutor.com/render.html#code=def%20max_subarray%28nums%29%3A%0A%20%20%20%20%23we%20return%200%20if%20list%20is%20empty%0A%20%20%20%20if%20not%20nums%3A%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20%0A%20%20%20%20%23here%20we%20initialise%20the%202%20variables,%20to%20the%20first%20element%20of%20the%20list%0A%20%20%20%20%23%23maxSub%20stores%20the%20max%20subarray%20sum%20found%20so%20far%0A%20%20%20%20%23%23%23curSum%20keeps%20track%20of%20the%20max%20subarray%20sum%20ending%20at%20the%20cur%20position%0A%20%20%20%20maxSub%20%3D%20curSum%20%3D%20nums%5B0%5D%0A%20%20%20%20%0A%20%20%20%20%23let's%20iterate%20through%20the%20remaining%20elements%0A%20%20%20%20for%20n%20in%20nums%5B1%3A%5D%3A%0A%20%20%20%20%20%20%20%20%23update%20current%20sum%0A%20%20%20%20%20%20%20%20curSum%20%3D%20max%28n,%20curSum%20%2B%20n%29%0A%20%20%20%20%20%20%20%20%23update%20maxSub%20if%20cursum%20is%20larger%0A%20%20%20%20%20%20%20%20maxSub%20%3D%20max%28maxSub,%20curSum%29%0A%20%20%20%20%23return%20max%20subarray%20sum%20%20%20%20%0A%20%20%20%20return%20maxSub%0A%0A%23%20Example%201%3A%20Simple%20case%20with%20positive%20and%20negative%20numbers%0Ainput_case_1%20%3D%20%5B-2,%201,%20-3,%204,%20-1,%202,%201,%20-5,%204%5D%0Aresult_1%20%3D%20max_subarray%28input_case_1%29%0Aprint%28%22Example%201%3A%20Input%3A%22,%20input_case_1,%20%22%5CnResult%3A%22,%20result_1%29&cumulative=false&curInstr=32&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
##time complexity O(n) using Kadane's algorithm
def max_subarray(nums):
    #we return 0 if list is empty
    if not nums:
        return 0
    
    #here we initialise the 2 variables, to the first element of the list
    ##maxSub stores the max subarray sum found so far
    ###curSum keeps track of the max subarray sum ending at the cur position
    maxSub = curSum = nums[0]
    
    #the way this loop works, is simple:
    # - first we go through the 2nd element, and see which one is the max between index 0 and index 1
    ## - then we keep track of the highest "sum" or better say max, and return it
    #let's iterate through the remaining elements
    for n in nums[1:]:
        #update current sum
        curSum = max(n, curSum + n)
        #update maxSub if cursum is larger
        maxSub = max(maxSub, curSum)
    #return max subarray sum    
    return maxSub

# Example 1: Simple case with positive and negative numbers
input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray(input_case_1)
print("Example 1: Input:", input_case_1, "\nResult:", result_1)  

# Example 2: Case with a negative number in the middle
input_case_2 = [1, 2, 3, -4, 5, 6]
result_2 = max_subarray(input_case_2)
print("Example 2: Input:", input_case_2, "\nResult:", result_2) 

# Example 3: Case with all negative numbers
input_case_3 = [-1, -2, -3, -4, -5]
result_3 = max_subarray(input_case_3)
print("Example 3: Input:", input_case_3, "\nResult:", result_3) 
