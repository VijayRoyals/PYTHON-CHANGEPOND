class Demo:



    def __init__(self, a, b):
     
        self.a = a
        self.b = b

    def Fun(self):
        print(f"Fun method called for: a = {self.a}, b = {self.b}")

    def Gun(self):
        print(f"Gun method called for: a = {self.a}, b = {self.b}")


Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)


Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
