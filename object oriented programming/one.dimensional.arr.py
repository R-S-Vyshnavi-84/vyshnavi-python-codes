import numpy as np
n=int(input())                                    # size of the array
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    v=int(input())
    x[i]=v
print(x)