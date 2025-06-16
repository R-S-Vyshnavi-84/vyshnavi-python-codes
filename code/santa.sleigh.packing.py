size=int(input("enter the size of the toy's list"))
list=[]
Unique_list=[]
for i in range(size):
    temp=input(F"enter the name of the toy :")
    list.append(temp)
print(f"the in initial list is {list}")
for i in list:
    if i  not in Unique_list :
        Unique_list.append(i)
print(f"the finalised list is: {Unique_list}")
