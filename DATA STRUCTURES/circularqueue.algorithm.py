#insertion
f=-1
r=-1
q=[]
n=5

if f==-1 and r==-1:
    print("queue full")
elif f==-1 and r==-1:
    f=(f+1)%n
    r=(r+1)%n
    a=int(input())
    q[r]=a
else:
    r=(r+1)%n
    a=int(input())
    q[r]=a

#deletion
f=-1
r=-1
q=[]
n=5
if f==-1 and r==-1:
    print("empty")
elif f==r:
    x=q[f]
    f=-1
    r=-1
    print (x)
else:
    x=q[f]
    f=(f+1)%n
    print (x)

#printing the data
f=-1
r=-1
q=[]
n=5
if f==-1 and r==-1:
    print("no data")
elif f<r:
    for i in range(f,r+1,1):
        print(q[i])
else:
    for i in range(f,n,1):
        print(q[i])
    for i in range(0,r+1,1):
        print(q[i])