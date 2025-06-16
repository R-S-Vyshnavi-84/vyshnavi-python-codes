str=input("enter the mail id:")
name='' 
organisation=''
lenn=len(str)-4
for i in range(0,len(str)):
    if str[i]=='@':
        name=str[0:i]
        organisation=str[i+1:lenn]
print(f"name id",name)
print(f"organisation is",organisation)