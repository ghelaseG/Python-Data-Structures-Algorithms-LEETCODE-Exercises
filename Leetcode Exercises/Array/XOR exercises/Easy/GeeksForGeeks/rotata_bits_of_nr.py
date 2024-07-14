"""
Bit Rotation: A rotation (or circular shift) is an operation similar to shift except that the bits that fall off at one end are put back to the other end. 
In left rotation, the bits that fall off at left end are put back at right end. 
In right rotation, the bits that fall off at right end are put back at left end
"""

int_bits = 32

def leftRotate(n, d):
    return (n << d) | (n >> (int_bits - d))

def rightRotate(n, d):
    return (n >> d) | (n << (int_bits - d)) & 0xFFFFFFFFF

n = 16
d = 2

print("Left rotation by ", d, "is:")
print(leftRotate(n, d))

print("Right rotation by", d, "is:")
print(rightRotate(n, d))