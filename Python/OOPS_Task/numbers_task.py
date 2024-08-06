# 6)Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value1,Value2.
# Inside init method initialize all instance variables to 0.
# There are three instance methods inside class as Accept(),Addition(),Subtraction(),Multiplication(),Division().
# Accept method will accept value of value1 and value2 from user.
# Addition() method will perform addition of Value1 and Value2 and return result.
# Subtraction() method will perform subtraction of Value1 and Value2 and return result.
# Multiplication() method will perform multiplication of Value1 and Value2 and return result.
# Division() method will perform division of Value1 and Value2 and return result.
# After Designing the above class call all instance methods by creating multiple objects.


class Numbers:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = float(input("Enter the first value: "))
        self.value2 = float(input("Enter the second value: "))

    def Addition(self):
        print("Addition: ",self.value1 + self.value2)
    
    def Subtraction(self):
        print("Subtraction: ",self.value1 - self.value2)

    def Multiplication(self):
        print("Multiplication: ",self.value1 * self.value2)

    def Division(self):
        if self.value2 != 0:
            print("Multiplication: ",self.value1 / self.value2)
        else:
            print("Error: Division by zero is not allowed.")


num1 = Numbers()
num1.Accept()
num1.Addition()
num1.Subtraction()
num1.Multiplication()
num1.Division()


