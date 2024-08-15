"""
Euclid’s Algorithm when % and / operations are costly

Euclid’s algorithm is used to find GCD of two numbers. 
"""

# There are mainly two versions of algorithm. 

# # Version 1 (using substraction)
# def gcd(a, b):
#     if (a == b):
#         return a
    
#     return gcd(a - b, b) if (a > b) else gcd(a, b - a)

# # Version 2 (using modulo operator)
# def gcd(a, b):
#     if (a == 0):
#         return b
    
#     return (b % a, a)

"""
Consider a situation where modulo operator is not allowed, can we optimize version 1 to work faster?

We can find x/2 using x >> 1. We can check whether x is odd or even using x & 1.

gcd(a, b) = 2 * gcd(a/2, b/2) if both a and b are even.
gcd(a, b) = gcd(a/2, b) if a is even and b is odd.
gcd(a, b) = gcd(a, b/2) if a is odd and b is even.
"""

def gcd(a, b):
    if (b == 0 or a == b):
        return a
    if (a == 0):
        return b
    
    # if both a and b are even divide both a and b by 2
    # and multiply the result with 2

    if ((a & 1) == 0 and (b & 1) == 0):
        return gcd(a >> 1, b >> 1) * 2
    
    # if a is even and b is odd, divide a by 2
    if ((a & 1) == 0 and (b & 1) != 0):
        return gcd(a >> 1, b)
    
    # if a is odd and b is even, divide b by 2
    if ((a & 1) != 0 and (b & 1) == 0):
        return gcd(a, b >> 1)
    
    #if both are odd then we apply normal substraction algorithms
    #note that odd-odd case always converts odd-even case after one recursion
    return gcd(a - b, b) if a > b else gcd(a, b - a)


print(gcd(45, 10))

print(gcd(3768, 1701))