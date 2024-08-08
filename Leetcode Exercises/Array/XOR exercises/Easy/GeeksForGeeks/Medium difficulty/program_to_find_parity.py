"""
Parity: Parity of a number refers to whether it contains an odd or even number of 1-bits. The number has “odd parity” if it contains an odd number of 1-bits and is “even parity” if it contains an even number of 1-bits. 
"""
# # Method 1
# # return 1 if number is odd
# # return 0 if number is even

# def getParity(n):

#     parity = 0
#     while n:
#         parity = ~parity
#         n = n & (n - 1)
#     return parity

# n = 10
# print("Parity of nr", n,"is", "odd" if getParity(n) else "even")

# # Method 2

# def getParity(n):
#     return(bin(n).count("1"))%2

# #example
# n = 7
# print("odd" if getParity(n) else "even")


# Method 3

#we first build the 16 length array of the number of bits to form a nibble
nibble_to_bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

# function to recursively get the nibble of a number and map them in the array

def CountSetBits(num):
    nibble = 0
    if (0 == num):
        return nibble_to_bits[0]
    
    #find last nibble
    ## recursively count the set of the bits by taking the last nibble (4 bits) from the array
    
    nibble = num & 0xf

    #we then use pre stored values to find count in last nibble plus recursively add remaining nibble
    ## in short, we get each successive nibble by discarding the last 4 bits using >> operator

    return nibble_to_bits[nibble] + CountSetBits(num >> 4)

#function to get the parity of a number

def getParity(num):
    return CountSetBits(num) % 2

#Example
n = 10

print("Parity of a number", n, "=", ["even", "odd"][getParity(n)])
