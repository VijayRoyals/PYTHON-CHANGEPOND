class Demo:
    
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2
 
    def fun(self):
        print(f'Fun method : {self.value1},{self.value2}')
   
    def gun(self):
        print(f'Gun method : {self.value1},{self.value2}')
 
Obj1 = Demo('11','21')
Obj2 = Demo('51','101')
 
Obj1.fun()
Obj2.fun()
Obj1.gun()
Obj2.gun()

