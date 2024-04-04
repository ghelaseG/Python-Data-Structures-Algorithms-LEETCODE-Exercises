#set of nested dictionaries
#this shows how a linked list works - for example 11 -> 3 -> 23 -> 7 -> None
head =    {
            "value": 11,
            "next": {
                     "value": 3,
                     "next": {
                              "value": 23,
                              "next": {
                                       "value": 7,
                                       "next": None
                                      }
                             }
                    }
          }

print(head['next']['next']['value'])

#next block code will only run with a Linked List
print(my_linked_list.head.next.next.value)