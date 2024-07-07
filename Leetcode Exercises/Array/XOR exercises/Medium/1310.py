"""
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.
"""

from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        #compute prefix xoRs
        n = len(arr)
        prefix = [0 for _ in range(n+1)]

        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]

        #compute queries XoR
        result = []
        for L, R in queries:
            result.append(prefix[R+1] ^ prefix[L])

        return result
