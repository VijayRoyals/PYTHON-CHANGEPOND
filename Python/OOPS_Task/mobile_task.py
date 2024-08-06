class Mobile():
    def __init__(self,mobile,ram):
        self.mobile = mobile
        self.ram = ram
    
    def Display(self):
        print(f'Mobile : {self.mobile} \nRAM : {self.ram}')

obj1 = Mobile('Samsung','8 GB')
obj1.Display()