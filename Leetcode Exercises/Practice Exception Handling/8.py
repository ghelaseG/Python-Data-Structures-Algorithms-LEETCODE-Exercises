"""
Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
"""

def division(dividend, divisor):
    try:
        result = dividend / divisor
        print("Total: ", result)
    except ArithmeticError:
        print("Error: arithmetic error occurred")

dividend = float(input("Write the dividend:"))
divisor = float(input("Write the divisor:"))

division(dividend, divisor)