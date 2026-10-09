class BankAccount:
    def __init__(self, accountNumber, holderName, balance):
        self.accountNumber = accountNumber
        self.holderName = holderName
        self.balance = balance

    def deposit(self, depositamount):
        if depositamount <= 0:
            print("Give a valid amount")
        else:
            self.balance += depositamount
            print(f"Deposited ₹{depositamount}. Updated Balance: ₹{self.balance}")

    def withdraw(self, withdrawamount):
        if withdrawamount <= 0:
            print("Withdrawal amount must be positive!")
        elif withdrawamount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= withdrawamount
            print(f"Withdrew ₹{withdrawamount}. Remaining Balance: ₹{self.balance}")

    def checkBalance(self):
        return self.balance

    def displayAccount(self):
        return f"Account No: {self.accountNumber}\nHolder: {self.holderName}\nBalance: ₹{self.balance}"


obj = BankAccount(123456, "Yash", 2000)
obj.deposit(10)
obj.withdraw(-1)
Details = obj.displayAccount()
print(Details)
