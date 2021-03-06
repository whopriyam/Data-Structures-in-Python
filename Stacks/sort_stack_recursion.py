def sortedInsert(s , element): 
      
    #Check item is greater than top (more than all existing) 
    if len(s) == 0 or element > s[-1]: 
        
        s.append(element) 
        return
    
    else: 
          
        #Remove the top item and recur 
        temp = s.pop() 
        sortedInsert(s, element) 
  
        #Put back the top item removed earlier 
        s.append(temp) 
  

def sortStack(s): 
      
    #If stack is not empty 
    if len(s) != 0: 
          
        #Remove the top item 
        temp = s.pop()  
        #Sort remaining stack 
        sortStack(s) 
        #Push the top item back in sorted stack 
        sortedInsert(s , temp) 
  
#Printing stack 
def printStack(s): 
    for i in s[::-1]: 
            print(i , end=" ") 
    print() 
      
if __name__=='__main__': 
    s = [ ] 
    s.append(30) 
    s.append(-5) 
    s.append(18) 
    s.append(14) 
    s.append(-3) 
  
    print("Stack elements before sorting: ") 
    printStack(s) 
  
    sortStack(s) 
  
    print("\nStack elements after sorting: ") 
    printStack(s) 