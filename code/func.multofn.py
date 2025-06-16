def multiplication(num):
    i=1
    while(i<=10):
        if(i%num==0 or i%num!=0):
            print(num,"x",i,"=",num*i)
        i=i+1
num=int(input("enter the number:"))
multiplication(num)