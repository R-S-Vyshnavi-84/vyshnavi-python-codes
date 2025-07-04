class calculation1:
    def summation(self,a,b):
        return a+b;
class calculation2:
    def multiplication(self,a,b):
        return a*b;
class derived(calculation1,calculation2):
    def divide(self,a,b):
        return a/b;
d=derived()
print(isinstance(d,derived))
print(isinstance(d,calculation1))
print(isinstance(d,calculation2))
