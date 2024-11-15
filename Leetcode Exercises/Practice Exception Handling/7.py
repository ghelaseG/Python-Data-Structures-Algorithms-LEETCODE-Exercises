"""
Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
"""

def keyboard_intr(prompt):
    try:
        prompt = int(input(prompt))
        print("The number you chose is:", prompt)
    except KeyboardInterrupt:
        print("This has been cancelled")

keyboard_intr("Write a number:") #CTRl + C