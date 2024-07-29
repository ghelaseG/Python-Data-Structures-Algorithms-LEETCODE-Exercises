"""
Given two integers, write a function to multiply them without using multiplication operator.
There are many other ways to multiply two numbers (For example, see this). One interesting method is the Russian peasant algorithm. The idea is to double the first number and halve the second number repeatedly till the second number doesn’t become 1. In the process, whenever the second number become odd, we add the first number to result (result is initialized as 0) 
"""

def russianPeasant(x, y):

    result = 0 

    #while second number does not become 1

    while (y > 0):

        #if second number becomes odd, 
        ## add the first number to the result

        if (y & 1):
            result = result + x

        #double the first number
        ## halve the second number 
        x = x << 1
        y = y >> 1
    
    return result

print(russianPeasant(18, 1))

print(russianPeasant(20, 12))