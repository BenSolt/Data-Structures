class Node: 
  
    def __init__(self, data): 
        self.data = data 
        self.next = None  
  
  
# Linked List class contains a Node
class LinkedList: 
  
    def __init__(self): 
        self.head = None

    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data)
            temp = temp.next
  
  
if __name__=='__main__': 
  
    
    llist = LinkedList() 
  
    llist.head = Node('list 1') 
    second = Node('list 2') 
    third = Node('list 3') 
  
    llist.head.next = second 
    second.next = third
  
    llist.printList() 
    
    