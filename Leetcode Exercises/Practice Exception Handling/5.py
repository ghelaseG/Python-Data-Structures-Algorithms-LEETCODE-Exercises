"""
Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
"""

def open_file(filename):
    try:
        #we try to open the file in write mode
        with open(filename, 'w') as file:
            #the following statement will not be executed because we are opening the file in write mode
            contents = file.read()
            print("File contents:", contents)
    except PermissionError:
        print("Error: permission denied to open the file.")

file_name = input("Write the name of the file:")
open_file(file_name)