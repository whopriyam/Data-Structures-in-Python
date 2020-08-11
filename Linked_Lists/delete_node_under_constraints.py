'''
Given a Singly Linked List, write a function to delete a given node. Your function must follow following constraints:
1) It must accept a pointer to the start node as the first parameter and node to be deleted as the second parameter i.e., a pointer to head node is not global.
2) It should not return a pointer to the head node.
3) It should not accept pointer to pointer to the head node.
'''

class Node:
    def __init__(self,data):
        self.data = None
        self.next = None
        
class linkedList:
    def __init(self,data):
        self.head = None
        
    def deleteNode(self,data):
        temp = self.head()
        prev = self.head()
        
        if temp.data == data:
            if temp.next is None:
                print("Can't delete since list will become empty")
            else:
                temp.data = temp.next.data
                temp.next = temp.next.next
            return
        
        while temp.next is not None and temp.data != data:
            prev = temp
            temp = temp.next
            if temp.next is None and temp.data != data:
                print ("Node does not exist")
            elif temp.next is None and temp.data == data:
                prev.next = None
            else:
                prev.next = temp.next
    
    def push(self, newData): 
        newNode = Node(newData) 
        newNode.next = self.head 
        self.head = newNode 
        
    def PrintList(self): 
  
        temp = self.head 
        while(temp): 
            print(temp.data, end = " ") 
            temp = temp.next