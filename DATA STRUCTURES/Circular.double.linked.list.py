import sys
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dclinkedlist:
    def __init__(self):
        self.head=None
        self.last=None

    def display(self):
        if(self.head==None):
            print("Empty list")
        else:
            first=self.head
            while(first!=None):
                if first.data is not None:
                    print(first.data,end=' ')
                    first=first.next
                    if(first==self.head):
                        break

    def atstart(self,newdata):
        temp=node(newdata)
        if(self.head==None):
            self.head=temp
            self.last=temp
        else:
            temp.next=self.head
            temp.prev=self.last
            self.head=temp

    def atend(self,newdata):
        temp=node(newdata)
        if(self.head==None):
            self.head=temp
            self.last=temp
        else:
            self.last.next=temp
            temp.prev=self.last
            temp.next=self.head
            self.last=temp

    def inmid(self,key,newdata):
        temp=node(newdata)
        var=self.head
        while(var.data!=key and var.next!=self.head):
            var=var.next
        if(var==None):
            print("key not present")
        else:
            t=var.next
            var.next=temp
            temp.prev=var
            temp.next=t
            t.prev=temp

    def removenode(self,removekey):
        flag =0
        temp = self.head
        if temp is not None:
            if(temp.data==removekey):
                flag = 1
                temp.data = None
                temp=temp.next
                self.head=temp
                return
        else:
            while temp is not None:                                  # temp = 1000 data = 2  #prev lo node 1 info lo undhi 
                if(temp.data==removekey):   
                    flag =1              #deleting at particulae node
                    break
                if(temp.next == self.head):
                    break
                prev = temp
                temp=temp.next
        if flag==0:
            print("dal     ta not found")
            return
        if flag==1:
            if(temp == self.head):
                return 
            prev.next=temp.next
            temp = None

dlist = dclinkedlist()
dlist.atstart("10")
dlist.display()
print()
dlist.atstart("5")
dlist.display()
print()
dlist.atend("20")
dlist.display()
print()
dlist.inmid(10,15)
dlist.display()
print()
dlist.removenode(5)
dlist.display()
print()
       
