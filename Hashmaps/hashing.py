stock_prices = {}
with open("stock_data.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

print(stock_prices["march 8"])

class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def add(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val
        
    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        
t = HashTable()
print(t.get_hash('march 7'))
print(t.add('march 6', 130))
print(t.get('march 7'))