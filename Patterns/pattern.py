n=int(input())
sp=n-1
st=1
for i in range(n):
    for k in range (sp):
        print(' ',end=' ')
    for j in range (st):
        print('*',end=' ')
    print()
    sp=sp-1
    st=st+2
