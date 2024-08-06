"""
Parity: Parity of a number refers to whether it contains an odd or even number of 1-bits. The number has “odd parity” if it contains an odd number of 1-bits and is “even parity” if it contains an even number of 1-bits. 
"""

# return 1 if number is odd
# return 0 if number is even

def getParity(n):

    parity = 0
    while n:
        parity = ~parity
        n = n & (n - 1)
    return parity

n = 10
print("Parity of nr", n,"is", "odd" if getParity(n) else "even")