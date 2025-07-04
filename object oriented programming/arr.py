# do in online, or google olapse
import numpy as np
x=np.arr([10,20,30,40])
print(x)
print(type(x))
x=np.arr([1.1,2.2,3.3])
x=np.arr(['abc',"ABC",'def'])
x=np.arr([2.2,'abc',"ABC",'def'])

# constant addition,subtraction,division,modular division,exponential
# const addition
import numpy as np
x=np.arr([1,2,3,4,5])
print(x)
x+=2
print(x)

# const multiplication
import numpy as np
x=np.arr([1,2,3,4,5])
print(x)
x*=2
print(x)

# const division
import numpy as np
x=np.arr([1,2,3,4,5])
print(x)
x=x/2
print(x)

#const modular division
import numpy as np
x=np.arr([1,2,3,4,5])
print(x)
x=x%2
print(x)

# const subtraction
import numpy 
a=numpy.array([1,2,3,4,5])
b=numpy.array([2,4,6,8,10])
c=a+b
print(c)                       # 1+2=3,2+4=6,3+6=9,4+8=12....
c=a-b
print(c)                       #'' '' '' ''
c=a*b
print(c)
c=a/b
print(c)
c=a%b                          #modular division
print(c)
c=a//b                         # floor division
print(c)
c=a**b                         # exponential 
print(c)

# sum(),max(),min(),len() functions
import numpy 
a=numpy.arr([1,2.2,3,4,5])
print(sum(a))

#max() function
import numpy 
a=numpy.arr([1,2.2,3,4,5,'abc'])
print(max(a))


# min function
import numpy 
a=numpy.arr([1,2.2,3,4,5,'abc'])
print(min(a))

# len() function
import numpy 
a=numpy.arr([1,2.2,3,4,5,'abc'])
print(len(a))

# accessing
import numpy 
a=numpy.arr([1,2.2,3,4,5,'abc'])
print(a)    # print complete data
print(*a)

# accessing array using index
import numpy 
a=numpy.arr([1,2.2,3,4,5,'abc'])
for i in a:   # i is data not index here
    print(i)
for i in range(len(a)):     # i is index here
    print(a[i])

# slicing
import numpy 
a=numpy.arr([1,2.2,3,4,5,'abc'])
print(a[::-1])

#zeros()-function:    # creates an array with al values zero
a=np.zeros(5,int)
print(a)

# ones() function: # craetes an array with all values 1
a=np.ones(4,int)
print(a)

import numpy as np
a=np.arr([1,2.2,3,4,5.2,'vyshu'])
print(a.dtype)
print(a.nd)