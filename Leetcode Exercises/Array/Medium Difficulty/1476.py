"""
Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:

1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)

Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).
2. getValue(int row, int col)

Returns the current value of the coordinate (row,col) from the rectangle.
"""
#for better understanding of this problem, go back to 2373.Largest Local Values in a Matrix

from typing import List

class SubrectangleQueries:
    
    def __init__(self, rectangle: List[List[int]]):
        #let's copy and initialise the List of lists(matrix)
        self.matrix = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        #now we can iterate throughout the rows and cols that are given using nested for loops
        ##make sure we use +1 as we want to include the number row or col
        ###for each row or col, we add the new value given
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.matrix[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        #now to return our new matrix
        return self.matrix[row][col]