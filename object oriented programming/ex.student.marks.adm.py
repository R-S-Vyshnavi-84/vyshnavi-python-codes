class student:
    def __init__(self,name,rollno,maths,phy,chem):
        self.rollno=rollno
        self.maths=maths
        self.phy=phy
        self.chem=chem
    
    def calculation(self):
        if(self.maths>=40 and self.phy>=40 and self.chem>=40):
            tot=self.maths+self.phy+self.chem
            avg=tot/3
            print(tot)
            print(avg)
            if(self.maths>75 and self.phy>75) or (self.phy>75 and self.chem>75) or (self.chem>75 and self.maths>75):
                print("Admission is confirmed...!")
            else:
                print("Admission iss not confirmed!")
        else:
            print("Fail")
s1=student("Vyshnavi",108,94,92,95)
s1.calculation()