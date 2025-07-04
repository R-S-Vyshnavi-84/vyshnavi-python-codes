# insertion sort ascending order
import numpy as  np
n=int(input())
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    a=int(input())
    x[i]=a
print (x)

for i in range(1,n,1):
    data=x[i]
    j=i
    while(j>0 and x[j-1]>data):
            x[j]=x[j-1]
            j-=1
    x[j]=data
    print(x)          # to observe swap stage by stage

print(x) 

# insertion sort descending order
import numpy as  np
n=int(input())
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    a=int(input())
    x[i]=a
print (x)

for i in range(1,n,1):
    data=x[i]
    j=i
    while(j>0 and x[j-1]<data):    # change ( < )symbol after x[j-1] for descending order
            x[j]=x[j-1]
            j-=1
    x[j]=data
    print(x)          # to observe swap stage by stage

print(x) 
