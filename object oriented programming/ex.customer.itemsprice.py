class store:
    def __init__(self,name,no_of_items):
            self.name=name
            self.no_of_items=no_of_items
     
    
    def calculation(self):
        x=self.no_of_items
        tot_price=0
        for i in range(x):
            p=int(input())
            tot_price += p
        return tot_price
    
name=input()
no_of_items=int(input())
cust1=store("vyshnavi",4)
tot_price=cust1.calculation()
if(tot_price>200):
    print(tot_price - tot_price*0.2)
else:
    print(tot_price)
        
        