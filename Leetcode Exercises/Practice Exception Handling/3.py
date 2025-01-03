"""
Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
"""

def open_file(filename):
    try:
        #attempt to open the specified file in read mode
        file = open(filename, 'r')
        #read the contents of the file
        contents = file.read()
        #print the contents
        print("Contents of the file:", contents)
        #close the file to release system resources
        file.close()
    except FileNotFoundError:
        print("Error: File not found")

#usage, prompt the user to input a file name and store it in the filename variable
file_name = input("Input a file name: ")
open_file(file_name)