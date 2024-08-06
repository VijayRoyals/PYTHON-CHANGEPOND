class Salary:
    def __init__(self,baseSalary):
        self.baseSalary=baseSalary
    def getSalary(self):
        print(f'your base  salary is : {self.baseSalary}')

class Allowances(Salary):
    def __init__(self,salary):
        self.hra=int(0.2*salary)
        self.da=int(0.4*salary)
        self.ta=int(0.25*salary)
        self.allowances=self.hra+self.da+self.ta
        super().__init__(salary)
    def get_allowances(self):
        print(f'your allowances are : \nHRA (20%) : {self.hra}\nDA (40%) : {self.da}\nTA (25%) : {self.ta}\ntotal allowances: {self.hra+self.da+self.ta}')
class Deduction(Allowances):
    def __init__(self,salary):
        self.insurance=5000
        self.pf=int(0.12*salary)
        self.graduity=int(0.05*salary)
        self.deductions=self.insurance+self.pf+self.graduity
        # print(self.insurance,self.pf,self.graduity,salary)
        super().__init__(salary)
    def get_deductions(self):
        print(f'your deductions are : \nInsurance    : {self.insurance}\nPF (12%) : {self.pf}\nGRADUITY (5%) : {self.graduity}\ntotal deductions: {self.insurance+self.pf+self.graduity}')

class CalculateSalarySlip(Deduction):
    def __init__(self, salary):
        super().__init__(salary)
    def getSalarySlip(self):
        print('----------------Salary slip-----------------')
        super().getSalary()
        super().get_allowances()
        super().get_deductions()
        print(f'your gross salary is {super().__getattribute__('baseSalary')+super().__getattribute__('allowances')}')
        print(f'your net salary is {super().__getattribute__('baseSalary')+super().__getattribute__('allowances')-super().__getattribute__('deductions')}')


def main():
    cs= CalculateSalarySlip(10000)
    cs.getSalarySlip()


if __name__=="__main__":
    main()