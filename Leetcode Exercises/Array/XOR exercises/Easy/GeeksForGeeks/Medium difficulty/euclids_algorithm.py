"""
Euclid’s Algorithm when % and / operations are costly

Euclid’s algorithm is used to find GCD of two numbers. 
"""

# There are mainly two versions of algorithm. 

# Version 1 (using substraction)
def gcd(a, b):
    if (a == b):
        return a
    
    return gcd(a - b, b) if (a > b) else gcd(a, b - a)

# Version 2 (using modulo operator)
def gcd(a, b):
    if (a == 0):
        return b
    
    return (b % a, a)
