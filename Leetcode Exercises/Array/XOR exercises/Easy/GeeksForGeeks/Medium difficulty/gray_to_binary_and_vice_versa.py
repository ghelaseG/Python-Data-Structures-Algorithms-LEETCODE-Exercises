"""
Binary Number is the default way to store numbers, but in many applications, binary numbers are difficult to use and a variety of binary numbers is needed. This is where Gray codes are very useful. 

Gray code has a property that two successive numbers differ in only one bit because of this property gray code does the cycling through various states with minimal effort and is used in K-maps, error correction, communication, etc.
"""

"""
How to generate n bit Gray Codes? 

Following is 2-bit sequence (n = 2)
  00 01 11 10
Following is 3-bit sequence (n = 3)
  000 001 011 010 110 111 101 100
And Following is 4-bit sequence (n = 4)
  0000 0001 0011 0010 0110 0111 0101 0100 1100 1101 1111 
  1110 1010 1011 1001 1000
n-bit Gray Codes can be generated from a list of (n-1)-bit Gray codes using the following steps. 

Let the list of (n-1)-bit Gray codes be L1. Create another list L2 which is the reverse of L1.
Modify the list L1 by prefixing a ‘0’ in all codes of L1.
Modify the list L2 by prefixing a ‘1’ in all codes of L2.
Concatenate L1 and L2. The concatenated list is the required list of n-bit Gray codes.

"""

"""
How to Convert Binary To Gray and Vice Versa? 

Binary : 0011
Gray   : 0010

Binary : 01001
Gray   : 01101
In computer science many a time we need to convert binary code to gray code and vice versa. This conversion can be done by applying the following rules :

Binary to Gray conversion : 

The Most Significant Bit (MSB) of the gray code is always equal to the MSB of the given binary code.
Other bits of the output gray code can be obtained by XORing binary code bit at that index and previous index.

Binary code to gray code conversion

Gray to binary conversion :

The Most Significant Bit (MSB) of the binary code is always equal to the MSB of the given gray code.
Other bits of the output binary code can be obtained by checking the gray code bit at that index. If the current gray code bit is 0, then copy the previous binary code bit, else copy the invert of the previous binary code bit.
"""

def greyConverter(n):

    return n ^ (n >> 1)

n = 3
print(greyConverter(n))

n = 9
print(greyConverter(n))