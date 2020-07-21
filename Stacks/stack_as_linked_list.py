class StackNode:
    
    #Initializing the node
    def __init__(self,data):
        self.data = data
        self.next = None
 
class Stack:
    
    #Initializing root of list
    def __init__(self):
        self.root = None
    
    #Checking if Linked List is empty or not
    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False
        
    def push(self,data):
        new_node = StackNode(data)
        new_node.next = self.root
        self.root = new_node
        
    def pop(self): 
        if (self.isEmpty()): 
            return float("-inf") 
        temp = self.root  
        self.root = self.root.next 
        pop_item = temp.data 
        return pop_item
    
    def peek(self): 
        if self.isEmpty(): 
            return float("-inf") 
        return self.root.data 
  
# Driver program to test above class  
stack = Stack() 
stack.push(10)         
stack.push(20) 
stack.push(30) 

print ("% d Popped from stack" %(stack.pop()))
print ("Top Element is % d " %(stack.peek()))