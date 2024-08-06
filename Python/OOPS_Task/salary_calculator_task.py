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









class BasicSalary:
    def __init__(self, salary):
        self.basic_salary = salary

    def display_salary(self):
        print("Base Salary: ", self.basic_salary)
class Allowance(BasicSalary):
    def calculate_allowances(self):
        self.hra = (self.basic_salary / 100) * 20  # House Rent Allowance
        self.da = (self.basic_salary / 100) * 40  # Dearness Allowance
        self.ta = (self.basic_salary / 100) * 25  # Travel Allowance
        self.total_allowance = self.hra + self.da + self.ta
class Deduction(BasicSalary):
    def calculate_deductions(self):
        self.insurance = 5000
        self.pf = (self.basic_salary / 100) * 12  # Provident Fund
        self.gratuity = (self.basic_salary / 100) * 5  # Gratuity
        self.total_deduction = self.insurance + self.pf + self.gratuity
class SalarySlip(Allowance, Deduction):
    def generate_salary_slip(self):
        self.calculate_allowances()
        self.calculate_deductions()
        
        print("=" * 50)
        print("Base Salary: ", self.basic_salary)
        print("=" * 50)
        print("Total Allowances: ", self.total_allowance)
        print("=" * 50)
        print("Total Deductions: ", self.total_deduction)
        print("=" * 50)
        
        gross_salary = self.basic_salary + self.total_allowance
        print("Gross Salary: ", gross_salary)
        
        net_salary = gross_salary - self.total_deduction
        print("=" * 50)
        print("Net Salary: ", net_salary)
        print("=" * 70)
salary_input = int(input("Enter the  salary: "))
employee_salary_slip = SalarySlip(salary_input)
employee_salary_slip.generate_salary_slip()