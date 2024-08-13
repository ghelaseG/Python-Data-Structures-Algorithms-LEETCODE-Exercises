"""
Given a number N, generate bit patterns from 0 to 2^N-1 such that successive patterns differ by one bit.

Examples:

Input: N = 2
Output: 00 01 11 10

Input: N = 3
Output: 000 001 011 010 110 111 101 100
"""

def GreyCode(n):
    # power of 2
    for i in range(1 << n):
        #generating the decimal values of gray code 
        #then using bitset to convert them to binary form
        value = (i ^ (i >> 1))

        #converting to binary string
        s = bin(value)[2::]
        print(s.zfill(n), end = " ")

n = 4

GreyCode(4)