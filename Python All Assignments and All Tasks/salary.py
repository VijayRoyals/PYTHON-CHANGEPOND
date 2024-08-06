class Salary:
    @staticmethod
    def get_base_salary(base_salary):
        return base_salary

class Allowances:
    @staticmethod
    def calculate_allowances(base_salary):
        hra = 0.2 * base_salary
        da = 0.4 * base_salary
        ta = 0.25 * base_salary
        total_allowances = hra + da + ta
        return {
            "HRA": hra,
            "DA": da,
            "TA": ta,
            "Total Allowances": total_allowances
        }

class Deductions:
    @staticmethod
    def calculate_deductions(base_salary):
        insurance = 5000
        pf = 0.12 * base_salary
        gratuity = 0.05 * base_salary
        total_deductions = insurance + pf + gratuity
        return {
            "Insurance": insurance,
            "PF": pf,
            "Gratuity": gratuity,
            "Total Deductions": total_deductions
        }

def calculate_salary_slip(base_salary):
    # Calculate base salary
    base = Salary.get_base_salary(base_salary)
    
    # Calculate allowances
    allowances = Allowances.calculate_allowances(base_salary)
    
    # Calculate deductions
    deductions = Deductions.calculate_deductions(base_salary)
    
    # Compute gross and net salary
    gross_salary = base + allowances["Total Allowances"]
    net_salary = gross_salary - deductions["Total Deductions"]

    # Print the salary slip
    print('---------------- Salary Slip ----------------')
    print(f'Base Salary          : {base:.2f}')
    print('Allowances:')
    for key, value in allowances.items():
        print(f'  {key: <20}: {value:.2f}')
    print('Deductions:')
    for key, value in deductions.items():
        print(f'  {key: <20}: {value:.2f}')
    print(f'Gross Salary         : {gross_salary:.2f}')
    print(f'Net Salary           : {net_salary:.2f}')
    print('--------------------------------------------')

def main():
    base_salary = 10000
    calculate_salary_slip(base_salary)

if __name__ == "__main__":
    main()
