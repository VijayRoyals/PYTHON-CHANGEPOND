class BankAccount:
    ROI = 10.5  

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Deposit(self, amount):
        self.Amount += amount
        print(f"Deposited: {amount}")

    def Withdraw(self, amount):
        if amount <= self.Amount:
            self.Amount -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest calculated: {interest}")
        return interest

    def Display(self):
        print(f"Name: {self.Name}")
        print(f"Amount: {self.Amount}")


account1 = BankAccount("Alice", 1000)
account1.Display()
account1.Deposit(500)
account1.Withdraw(200)
account1.CalculateInterest()
account1.Display()

account2 = BankAccount("Bob", 2000)
account2.Display()
account2.Deposit(300)
account2.Withdraw(1000)
account2.CalculateInterest()
account2.Display()
