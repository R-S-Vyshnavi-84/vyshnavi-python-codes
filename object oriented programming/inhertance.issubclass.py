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
print(issubclass(derived,calculation1))
print(issubclass(derived,calculation2))
print(issubclass(calculation1,calculation2))