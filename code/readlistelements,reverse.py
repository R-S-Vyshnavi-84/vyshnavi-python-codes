size=int(input("enter the size of list :"))
list=[]
for i in range(size):
    temp=int(input(f"enter the integer value at {i} :"))
    list.append(temp)
print(list[::-1])
