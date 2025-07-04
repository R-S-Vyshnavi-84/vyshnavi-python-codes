class base:
    def __init__(self):
        self._a=32
        print(self._a)

class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self._a+2)

class derived1(derived):     #derived is a class
    def __init__(self):
        derived.__init__(self)
        print(self._a*2)

x=derived1()

