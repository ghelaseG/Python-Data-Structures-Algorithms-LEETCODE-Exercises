"""
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.
"""

from typing import List

class Solution:
    def countTriplets(slef, arr: List[int]) -> int:
        N = len(arr)
        count = 0

        for i in range(N - 1):
            a = 0
            for j in range(i+1, N):
                a = a ^ arr[j - 1]
                b = 0
                for k in range(j, N):
                    b = b ^ arr[k]

                    if a == b:
                        count += 1
        
        return count

#Time complexity: O(N^3)