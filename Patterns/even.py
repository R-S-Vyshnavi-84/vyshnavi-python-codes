n=int(input())
eps,ops=0,0
pos=0
while n>0:
    r=n%10
    if pos%2==0: 
     print(r,end=' ')
    n=n//10
    pos=pos+1
