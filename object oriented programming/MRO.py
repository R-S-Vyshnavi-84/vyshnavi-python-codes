class A:
    def myname(self):
        print("I am a class A")

class B(A):
    def myname(self):                     #pass
        print("I am a class B")

class C(A):
    def myname(self):
        print("I am a class C")

class D(C,B):                                           # classes ordering
    pass
d=D()
d.myname()
print(D.__mro__)
print(D.mro())