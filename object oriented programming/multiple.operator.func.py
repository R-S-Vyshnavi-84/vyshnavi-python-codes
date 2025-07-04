class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person('vyshu',18)
print(getattr(p1,'name'))#print(p1.name)
print(getattr(p1,'age'))
setattr(p1,'age',18)
print(getattr(p1,'age'))
print(hasattr(p1,'age'))
print(hasattr(p1,'id'))