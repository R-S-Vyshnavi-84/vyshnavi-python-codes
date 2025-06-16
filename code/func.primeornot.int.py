def is_primeone(num):
    count=0
    for i in range(1,num+1):
          if(num%i==0):
               count+=1
    if(count==2):
         print(f"{num} is prime")
    else:
         print(f"{num} is not prime")
is_primeone(0)


def is_primeone(num):
    count=0
    if num>1:
        for i in range(2,num//2+1):
            if(num%i==0):
               count+=1
        if(count==0):
            print(f"{num} is prime")
    else:
         print(f"{num} is not prime")
is_primeone(18)