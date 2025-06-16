ipl_list=['csk','rcb','mi','srh','gt','pbks']
print("accessing without index loop:")
for i in ipl_list:
    print(i)
print("accessing with index loop:")
for i in range(len(ipl_list)):
    print(ipl_list[i])

print("accessing list elements with index using while loop:")
i=0
while(i<len(ipl_list)):
    print(ipl_list[i])
    i+=1
    