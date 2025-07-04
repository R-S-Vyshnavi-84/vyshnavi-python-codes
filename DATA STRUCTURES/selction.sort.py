import numpy as  np
n=int(input())
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    a=int(input())
    x[i]=a
print (x)
 
for i in range(0,n-1,1):
    min1=i
    for j in range(i+1,n,1):
        if x[min1]>x[j]:      # change greater than symbol to lesser than symbol
            min1=j
            x[i],x[min1]=x[min1],x[i]
            print(x)   # to observe swap stage by stage
            
print(x)             