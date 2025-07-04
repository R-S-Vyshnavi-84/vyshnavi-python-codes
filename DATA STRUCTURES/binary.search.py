'''# ascending order
n=int(input())
x=list(map(int,input().split(' ',n-1)))
print (x)
x.sort()
print(x)
key=int(input())
low=0
high=n-1
flag=0
while low<=high:
    print(low,high)
    mid=(low+high)//2
    if x[mid]==key:
        print(mid)
        flag=1   #data identified
        break
    elif key>x[mid]:
        low=mid+1
    else:
        high=mid-1
if(flag==0):
    print("data not present")

#descending order
n=int(input())
x=list(map(int,input().split(' ',n-1)))
print (x)
x.sort(reverse=True)      # reverse=true for descending order
print(x)
key=int(input())
low=0
high=n-1
flag=0
while low<=high:
    print(low,high)
    mid=(low+high)//2
    if x[mid]==key:
        print(mid)
        flag=1   #data identified
        break
    elif key>x[mid]:
         high=mid-1
    else:
        low=mid+1
if(flag==0):
    print("data not present")
'''
# recursuve funct
def rbs(x,l,h,key):
    if l<=h:
        print(l,h)
        mid=(l+h)//2
        if x[mid]==key:
            return mid
        elif key>x[mid]:
            rbs(x,mid+1,h,key)
        else:
            rbs(x,l,mid-1,key)
    return -1
n=int(input())
x=list(map(int,input().split(' ',n-1)))
print (x)
x.sort()
print(x)
key=int(input())
low=0
high=n-1
ans=rbs(x,low,high,key)
if(ans==-1):
    print("data not present")
else:
    print(ans)