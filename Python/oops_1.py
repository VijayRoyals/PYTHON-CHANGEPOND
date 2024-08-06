# #creating class 
# class Student: 
#     def __init__(self,firstname,lastname): 
#         self.firstname = firstname #instance variable #properties 
#         self.lastname = lastname 
#     def Display(self): #instance method 
#         print(f'{self.firstname} {self.lastname}') 
# obj1 = Student('Vijay', 'Kumar') 
# #print(obj1.firstname) 
# obj1.Display() 





class Mobile:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def Display(self):
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram} GB")


if __name__ == "__main__":
    my_mobile = Mobile("Samsung", 16)
    my_mobile.Display()
