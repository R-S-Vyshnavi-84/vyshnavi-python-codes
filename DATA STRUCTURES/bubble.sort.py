'''
a=int(input())
b=int(input())
a,b=b,a
print(a)
'''
## bubble sort in ascending order
import numpy as  np
n=int(input())
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    a=int(input())
    x[i]=a
print (x)
 
for i in range(0,n-1,1):
    for j in range(i+1,n,1):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
            print(x)
print(x)                               

#bubble sort in descending order
import numpy as  np
n=int(input())
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    a=int(input())
    x[i]=a
print (x)
 
for i in range(0,n-1,1):
    for j in range(i+1,n,1):
        if x[i]<x[j]:    # change greater than symbol to lesser than symbol
            x[i],x[j]=x[j],x[i]
            print(x)
print(x)             