def arithmatic(x,y):
    c = x+y
    d = x-y
    e = x*y
    f = x/y
    g = x//y
    h = x%y
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
arithmatic(2,10)


def arithmatic(x,y):
    c = x+y
    d = x-y
    e = x*y
    f = x/y
    g = x//y
    h = x%y

    return(c,d,e,f,g,h)
res=arithmatic(5,10)
print(res)