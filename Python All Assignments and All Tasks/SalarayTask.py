class Salary:
    def __init__(self, basic_salary):
        self.basic_salary = basic_salary
        self.hra = 0.2 * self.basic_salary
        self.da = 0.4 * self.basic_salary
        self.ta = 0.25 * self.basic_salary
        self.insurance = 5000
        self.pf = 0.12 * self.basic_salary
        self.gratuity = 0.05 * self.basic_salary

    @staticmethod
    def calculate_salary(basic_salary):
        hra = 0.2 * basic_salary
        da = 0.4 * basic_salary
        ta = 0.25 * basic_salary
        insurance = 5000
        pf = 0.12 * basic_salary
        gratuity = 0.05 * basic_salary

        gross_salary = basic_salary + hra + da + ta
        deductions_total = insurance + pf + gratuity
        net_salary = gross_salary - deductions_total

        salary_slip = {
            "Basic Salary": basic_salary,
            "Gross Salary": gross_salary,
            "Net Salary": net_salary,
            "Allowances": {
                "HRA": hra,
                "DA": da,
                "TA": ta
            },
            "Deductions": {
                "Insurance": insurance,
                "PF": pf,
                "Gratuity": gratuity
            }
        }
        return salary_slip


# Example usage:
cs = Salary.calculate_salary(10000)

print("Salary Slip:")
print(f"Basic Salary: {cs['Basic Salary']}")
print(f"Gross Salary: {cs['Gross Salary']}")
print(f"Net Salary: {cs['Net Salary']}")
print("Allowances:")
for key, value in cs['Allowances'].items():
    print(f"  {key}: {value}")
print("Deductions:")
for key, value in cs['Deductions'].items():
    print(f"  {key}: {value}")