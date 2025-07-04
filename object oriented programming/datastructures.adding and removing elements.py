class node:                                  #creating node  for
    def __init__(self,dataval=None):
        self.dataval = dataval             # 12
        self.nextval = None                   #address
class slinkedlist:                             # fosr linked list 
    def __init__(self):
        self.headval = None
    
    def listprint(self):                       # to print the linked list data
        printval=self.headval                   # head node address 1000 is stored
        while printval is not None:                 # printval is node name
            print(printval.dataval,end=' ')       #1000 ! = None
            printval=printval.nextval
        print()
    def atbeg(self,newdata):
        newnode = node(newdata)                          #node is monday
        if self.headval is None:
            self.hradva1 = newnode                    #newnode 
        newnode.nextval=self.headval                       #1000 ois storde in newnoode()
        self.headval = newnode

    def atend(self,newdata):
        newnode = node(newdata)
        if self.headval is None:
            self.headval = newnode
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = newnode
    def inmid(self,middle,newdata):
        if middle is None:
            print("data not present")
        temp = self.headval                     #temp = 1000
        newnode = node(newdata)
        while(temp.dataval!=middle and temp.nextval!=None):        #dataval=1000
            temp = temp.nextval                              # 
        newnode.nextval = temp.nextval
        temp.nextval = newnode        
    def removenode(self,removekey):
        headval = self.headval 
        if(headval is not None):
            if(headval.dataval == removekey):
                self.headval = headval.nextval
                headval=None
                return 
        while(headval is not None):
            if(headval.dataval == removekey):
                break
            prev = headval
            headval = headval.nextval
        if (headval==None):
            prev.nextval = None
            return                         #prev.nextval = None
        prev.nextval = headval.nextval
        headval=None

s1 = slinkedlist()
s1.headval=node("monday")
e2 = node("tuesday")
e3 = node("wednesday")
s1.headval.nextval=e2
e2.nextval=e3
s1.listprint()
s1.atbeg("sunday")
s1.listprint()
s1.atend("thursday")
s1.listprint()
s1.inmid("tuesday","friday")
s1.listprint()
s1.removenode("friday")
s1.listprint()

      





