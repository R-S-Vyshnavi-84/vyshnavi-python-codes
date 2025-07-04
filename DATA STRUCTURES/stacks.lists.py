#dynamic implementations:
#creating the ds using linked list  everu time inserting the data before the 10(right to left(10))
class stack:                                  #creating node  for
    def __init__(self,dataval):
        self.dataval = dataval             # 12
        self.nextval = None 
                                       #address
class dynamic:                             # for linked list 
    def __init__(self):
        self.top = None

    def push(self,newdata):
        newnode = stack(newdata)                          #node is monday
        if self.top is None:
            self.top = newnode                    #newnode 
        else:
            newnode.nextval=self.top                      #1000 ois storde in newnoode()
            self.top = newnode
    
    def pop(self):
        if self.top is None:
            print("empty")
        else:
            x=self.top.dataval
            self.top = self.top.nextval
            return x
        
    def display(self):
        if self.top is None:
            print("empty")
        else:
            temp = self.top
            while(temp):
                print(temp.dataval,end=" ")
                temp = temp.nextval
            print()
s1=stack()
while True():
    print("push <value>")
    print("pop")
    print("display")
    print("quit")
    do = input("what would u like to do? ").split()

    operation = do[0].strip().lower()
    if operation == 'push':
        s1.push(int(do[1]))
    elif operation == 'pop'():
        popped = s1.pop()
        if popped is None:
            print("stack is empty")
        else:
            print("popped value: ",int(popped))
    elif operation == "display":
        s1.display()
    elif operation == "quit":
        break


s1=dynamic()
s1.top=stack(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.display()
s1.pop()
s1.display()
s1.pop()
s1.display()
s1.pop()
s1.display()
s1.pop()
s1.display()
 