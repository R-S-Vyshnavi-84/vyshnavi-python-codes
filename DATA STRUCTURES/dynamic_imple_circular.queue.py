class circularqueue():
    #constructor
    def __init__(self,size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enque(self,data):
        if((self.rear + 1) % self.size == self.front):
            print("queue is full \n")
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear] = data

    def deque(self):                             # condition for empty queue
        if (self.front == -1): 
            print("Queue is empty\n")
        elif (self.front == self.rear):          # condition for only element
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
    def display(self):                                      # condition is empty
        if(self.front == -1):
            print("queue is empty")
        elif (self.rear >= self.front):
            print("elemnet in the cicular queue are:",end = ' ')
            for i in range (self.front, self.rear+1):
                print(self.queue[i],end=" ")
            print()

        else:
            print("element in circular queue are:",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()        

#driver code:
ob = circularqueue(5)
ob.enque(14)
ob.enque(22)
ob.enque(13)
ob.enque(-6)
ob.display()
print("deleted value = ", ob.deque())
print("deleted value = ", ob.deque())
ob.display()
ob.enque(9)
ob.enque(20)
ob.enque(5)
ob.display()