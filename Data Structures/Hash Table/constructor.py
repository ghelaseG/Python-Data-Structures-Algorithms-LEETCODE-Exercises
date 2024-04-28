# here we build a list from 0 to 6 
class HashTable:
    def __init__(self, size = 7): #our default size it is going to be 7
        self.data_map = [None] * size # list containing None with 7 items in it

    def __hash(self, key): #the hash method is what we pass the key to determine the address of a key value pair(where we store it)
        my_hash = 0
        for letter in key:
            #ord(letter) is ordinal letter, getting the ASCII number for each letter as we are looping through it
            #we can use 23 or any other prime number
            #%(modulo operator) gives us the remainder when we divide
            #for example, our length is 7, so if we divide any number by 7, the remainder will be between 0 to 6 
            my_hash = (my_hash * ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

my_hash_table = HashTable()

my_hash_table.print_table()