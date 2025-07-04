'''import numpy as np
n=int(input())
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    v=int(input())
    x[i]=v
print(x)
ans=np.where(x%2!=0)
print(ans)

# index of given particular value present in list 5,10,5,10
import numpy as np
n=int(input())
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    v=int(input())
    x[i]=v
print(x)
ans=np.where(x==k)
print(ans)

# even number, odd number
import numpy as np
n=int(input())
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    v=int(input())
    x[i]=v
print(x)
ans=np.where(x>k)
print(ans)
   

# program to find the index to insert new element into the list in the correct position by maintaining order
import numpy as np
n=int(input())
a=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    x=int(input())
    a[i]=x
print(a)
d=int(input())
ans=np.searchsorted(a,d)
print(ans)
print(a)
   

import numpy as np
n=int(input())
a=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    x=int(input())
    a[i]=x
print(a)
a.sort()
print("after sort",a)
            

# 2 dimensional array:
import numpy as np
x=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(x)
print(a)
print(a.dtype)      #datatype
print(a.shape)
print(a.ndim)    # give the dimnsion of array which is 2-dimensional
print(a.size)    # array size

# symbol removal (* is used to remove symbol)
import numpy as np
x=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(x)
print(a)
print(*a)
      
# using loop for removal of extra bracket
import numpy as np
x=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(x)
for i in range(3):
    for j in range(3):
        print(a[i][j],end=' ')
    print()
              
# to  print index information of i and j
import numpy as np
x=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(x)
for i in range(3):
    for j in range(3):
        print(a[i][j],(i,j),end=' ')    # to  print index information of i and j
    print()
        
#2d array data matrix
import numpy as np
x=[[1,2,3],[4,5,6],[7,8,9]]
m=np.matrix(x)                   # matrix is a class 
print(m)
print(m.type)


# flatten a line and get in barcket
import numpy as np
x=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(x)
m=np.matrix(x)
ans=a.flatten()
print(ans)
ans1=m.flatten()
print(ans1)

# reshape rows and columns
import numpy as np
x=[[1,2,3],[4,5,6]]
a=np.array(x)
m=np.matrix(x)
a1=a.reshape(3,2)   #  changed 2rows, 3columns to 3rows,2 columns
print(a1)
m1=m.reshape(3,2)          # converted value always stored in a1
print(m1)
        

# constant addition, subtraction, multiplication, division, modular division, floor division:
import numpy as np
a=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(a)
m=np.matrix(a)
a=a+1
print(a)
m+=1             # cont addition
print(m)

a=a-1
print(a)
m-=1             # const subtraction
print(m)

a=a*2
print(a)
m*=2            #const multiplication
print(m)

a=a/2
print(a)
m=m/2           # const division
print(m)

a=a%2
print(a)
m%=2            # modular diviaion result is always 0 or 1
print(m)

a=a**2
print (a)
m**=2          # const exponential
print(m)

a=a//2
print(a)
m=m//2
print(m)          # floor division
      


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
print(a)
print(a.sum())
print(m.sum())
print(a.cumsum())    # adding elemnts data one by one = cumulative sum
print(m.cumsum())
print(a.sum(axis=1))
print(m.sum(axis=1))
print(a.sum(axis=0))
print(m.sum(axis=0))

# max func()
print(a.max(axis=1))            
print(m.max(axis=1))
print(a.max(axis=0))
print(m.max(axis=0))

# min func()
print(a.min(axis=1))            
print(m.min(axis=1))
print(a.min(axis=0))            
print(m.min(axis=0))

print(len(a))            #length of row=3
print(len(m))

# product func()
print(a.prod())
print(m.prod())
print(a.prod(axis=1))
print(m.prod(axis=1))
print(a.prod(axis=0))
print(m.prod(axis=0))

# transposing
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
print(a.T)
print(a.T)                      # a.T,m.T transpose of array and matrix data
print(a.transpose())
print(m.transpose())            # transposing using transpose func()

# tracing diagonal elements
print(a.trace())
print(a.trace())            
             

#
import numpy as np
a=np.array([[1,1,1],[2,2,2],[3,3,3]])
m=np.matrix('1,1,1;2,2,2;3,3,3')
print(np.unique(a))
print(np.unique(m))
        

# finding determinant of matrix
import numpy as np
a=np.array([[6,1,1],[4,-2,5],[2,8,7]])
m=np.matrix('6,1,1;4,-2,5;2,8,7')
ans=np.linalg.det(a)
print(ans)
ans=a.mean()
ans1=m.mean()
print(ans)
print(ans1)

#zeros operation
import numpy as np
a = np.zeros((3,4),dtype=int)
print(a)
import numpy as np
a = np.ones((3,4),dtype=int)
print(a)
import numpy as np
a = np.ones((3,4))
print(a)
a = np.full((3,4),5)
print(a)

#sort operation
import numpy as np
a=np.array([[2,4,6],[3,6,9],[4,8,12]])
m=np.matrix('2,4,6;3,6,9;4,8,12')
x=np.sort(a,axis=None)
y=np.sort(m,axis=None)     #complete sort
print(x)
print(y)

x=np.sort(a,axis=1)
y=np.sort(m,axis=1)     #row sort
print(x)
print(y)

x=np.sort(a,axis=0)
y=np.sort(m,axis=0)     #column sort
print(x)
print(y)

# descending order(compete,row and column wise)
import numpy as np
a=np.array([[2,4,6],[3,6,9],[1,3,2]])
m=np.matrix('2,4,6;3,6,9;4,8,12')
x=(np.sort(-a,axis=1))*-1
print(x)
y=(np.sort(-a,axis=0))*-1
print(y)
'''
#matrix addition operation,matrix subtraction, matrix multiplication by comparing two matrices
import numpy as np
a=np.array([[1,2,3]],[[4,5,6]])
b=np.matrix([[4,5,6]],[[1,2,3]])
c=np.matrix('1,2,3;4,5,6')
d=np.matrix('4,5,6;1,2,3')
print(a+b)
print(c+d)
print(a-b)
print(c-d)