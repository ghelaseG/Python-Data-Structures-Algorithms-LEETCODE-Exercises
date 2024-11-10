"""
Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
"""

def get_input(prompt):
    try:
        user_input = int(input(prompt))
        return user_input
    except ValueError:
        print("Error: Invalid input, input a valid integer.")

n = get_input('Write a number: ')
print("Input value:", n)