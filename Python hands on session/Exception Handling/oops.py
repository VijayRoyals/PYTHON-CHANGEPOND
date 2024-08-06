import datetime 
today = datetime.date.today() 
year = today.year 
class Company: 
    area = "SIPCOT, SiruSeri"
    __city = "Chennai"
    def __init__(self,cname): 
        self._cname = cname 
    def displayCname(self): 
        print("Company Name: ", self._cname) 
    def address(self):   
        return self.area + " ," + self.__city + ", TamilNadu";  


class Employee: 
    empcount = 0 
    isMarried = False 
    def __init__(self,fname,lname,yob): 
        # self._cname = cname 
        self._fname = fname 
        self._lname = lname 
        self.__age = year-yob 
        Employee.empcount +=1 
        self.__id=self.empcount 
        
    def getEmpDetails(self): 
        print("Employee Id:" , self.__id) 
        print("Full Name:", self._fname," ",self._lname); 
        print("Age :", self.__age, "Years") 
        print("Maritial Status: ",self.isMarried)
        
        
c1 = Company("ChangePond Technologies") 
c1.displayCname()
c1.__city ="Pune"
print("Address: ",c1.address())

print("*" * 70) 

e1 = Employee("VIJAY","KUMAR",2002) 
e1.isMarried = True 
e1.getEmpDetails(); 
print("*" * 70)

c1 = Company("ChangePond Technologies") 
c1.displayCname() 


