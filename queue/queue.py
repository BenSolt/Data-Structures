"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
#3.  In array you can access any index. Linked list you can only access one adjacent to itself.

import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = ?

        self.storage =  DoublyLinkedList()
    
    def __len__(self):
        #get the length
        return self.size

    def enqueue(self, value):
        # add 1 to length of array
        self.size += 1
        #return length of array, add to end.
        return self.storage.add_to_tail()

    def dequeue(self):
        # if length of array is greater than 0
        if self.size > 0:
            #subtract 1
            self.size -= 1
        #return length of array, remove from front.
            return self.storage.remove_from_head()
        else:
        # do nothing
            return None
