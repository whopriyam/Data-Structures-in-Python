#Node class representing an individual element in the linkedlist
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def prints(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
        
        itr = self.head    
        while(itr.next):
            itr = itr.next
            
        itr.next = Node(data,None)

    
    def insert_list(self,data_list):
        self.head = None
        for item in data_list:
            self.insert_at_end(item)
    
    def get_length(self):
        itr = self.head
        count = 0
        while(itr):
            count = count + 1
            itr = itr.next
        print (count)
    
    def remove_at_index(self,index):
        if index < 0:
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0
        while(itr):
            count = count + 1
            if count == index-1:
                itr.next=itr.next.next
                break
            itr = itr.next
                
    def insert_at_index(self,index,data):
        if index<0:
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)  
            return
        
        itr = self.head
        count = 0
        while(itr):
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break            
            
            itr = itr.next
            count = count+1
    
    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        count = 0
        while(itr):        
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                break
            itr = itr.next
            count = count + 1
            
    def remove_by_value(self, data):
        itr = self.head
        count = 0
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        while(itr):
            count = count+1
            if itr.next != None:
                if str(itr.next.data) == str(data):
                    itr.next = itr.next.next
                    break
            itr = itr.next
                
                
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_list(["banana","mango","grapes","orange"])
    ll.prints()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.prints()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.prints()
    ll.remove_by_value("figs")
    ll.prints()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.prints()