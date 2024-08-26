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

# function to get the nr of set bits in binary representation of passed binary nr

def countSetBits(x):

    count = 0

    while (x):
        x = x & (x - 1)
        count += 1

    return count

# return True if n is Bleak

def isBleak(n):

    #check for all numbers 'x' smaller than n
    #if x + countSetBits(x) become n, then n can't be Bleak

    for x in range(1, n):

        if (x + countSetBits(x) == n):
            return False
    
    return True

if (isBleak(3)):
    print('Yes')
else:
    print('No')

if (isBleak(4)):
    print('Yes')
else:
    print("No")
