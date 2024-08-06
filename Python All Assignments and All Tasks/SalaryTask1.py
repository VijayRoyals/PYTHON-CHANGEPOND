class Allowance:
    @staticmethod
    def calculate(basic_salary):
        hra = 0.2 * basic_salary
        da = 0.4 * basic_salary
        ta = 0.25 * basic_salary
        return {
            "HRA": hra,
            "DA": da,
            "TA": ta
        }

class Salary:
    def __init__(self, basic_salary):
        self.basic_salary = basic_salary
        self.allowances = Allowance.calculate(basic_salary)
        self.insurance = 5000
        self.pf = 0.12 * basic_salary
        self.gratuity = 0.05 * basic_salary

    def calculate_salary(self):
        hra = self.allowances['HRA']
        da = self.allowances['DA']
        ta = self.allowances['TA']

        gross_salary = self.basic_salary + hra + da + ta
        deductions_total = self.insurance + self.pf + self.gratuity
        net_salary = gross_salary - deductions_total

        salary_slip = {
            "Basic Salary": self.basic_salary,
            "Gross Salary": gross_salary,
            "Net Salary": net_salary,
            "Allowances": self.allowances,
            "Deductions": {
                "Insurance": self.insurance,
                "PF": self.pf,
                "Gratuity": self.gratuity
            }
        }
        return salary_slip

# Example usage
if __name__ == "__main__":
    basic_salary = 10000
    salary = Salary(basic_salary)
    salary_slip = salary.calculate_salary()

    # Displaying the salary slip in a formatted way
    print("===================================")
    print("           SALARY SLIP             ")
    print("===================================")
    print(f"Basic Salary      : {salary_slip['Basic Salary']:.2f}")
    print(f"Gross Salary      : {salary_slip['Gross Salary']:.2f}")
    print(f"Net Salary        : {salary_slip['Net Salary']:.2f}")
    print("\nAllowances:")
    for key, value in salary_slip['Allowances'].items():
        print(f"  {key: <10}: {value:.2f}")
    print("\nDeductions:")
    for key, value in salary_slip['Deductions'].items():
        print(f"  {key: <10}: {value:.2f}")
    print("===================================")
