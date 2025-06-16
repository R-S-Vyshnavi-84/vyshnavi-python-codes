size=int(input("enter the size of list :"))
list=[]
#[2,2,6,9,10]
Unique_list=[]
for i in range(size):
    Temp=int(input(f"enter the integer value at{i} Index position"))
    list.append(Temp)
print(f"User Entered List : {list}")
for i in list:
    if i not in Unique_list:
        Unique_list.append(i)
print(f"Unique list :{Unique_list}")