"""
Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).
"""

def find_duplicates(nums):
    num_counts = {} #we first initialize a dict to count numbers

    for i in nums:
        num_counts[i] = num_counts.get(num, 0) + 1 #here we check how many times each number appears in the list
    
    duplicates = [] #here we store the duplicates

    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)

    return duplicates


    