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

        prefix = 0
        prev_xor_cnt = defaultdict(int)
        prev_xor_cnt[0] = 1
        prev_xor_index_sum = defaultdict(int)

        for i in range(N):
            prefix ^= arr[i]

            if prev_xor_cnt[prefix]:
                count += i * prev_xor_cnt[prefix] - prev_xor_index_sum[prefix]

            prev_xor_cnt[prefix] += 1
            prev_xor_index_sum[prefix] += i + 1
        
        return count

#Time complexity: O(N)