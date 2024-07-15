"""
Compute modulus division by a power-of-2-number

Compute n modulo d without division(/) and modulo(%) operators, where d is a power of 2 number. 
"""

def getModulo(n, d):

    return n & (d - 1)

n = 12

#make sure d is a power of 2, so:
d = 8

print(n, "modulo", d, "is", getModulo(n, d))