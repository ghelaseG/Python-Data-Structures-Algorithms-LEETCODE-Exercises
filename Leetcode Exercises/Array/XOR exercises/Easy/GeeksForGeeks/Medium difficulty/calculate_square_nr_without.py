"""
Given an integer n, calculate the square of a number without using *, / and pow(). 
"""
# method 1

# def square(num):

#     if num < 0:
#         num = -num

#     power, result = 0, 0
#     temp = num

#     while temp:
#         if temp & 1:
#             # result + (num*(2^power))
#             result += (num << power)
#         power += 1

#         #temp / 2
#         temp = temp >> 1

#     return result

# #Example:
# for n in range(10, 16):
#     print(f"n = {n}, n^2 = {square(n)}")


# method 2

def square(n):

    if (n == 0):
        return 0
    
    #handle negative number
    if (n < 0):
        n = -n

    #get floor(n/2) using right shift
    x = n >> 1

    # if n is odd
    if (n & 1):
        return ((square(x) << 2) + (x << 2) + 1)
    
    #if n is even
    else:
        return (square(x) << 2)
    

#driver code
for n in range(1, 6):
    print("n = ", n, " n ^2 =", square(n))
