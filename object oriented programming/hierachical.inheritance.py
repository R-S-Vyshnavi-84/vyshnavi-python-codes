class shape:
    def area(self):
        print("Calculate area:")

class circle(shape):
    def circlearea(self,radius):
        print("Area of circle=",3.14*radius*radius)

class square(shape):
    def squarearea(self,side):
        print("Area of square=",side*side)

c1=circle()
c1.area()
c1.circlearea(10)
s1=square()
s1.area()
s1.squarearea(10)