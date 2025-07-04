class node:                                  #creating node  for
    def __init__(self,dataval):
        self.dataval = dataval             # 12
        self.nextval = None                   #address
class queue:                             # fosr linked list 
    def __init__(self):
        self.front = None

    def enque(self,newdata):
        newnode = node(newdata)
        if self.front is None:
            self.front = newnode
        last = self.front
        while(last.nextval):
            last = last.nextval
        last.nextval = newnode
      
    def deque(self):
        if self.front is None:
            print("empty")
        else:
            x=self.front.dataval
            self.front = self.front.nextval
            return x
        
    def display(self):
        if self.front is None:
            print("empty")
        else:
            temp = self.front
            while(temp):
                print(temp.dataval,end=" ")
                temp = temp.nextval
            print()

s1=queue()
s1.front=node(10)
s1.enque(20)
s1.enque(30)
s1.enque(40)
s1.display()
s1.deque()
s1.display()
s1.deque()
s1.display()
s1.deque()
s1.display()
s1.deque()
s1.display()

