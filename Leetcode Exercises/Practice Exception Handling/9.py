"""
Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
"""

def open_file(filename):
    #propmpt the user to input the file encoding (ASCII, UTF-16, UTF-8)
    encoding = input("Write the encoding (ASCII, UTF-16, UTF-8) for the file:")
    try:
        #try to open the file in read mode with the selected encoding
        with open(filename, 'r', encoding=encoding) as file:
            #read and store in the variable name 'contents'
            contents = file.read()
            print("Contents:", contents)
    except UnicodeDecodeError:
        print("Error: Encoding issue while trying to read the file")

file_name = input("Select the file name:")
open_file(file_name)