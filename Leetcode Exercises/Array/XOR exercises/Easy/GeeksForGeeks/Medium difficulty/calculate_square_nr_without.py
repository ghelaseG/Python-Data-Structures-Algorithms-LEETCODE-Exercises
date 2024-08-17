"""
Given an integer n, calculate the square of a number without using *, / and pow(). 
"""

def square(num):

    if num < 0:
        num = -num

    power, result = 0, 0
    temp = num

    while temp:
        if temp & 1:
            # result + (num*(2^power))
            result += (num << power)
        power += 1

        #temp / 2
        temp = temp >> 1

    return result

#Example:
for n in range(10, 16):
    print(f"n = {n}, n^2 = {square(n)}")