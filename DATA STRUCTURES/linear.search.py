'''   
#using loops
import numpy as  np
n=int(input())
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    d=int(input())
    x[i]=d
print (x)
key=int(input())
flag=0
for i in range(n):
    if key==x[i]:
        print(i)
        flag=1
        break
if(flag==0):
    print("data not present")
           
    
# recursive linear search(using functions)

def rls(x,i,key):
    if(x[i]==key):
        return 1
    if(len(x)-1==i):
        return -1
    return rls(x,i+1,key)
import numpy as  np
n=int(input())
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    d=int(input())
    x[i]=d
print (x)
key=int(input())
ans=rls(x,0,key)   #calling funct
if(ans==-1):
    print("data not present")
else:
    print("data identified",ans)
'''

def rls(x,i,key):
    if(x[i]==key):
        return i
    if(i==0):
        return -1
    return rls(x,i-1,key)
import numpy as  np
n=int(input())
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    d=int(input())
    x[i]=d
print (x)
key=int(input())
ans=rls(x,n-1,key)   #calling funct
if(ans==-1):
    print("data not present")
else:
    print("data identified",ans)
