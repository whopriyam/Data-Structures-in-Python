#Stack as a list
s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')

print(s[-1])
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

#Stack as a deque
from collections import deque
stack = deque()
print(dir(stack))

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)
print(stack.pop())
print(stack.pop())

class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self,val):
            self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
s1 = Stack()
s1.push(7)
s1.push(10)
s1.pop()
print(s1.size())
print(s1.peek())
print(s1.is_empty())