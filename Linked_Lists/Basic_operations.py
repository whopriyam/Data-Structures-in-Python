#Return number of nodes
def getCount(head_node):
    count = 0
    while(head_node):
        count += 1
        head_node = head_node.next
    return count

#Remove duplicate elements
def removeDuplicates(head):
    temp=head
    while(temp.next!=None):
        x=temp.next
        while(x!=None and temp.data==x.data):
            x=x.next
        temp.next=x
        if(temp.next!=None):
            temp=temp.next
            
