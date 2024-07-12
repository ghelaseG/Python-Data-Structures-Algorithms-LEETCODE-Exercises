"""
Count set bits in an integer

"""

def countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n = n >> 1
    return count

i = 9
print(countSetBits(i))