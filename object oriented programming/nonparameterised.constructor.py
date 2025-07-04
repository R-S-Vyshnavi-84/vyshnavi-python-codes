class person:
    c=0
    def __init__(self):
        person.c+=1

p1=person()
print(p1.c)
p2=person()
print(person.c)
p3=person()
print(person.c)