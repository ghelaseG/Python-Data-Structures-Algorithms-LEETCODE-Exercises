"""
Given a list of integers nums and an integer val, write a function remove_element that removes all occurrences of val in the list in-place and returns the new length of the modified list.

The function should not allocate extra space for another list; instead, it should modify the input list in-place with O(1) extra memory.



Input:

A list of integers nums .

An integer val representing the value to be removed from the list.



Output:

An integer representing the new length of the modified list after removing all occurrences of val.



Constraints:

Do not use any built-in list methods, except for pop() to remove elements.

It is okay to have extra space at the end of the modified list after removing elements.
"""

def remove_element(nums, val):
    i = 0
    #because i is 0, once it reaches the same value as the length, the loop ends
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)

# Test case 1: removing a single instance of a value (1) in the middle of the list
nums1 = [-2, 1, -3, 4, -1,2,1,-5, 4]
val1 = 1
print("\nRemove a single instance of value", val1, "in the middle of the list.")
print("Before:", nums1)
new_length1 = remove_element(nums1, val1)
print("After:", nums1, "\nNew length:", new_length1)
print("--------------------------")

# Test case 2: removing a value that is located at the end of the list
nums2 = [1,2,3,4,5,6]
val2 = 6
print("\nRemove a single instance of value", val2, "in the middle of the list.")
print("Before:", nums2)
new_length2 = remove_element(nums2, val2)
print("After:", nums2, "\nNew length:", new_length2)
print("--------------------------")

# Test case 3: removing a value that is located at the start of the list
nums3 = [-1,-2,-3,-4,-5]
val3 = -1
print("\nRemove a single instance of value", val3, "in the middle of the list.")
print("Before:", nums3)
new_length3 = remove_element(nums3, val3)
print("After:", nums3, "\nNew length:", new_length3)
print("--------------------------")

# Test case 4: attempting to remove a value from an empty list
nums4 = []
val4 = 1
print("\nRemove a single instance of value", val4, "in the middle of the list.")
print("Before:", nums4)
new_length4 = remove_element(nums4, val4)
print("After:", nums4, "\nNew length:", new_length4)
print("--------------------------")

# Test case 5: removing all instances of a repeated value
nums5 = [1,1,1,1,1]
val5 = 1
print("\nRemove a single instance of value", val5, "in the middle of the list.")
print("Before:", nums5)
new_length5 = remove_element(nums5, val5)
print("After:", nums5, "\nNew length:", new_length5)
print("--------------------------")