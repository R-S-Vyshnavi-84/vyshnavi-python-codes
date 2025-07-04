class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("vyshnavi",19)
p2=person("shalini",46)
print(p1.name,p1.age)
print(p2.name,p2.age)


class person:
    def __init__(se,name,age):
        se.name=name
        se.age=age

p1=person("vyshnavi",19)
p2=person("shalini",46)
print(p1.name,p1.age)
print(p2.name,p2.age)

# not printing too many statements
class person:
    def __init__(se,name,age):
        se.name=name
        se.age=age
    def printing(self):
        print(self.name,self.age)
p1=person("vyshnavi",19)
p2=person("shalini",46)
p1.printing()
p2.printing()

#without instance variable(init)

class person:
    name=''
    age=''

p1=person()
p1.name="vyshanvi"
p1.age="18"
p2=person()
p2.name="srinivas"
p2.age="50"
print(p1.name,p1.age)
print(p2.name,p2.age)

#deciding eligible or not eligible, converting to uppercase
class person:
    def __init__(se,name,age):
        se.name=name
        se.age=age
    def printing(self):
        print(self.name,self.age)

    def decide(self):
        print(self.age)
        if (self.age>18):
            print("eligible")
        else:
            print("not eligible")

    def uppercaseconversion(self):
        x=self.name
        print(x.upper())

    def lengthprinting(self):
        print(len(self.name))

p1=person("vyshnavi",10)
p2=person("shalini",46)
p1.printing()
p2.printing()
p1.decide()
p2.decide()
p1.uppercaseconversion()
p2.uppercaseconversion()
p1.lengthprinting()
p2.lengthprinting()


