"""
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.
"""
#based on this video we can use convolution or ffts: https://www.youtube.com/watch?v=MYYvjvvqj-4&ab_channel=ProgrammingLivewithLarry
##here is a helpful video about convolution: https://www.youtube.com/watch?v=KuXjwB4LzSA&ab_channel=3Blue1Brown

from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
