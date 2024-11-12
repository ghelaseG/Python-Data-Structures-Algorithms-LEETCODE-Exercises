"""
Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
"""

def get_numeric_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid input. Please input a valid number.")

n1 = get_numeric_float("Input the first nr:")
n2 = get_numeric_float("Input the first nr:")

result = n1 * n2
print("Product of the said 2 nr:", result)