class father:
    def __init__(self,name):
        self.name=name
    def show(self):
            print(self.name)

class son(father):
    def __init__(self,name):
        self.name=name
    def show1(self):
        print(self.name)

x=father('Srinivas')
x.show()
y=son('kartheek')
y.show1()
y.show
x.show()


class subjects:
    def __init__(self,name):
        self.name=name
    def show(self):
            print(self.name)

class department(subjects):
    def __init__(self,name):
        self.name=name
    def show1(self):
        print(self.name)

x=subjects('microbiology')
x.show()
y=department('biotechnology')
y.show1()
y.show
x.show()