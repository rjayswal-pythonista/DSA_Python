# Queqe using Two Stack

class Stack:
    def __init__(self):
        self.list = []
        
    def __len__(self):
        if not self.list:
            return 0
        return len(self.list)
    
    def __str__(self):
        if not self.list:
            return None
        return self.list
    
    def push(self, data):
        return self.list.append(data)
    
    def pop(self):
        if not self.list:
            return None
        return self.list.pop()
    
    
class QueqeViaStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()
    
    def __str__(self):
        if not self.inStack.list:
            return None
        else:
            string = ''
            for i in (self.inStack.list):
                string += str(i) + ' '
            return string
    
    def enqueqe(self, data):
        return self.inStack.push(data)
            
    def dequeqe(self):
        if not self.inStack.list:
            return "Queqe is Empty"
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        data = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        
        return data    

myqueqe = QueqeViaStack()
for i in range(1,11):
    myqueqe.enqueqe(i)
print(myqueqe)

print(myqueqe.dequeqe())
print(myqueqe)


"""
[output]

1 2 3 4 5 6 7 8 9 10
1
2 3 4 5 6 7 8 9 10

"""