"""
Given a number x and two positions (from the right side) in the binary representation of x, write a function that swaps n bits at the given two positions and returns the result. It is also given that the two sets of bits do not overlap.
"""


def swapBits(x, p1, p2, n):

    # move all bits of first set to the rightmost side
    ## here the expression ( 1 << n) - 1 gives a number that contains the last n bits set and other bits as 0
    ### we do '&' so that bits other than the last n bits become 0

    set1 = ( x >> p1) & (( 1 << n ) - 1)
    
    # move all bits of second set to the rightmost side

    set2 = ( x >> p2 ) & (( 1 << n ) - 1)

    # xor the two sets

    xor = ( set1 ^ set2 )

    # put the xor bits back to their original positions

    xor = ( xor << p1 ) | ( xor << p2 )

    # finally, we XOR the 'xor' with the original number so that the two sets are swapped

    result = x ^ xor

    return result


res = swapBits(47, 1, 5, 3)

print(' Result = ', res)