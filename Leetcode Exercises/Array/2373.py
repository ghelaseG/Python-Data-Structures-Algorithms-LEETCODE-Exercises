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
        n = len(grid)
        #let's create a 2 dimensional matrix
        ##we start by creating a zeros matrix 
        result = [[0] * (n - 2) for _ in range(n-2)]
        #next loop will populate the matrix
        for i in range(n-2):
            for j in range(n-2):
                #here we check for the max value in our 3 by 3 matrix
                for row in range(i, i + 3):
                    for column in range(j, j + 3):
                        result[i][j] = max(result[i][j], grid[row][column])
        return result
    
example = Solution()
print(example.largestLocal(grid=[[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))