# 3)Write a program which contains one class named as Circle
# Circle class contains three instance variables as Radius,Area ,Circumference.
# That class contains one class variable as PI which is initialize to 3.14
# Inside init method initialize all instance variables to 0.0
# There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference( ),
# ,Display( )
# Accept method will accept value of Radius from user.
# CalculateArea () method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference () method will calculate circumference of circle and store it into instance variable
# Circumference.
# And Display( ) method will display value of all the instance variables as radius , Area , Circumference.
# After designing the above class call all instance methods by creating multiple objects


class Circle:
    PI = 3.14
    def __init__(self) :
        self.Radius =  0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = int(input('Enter the Radius of a Circle : '))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print(f'Radius : {self.Radius} \nArea : {self.Area} \nCircumference : {self.Circumference}')

obj1 = Circle()
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()


obj3 = Circle()
obj3.Accept()
obj3.CalculateArea()
obj3.CalculateCircumference()
obj3.Display()
