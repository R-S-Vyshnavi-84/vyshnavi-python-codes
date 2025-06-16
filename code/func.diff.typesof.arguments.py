# positiuonal arguments
def pw(x,y):
    z=x**y
    print(z)
pw(5,2)

#keyword argument
def show(name,age):
    print(name,age)
show(name="vyshnavi", age=18)

#default argument
def show(name,age=18):
    print(name,age)
show(name="vyshnavi",age=19)

#variable length arguments
def add(*num):
    z=num[0]+num[1]+num[2]
    print(z)
add(5,2,4)
#keyword variable length
def add(**num):
    z=num['a']+num['b']+num['c']
    print(z)
add(a=5, b=2, c=4)