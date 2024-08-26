"""
A number ‘n’ is called Bleak if it cannot be represented as sum of a positive number x and set bit count in x, i.e., x + countSetBits(x) is not equal to n for any non-negative number x.

Example:

Input : n = 3
Output : false
3 is not Bleak as it can be represented
as 2 + countSetBits(2).

Input : n = 4
Output : true
4 is t Bleak as it cannot be represented 
as sum of a number x and countSetBits(x)
for any number x.
"""


