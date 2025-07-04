class father:
    fathername=''
    def father(self):
        print(self.fathername)

class mother:
    mothername=''
    def mother(self):
        print(self.mothername)

class son1(father,mother):
    son1name=''
    def son1information(self):
        print(self.fathername)
        print(self.mothername)
        print(self.son1name)

class son2(father):
    son2name=''
    def son2information(self):
        print(self.fathername)
      
        print(self.son2name)

        
s1=son1()
s1.son1name="Lava"
s1.fathername="Ram"
s1.mothername="Sitha"
s1.son1information()
s2=son2()
s2.fathername="Rama"
s2.son2name="Kusha"
s2.son2information()