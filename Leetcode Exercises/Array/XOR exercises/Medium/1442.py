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
            currXOR = arr[i]
            for k in range(i + 1, N):
                currXOR = currXOR ^ arr[k]
                if currXOR == 0:
                    count += (k - i)
        
        return count

#Time complexity: O(N^2)