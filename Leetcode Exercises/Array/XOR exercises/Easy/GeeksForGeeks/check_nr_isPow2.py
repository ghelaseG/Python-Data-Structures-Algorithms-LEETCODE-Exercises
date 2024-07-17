"""
Given a positive integer n, write a function to find if it is a power of 2 or not
"""

def is_power_of_two(x):
    #first x is for the case when x is 0
    return (x and (not (x & (x - 1))))

if __name__ == "__main__":

    if(is_power_of_two(31)):
        print('Yes')
    else:
        print('No')

    if(is_power_of_two(64)):
        print('Yes')
    else:
        print('No')

