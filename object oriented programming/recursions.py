'''#1. prog to print a to b numbers of given input 5 to 10
#non recursive
a,b=map(int,input())
while a<=b:
    print(a)
    a+=1

n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    print(i)

# recursive method
def rlh(x,y):
    if(x<=y):
        print(x)
        x+=1
        rlh(x,y)
a,b=map(int,input().split())
rlh(a,b)
        
    
# low to high:<,<=
# high to low: >,>=


# 2. recursive program to print nos from a to b where a is high and b is low:
def rlh(x,y):
    if(x>=y):
        print(x)
        x-=1
        rlh(x,y)
a,b=map(int,input().split())
rlh(a,b)


#3. recursive program to print the factorial of given number
#recursive
def rlh(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    print(fact)
n=int(input())
rlh(n)
# 2nd method
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
#non-recursive
n=int(input())
f=1
while n>=1:
    f*=n
    n-=1
print(f)

#4. 
def fact(n,a,b):
    if(n==0 or n==1):
        print(n)
    if (n==a):
        print(b)
    else:
        n-=1
        return fact(n,a,b*n)
n=int(input())
fact(n,1,n)


# 5.recursive prog to print hcf/gcf of a no:
#import math
#print(math.gcd(5,12))
#print(math.lcm(5,12))
a,b=map(int,input().split())
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(a)
print(b)

#non recursive:
def rgcd(a,b):
    if(a==b):
        return a
    if (a>b):
        return rgcd(a-b,b)#recursive call-1
    else:
        return rgcd(a,b-a)#recursive call-2
a,b=map(int,input().split())
ans=rgcd(a,b)
print(ans)


# recursive prog to print lcf of two num:
def rlcm(a,b,x,y):
    if(a==b):
        return (x*y)//a
    if (a>b):
        return rlcm(a-b,b,x,y)#recursive call-1
    else:
        return rlcm(a,b-a,x,y)#recursive call-2
a,b=map(int,input().split())
ans=rlcm(a,b,a,b)   # for multiplication
print(ans)

 
#
import sys
sys.setrecursionlimit(100)
def vignan():
    global i     #change the input i=0 to i=1 using global func
    i+=1
    print(i)
    vignan()
i=0
vignan()
'''
# towers of hanoi maths puzzle problem
def toh(n,a,b,c):
    if(n>0):
        toh(n-1, a,c,b)        #A=INPUT, c=output, b=
        print(a,'->',c)
        toh(n-1,b,c,a)
n=int(input())
toh(n,'a','b','c')
