class base:
    def __init__(self):
        self.__a=32
        print(self.__a)

class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self.__a+2)

b1=base()