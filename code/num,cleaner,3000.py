size=int(input("enter the range of list"))
num=[]
temp=0
for i in range(size):
    value=int(input(f"enter the value at {i} index :"))
    num.append(value)
print("original list :{num}")
for i in range(size):
    if(num[i]<0):
        num[i]=0
    if(num[i]%3==0):
        print(num[i])