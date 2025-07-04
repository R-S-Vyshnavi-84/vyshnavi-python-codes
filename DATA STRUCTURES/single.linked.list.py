# single circular linked list
# no node is null , the last node points to the first node.
class node:                                       #NODE CREATION 
    def  __init__(self,dataval):
        self.dataval = dataval                     #DATA
        self.nextval = None                            #ADDRESS

class sclinkedlist:
    def __init__(self):
        self.headval = None                          #initailly head value

# beginning of insertion:
    def listprint(self):
        printval = self.headval                       #head node address 1000 starting 
        while printval is not None:
            if(printval.dataval is not None):
                print(printval.dataval,end=" ")         # 1000 data = 1          
            printval = printval.nextval   
 # 2000,3000/.. 2000 is equal to 3000 (next data address we have to check untill 
 # it is equal to stat to end node 1000 = 1000)
            if(printval==self.headval):              #printval = 2000 headval(evary time) = 1000 1st case # startinh is head nood and endinh is also head node is last
                break
        print()

# starting

    def atstart(self,newdata):
        newnode = node(newdata)                 # we dont have the list so we created the new node
        if(self.headval is None):            # the lis empty not present in this condition
            newnode.nextval = newnode                  # none first staring  we will add the 1000 in none place 
            self.headval = newnode
        else:
            newnode.nextval = self.headval         #new node lo unna none tisi 1000 value add ayidhi in (newnode address)
            self.headval=newnode                   # aa vachina new node ipudu headnode ayidhi 
    
    def atend (self,newdata):
        newnode = node(newdata)          #create node and stored in  node
        if self.headval is None:
            newnode.nextval = newnode
            self.headval= newnode
        else:
            temp = self.headval       #temp = 1000
            while(temp.nextval):       # 2000 = temnp.nextvale
                temp = temp.nextval
                if(temp == self.headval):    # 1000 = 1000 and taht 100 is stored in temp in temp we have last node value
                    break
            temp.nextval = newnode            # temp.newval = 1000 = 5000
            newnode.nextval = self.headval     # (newnode)5000.newvalue ante (1000) = 1000(self.head) ki equal chesam
#at end 
    def inmid(self,middle,newdata):
        newnode = node(newdata)
        if middle is None:
            print("data not present")
            return
        else:
            temp=self.headval         #temp = 1000 sunday 
            while (temp.dataval!=middle and temp.nextval!=self.headval): # middle = tuesday , 2000!=1000
                temp = temp.nextval                           #temp.nextval = 2000
            newnode.nextval = temp.nextval
            temp.nextval=newnode

# deleting:
    def removenode(self,removekey):
        flag =0
        temp = self.headval
        if temp is not None:
            if(temp.dataval==removekey):
                flag = 1
                temp.dataval = None
                temp=temp.nextval
                self.headval=temp
                return
        else:
            while temp is not None:                                  # temp = 1000 data = 2  #prev lo node 1 info lo undhi 
                if(temp.dataval==removekey):   
                    flag =1              #deleting at particulae node
                    break
                if(temp.nextval == self.headval):
                    break
                prev = temp
                temp=temp.nextval
        if flag==0:
            print("dota not found")
            return
        if flag==1:
            if(temp == self.headval):
                return 
            prev.nextval=temp.nextval
            temp = None

s1 = sclinkedlist()
s1.headval=node("monday")
s1.atstart("sunday")
s1.listprint()
s1.atend("thursday")
s1.listprint()
s1.inmid("tuesday","friday")
s1.listprint()
s1.removenode("sunday")
s1.listprint()

