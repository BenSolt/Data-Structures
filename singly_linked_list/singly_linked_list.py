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
    fourth = Node('list 4')
  
    llist.head.next = second 
    second.next = third
    third.next = fourth
  
    llist.printList() 
    
    while True:
        cmd = input("Enter a number:").split(' ')

        if cmd[0] == "a":
            print("list 1")
        elif cmd[0] == 'b':     
            print("list 2")
        
   
    