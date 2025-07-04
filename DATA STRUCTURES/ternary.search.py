'''
n=int(input())
x=list(map(int,input().split(' ',n-1)))
print(x)
x.sort()
print(x)
key=int(input())
l=0
r=n-1
flag=0
while l<=r:
    print(l,r)
    mid1=l+(r-l)//3
    mid2=r-(r-l)//3
    print(mid1,mid2)
    if(x[mid1]==key):      #first part
        flag=1
        print(mid1)
        break
    elif(x[mid2]==key):     # second part
        flag=1
        print(mid2)
        break
    elif(key<x[mid1]):       #middle
        r=mid1-1
    elif(key>x[mid2]):
        l=mid2+1
    else:
        l=mid1+1
        r=mid2-1
if(flag==0):
    print("data not found")
'''
#recursive program

def rts(x,l,r,key):
    if l<=r:
        print(l,r)
        mid1 = l+(r-l)//3
        mid2 = r-(r-l)//3
        print (mid1,mid2)
        if(x[mid2]==key):
            return mid2
        elif(key<x[mid1]):                 # first part
            return rts (x,l,mid1-1,key)
        elif(key>x[mid2]):                 # second part
            return rts (x,mid2+1,r,key)
        else:                              # third part
            return rts(x,mid1+1,mid2+1,key)
    return -1

n = int(input())
x=list(map(int,input().split(' ',n-1)))
print(x)
x.sort()
print(x)
key = int(input())
l = 0
r=n-1
ans=rts(x,l,r,key)
if ans==-1:
    print('data not found')
else:
    print('date is present in',ans)