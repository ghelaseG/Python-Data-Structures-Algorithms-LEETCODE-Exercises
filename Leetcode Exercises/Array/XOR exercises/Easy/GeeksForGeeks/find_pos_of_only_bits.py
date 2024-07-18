"""
Find position of the only set bit

Given a number N having only one ‘1’ and all other ’0’s in its binary representation, find position of the only set bit. If there are 0 or more than 1 set bit the answer should be -1. Position of set bit ‘1’ should be counted starting with 1 from the LSB side in the binary representation of the number.

"""


#we can use this function to check if the binary position is at the power of 2
#meaning that, if it is at the power of 2, then it's only 1 bit

def isPowerofTwo(n):

    return (n and (not (n & (n - 1))))

def findPosition(n):
    if not isPowerofTwo(n):
        return -1
    
    count = 0

    #we gonna use a while loop to iterate one by one till the end

    while (n):

        n = n >> 1

        count += 1

    return count

if __name__ == "__main__":
    n = 0
    position = findPosition(n)

    if position == -1:
        print("n =", n, "Invalid Number")
    else:
        print("n = ", n, "Position", position)

    n = 12
    position = findPosition(n)

    if position == -1:
        print("n =", n, "Invalid Number")
    else:
        print("n = ", n, "Position", position)

    n = 128
    position = findPosition(n)

    if position == -1:
        print("n =", n, "Invalid Number")
    else:
        print("n = ", n, "Position", position)