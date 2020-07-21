'''
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and 
we need to calculate span of stock’s price for all n days. 
The span Si of the stock’s price on a given day i is defined as the maximum number 
of consecutive days just before the given day, for which the price of the stock on the current day 
is less than or equal to its price on the given day. For example, if an array of 7 days prices is given as 
{100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}
'''

def span(price,stack):
    n = len(price)
    s = []
    s.append(0)
    stack[0] = 1
    
    for i in range(1, n): 
        
        while( len(s) > 0 and price[s[-1]] <= price[i]): 
            s.pop() 
        stack[i] = i + 1 if len(s) <= 0 else (i - s[-1]) 
  
        # Push this element to stack 
        s.append(i)
        
def printArray(arr, n): 
    for i in range(0, n): 
        print (arr[i], end =" ") 
    
    
    
price = [10, 4, 5, 90, 120, 80] 
stack = [0 for i in range(len(price)+1)] 
    
# Fill the span values in array S[] 
span(price, stack) 
    
# Print the calculated span values 
printArray(stack, len(price))