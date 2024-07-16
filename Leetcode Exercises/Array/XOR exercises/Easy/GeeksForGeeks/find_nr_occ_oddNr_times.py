"""
Find the Number Occurring Odd Number of Times


Given an array of positive integers. All numbers occur an even number of times except one number which occurs an odd number of times. Find the number in O(n) time & constant space.
"""

def getOddNr(arr, arr_size):
    for i in range(0, arr_size):
        count = 0
        for j in range(0, arr_size):
            if arr[i] == arr[j]:
                count += 1
        
        if (count % 2 != 0):
            return arr[i]
    
    return -1

arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2 ]
n = len(arr)
print(getOddNr(arr, n))
