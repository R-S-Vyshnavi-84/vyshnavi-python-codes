def qs(arr):
    global a
    if(len(arr)<=1):
        return arr
    pivot=arr[len(arr)//2]
    print(pivot,a)
    a+=1
    left=[i for i in arr if i<pivot]  #expression(3), loop(1), condition(2)
    middle=[i for i in arr if i==pivot]
    right=[i for i in arr if i>pivot]
    return qs(right)+middle+qs(left)   #recursive call total 2 recursive-calls (1 for left and other for right)
                                       # if ans you want in descending order change right to left and left to right(viceversa)

a=1
n=int(input())
x=list(map(int,input().split(' ',n-1)))
print(x)
ans=qs(x)
print(ans)

