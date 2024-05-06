"""
Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.

Output: An integer representing the length of the longest consecutive sequence in nums.
"""

def longest_consecutive_sequence(my_list):
    numSet = set(my_list)
    longest = 0

    for n in numSet:
        if (n - 1) not in numSet:
            current = 0
            while (n + current) in numSet:
                current += 1
            longest = max(current, longest)

    return longest

print(longest_consecutive_sequence([100,4,200,1,3,2]))