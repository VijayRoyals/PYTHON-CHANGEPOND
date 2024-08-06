# 4) Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That Class Contains one class variable as ROI which is initialize to 10.5
# Inside init method initialize all name and amount variable by accepting the values from user.
# There are four instance methods inside class as Display() , Deposit (), Withdraw( ), CalculateInterest()
# Deposit( ) method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateInterst() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI
# And Display () method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects

class BankAccount:
    ROI = 10.5  

    def __init__(self):
        self.name = input('Enter the Name : ') 
        self.amount = int(input('Enter the Amount : '))  

    def Display(self):
        print(f"Name: {self.name}")
        print(f"Amount: {self.amount}")

    def Deposit(self):
        deposit_amount = int(input('Enter the Amount to be deposited : '))
        self.amount += deposit_amount
        print(f"Deposited : {deposit_amount}\nNew Balance: {self.amount}")

    def Withdraw(self):
        withdraw_amount = int(input('Enter the Amount to be Withdrawed : '))
        if withdraw_amount > self.amount:
            print("Insufficient balance.")
        else:
            self.amount -= withdraw_amount
            print(f"Withdrew : {withdraw_amount}\nNew Balance : {self.amount}")

    def CalculateInterest(self):
        interest = self.amount * BankAccount.ROI / 100
        print(f"Interest: {interest}")

obj1 = BankAccount()
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()
 