num=int(input("enter the value of num :"))
even_list=[]
odd_list=[]
for i in range(1,num+1,2):
    odd_list.append(i)
for i in range(2,num+1,2):
    even_list.append(i)
print("even_list :",even_list)
print("odd_list",odd_list)