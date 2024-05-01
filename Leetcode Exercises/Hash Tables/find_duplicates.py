"""
Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).
"""

def find_duplicates(nums):
    num_counts = {} #we first initialize a dict to count numbers

    for i in nums:
        num_counts[i] = num_counts.get(i, 0) + 1 
        # if for example, the number is not in the dict, the key it will be the same, and the value it will increment by 1
        # after this, if we get the same i, let's say our list is [1,1,1,2], then the second i= it will be again 1,
        # but now this key, got the value 1, from previous itteration, so then will increment by 1, it will become, num_counts = {1, 2}
    duplicates = [] #here we store the duplicates

    for num, count in num_counts.items():
        # now we continue our example, here we iterate through let's say {1, 2} - the items of the dictionary,
        # therefore, count will be = 2, now if 2 > 1, the value of the key, then we add it to our empty array called 'duplicates'
        if count > 1:
            duplicates.append(num)

    return duplicates


print( find_duplicates( [1, 2, 3, 4, 5]) )
print( find_duplicates([1, 1, 2, 2, 3]) )
print( find_duplicates([1,1,1,1,1]) )
print( find_duplicates([1,2,3,3,3,4,4,5]) )
print( find_duplicates([1,1,2,2,2,3,3,3,3]) )
print( find_duplicates([1,1,1,2,2,2,3,3,3,3]) )
print( find_duplicates([]) )