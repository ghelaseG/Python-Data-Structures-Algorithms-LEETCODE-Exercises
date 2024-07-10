"""
Write a program to print a Binary representation of a given number. 
"""

def bin_representation(n):
    binary_str = "0"

    for i in range(31, -1, -1):
        if n & (1 << i):
            binary_str += "1"
        else:
            binary_str += "0"
    return binary_str

def main():
    print(bin_representation(7))
    print(bin_representation(4))

if __name__ == "__main__":
    main()
