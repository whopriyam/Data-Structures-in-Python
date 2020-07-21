#Check for balanced paranthesis
def paranthesis(input_string):
    stack  = []
    for char in input_string:
        if char in ["{","(","["]:
            stack.append(char)
            
        else:
            if not stack:
                False
            current = stack.pop()
            if char == ')':
                if current != '(':
                    return False
            if char == '}':
                if current != '{':
                    return False
            if char == ']':
                if current != '[':
                    return False
    if stack:
        return False
    else:
        return True

if __name__ == "__main__" :  
    input_string = "({()}[])"  
    if paranthesis(input_string) : 
        print("Balanced");  
    else : 
        print("Not Balanced")

