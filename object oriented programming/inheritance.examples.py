#multi level inheritance
class flowers:
    def __init__(self):
        self._a=32
        print(self._a)

class derived(flowers):
    def __init__(self):
        flowers.__init__(self)
        print(self._a+2)

class derived1(derived):     #derived is a class
    def __init__(self):
        derived.__init__(self)
        print(self._a*2)
x=derived1()


#hierarchical inheritance
class flower:
    flowername=''
    def flower(self):
        print(self.flowername)

class fruit:
    fruitname=''
    def fruit(self):
        print(self.fruitname)

class seed1(flower,fruit):
    seed1name=''
    def seed1information(self):
        print(self.flowername)
        print(self.fruitname)
        print(self.seed1name)

class seed2(flower):
    seed2name=''
    def seed2information(self):
        print(self.flowername)
        print(self.seed2name)

        
s1=seed1()
s1.seed1name="mango seed"
s1.flower="mango flower"
s1.fruit="mango fruit"
s1.seed1information()
s2=seed2()
s2.flowername="mangoflower"
s2.seed2name="mangoseed"
s2.seed2information()

#multiple.inheritance
class flower:
    flowername=''
    def flower(self):
        print(self.flowername)

class fruit:
    fruitname=''
    def fruit(self):
        print(self.fruitname)

class seed1(flower,fruit):
    seed1name=''
    def seed1information(self):
        print(self.flowername)
        print(self.fruitname)
        print(self.seed1name)

class seed2(flower):
    seed2name=''
    def seed2information(self):
        print(self.flowername)
        print(self.seed2name)

s1.seed1information()
s1.flowername="mango flower"
s1.seed1name="mango seed"
s1.fruitname="mango fruit"
