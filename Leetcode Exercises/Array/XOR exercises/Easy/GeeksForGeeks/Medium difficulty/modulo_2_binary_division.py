"""
CRC or Cyclic Redundancy Check is a method of detecting accidental changes/errors in the communication channel. 
CRC uses Generator Polynomial which is available on both sender and receiver side. An example generator polynomial is of the form like x3 + x + 1. This generator polynomial represents key 1011. Another example is x2 + 1 that represents key 101. 

n : Number of bits in data to be sent 
    from sender side.  
k : Number of bits in the key obtained 
    from generator polynomial.

 Receiver Side (Check if there are errors introduced in transmission)
Perform modulo-2 division again and if the remainder is 0, then there are no errors. 

In this article we will focus only on finding the remainder i.e. check word and the code word.

Modulo 2 Division:
The process of modulo-2 binary division is the same as the familiar division process we use for decimal numbers. Just that instead of subtraction, we use XOR here.

In each step, a copy of the divisor (or data) is XORed with the k bits of the dividend (or key).
The result of the XOR operation (remainder) is (n-1) bits, which is used for the next step after 1 extra bit is pulled down to make it n bits long.
When there are no bits left to pull down, we have a result. The (n-1)-bit remainder which is appended at the sender side.
"""

#for more info use this link: https://www.geeksforgeeks.org/modulo-2-binary-division/


#return xor of a and b
def xor(a, b):

    #initialise result
    result = []

    #traverse all bits, if bits are same, then XOR is zero, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)

#perform modulo 2 division
def mod2div(dividend, divisor):

    #number of bits to be XORed at a time
    pick = len(divisor)

    #slicing the dividend to appropriate length for particular step
    tmp = dividend[0: pick]

    while pick < len(dividend):

        if tmp[0] == '1':
            #replace the dividend by the result of XOR and pull 1 bit down
            tmp = xor(divisor, tmp) + dividend[pick]

        else:
            #if the leftmost bit of the dividend (or the part used in each step) is 0, 
            #the step cannot use the regular divisor; we need to use an all -0s divisor
            tmp = xor('0'*pick, tmp) + dividend[pick]

        #increment pick to move further
        pick += 1

    #for the last n bits, we have to carry it out normally as increased value of pick will 
    #cause Index Out of Bounds
        
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    checkword = tmp
    return checkword

#function used at the sender side to encode data by appending remainder of modular
#division at the end of data

def encodeData(data, key):

    l_key = len(key)

    #appends n-1 zeros at the end of data
    append_data = data + "0"*(l_key-1)
    remainder = mod2div(append_data, key)

    #append remainder in the original data
    codeword = data + remainder
    print("Remainder:", remainder)
    print("Encoded Data (Data + Remainder): ", codeword)

#Driver code
data = "100100"
key = "1101"

encodeData(data, key)