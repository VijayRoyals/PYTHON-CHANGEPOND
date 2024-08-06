class BankAccount:
    def __init__(self, name, amount, address, accountNo):
        self.name = name
        self.amount = amount
        self.address = address
        self.accountNo = accountNo

    def createAccount(self):
        print(f"Account for {self.name} created with account number {self.accountNo}.")

    def displayAccountInfo(self):
        print(f"Name: {self.name}")
        print(f"Amount: ${self.amount}")
        print(f"Address: {self.address}")
        print(f"Account Number: {self.accountNo}")


def main():
    name = input("Enter account holder's name: ")
    amount = int(input("Enter initial amount: "))
    address = input("Enter address: ")
    accountNo = input("Enter account number: ")
    
    account = BankAccount(name, amount, address, accountNo)
    account.createAccount()
    account.displayAccountInfo()

if __name__ == "__main__":
    main()
