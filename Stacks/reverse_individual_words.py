def reverserWords(string): 
    string = string + " "
    stack = [] 
  
    for i in range(len(string)): 
        if string[i] != " ": 
            stack.append(string[i]) 
            
        else: 
            while len(stack) > 0: 
                print(stack[-1], end= "") 
                stack.pop() 
            print(end = " ") 
   

if __name__ == "__main__": 
    string = "Hello this is Skynet"
    reverserWords(string) 