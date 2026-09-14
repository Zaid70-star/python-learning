class bankaccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    def display(self):
        print(f"Account holder: {self.name}, Balance: {self.balance}")
first_account = bankaccount("Alice")
first_account.deposit(1000)
first_account.deposit(100)
first_account.display()
first_account.withdraw(500)